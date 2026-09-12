# Classes de falha

O registro de como o assistente já errou. Toda preocupação num relatório de advogado do diabo
nomeia uma destas. Quando um erro não cabe em nenhuma, o relatório propõe uma entrada nova e ela
só é adicionada quando a pessoa diz. Cada entrada: o padrão, a checagem que o pega, e um exemplo.

Os exemplos vêm de um projeto real de auditoria de SEO e foram anonimizados. Substitua pelos
seus conforme aparecerem. Adicione no fim. Não renumere.

## F01 Inferido, afirmado como fato

**Padrão.** Uma conclusão que segue plausivelmente da evidência é escrita como se tivesse sido
observada. "Fulano fez os redirecionamentos" quando tudo que se observou foi que redirecionamentos
apareceram na semana em que Fulano ainda estava na empresa.
**Checagem.** Para cada afirmação, perguntar: isto foi observado ou deduzido? Deduções são
rotuladas "suposição" ou "provável", com o que as confirmaria.
**Exemplo.** Uma auditoria de vários dias: catorze achados no passe de advogado do diabo, todos
uma inferência apresentada como fato.

## F02 Contado no olho

**Padrão.** Um número lido de uma tabela, de um resumo ou de uma tela em vez de computado dos
dados. Também: um número tirado do resumo que o modelo fez de um arquivo, e não do arquivo.
**Checagem.** Toda contagem e toda porcentagem rastreiam até um script, uma consulta ou uma
enumeração explícita. Se não rastreia, não está verificada.
**Exemplo.** "Dezenove contas em queda" lido de uma tabela no olho; o script disse dezesseis. Um
sitemap reportado com 368 URLs a partir de um resumo; a contagem direta deu 435.

## F03 Contexto vencido

**Padrão.** Um fato que era verdade quando foi escrito no `CLAUDE.md`, na memória ou numa nota,
e que desde então mudou no disco ou no mundo, é repetido como atual. É a falha mais comum e a
mais difícil de ver, porque o fato errado está documentado.
**Checagem.** Qualquer fato tirado do `CLAUDE.md`, da memória ou de uma nota é checado contra a
fonte por baixo (arquivo, banco, ferramenta, registro datado) nesta execução. Quando discordam,
a fonte por baixo vence e o fato documentado é corrigido na hora. Para o estado de um sistema
vivo (tarefas, canal, índice, perfil, caixa de e-mail) a fonte por baixo é uma leitura ao vivo
nesta execução, nunca um pull salvo: o pull já é contexto vencido no momento em que é escrito.
**Exemplo.** Um arquivo de memória ainda dizia "7 fora" e "a planilha ao vivo vem quando a API
for habilitada" depois de o `CLAUDE.md` registrar 6 fora (contado por script) e a planilha ter
sido construída naquele mesmo dia.
**Exemplo.** Um post dizia "3 páginas em Publicação, todas com a mesma pessoa", verificado contra
um pull de dois dias antes. Um GET ao vivo na mesma hora mostrou uma página em outro estágio com
outra pessoa e as outras duas como a mesma URL cadastrada duas vezes. A chamada não custava nada
e não foi feita.

## F04 Afirmação de estado sem data

**Padrão.** "A página redireciona", "o sitemap tem 435 URLs", "o site está em redesign", sem
data. Sites e contas mudam por baixo do trabalho; uma afirmação de estado sem data não pode ser
falsificada nem rechecada.
**Checagem.** Toda afirmação sobre o estado de um site, conta, arquivo ou ferramenta carrega a
data em que foi observada.
**Exemplo.** Cinco URLs "concorrentes" reportadas que já eram redirecionamentos quando o relatório
foi lido; uma URL mudou entre duas checagens com vinte minutos de intervalo.

## F05 Artefato do método

**Padrão.** A medição produziu o resultado, não a coisa medida. Uma página de bloqueio de
firewall retornando zero ocorrências parece um defeito corrigido; um 403 parece uma página
morta; uma exportação de interface limitada a 1.000 linhas parece uma lista completa.
**Checagem.** Antes de reportar um resultado, dizer como o método poderia tê-lo produzido sozinho,
e o que foi feito para descartar isso.
**Exemplo.** 403s de um firewall contados como páginas mortas de sitemap em quatro sites. Eram
bloqueios.

