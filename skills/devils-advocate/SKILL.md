---
name: devils-advocate
description: Passe de advogado do diabo, em rodadas, sobre um rascunho de e-mail, um achado, um relatório, uma tabela, um plano ou uma decisão. Verifica cada afirmação factual contra arquivos e ferramentas de leitura, nomeia a classe de falha, corrige fatos vencidos no CLAUDE.md e na memória, dá um veredito. Auto-invocar (com anúncio de uma linha) só quando uma saída com cara de entregável está prestes a sair da conversa, ou quando a pessoa pede cuidado, precisão, ou "sem erros". Fora disso, não invocar. Gatilhos: advogado do diabo, desafia isso, procura furo, isso está certo, confere de novo, devil's advocate.
---

# Advogado do diabo

Este skill existe porque o assistente erra com confiança de dois jeitos recorrentes: afirma como
fato algo que foi só inferido, e repete algo do `CLAUDE.md` ou da memória que era verdade quando
foi escrito e não é mais. Os dois parecem idênticos de fora. A única defesa é tratar toda
afirmação factual como não verificada até ser checada contra a fonte atual, nesta execução, e
corrigir a fonte vencida no momento em que a contradição aparece.

O skill também roda no sentido contrário: contra o plano, o argumento ou a decisão da própria
pessoa, como interrogatório.

## Quando rodar

**Invocado pela pessoa.** `/devils-advocate [alvo] [meu|seu] [full]`. Todos os argumentos são
opcionais.

**Auto-invocado.** Anunciar antes, em uma linha, sem pedir permissão:
`Rodando devils-advocate em <alvo>, modo <verificação|interrogatório>.` Auto-invocar só quando
uma destas é verdade:

1. Uma saída com cara de entregável está prestes a sair da conversa: rascunho de e-mail, achado
   de auditoria, relatório, tabela ou número indo para alguém, documento de plano.
2. A pessoa pediu cuidado, precisão, atenção ou "sem erros" nesta tarefa, em qualquer redação
   ("vai com calma", "não erra", "quero isso certo", "confere de novo").

Fora disso, não rodar. Não rodar em turnos comuns de chat, em arquivos de trabalho ou em código.
Não rodar duas vezes na mesma revisão do mesmo alvo sem ser pedido.

## Alvo

Padrão: a última coisa com cara de entregável produzida na conversa. Também aceito: um caminho de
arquivo, ou um plano, argumento ou decisão que a pessoa cola ou descreve. Se nada na conversa se
qualifica, perguntar exatamente isto: "O que eu devo desafiar? (a) minha última saída, (b) um
arquivo, (c) o seu raciocínio."

## Modo

- **Verificação** (`meu`), o padrão. O alvo é algo que o assistente escreveu.
- **Interrogatório** (`seu`). O alvo é o plano, argumento ou decisão da pessoa.

Assumir verificação. Se o alvo é claramente o raciocínio da pessoa e nenhum modo foi dado,
perguntar "Meu ou seu?" uma vez e seguir.

## Fontes de contexto, lidas no início de toda execução

Ler as que existirem, nesta ordem:

1. O `CLAUDE.md` do projeto.
2. `LESSONS.md` ou o arquivo equivalente de regras de método na raiz do projeto.
3. `notes/findings_log.md` ou o registro equivalente de achados do projeto.
4. O índice de memória `MEMORY.md` e todo arquivo de memória que ele lista.
5. Todo arquivo, tabela, banco ou documento que o alvo cita.
6. `reference/classes_de_falha.md` e `reference/checklists.md` na pasta deste skill.

É desses arquivos que vêm as regras da casa e os fatos do projeto. **Eles também são suspeitos.**
Um fato no `CLAUDE.md` ou na memória é uma afirmação com data, não uma fonte de verdade. Quando o
alvo e um desses arquivos concordam, isso não é verificação; verificação é o arquivo vivo, o
banco, a ferramenta. Quando o alvo discorda de um desses arquivos, checar os dois contra a fonte
por baixo antes de decidir qual está vencido.

## Orçamento de verificação

