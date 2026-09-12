---
name: regra-dos-5-prompts
description: A cada 5 prompts da pessoa, parar e escrever todo fato, decisão, correção e promessa daqueles prompts nos arquivos e na memória antes de responder o próximo.
metadata:
  type: feedback
---

A cada 5 prompts, juntar tudo daqueles prompts que pertence ao disco (estado no `CLAUDE.md`,
`notes/TASKS.md`, o registro de achados, os arquivos de memória) e escrever, anunciando em uma
linha. Nada importante vive só no chat.

**Por quê:** duas sessões rodaram em paralelo por uma noite inteira e vários resultados de uma
delas (decisões, tarefas fechadas, versões de um relatório) não estavam no disco quando a pessoa
perguntou. A janela fecha ou compacta, e o que só estava no chat some.

**Como aplicar:** manter a contagem de prompts; no quinto, rodar `/log-to-disk`, que é a
implementação desta regra. Ele lê a transcrição do disco em vez do contexto (funciona depois de
uma compactação), roda o advogado do diabo sobre a lista de afirmações extraída, roteia cada
item para o arquivo certo, e checa o material novo contra o que o `CLAUDE.md` já diz, corrigindo
contradições em vez de empilhar uma seção nova. Também escrever na hora, independente da
contagem, sempre que aparecer uma decisão, uma regra, uma correção a um fato ou uma mensagem
enviada. Relacionado: [[contar-por-script]], [[verificar-ao-vivo]].
