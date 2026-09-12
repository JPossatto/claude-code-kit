---
name: ler-o-relogio
description: Esta máquina está em <fuso, por exemplo BRT, UTC menos 3>; ler a hora no mesmo comando que a escreve, e nunca converter de cabeça.
metadata:
  type: project
---

Esta máquina roda em <fuso>. `date` ou `Get-Date` sem argumentos devolvem a hora local. Toda
hora escrita numa nota, no `CLAUDE.md` ou num relatório é lida do relógio no mesmo comando que a
escreve, nunca copiada de uma nota anterior nem convertida de cabeça.

**Por quê:** um comando com fuso nomeado (`TZ=<nome> date`) não resolveu o nome no Git Bash do
Windows e imprimiu UTC rotulado como GMT. Todas as horas escritas por uma hora inteira estavam
três horas adiantadas e tiveram de ser corrigidas no disco.

**Como aplicar:** ler o relógio no mesmo passo que escreve a hora. Quando uma hora registrada
discorda da hora de modificação do arquivo, o arquivo vence e a hora é marcada como suspeita.
Pessoas em outro fuso: anotar o fuso delas aqui, com a diferença em horas, para não recalcular a
cada sessão.
