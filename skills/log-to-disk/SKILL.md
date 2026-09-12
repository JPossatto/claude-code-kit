---
name: log-to-disk
argument-hint: "[full | <session-id>] (padrão: desde a última âncora)"
description: Passagem completa pela transcrição da sessão no disco, escrevendo toda decisão, fato, correção, promessa, ferramenta e arquivo que ainda não está registrado no arquivo a que pertence, e depois checando o material novo contra o CLAUDE.md e corrigindo o que ele contradiz. Roda o passe de advogado do diabo sobre a lista de afirmações extraída antes de escrever qualquer coisa. Invocar em /log-to-disk, a cada quinto prompt da pessoa (a regra dos 5 prompts), no fim de uma sessão, e sempre que a pessoa mandar registrar, escrever tudo, salvar isso, ou perguntar se algo foi anotado.
---

# Log to disk

O valor de um projeto está no disco, não em nenhuma conversa. Um fato que existe só num chat se
perde no momento em que a janela fecha ou compacta. Este skill é o mecanismo que impede isso, e
é a implementação da regra dos 5 prompts.

Não é um resumidor. Um resumo de sessão é um documento novo que ninguém lê. Isto escreve nos
arquivos que já são lidos: o estado no `CLAUDE.md`, `notes/TASKS.md`, o registro de achados, o
registro de cada cliente ou item, os arquivos de memória.

## As três coisas que o diferenciam de anotar à mão

1. **Ele lê a transcrição do disco, não do contexto.** Depois de uma compactação, o chat no
   contexto é um resumo de um resumo; o JSONL da transcrição é o que foi dito de fato. Por isso o
   skill ainda funciona às 2 da manhã numa sessão que rodou o dia inteiro.
2. **O passe de advogado do diabo roda sobre a lista de afirmações extraída, não sobre a
   conversa.** Uma lista de afirmações é concreta o bastante para verificar. Uma conversa não é.
3. **Ele corrige, não acrescenta.** Toda execução checa o material novo contra o que o `CLAUDE.md`
   já diz e conserta a contradição. Sem este passo o arquivo cresce até se contradizer, que foi
   exatamente o que aconteceu no projeto de origem (24 contradições em 133 KB).

## Rodar

```
/log-to-disk              desde a última âncora desta sessão (o padrão)
/log-to-disk full         a sessão inteira, ignorando a âncora
/log-to-disk <session-id> outra sessão, por exemplo uma que rodou em outra janela
```

Anunciar em uma linha antes de começar, e de novo em uma linha quando o recibo for impresso.

## Os sete passos

### 1. Extrair

```
python "<pasta-de-skills>/log-to-disk/scripts/session_extract.py" [--full] [--session <id>]
```

O script descobre a pasta de transcrições do projeto a partir do diretório de trabalho atual
(ou de `--project` / da variável `LOG_PROJECT_DIR`), escolhe a transcrição mais nova, diz qual
arquivo escolheu, e emite: cada prompt da pessoa por inteiro, a prosa do assistente aparada, e
uma linha por efeito colateral (arquivo escrito, arquivo editado, comando rodado, mensagem
rascunhada ou enviada). As horas são convertidas para o fuso local da máquina.

`--list` mostra as sessões do projeto. Se dois chats rodaram em paralelo, rodar o skill uma vez
por id de sessão em vez de confiar que o arquivo mais novo é o certo.

### 2. Classificar

Percorrer o digest e puxar só isto. Todo o resto é conversa, não registro.

- **Decisões** da pessoa, com as palavras dela onde são curtas e a razão onde ela deu uma.
- **Fatos estabelecidos**, com o método que os estabeleceu e a data.
- **Correções** a algo em que se acreditava antes, incluindo correções ao meu próprio trabalho.
- **Promessas e compromissos**, da pessoa a alguém, ou meus à pessoa, com o prazo.
- **Regras** sobre como ela quer que eu trabalhe.
- **Artefatos**: arquivos, scripts, ferramentas, planilhas, documentos, cartões, rascunhos
  criados ou enviados.
- **Perguntas abertas e coisas bloqueadas em outras pessoas**, com quem deve o quê.

