---
name: verificar-ao-vivo
description: Uma afirmação sobre o estado atual de um sistema vivo (tarefa, thread, índice, rascunho, calendário) só se verifica com uma leitura ao vivo naquela execução; um arquivo salvo prova o que era verdade na data dele, nada depois.
metadata:
  type: feedback
---

Qualquer afirmação sobre o que um sistema vivo contém agora (o estágio ou o responsável de uma
tarefa, uma thread, um índice, um campo de perfil, uma agenda, um rascunho ou uma pasta de
enviados) é verificada por uma leitura ao vivo desse sistema, nesta execução. Um pull salvo, uma
exportação ou uma nota é evidência da própria data e não decide nada sobre "agora".

**Por quê:** um passe de verificação deu "3 páginas em Publicação, todas com a mesma pessoa" como
verificado, contra um pull de dois dias antes. A leitura ao vivo, na mesma hora, mostrou uma
página em outro estágio com outra pessoa e as outras duas como a mesma URL cadastrada duas vezes.
A chamada de API não custava nada e não foi feita.

**Como aplicar:** quando a leitura ao vivo é impossível daqui (sem chave, sem conector, endereço
bloqueado), a afirmação fica como "não verificável daqui", com a leitura que a decidiria nomeada,
nunca como "verificada" na força do arquivo. Escolher o arquivo salvo porque é mais barato é o
erro que o passe de advogado do diabo existe para pegar. Ver [[contar-por-script]].