## F06 Citação acima do nível dela

**Padrão.** Uma observação de praticante, um post de fórum ou o julgamento do próprio assistente é
apresentado com a autoridade da documentação oficial. Ou a fala de um funcionário da plataforma é
citada sem o contexto.
**Checagem.** Toda afirmação externa carrega o nível: 1 (documentado pela plataforma), 2
(funcionário da plataforma em registro público, com contexto), 3 (consenso de praticantes ou
nosso julgamento). A afirmação é redigida na força do nível dela.
**Exemplo.** "A plataforma remove os metadados no upload" afirmado como fato; é observação de
praticante, nível 3.

## F07 Atribuição sem grupo de controle

**Padrão.** Um padrão visto em tudo na única lista examinada é atribuído à única coisa que essa
lista tem em comum. Coocorrência dentro de uma lista não é evidência de causa comum.
**Checagem.** Antes de atribuir um padrão a uma agência, a um cliente ou a qualquer ator, checar um
grupo de controle que esse ator nunca tocou.
**Exemplo.** Backlinks com cara de comprados em 38 de 39 domínios de uma mesma conta pareciam
uma compra. Sete concorrentes que a conta nunca tocou carregavam as mesmas âncoras na mesma
semana. Spray de mercado, sem escalada.

## F08 Editorial sobre quem fez o quê

**Padrão.** Crédito ou culpa atribuídos num documento que deveria dizer fatos e datas. "O SEO
anterior quebrou o site."
**Checagem.** Texto para cliente ou para gestor diz o que aconteceu e quando. Atores são nomeados só
quando o fato está confirmado, e nunca com julgamento junto.
**Exemplo.** Um rascunho atribuiu redirecionamentos a uma pessoa nomeada antes de a pessoa
responsável confirmar.

## F09 Volume tomado por resultado

**Padrão.** Impressões, páginas publicadas, posições melhoradas, links adquiridos, tratados como
resultado. O resultado é o que paga: cliques que viram clientes, chamadas, vendas.
**Checagem.** Toda afirmação de "melhorou" nomeia a métrica que paga. Métricas de volume são
contexto, não achado.
**Exemplo.** Um diretório que melhorou em impressões e posição por três meses produziu zero
cliques.

## F10 Pontuar a ausência de algo que não existe mais

**Padrão.** Um recurso, regra ou padrão é checado sem antes checar se ainda existe.
**Checagem.** Antes de pontuar uma ausência, confirmar que o recurso ou a exigência é atual, com
fonte datada.
**Exemplo.** Um rascunho criticou um cliente por não ter uma seção de perguntas e respostas no
perfil. A plataforma tinha removido a seção meses antes.

## F11 Olhar depois de afirmar

**Padrão.** Uma afirmação sobre o que um perfil, página, arquivo ou documento contém, escrita
antes de abri-lo.
**Checagem.** Qualquer "não contém" ou "não menciona" nomeia a coisa que foi aberta e quando.
**Exemplo.** "Nenhum item aponta para uma página de serviço" escrito antes de olhar; o item atual
apontava.

## F12 Páginas novas absorvidas em silêncio

**Padrão.** Um censo ou pull encontra páginas que não estavam no anterior, e elas entram nos
totais sem serem reportadas.
**Checagem.** Todo pull é comparado com o anterior da mesma conta; adições são reportadas antes
de tudo e o escopo delas é questionado.
**Exemplo.** Treze páginas de um site reescritas num template entre duas medições, descobertas só
porque o teste foi rodado de novo.

## F13 Contornar uma lacuna de ferramenta que deveria ser pedida

