# Kit de partida para o Claude Code

Práticas, modelos de arquivo e dois skills, extraídos de um projeto real de várias semanas com o
Claude Code. Tudo aqui foi aprendido errando: cada regra existe porque a falta dela custou algo.

Nada neste kit é específico de um cliente ou de uma empresa. Os exemplos foram anonimizados.

## O que tem aqui

```
README.md                       este arquivo: as práticas e como instalar
modelos/CLAUDE.md               o esqueleto do arquivo de instruções do projeto
modelos/LESSONS.md              o esqueleto do arquivo de lições de método
memory/                         7 arquivos de memória genéricos e o índice MEMORY.md
skills/devils-advocate/         o passe de advogado do diabo: verifica cada afirmação antes de sair do chat
skills/log-to-disk/             a regra dos 5 prompts: tudo importante vai para o disco, e o CLAUDE.md é corrigido, não acumulado
skills/grilling/                a entrevista sem trégua: o Claude interroga o seu plano em rodadas até nada ficar em suposição
skills/grill-me/                o atalho /grill-me, que só você invoca; ele roda o grilling
```

O terceiro skill, o **humanizer** (e o seu par, **structural-humanizer**), não é meu. Ele vem
do repositório público https://github.com/NulightJens/humanizer-stack e se instala de lá.
Veja "Instalar" abaixo.

## As práticas, em ordem de importância

### 1. A regra que governa tudo

**Nada entra num entregável que você não consiga explicar em voz alta.**

O corolário: **nunca afirme como fato o que foi só inferido.** Toda afirmação é verificada, tem
fonte, ou vem rotulada como suposição. Conte os números por script, nunca no olho. Date toda
frase que descreve o estado de alguma coisa, porque sistemas mudam por baixo de você. Antes de
reportar um resultado, descarte a hipótese de que o método produziu o resultado sozinho.

Num passe de revisão sobre um trabalho de vários dias, apareceram 14 problemas. Todos eram a
mesma coisa: uma inferência escrita como fato. O Claude vai fazer isso. A defesa é tratar cada
afirmação factual como não verificada até ser checada contra a fonte, naquela execução.

### 2. CLAUDE.md guarda estado, não narrativa

O `CLAUDE.md` é carregado em toda sessão antes de você digitar. Ele responde "o que é verdade
agora, e o que eu preciso saber antes de mexer em qualquer coisa". A história do dia a dia vai
para notas datadas em `notes/`.

A regra de ouro: **quando um fato muda, a linha antiga é corrigida ou apagada, nunca fica ao
lado da nova.** Sem isso o arquivo cresce até se contradizer. Aconteceu: 133 KB, 31 seções, 24
contradições vivas e cinco instruções diferentes de "leia isto primeiro".

Estrutura que funciona (o modelo está em `modelos/CLAUDE.md`):

- Ordem de leitura no topo: este arquivo, depois `LESSONS.md`, depois um único handoff nomeado.
- "Estado atual" com data e hora, no alto. Tudo abaixo é referência que muda devagar.
- Uma tabela "qual número significa o quê" quando a mesma coisa tem várias contagens.
- Quem você é, quem são as pessoas, as regras permanentes.
- "Correções que precisam sobreviver": cada erro que custou algo, e a regra que ele ensinou.
- "Ainda aberto" e "ainda desconhecido", com quem deve o quê.
- Layout de pastas com o que cada script faz e as armadilhas dele.

### 3. LESSONS.md guarda o que não pode ser recalculado

O `CLAUDE.md` diz o que é verdade agora. O `LESSONS.md` diz o que foi aprendido e por quê. Ele
muda devagar e as linhas dele não se apagam.

Todo número que pode ser puxado de novo de uma API ou de um arquivo fica de fora, de propósito.
O que entra: regras de método com o erro real que gerou cada uma, os conceitos que você domina
nas frases que você mesmo usa, o que foi confirmado por escrito por alguém, o último estado
verificado de cada coisa (datado, com "RE-VERIFICAR" escrito), as decisões que ainda governam, e
um glossário. O modelo está em `modelos/LESSONS.md`.

### 4. Memória: um fato por arquivo, com índice

O Claude Code tem uma memória persistente por projeto. Use um arquivo por regra, com o "por
quê" e o "como aplicar" dentro. O índice `MEMORY.md` tem uma linha por arquivo e nunca o
conteúdo. E resuma as regras da memória numa tabela dentro do `CLAUDE.md`, para que uma sessão
sem memória continue funcionando. Sete exemplos genéricos estão em `memory/`.

### 5. Advogado do diabo antes de qualquer coisa sair do chat

Um passe de verificação, em rodadas, sobre qualquer coisa com cara de entregável: e-mail,
relatório, tabela, plano, decisão. Cada afirmação termina em um de quatro estados: verificada
(com fonte, nível e data), contradita, não verificável daqui, ou aceita como suposição (só você
concede esse estado, e aí ela aparece rotulada no texto). Cada problema recebe uma classe de
falha de uma lista numerada que cresce com o projeto. Está em `skills/devils-advocate/`.

### 5b. Ser interrogado antes de decidir

O oposto do advogado do diabo: em vez de o Claude verificar o que ele escreveu, ele interroga o
que você pensou. `/grill-me` abre uma entrevista em rodadas. Cada rodada traz todas as perguntas
que já dá para fazer, numeradas, cada uma com a resposta que ele recomenda; você responde, a
árvore de decisões cresce, vem a próxima rodada. Fatos ele busca sozinho; decisões ele pede a
você. Termina quando não sobra nada em suposição silenciosa. Use antes de um plano, de uma
arquitetura ou de uma decisão cara. Está em `skills/grilling/` e `skills/grill-me/`.

