# Lições: o que foi aprendido e não pode ser recalculado

Escrito em <data>.

**O que este arquivo é.** O `CLAUDE.md` diz o que é verdade agora. Este arquivo diz o que foi
aprendido, e por quê. Todo número que pode ser puxado de novo de uma API, de um arquivo ou de uma
página fica de fora, de propósito: o trabalho recalcula. O que entra é o que não se recalcula: o
que foi aprendido, o que foi confirmado por escrito, e o que precisa ser re-verificado antes que
alguém repita.

**Nada nas seções 4 e 5 é um fato sobre o estado de hoje.** É o último estado verificado, datado,
para re-checar.

---

## 1. Regras de método, cada uma aprendida de um erro real

O formato: a regra em negrito, o erro concreto que a gerou, e o que ela ensinou. Adicione no
fim. Nunca apague uma regra: se ela deixou de valer, escreva por quê embaixo dela.

- **Conte você mesmo.** <Exemplo: um total foi reportado a partir do resumo que o modelo fez de
  um arquivo; a contagem direta deu outro número. Um resumo nunca é uma fonte.>
- **Cheque ao vivo, naquele dia, e date a afirmação.** <Exemplo: itens reportados como problema
  já tinham sido corrigidos quando o relatório foi lido. Coisas mudam por baixo de você.>
- **Descarte o método antes de reportar o resultado.** <Exemplo: uma página de bloqueio que
  retorna zero resultados parece exatamente um defeito corrigido.>
- **Verifique se o recurso ainda existe antes de pontuar a ausência dele.** <Exemplo: um
  rascunho criticou a falta de algo que a plataforma já tinha removido.>
- **Olhe antes de afirmar o que um documento contém.** <Exemplo: "não menciona X" escrito antes
  de abrir; mencionava.>
- **Nunca deixe uma citação afirmar mais do que ela diz.** Nível 1 é o que a plataforma
  documenta. Nível 2 é o que um funcionário dela disse publicamente, com o contexto. Nível 3 é
  consenso de praticantes ou nosso julgamento. Rotule qual está usando.
- **Não editorialize sobre quem fez o quê.** Fatos e datas. Suposições rotuladas como
  suposições. Nenhum crédito ou culpa num documento que sai para outra pessoa.
- **Cheque um grupo de controle antes de atribuir um padrão a alguém.** <Exemplo: um padrão
  visto em toda a lista examinada parecia obra de quem a lista tinha em comum; sete casos que
  essa pessoa nunca tocou mostravam o mesmo padrão na mesma semana.>
- **Um token que autentica não é um token que funciona.** <Exemplo: a tela disse "autenticação
  concluída" e o token via uma coisa e lia nada. O teste é uma leitura real de dados.>
- **Uma regra que vive num documento e não no código não é uma regra.** <Exemplo: uma regra
  escrita no CLAUDE.md foi violada por um script no dia seguinte porque nada a impunha.>
- **Uma checagem de completude precisa nomear as colunas que contam como resposta.** <Exemplo:
  contar qualquer célula não vazia chamou de "completo" um arquivo cujas colunas de resposta
  estavam todas vazias.>
- **Normalização pode fabricar um achado.** <Exemplo: uma contagem de loops era um artefato do
  tratamento de barra final.>

---

## 2. Os conceitos que eu domino, nas frases que eu uso

Um conceito por item, escrito do jeito que eu explicaria em voz alta. Se eu não consigo escrever
a frase, eu não domino o conceito ainda.

- **<Conceito>:** <a explicação em uma ou duas frases, com a analogia que funcionou>.
- **<Conceito>:** <...>

---

## 3. Confirmado por escrito

O que alguém confirmou por escrito, com quem, onde e quando. É o que sustenta uma afirmação
quando alguém pergunta "quem disse isso".

- <O quê>, confirmado por <nome>, em <canal>, <data>.

---

## 4. Último estado verificado. RE-VERIFICAR TUDO.

Por item ou conta: o que foi visto, em que data, com que método. Não é o estado de hoje.

- **<Item>**, verificado <data>: <estado>. Método: <script ou leitura>.

---

## 5. Decisões que ainda governam

Decisões tomadas por alguém que continuam valendo, com quem tomou e quando. Quando uma deixa de
valer, ela sai daqui e a nova entra no `CLAUDE.md`.

- <Decisão>, <nome>, <data>.

---

## 6. Glossário

Termos, siglas, nomes de documentos e IDs que aparecem no projeto e que uma sessão nova não
reconheceria.

| Termo | O que é |
|---|---|
| <termo> | <definição> |
