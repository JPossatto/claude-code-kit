# <Nome do projeto>, contexto do projeto

**Ordem de leitura:** este arquivo, depois `LESSONS.md`, depois o único handoff nomeado em
"Estado atual". Tudo abaixo de "Estado atual" é referência que muda devagar. A narrativa do dia a
dia fica em `notes/`, por data.

**Uma regra sobre este arquivo:** ele guarda estado, não narrativa. Quando um fato muda, a linha
antiga é corrigida ou apagada, nunca fica ao lado da nova. `/log-to-disk` aplica isso.

---

## Estado atual, <dia da semana> <data>, <hora> (<Dia N de M, se houver prazo>)

**Leia em seguida:** `notes/<data>_session_handoff.md`, depois `notes/TASKS.md`.

**O compromisso.** <O que foi prometido, a quem, para quando. Datas absolutas, nunca "semana que
vem".>

**A direção em vigor.** <A regra que decide o que se faz e o que não se faz agora. Uma ou duas
frases.>

**O que está medido, e o que não está.** <Uma linha por coisa medida, com a data e o script que
contou.>

**Aberto do meu lado, em ordem:**
- <item, com prazo>
- <item, com prazo>

**Esperando outras pessoas:** <nome> deve <o quê> desde <data>; <nome> deve <o quê>.

---

## Escopo: qual número significa o quê

Quando a mesma coisa tem várias contagens, todas corretas para perguntas diferentes, defina cada
uma aqui uma única vez. Toda outra menção aponta para esta tabela. Nunca escreva uma contagem sem
dizer o que ela conta.

| Número | O que conta | Fonte |
|---|---|---|
| <N> | <definição> | `<arquivo ou script>` |
| <N> | <definição> | `<arquivo ou script>` |

---

## O trabalho

<O que você foi contratado ou se propôs a fazer, nas palavras do documento que define isso. O que
é seu. O que fica com outras pessoas. As datas de revisão ou entrega.>

| Marco | Data | O que é avaliado |
|---|---|---|
| <marco> | <data absoluta> | <critério> |

---

## Quem eu sou

<Duas ou três linhas: formação, o que já fez, como pensa.>

**Forte em:** <áreas>.

**Aprendendo, no trabalho:** <áreas>.

**Sem experiência:** <áreas>.

**Como eu trabalho:** <por exemplo: "travo com alvo vago, me dê sempre a meta e o próximo passo
concreto"; "aprendo fazendo, não lendo teoria"; "quero a explicação do mecanismo em palavras
simples quando o conceito é novo">.

---

## As pessoas

- **<Nome>**, <cargo>. <Como se comunica, o que prefere, uma regra dele se houver.>
- **<Nome>**, <cargo>. <...>

---

## Regras permanentes

1. **<Idioma das respostas.>**
2. **Ensinar enquanto faz, sem quiz.** Explicar o mecanismo em palavras simples. Nunca terminar
   uma resposta com pergunta, quiz ou "me explica de volta"; terminar com os próximos passos.
3. **<Regra de estilo da casa, por exemplo: sem travessão em nada que sai para outra pessoa.>**
4. **Confidencialidade.** <O que não sai desta pasta.>
5. **Rodar o skill `devils-advocate` antes de qualquer saída com cara de entregável** (e-mail,
   relatório, tabela, plano) e sempre que eu pedir cuidado, precisão ou "sem erros". Anunciar em
   uma linha. Fora disso, não rodar.
6. **A regra dos 5 prompts.** A cada 5 prompts meus, rodar `/log-to-disk`: toda decisão, fato,
   correção, promessa, ferramenta e arquivo daqueles prompts vai para o arquivo certo antes da
   próxima resposta. Nunca deixar uma sessão terminar com algo só no chat.
7. **Propor livremente, mudar nada sozinho.** Nenhum documento, plano ou apresentação sem meu
   sinal verde explícito. Arquivos de trabalho são livres.
8. **<Regra de lane: no que este projeto mexe e no que não mexe.>**

## As regras que vivem na memória

Os arquivos de memória ficam fora desta pasta, um por regra, com `MEMORY.md` como índice. Estão
resumidos aqui para que uma sessão sem memória continue funcionando. Onde os dois existem, o
arquivo de memória é a versão completa e vence.

| Arquivo de memória | A regra, em uma linha |
|---|---|
| sem-perguntas-no-final | Nunca terminar uma resposta com pergunta ou quiz; terminar com os próximos passos. |
| sem-documentos-sem-sinal-verde | Nenhum entregável sem aprovação explícita; discutir os passos antes. |
| regra-dos-5-prompts | A cada 5 prompts, `/log-to-disk`. |
| contar-por-script | Nenhum número entra num arquivo por ter sido lido no olho. |
| verificar-ao-vivo | Estado de um sistema vivo só se verifica com leitura ao vivo naquela execução. |
| ler-o-relogio | Esta máquina está em <fuso>; ler a hora no mesmo comando que a escreve. |
| como-eu-trabalho | <resumo de uma linha do arquivo preenchido>. |

## A REGRA QUE GOVERNA

**Nada entra em nenhum entregável que eu não consiga explicar em voz alta.**

O corolário: **nunca afirmar como fato o que foi só inferido.** Toda afirmação é verificada, tem
fonte, ou vem explicitamente rotulada como suposição. Contar os números por script. Datar toda
frase sobre o estado de alguma coisa, porque as coisas mudam por baixo de você. Descartar a
hipótese de que o resultado é um artefato do método. Classificar a evidência: documentação
oficial (nível 1), funcionário da plataforma em registro público (nível 2), consenso de
praticantes ou nosso julgamento (nível 3).

---

## Correções que precisam sobreviver

Cada uma custou algo, e cada uma é a evidência de uma regra de método. Adicione no fim. Nunca
apague.

- **<A regra, em negrito.>** <O erro concreto, com a data, e o que ele ensinou.>
- **Contar por script, nunca no olho.** <exemplo do projeto>
- **Uma checagem de completude precisa nomear as colunas que contam como resposta.** <exemplo>

---

## Ainda aberto, e ainda desconhecido

**Decisões esperando outras pessoas:** <nome> sobre <o quê>.

**Ainda desconhecido:**
- <Pergunta, e quem pode responder.>

---

## Layout de pastas

```
CLAUDE.md            este arquivo: estado, não narrativa
LESSONS.md           regras de método, conceitos, glossário
notes/               notas de trabalho por data: TASKS.md, handoffs de sessão, registro de achados
data/                tabelas computadas, CSV e JSON; o bruto fica em data/raw/ e nunca é lido na sessão
tools/               scripts, todos re-executáveis; uma linha por script aqui com o que faz e as armadilhas
deliverables/        documentos que saem para outras pessoas, datados, fonte .md mais a exportação
archive/superseded/  todo documento substituído, no dia em que foi substituído
```

## Disciplina de dados e tokens

Tokens são gastos no que entra na conversa, não no que fica no disco.

1. Scripts puxam dados, salvam o bruto e escrevem um resumo pequeno.
2. Sessões leem o resumo, nunca o bruto.
3. Consultas ad hoc passam por um script com teto de linhas. Agregar, não listar.
4. Nunca dar `cat` num arquivo bruto. Abrir um só para depurar um script.

---

## Linha do tempo: o que aconteceu em que dia

O detalhe está nas notas nomeadas aqui. Este arquivo não repete.

| Data | O que foi | Onde está escrito |
|---|---|---|
| <data> | <uma linha> | `notes/<data>_<tema>.md` |