### 6. A regra dos 5 prompts

A cada 5 prompts seus, tudo importante vai para o disco: decisões, fatos, correções, promessas,
arquivos criados. Nenhuma sessão termina com algo que só existe no chat. O skill `log-to-disk`
implementa isso: lê a transcrição do disco (funciona depois de uma compactação), roda o advogado
do diabo sobre a lista de afirmações, roteia cada item para o arquivo certo e **corrige** o
`CLAUDE.md` em vez de empilhar uma seção nova. Está em `skills/log-to-disk/`.

### 7. Verificar ao vivo, não contra uma leitura antiga

Uma afirmação sobre o que um sistema vivo contém agora (um cartão num sistema de tarefas, uma
thread, um índice, um rascunho de e-mail) só se verifica com uma leitura ao vivo naquela
execução. Um arquivo salvo prova o que era verdade na data dele, nada depois. Escolher o arquivo
porque é mais barato é o erro que o passe existe para pegar.

### 8. Propor livremente, mudar nada sozinho

O Claude não constrói um documento, plano ou apresentação sem o seu sinal verde explícito.
Arquivos de trabalho são livres; o que é gated é qualquer coisa com cara de entregável que você
não pediu. Ele propõe o roteiro, você diz sim, ele escreve. E nada que altere um processo
documentado é decidido por ele: é proposto, por escrito, com evidência.

### 9. Disciplina de tokens

Tokens são gastos no que entra na conversa, não no que fica no disco. Scripts puxam dados e
escrevem um resumo pequeno; a sessão lê o resumo, nunca o arquivo bruto. Consultas ad hoc têm
teto de linhas. Nunca dê `cat` num arquivo bruto para responder uma pergunta.

### 10. Tudo como dado, renderizado depois

Plano em JSON, relatórios em JSON, tabelas em CSV, e scripts que renderizam a página ou o PDF a
partir deles. Scripts idempotentes: rodar duas vezes escreve o mesmo resultado. Cada script
documentado no `CLAUDE.md` com uma linha do que faz e as armadilhas que já mordeu.

### 11. Regras de escrita explícitas

Diga ao Claude, no `CLAUDE.md`, como você quer ler: idioma, listas, sem travessão (ou com),
terminar com os próximos passos e nunca com uma pergunta, ensinar o mecanismo enquanto faz o
trabalho sem transformar cada resposta num quiz. Ele obedece se está escrito; se não está, ele
volta ao padrão dele em toda sessão.

### 12. Diga quem você é e como você trabalha

Uma seção "Quem eu sou" no `CLAUDE.md`: no que você é forte, o que está aprendendo, o que não
sabe, e como você funciona (por exemplo, "travo com alvo vago; me dê sempre a meta e o próximo
passo concreto"). O Claude calibra a explicação a partir disso. Sem essa seção ele chuta.

## Instalar

1. **CLAUDE.md e LESSONS.md.** Copie `modelos/CLAUDE.md` e `modelos/LESSONS.md` para a raiz do
   seu projeto e preencha as seções. Apague o que não se aplica. Um `CLAUDE.md` de 30 linhas
   preenchido vale mais que um de 300 com placeholders.

2. **Os skills deste kit.** Copie as pastas para `~/.claude/skills/`:

   ```bash
   cp -r skills/* ~/.claude/skills/
   ```

   No Windows a pasta é `C:\Users\<você>\.claude\skills\`. O Claude Code lista os skills no início
   de cada sessão; `/devils-advocate`, `/log-to-disk` e `/grill-me` passam a existir.

3. **O humanizer.** Instale do repositório original, que tem o `install.sh` e recebe atualizações:

   ```bash
   git clone https://github.com/NulightJens/humanizer-stack ~/.claude/repos/humanizer-stack
   cd ~/.claude/repos/humanizer-stack && ./install.sh
   ```

   Ele instala `humanizer` (palavras e frases) e `structural-humanizer` (estrutura do texto).
   Rode o primeiro antes do segundo. Ele custa uns 11 mil tokens para carregar, então carregue
   quando aparecer o primeiro texto que uma pessoa vai ler, não no começo da sessão.

4. **A memória.** Peça ao Claude, na primeira sessão do projeto, o caminho da pasta de memória
   dele (ele conhece; é algo como `~/.claude/projects/<seu-projeto>/memory/`). Copie os arquivos
   de `memory/` para lá e ajuste o `como-eu-trabalho.md`, que é um modelo para você preencher.

5. **A primeira sessão.** Abra o projeto e diga ao Claude, em uma mensagem: quem você é, o que o
   projeto é, e que ele deve ler `CLAUDE.md`, `LESSONS.md` e a memória antes de qualquer coisa.
   Depois peça para ele rodar `/log-to-disk` no fim da sessão. A partir daí a regra dos 5
   prompts se sustenta sozinha, porque está escrita no `CLAUDE.md`.

## Por que funciona

O Claude é bom em fazer o trabalho e ruim em lembrar o que já sabia. Tudo neste kit é um jeito
de colocar a memória no disco, em arquivos que ele lê antes de você digitar, e de forçar a
verificação antes de qualquer coisa chegar a outra pessoa. Se você seguir só uma coisa daqui,
que seja a regra número 1.
