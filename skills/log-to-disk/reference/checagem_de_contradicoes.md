# A checagem de contradições

Rodar antes de escrever no `CLAUDE.md`, toda vez. É o passo que impede o arquivo de virar o que
virou no projeto de origem: 133 KB, 31 seções, 24 contradições vivas, cinco instruções
concorrentes de "leia isto primeiro".

## O que buscar

Para toda entidade que o material novo toca, dar grep no `CLAUDE.md` e ler o que ele diz hoje:

- o identificador do item e o nome de exibição dele (cliente, conta, módulo)
- o nome da pessoa
- o nome do arquivo da ferramenta ou do script
- qualquer contagem que o material novo muda (contas, linhas, páginas, cartões, itens)
- a data ou a janela que o material novo usa

## As classes que continuam aparecendo

**1. Uma contagem dita três vezes com três valores.** "As contas" foram 34, 30, 28, 29, 26, 42 e
43 num só arquivo, todas corretas para perguntas diferentes. Correção: uma tabela de escopo que
define cada número uma vez, e toda outra menção aponta para ela. Nunca escrever uma contagem nua.

**2. Um número sem denominador.** "226 conjuntos em 16 itens, 63% de falha" e "293 linhas em 25
itens" são ambos verdadeiros sobre a mesma tabela: um é o subconjunto medido, o outro é o
tamanho da tabela. Correção: toda taxa carrega do que ela é taxa.

**3. Uma janela datada pelo dia em que a consulta rodou.** "92 dias até dia 7" quando todo pull
termina no dia 5. Correção: ler a janela dos dados, nunca da memória.

**4. Um item aberto que já está fechado.** Listas de abertos sobrevivem ao trabalho. Correção: em
toda execução, percorrer as listas de abertos e tirar o que o digest mostra como feito.

**5. A função de uma pessoa descrita de dois jeitos.** Correção: uma frase por pessoa, na seção de
pessoas.

**6. Uma ferramenta descrita pela implementação antiga.** Um script ficou documentado com o estilo
antigo por horas depois de ter sido reescrito, no `CLAUDE.md` **e** num arquivo de memória.
Correção: quando uma ferramenta muda, dar grep nos dois lugares.

**7. Um arquivo substituído ainda no lugar onde o leitor o acha primeiro.** Correção: mover
arquivos substituídos para `archive/superseded/` na mesma execução que os substitui.

**8. Vários ponteiros de "leia isto primeiro".** Cada handoff de sessão acrescentou um e nenhum
removeu o anterior. Correção: exatamente um, no Estado atual.

**9. Uma regra que caiu mas continua escrita.** "Menos de 300 palavras" sobreviveu à decisão de
que contagem de palavras não é regra. Correção: quando uma regra cai, apagar em vez de acrescentar
a contradição ao lado.

**10. Trabalho feito num item fora do escopo.** Correção: quando um número é computado sobre o
conjunto inteiro, checar a coluna de escopo e excluir, dizendo isso.

## O que fazer com cada contradição encontrada

- **Fato novo substitui o antigo:** editar a linha antiga. Nunca deixar as duas de pé.
- **A linha antiga nunca foi verdade:** corrigir, e se o erro ensina uma regra de método,
  acrescentar uma linha em "Correções que precisam sobreviver".
- **Ambas verdadeiras, perguntas diferentes:** manter as duas e escrever a cláusula que as
  distingue em cada uma.
- **Não dá para saber qual é verdade:** não chutar e não tirar média. Colocar em "Ainda
  desconhecido" com os dois valores e o que decidiria, e dizer isso no recibo.

## Depois da checagem

Reportar as contradições encontradas no recibo, mesmo quando não há nenhuma, como contagem. Uma
execução que reporta zero toda vez é uma execução que não está olhando.