### 3. Checar o que já está no disco

Para cada item, ler o destino e ver se já está lá. Idempotência é o ponto: rodar o skill duas
vezes tem de escrever nada na segunda. Não confiar na memória de ter escrito antes na sessão;
checar o arquivo.

### 4. Advogado do diabo, sobre a lista de afirmações

Escrever os itens candidatos como lista numerada de afirmações, cada uma com o destino
proposto, e rodar o skill `devils-advocate` sobre essa lista. Corrigir o que voltar antes de
escrever qualquer coisa. As regras que mais importam aqui, das classes de falha daquele skill:

- Verificar contra uma **leitura ao vivo nesta execução**, não contra um pull anterior da mesma
  sessão (F03 com F04). Estado de tarefas, de canal e de índice vence em horas.
- **Contar por script.** Nenhum número entra num arquivo por ter sido lido de uma tabela no olho.
- **Nomear as colunas que contam como resposta** antes de chamar qualquer coisa de completa.
- Qualquer coisa inferida é escrita com a palavra inferência e a base dela, nunca como fato.
- Datar toda frase sobre o estado de alguma coisa.

### 5. Rotear

Um destino por item, conforme `reference/roteamento.md`. A regra que governa todos:
**o `CLAUDE.md` guarda estado, as notas guardam a narrativa.** Se o item é "o que é verdade agora",
vai para o `CLAUDE.md` e substitui a linha que não é mais verdade. Se é "o que aconteceu hoje",
vai para uma nota datada em `notes/` e o `CLAUDE.md` recebe no máximo um ponteiro.

### 6. Checagem de contradições

Antes de escrever no `CLAUDE.md`, dar grep nele por toda entidade que o material novo toca (o
nome do cliente ou do item, o nome da pessoa, a ferramenta, a contagem) e ler o que ele diz
hoje. Então:

- Se o fato novo substitui um antigo, **editar a linha antiga**. Não deixar as duas.
- Se a linha antiga nunca foi verdade, corrigir e acrescentar uma linha em "Correções que precisam
  sobreviver" se o erro ensina uma regra de método.
- Se uma contagem mudou, checar todo outro lugar em que ela aparece.
- Se o item fecha algo listado como aberto, tirar da lista de abertos.

Reler o `CLAUDE.md` imediatamente antes de editá-lo, porque outro chat pode ter escrito nele
enquanto este trabalhava. Editar por substituição ancorada, nunca reescrevendo uma seção inteira
a partir de uma cópia lida antes.

### 7. Recibo, depois âncora

Imprimir uma tabela curta: item, destino, e a linha que prova que ele está no arquivo agora, lida
de volta depois da escrita. Então fixar a âncora:

```
python "<pasta-de-skills>/log-to-disk/scripts/session_extract.py" --set-anchor [--session <id>]
```

Fixar a âncora só depois de as escritas estarem verificadas. Se uma escrita falhou, deixar a
âncora onde está para que a próxima execução pegue o item de novo.

## O que nunca entra

- Credenciais, chaves de API, senhas, dados de cartão e telefone.
- Rascunhos substituídos, e abordagens tentadas e abandonadas, a não ser que a lição seja o ponto.
- Números brutos que pertencem a um CSV. Escrever o CSV e referenciar.
- Qualquer coisa fora do escopo do projeto (ver a tabela de escopo do `CLAUDE.md`).

## Sessões paralelas

Dois chats escrevem na mesma pasta ao mesmo tempo, e é por isso que a regra existe. Portanto:

1. Escrever a nota datada primeiro. Nenhuma outra sessão está mexendo nela, então não há
   conflito.
2. Depois editar o `CLAUDE.md` e os arquivos de memória, relendo cada um imediatamente antes da
   edição.
3. Se uma seção parece diferente do que o digest espera, outra sessão a escreveu. Ler, mesclar, e
   dizer isso no recibo em vez de sobrescrever.

## Referência

- `reference/roteamento.md`: o mapa de destinos, tipo de item por tipo de item.
- `reference/checagem_de_contradicoes.md`: o que buscar, e as classes de contradição que
  continuam aparecendo.