**Padrão.** Um acesso, ferramenta ou fonte de dados que falta é contornado com uma estimativa,
um proxy ou um passe mais leve, em vez de nomeado como pedido.
**Checagem.** Toda dependência de algo que não está em mãos é enquadrada como pedido explícito de
acesso ou ferramenta. Profundidade nunca é cortada para cumprir uma data.
**Exemplo.** O primeiro plano propôs passes mais curtos como alternativa e pediu ajuda a um gestor
com uma liberação em vez de pedir o acesso.

## F14 Achado sem consequência ou sem dono

**Padrão.** Um fato verdadeiro é solto num relatório como observação, sem severidade, sem
consequência na métrica que paga, sem dono e sem próximo passo. O leitor não consegue agir e o
autor não sabe dizer o que acontece com ele.
**Checagem.** Todo achado num entregável, incluindo uma frase dentro de um item maior, carrega
severidade na escala do projeto, a consequência na métrica que paga, um dono, e um próximo passo
ou uma pergunta. Números verificados não dispensam o "e daí".
**Exemplo.** Um relatório de primeiro dia: "as páginas principais do site estão no índice como
soft 404" passou por um passe de verificação com todos os números certos. Era prioridade
máxima: 13 das 20 páginas principais, um quarto das impressões do site, e nada na frase dizia
quem corrige nem até quando.

## F15 Mecanismo generalizado a uma classe sem checar os outros membros

**Padrão.** Uma causa é atribuída a uma categoria ("é assim que páginas só de JavaScript aparecem
para o Google", "sites dessa plataforma fazem isso") quando os dados no disco têm outros membros
da categoria que não mostram o mesmo. F07 é o mesmo erro para atores; este é para mecanismos.
**Checagem.** Antes de nomear uma causa para uma classe, todo membro da classe nos dados é
checado. Se os outros estão limpos, a causa é específica do caso e é redigida assim.
**Exemplo.** O estado de soft 404 foi explicado como inerente a páginas de uma plataforma. Os
outros três sites da mesma plataforma tinham 18 ou 19 das 20 páginas principais indexadas
normalmente; a causa era específica daquela construção.

## F16 Ação dita como feita que só foi agendada

**Padrão.** "Já pedi ao Fulano", "já pedi para segurarem as mudanças", escrito num relatório
porque o pedido está na lista de tarefas, antes de ter sido enviado.
**Checagem.** Todo "eu pedi", "eu enviei", "eu avisei", "eu registrei" num entregável é casado com
um registro datado; sem registro, a frase é reescrita no futuro com prazo.
**Exemplo.** Três pedidos num rascunho de relatório estavam na lista do dia e nenhum tinha saído;
a pessoa confirmou "nenhum dos três foi".

## F17 Hora escrita do relógio errado

**Padrão.** Uma hora derivada de uma leitura não confiável do relógio (um nome de fuso que não
resolve, UTC tomado como local, uma hora copiada de uma nota) e escrita no log, no `CLAUDE.md` ou
num relatório como observada.
**Checagem.** O relógio é lido no mesmo comando que escreve a hora, numa fonte cujo fuso é
conhecido. Uma hora registrada que discorda da hora de modificação de um arquivo é marcada, e o
arquivo vence.
**Exemplo.** `TZ=America/Sao_Paulo date` no Git Bash do Windows imprimiu UTC rotulado como GMT;
toda hora escrita por uma hora inteira estava três horas adiantada e foi corrigida no disco.

## F18 Verificou o arquivo fonte, não o artefato que o destinatário vê

**Padrão.** O passe lê o arquivo que alimentou um documento e verifica esse arquivo, enquanto o
documento vivo (uma aba de documento, um rascunho de mensagem, uma planilha) contém outra coisa,
porque alguém editou ou colou uma versão antiga.
**Checagem.** O alvo de um passe é lido ao vivo, de onde o destinatário vai lê-lo, e comparado com
o arquivo; quando diferem, o vivo é o alvo e a diferença é a primeira preocupação reportada.
**Exemplo.** O arquivo tinha um relatório de 365 palavras com "registrei os pedidos de remoção"; a
aba do documento tinha o rascunho longo anterior com "não vou registrar pedidos de remoção". A
pessoa pegou depois de o passe ter aprovado o arquivo.
