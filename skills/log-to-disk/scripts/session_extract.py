#!/usr/bin/env python3
"""Lê a transcrição da sessão do Claude Code no disco e emite um digest compacto.

Por que existe: /log-to-disk precisa funcionar depois de a conversa ter sido compactada,
quando o chat no contexto é um resumo de um resumo. A transcrição no disco é o registro real.

Uso
  python session_extract.py                  digest desde a última âncora, sessão mais nova
  python session_extract.py --full           sessão inteira, ignora a âncora
  python session_extract.py --session <id>   um id de sessão específico, ou um caminho .jsonl
  python session_extract.py --list           lista as sessões do projeto, mais nova primeiro
  python session_extract.py --set-anchor     grava a âncora no fim do que acabou de ser lido
  python session_extract.py --show-anchor    imprime as âncoras guardadas
  python session_extract.py --project <dir>  usa outro diretório de projeto (padrão: o atual)

Como acha a transcrição: o Claude Code guarda as transcrições em
~/.claude/projects/<caminho-do-projeto-codificado>/*.jsonl, onde a codificação troca todo
caractere que não é letra ou dígito por um hífen. O script recalcula isso a partir do
diretório do projeto. Se a sua instalação usa outro lugar, aponte com LOG_TRANSCRIPT_DIR.

Variáveis de ambiente (todas opcionais):
  LOG_PROJECT_DIR      diretório do projeto (senão --project, senão o diretório atual)
  LOG_TRANSCRIPT_DIR   pasta das transcrições (senão calculada como acima)
  LOG_ANCHOR_PATH      arquivo da âncora (senão <projeto>/.claude/log_anchor.json)

O digest carrega: cada prompt da pessoa por inteiro, a prosa do assistente aparada, e uma
linha por efeito colateral (arquivo escrito, arquivo editado, comando rodado, mensagem
rascunhada ou enviada). Resultados de ferramentas ficam de fora, porque já estão no disco e
são o que torna uma transcrição enorme. As horas saem no fuso local da máquina.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone

# Ferramentas cujo uso é um efeito colateral que vale registrar, e o campo que nomeia o alvo.
SIDE_EFFECT_TOOLS = {
    "Write": "file_path",
    "Edit": "file_path",
    "NotebookEdit": "notebook_path",
    "Bash": "command",
    "PowerShell": "command",
    "Artifact": "file_path",
    "SendUserFile": "files",
}
MESSAGE_TOOL_HINTS = ("slack", "gmail", "draft", "send_message", "create_event", "tasks")

ASSISTANT_TRIM = 1200
COMMAND_TRIM = 240


def encode_project_path(path):
    """D:\\claude\\meu-projeto -> D--claude-meu-projeto ; /home/eu/proj -> -home-eu-proj"""
    return re.sub(r"[^A-Za-z0-9]", "-", os.path.abspath(path))


def settings(project_arg):
    project = os.environ.get("LOG_PROJECT_DIR") or project_arg or os.getcwd()
    project = os.path.abspath(project)
    transcripts = os.environ.get("LOG_TRANSCRIPT_DIR") or os.path.join(
        os.path.expanduser("~"), ".claude", "projects", encode_project_path(project)
    )
    anchor = os.environ.get("LOG_ANCHOR_PATH") or os.path.join(
        project, ".claude", "log_anchor.json"
    )
    return project, transcripts, anchor


def sessions(transcript_dir):
    out = []
    if not os.path.isdir(transcript_dir):
        return out
    for name in os.listdir(transcript_dir):
        if not name.endswith(".jsonl"):
            continue
        path = os.path.join(transcript_dir, name)
        try:
            st = os.stat(path)
        except OSError:
            continue
        out.append((st.st_mtime, st.st_size, name[:-6], path))
    out.sort(reverse=True)
    return out


def resolve(session, transcript_dir):
    if session and os.path.exists(session):
        return os.path.splitext(os.path.basename(session))[0], session
    all_s = sessions(transcript_dir)
    if not all_s:
        sys.exit("nenhuma transcrição encontrada em %s" % transcript_dir)
    if session:
        for _, _, sid, path in all_s:
            if sid == session or sid.startswith(session):
                return sid, path
        sys.exit("sessão %s não encontrada" % session)
    return all_s[0][2], all_s[0][3]


def load_anchors(anchor_path):
    try:
        with open(anchor_path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {}


def save_anchors(anchor_path, data):
    os.makedirs(os.path.dirname(anchor_path), exist_ok=True)
    with open(anchor_path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)


def blocks(msg):
    content = msg.get("content")
    if isinstance(content, str):
        return [{"type": "text", "text": content}]
    if isinstance(content, list):
        return [b for b in content if isinstance(b, dict)]
    return []


def to_local(ts):
    """As horas da transcrição são ISO em UTC. O digest sai no fuso local da máquina."""
    if not ts:
        return "     "
    try:
        clean = ts.replace("Z", "+00:00")
        dt = datetime.fromisoformat(clean)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone().strftime("%m-%d %H:%M")
    except ValueError:
        return ts[11:16]


def short(value, limit):
    if value is None:
        return ""
    text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)
    text = " ".join(text.split())
    return text if len(text) <= limit else text[:limit] + " [...]"


def read(path, after_ts=None):
    events = []
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            ts = rec.get("timestamp") or ""
            if after_ts and ts and ts <= after_ts:
                continue
            kind = rec.get("type")
            msg = rec.get("message") or {}
            if kind == "user":
                # Um registro "user" é um prompt real ou um resultado de ferramenta devolvido.
                texts = []
                for b in blocks(msg):
                    if b.get("type") == "text" and b.get("text"):
                        texts.append(b["text"])
                    elif b.get("type") == "tool_result" and b.get("is_error"):
                        texts.append("[erro de ferramenta] " + short(b.get("content"), 200))
                if rec.get("isMeta") or rec.get("isCompactSummary"):
                    continue
                for t in texts:
                    if t.strip().startswith("<") and "system-reminder" in t:
                        continue
                    events.append({"ts": ts, "kind": "prompt", "text": t.strip()})
            elif kind == "assistant":
                for b in blocks(msg):
                    if b.get("type") == "text" and b.get("text", "").strip():
                        events.append(
                            {"ts": ts, "kind": "said", "text": short(b["text"], ASSISTANT_TRIM)}
                        )
                    elif b.get("type") == "tool_use":
                        name = b.get("name", "?")
                        inp = b.get("input") or {}
                        field = SIDE_EFFECT_TOOLS.get(name)
                        lowered = name.lower()
                        if field:
                            events.append(
                                {
                                    "ts": ts,
                                    "kind": "did",
                                    "text": "%s %s" % (name, short(inp.get(field), COMMAND_TRIM)),
                                }
                            )
                        elif any(h in lowered for h in MESSAGE_TOOL_HINTS):
                            events.append(
                                {"ts": ts, "kind": "did", "text": "%s %s" % (name, short(inp, COMMAND_TRIM))}
                            )
    return events


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--session")
    ap.add_argument("--project")
    ap.add_argument("--full", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--set-anchor", action="store_true")
    ap.add_argument("--show-anchor", action="store_true")
    a = ap.parse_args()

    project, transcript_dir, anchor_path = settings(a.project)

    if a.list:
        print("# projeto      %s" % project)
        print("# transcrições %s" % transcript_dir)
        for mtime, size, sid, _ in sessions(transcript_dir)[:15]:
            print(
                "%s  %8.1f MB  %s"
                % (datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M"), size / 1e6, sid)
            )
        return

    anchors = load_anchors(anchor_path)
    if a.show_anchor:
        print(json.dumps(anchors, indent=2, ensure_ascii=False))
        return

    sid, path = resolve(a.session, transcript_dir)
    after = None if a.full else (anchors.get(sid) or {}).get("last_ts")
    events = read(path, after)

    if a.set_anchor:
        if events:
            anchors[sid] = {
                "last_ts": events[-1]["ts"],
                "written_at": datetime.now().isoformat(timespec="seconds"),
                "events_logged": len(events),
            }
            save_anchors(anchor_path, anchors)
            print("âncora de %s fixada em %s (%d eventos)" % (sid, events[-1]["ts"], len(events)))
        else:
            print("nada novo, âncora inalterada")
        return

    prompts = sum(1 for e in events if e["kind"] == "prompt")
    print("# sessão   %s" % sid)
    print("# arquivo  %s" % path)
    print("# desde    %s" % (after or "início da sessão"))
    print("# eventos  %d (%d prompts da pessoa)" % (len(events), prompts))
    if not events:
        print("\nNada novo desde a âncora.")
        return
    print("# relógio  as horas abaixo estão no fuso local, convertidas do UTC da transcrição")
    print()
    label = {"prompt": "USER", "said": "SAID", "did": "DID "}
    for e in events:
        print("[%s] %s | %s" % (to_local(e["ts"]), label[e["kind"]], e["text"]))


if __name__ == "__main__":
    main()