| Nível | O quê | Permitido |
|---|---|---|
| 1 | Arquivos no disco: CSV, SQLite, JSON, notas, memória, as próprias fontes do alvo | Sempre, mas um pull salvo prova só o que era verdade na data dele; nunca decide uma afirmação sobre o estado atual de um sistema vivo (ver a regra abaixo da tabela) |
| 2 | Chamadas de leitura que não custam nada: leituras via MCP, GETs REST com chave guardada, listar uma planilha, ler um documento, ler uma thread | Sempre, e obrigatório para toda afirmação sobre o estado atual de um sistema vivo |
| 3 | Pulls novos de API que gastam cota ou escrevem no disco | Nunca dentro do passe. Rotular a afirmação como "precisa de pull novo" e deixar a pessoa decidir |
| 4 | Requisições HTTP a sites de terceiros (por exemplo um site de cliente) | Nunca, salvo regra explícita do projeto: firewalls bloqueiam e a requisição pode ter consequência |

Toda afirmação verificada declara o nível, a fonte e a data da fonte.

**Afirmações de estado exigem leitura ao vivo.** Uma afirmação sobre o que um sistema vivo
contém agora (o estágio, o responsável ou o conteúdo de uma tarefa; uma thread; um estado de
índice; um campo de perfil; uma agenda; um rascunho ou a pasta de enviados de um e-mail) só se
verifica com uma leitura de nível 2 desse sistema nesta execução. Um pull salvo, uma exportação
ou uma nota é nível 1 e não decide nada sobre "agora": é evidência da própria data, e a
afirmação então carrega essa data ou é relida ao vivo. Escolher o arquivo salvo porque é mais
barato é a falha que o skill existe para pegar (F03 com F04: "3 páginas em Publicação, todas com
a mesma pessoa" foi verificado contra um pull de dois dias antes enquanto uma página tinha mudado
de estágio e de pessoa e duas eram a mesma URL). Quando a leitura ao vivo é impossível daqui (sem
chave, sem conector, endereço bloqueado), a afirmação fica "Não verificável daqui" com a leitura
que a decidiria nomeada, nunca "Verificada" na força do arquivo.

## Estados de uma afirmação

Toda afirmação factual no alvo termina em exatamente um estado:

- **Verificada**: fonte, nível, data. "Verificada, gsc.db, nível 1, pull de 6 de setembro."
- **Contradita**: a fonte que a contradiz e o que ela diz no lugar.
- **Não verificável daqui**: o que a decidiria (um pull novo, uma pessoa, um acesso).
- **Aceita como suposição**: só a pessoa pode conceder este estado, e ela então aparece no alvo
  rotulada como suposição, nunca em silêncio.

Uma afirmação factual é qualquer número, data, contagem, estado de um site, arquivo, conta ou
ferramenta, o que um documento ou padrão diz, o que uma pessoa disse ou fez, ou quem fez o quê.
Uma ação que o autor diz ter tomado ("eu pedi", "eu enviei", "eu avisei", "eu registrei") é uma
afirmação: verifica-se contra um registro datado (mensagem, e-mail, nota com hora) e, sem
registro, reescreve-se no futuro com prazo. Uma causa atribuída a uma classe de coisas (uma
plataforma, um CMS, um tipo de página, um plugin) é uma afirmação sobre cada membro da classe:
checar os outros membros nos dados antes de ela ficar de pé. Extrair as afirmações como lista e
contar a lista por script ou por enumeração numerada, nunca no olho.

## Rodada 1, modo verificação

1. Anunciar (se auto-invocado) e nomear o alvo e o modo. Depois ler o alvo onde o destinatário
   vai lê-lo (a aba do documento, o rascunho na ferramenta de mensagens, a planilha), não o
   arquivo que o alimentou; se os dois diferem, o vivo é o alvo e a diferença é a primeira
   preocupação. Ler o relógio da máquina no mesmo passo e escrever toda hora a partir dele.
2. **Melhor versão do argumento (steel-man)**, três frases no máximo: por que o alvo é razoável
   como está.
3. **Extrair** as afirmações e dar a contagem.
4. **Verificar** cada afirmação dentro do orçamento: afirmações de estado sobre um sistema vivo
   por leitura ao vivo de nível 2, o resto contra o arquivo ou o banco por baixo. Registrar o
   estado.
