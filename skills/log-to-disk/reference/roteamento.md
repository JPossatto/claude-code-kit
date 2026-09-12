# Roteamento: qual arquivo recebe qual item

Um destino por item. Quando dois parecem certos, o mais específico vence, e o outro recebe um
ponteiro, não uma cópia. Ajuste os caminhos aos do seu projeto; a lógica é o que importa.

| Item | Destino | Forma |
|---|---|---|
| Uma decisão da pessoa que muda como o trabalho é feito daqui em diante | `CLAUDE.md` regras permanentes, **e** um arquivo de memória se for sobre como eu devo trabalhar | Uma linha na tabela de regras, a versão completa com Por quê e Como aplicar na memória |
| Uma decisão sobre este projeto, este item, esta semana | `CLAUDE.md` Estado atual, substituindo o que ela supera | Dizer como o que é verdade agora, com a data |
| Um fato estabelecido por medição | `notes/findings_log.md` como achado numerado ou adendo datado, com método e limites; o número em si no CSV | O achado carrega: o que foi medido, como, em que data, o que não cobre |
| Um número computado que outro trabalho vai citar | o CSV em `data/` ou na pasta do item, depois uma referência de uma linha | Nunca o número sozinho em prosa sem denominador e data |
| Uma correção a algo em que se acreditava antes | `CLAUDE.md` "Correções que precisam sobreviver" **se ensina uma regra de método**; senão corrigir a linha errada no lugar e não dizer mais nada | A lição, não o incidente |
| Uma tarefa para a pessoa ou para a equipe | `notes/TASKS.md` e o sistema de tarefas do projeto, se houver | Dono, prazo, e como é o "pronto" |
| Algo esperando outra pessoa | `CLAUDE.md` "Ainda aberto", com quem deve o quê | Nome, o quê, desde quando |
| Um compromisso que a pessoa assumiu com alguém | `CLAUDE.md` Estado atual, lista de abertos, com o prazo | Compromissos vencidos ficam visíveis até fechar |
| Um fato sobre um cliente ou item do projeto | o registro daquele item (`clients/<slug>/`, ou o equivalente) | Datado |
| Uma ferramenta ou script novo | `CLAUDE.md` layout de pastas, uma linha com o que faz e as armadilhas | Armadilhas importam mais que a descrição |
| Um arquivo, planilha, documento ou cartão criado | o manifesto do lote (`data/<tipo>_<data>.csv`) e uma linha onde quer que seja referenciado | Todo arquivo que uma tarefa cita é um link estável, nunca um anexo solto |
| Uma mensagem enviada, ou um rascunho segurado | uma nota datada em `notes/` com o texto como enviado, e uma linha no Estado atual se carrega um pedido | Texto como enviado, não como rascunhado |
| O que aconteceu hoje, em sequência | uma nota datada `notes/<data>_<tema>.md` | O `CLAUDE.md` recebe uma linha na linha do tempo apontando para cá, nada mais |
| Uma pergunta aberta sem resposta ainda | `CLAUDE.md` "Ainda desconhecido" | Redigir como pergunta, e nomear quem pode responder |
| Um artefato de método que eu mesmo gerei | `LESSONS.md`, e "Correções que precisam sobreviver" se vai recorrer | A classe do erro, para a próxima sessão reconhecer |

## A linha entre o CLAUDE.md e uma nota

O `CLAUDE.md` responde "o que é verdade agora, e o que eu preciso saber antes de mexer em
qualquer coisa". Uma nota responde "o que aconteceu, e qual foi a evidência". Se uma frase começa
com uma hora do dia, ela pertence a uma nota.

## Disciplina de tamanho

O `CLAUDE.md` é carregado em toda sessão antes de a pessoa digitar. Cada execução deste skill
deve deixá-lo do mesmo tamanho ou menor, a não ser que algo genuinamente novo seja verdade. Duas
alavancas:

- Um bloco datado com mais de uns três dias comprime para uma linha na linha do tempo mais um
  ponteiro.
- Duas linhas dizendo quase a mesma coisa viram uma.

Se o arquivo cresceu mais que algumas centenas de bytes numa execução em que nada estrutural
mudou, a narrativa vazou para dentro. Mover para uma nota.
