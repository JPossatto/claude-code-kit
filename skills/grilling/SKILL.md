---
name: grilling
description: Interrogar a pessoa sem trégua sobre um plano, uma decisão ou uma ideia. Usar quando a pessoa quer testar o próprio raciocínio sob pressão, ou usa qualquer gatilho do tipo "me grelha", "me interroga", "grill me", "stress-test".
---

Entreviste a pessoa sem trégua até chegar a um entendimento compartilhado. Mapeie isso como uma
**árvore de decisões**: cada decisão se ramifica nas decisões que dependem dela.

Trabalhe a árvore em **rodadas**. A **fronteira** é toda decisão cujos pré-requisitos já estão
resolvidos: as perguntas que dá para fazer _agora_ sem chutar respostas que você ainda não ouviu.
Faça a fronteira inteira numa rodada só: numere cada pergunta e dê a sua resposta recomendada.
Depois espere as respostas da pessoa antes da próxima rodada.

Cada pergunta segue este formato:

```
❓ **Q1** - **<título da pergunta>**: <corpo da pergunta, pode ter vários parágrafos, incluindo alternativas>

➡️ <a sua resposta recomendada>
```

Cada rodada de respostas remodela a árvore: decisões resolvidas empurram a fronteira para fora e
desbloqueiam perguntas que dependiam delas. Recalcule a fronteira e faça a próxima rodada. Uma
pergunta cuja resposta depende de outra ainda aberta nesta rodada pertence a uma rodada
_posterior_, não a esta.

Descobrir _fatos_ é trabalho seu, nunca da pessoa. Quando uma pergunta da fronteira precisa de
um fato do ambiente (sistema de arquivos, ferramentas, etc.), despache um subagente para
buscá-lo; não peça à pessoa nada que você mesmo consiga consultar. Não bloqueie nisso: uma
exploração em andamento é um pré-requisito não resolvido, então só as perguntas a jusante dela
esperam o subagente reportar; faça o resto da fronteira agora. As _decisões_ são da pessoa:
apresente cada uma e espere.

A sessão termina quando a fronteira está vazia: todo ramo da árvore visitado, nada deixado em
suposição silenciosa. Não aja sobre o resultado até a pessoa confirmar que vocês chegaram a um
entendimento compartilhado.