5. **Checklist**: aplicar o checklist do gênero em `reference/checklists.md` (e-mail, achado,
   relatório, plano ou decisão). Cada item é passa, falha ou não se aplica. Reportar só as
   falhas. Depois percorrer o alvo achado por achado, incluindo um achado de uma frase dentro de
   um item maior: cada um carrega a severidade na escala do próprio projeto, a consequência na
   métrica que paga, um dono, e um próximo passo ou uma pergunta para o leitor. Um achado com
   todos os números certos e nada disso é uma preocupação de severidade alta, porque o leitor não
   consegue agir e o autor não sabe dizer o que acontece com ele.
6. **Preocupações**: no máximo sete, ordenadas em crítica, alta, média. O que está abaixo de média
   é descartado, não listado. Severidade: crítica significa que o leitor seria enganado ou que
   dinheiro ou confiança estão em jogo; alta é uma afirmação que não se sustenta ou uma falha de
   checklist que muda o sentido; média é uma quebra de regra da casa ou uma afirmação deixada
   sem verificação. Cada preocupação nomeia a classe de falha de `reference/classes_de_falha.md`.
7. **Correção de fonte vencida**: quando uma contradição vem do `CLAUDE.md` ou de um arquivo de
   memória, corrigir aquele arquivo na hora e listar cada edição no relatório, uma linha cada,
   antes e depois.
8. **Idioma**: uma seção curta separada no fim, só o que o destinatário notaria, cada item com a
   forma correta. Nunca misturada com as preocupações de substância.
9. **Pré-mortem**, uma linha: "Isto foi enviado e deu errado. O que deu errado?" e a resposta.
10. **Veredito**: para um e-mail, enviar / enviar com mudanças / não enviar. Para qualquer outra
    coisa, publicar / publicar com mudanças / repensar. Uma frase de justificativa.
11. **Classe de falha nova**, se um erro não cabe em nenhuma do registro: propor, não adicionar até
    a pessoa dizer.

## Formato

As preocupações usam este layout para que as rodadas fiquem reconhecíveis:

```
❓ **C1** - **<afirmação ou item, curto>**: <estado> | <classe de falha> | <severidade>
<o que foi checado, com fonte, nível e data. Por que falha ou não pode ser decidido.>

➡️ <recomendação, ou a decisão que a pessoa tem de tomar>
```

Afirmações verificadas são reportadas como contagem com as fontes ("14 afirmações verificadas
contra gsc.db e roster.csv, nível 1, 6 de setembro"), não listadas, salvo se a pessoa passou
`full`, caso em que a tabela completa de afirmações segue o veredito.

O relatório em si segue as regras que impõe: sem travessão, toda afirmação de estado datada, nenhum
editorial sobre quem fez o quê.

## Rodadas

A pessoa responde, corrige, aceita suposições ou fornece fatos. Recomputar: re-verificar o que
mudou, descartar o que se resolveu, levar só os itens abertos e o veredito atualizado para a
rodada seguinte. Não repetir o steel-man nem os itens fechados.

**Terminado** só se declara quando toda afirmação está verificada, corrigida, ou aceita pela
pessoa como suposição rotulada, e toda preocupação está resolvida ou explicitamente estacionada
pela pessoa. Nunca declarar terminado com uma afirmação em "não verificável" sem a aceitação da
pessoa. A pessoa pode parar a qualquer momento; quando para, terminar com uma lista curta do que
segue aberto e não escrever nada no disco sobre isso.

## Modo interrogatório

Mesmo formato, mesmas rodadas, mesma condição de saída. As diferenças:

- O steel-man é da posição da pessoa, nos termos dela.
- Cada item é uma premissa do argumento. O corpo traz o contra-argumento mais forte e a
  evidência que decidiria de um lado ou de outro. A linha ➡️ é uma pergunta que a pessoa tem de
  responder, não uma recomendação: a pessoa aprende respondendo, então fazer responder.
- Fatos que o assistente consegue consultar são consultados antes de perguntar, dentro do
  orçamento. À pessoa se pedem decisões, e fatos que só ela tem.
- Veredito: seguir / seguir com mudanças / repensar.

## O que este skill não faz

- Não reescreve o alvo. A pessoa lê o relatório, decide, e pede a correção separadamente.
  Misturar desafio e correção esconde quais mudanças foram aceitas.
- Não fabrica preocupações. Se o alvo se sustenta, dizer isso e dar a contagem.
- Não suaviza. Sem elogio de enchimento, sem "ótimo trabalho no geral".
- Não escreve notas, logs ou arquivos próprios além das correções de fonte vencida acima.
- Não faz checagens de nível 3 ou 4.
