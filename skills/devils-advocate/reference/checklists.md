# Checklists por gênero

Aplicados no passo 5 de toda rodada. Cada item é passa, falha ou não se aplica; só as falhas são
reportadas, cada uma como preocupação com a classe de falha. Os itens são gerais o bastante para
qualquer cliente, gestor ou relatório. Os detalhes do projeto (pessoas, datas, limiares, qual
planilha é a de registro) vêm do `CLAUDE.md`, do `LESSONS.md` e da memória na hora de rodar, não
deste arquivo.

## E-mail (para um gestor, um colega ou um cliente)

1. Responde a pergunta que de fato foi feita, nas primeiras linhas, antes do contexto.
2. Toda afirmação sobre o estado de um site, conta, ferramenta ou arquivo carrega a data em que
   foi observada.
3. Todo número rastreia até um arquivo, consulta ou script que existe no disco hoje.
4. Nada de um documento arquivado ou substituído é citado como atual.
5. Dependências são enquadradas como pedidos de acesso ou ferramenta, não como pedidos de ajuda.
   Profundidade não é oferecida em troca de uma data.
6. O que não está na alçada de quem escreve (processo, preço, estratégia, a área de outra pessoa)
   é proposto, não decidido.
7. Datas e durações são dias corridos, com as datas reais.
8. Anexos ou links citados existem e batem com o que o texto diz deles.
9. Nenhum crédito ou culpa atribuído; fatos e datas.
10. Nada confidencial sai da fronteira a que pertence (dados de cliente, credenciais, termos
    comerciais, números de outro cliente).
11. O pedido, se há um, é explícito: quem faz o quê até quando.
12. Regras de estilo da casa respeitadas (por exemplo, sem travessão, se essa for a regra).
13. As preferências conhecidas do destinatário, do contexto do projeto, são respeitadas (formato,
    evidência anexada, nível de detalhe).
14. Todo "eu pedi", "eu enviei", "eu avisei", "eu registrei" bate com um registro datado; senão
    está no futuro com prazo.
15. O texto checado é o artefato vivo que o destinatário vai ler, não o arquivo por trás.
16. Toda hora escrita foi lida do relógio da máquina no mesmo passo.
17. Toda afirmação sobre o estado atual de um sistema de tarefas, um canal ou um índice foi
    verificada por leitura ao vivo nesta execução, não contra um pull salvo; um pull salvo é
    evidência da data em que foi tirado, nada depois.

## Achado (de auditoria, de análise, de investigação)

1. Contado por script ou consulta, nunca no olho; o script ou a consulta é nomeado.
2. Checado ao vivo numa data declarada; não carregado de uma checagem anterior.
3. O método foi descartado como causa do resultado (páginas de bloqueio, limites de exportação,
   renderização, amostragem, limitação de taxa).
4. Um grupo de controle foi checado antes de qualquer padrão ser atribuído a um ator, e todo
   membro de uma classe foi checado antes de um mecanismo ser atribuído à classe.
5. Toda afirmação externa carrega o nível de evidência e é redigida nesse nível.
6. O que foi examinado é o que importa (o que carrega resultado), não o que era mais fácil de
   achar.
7. O que apareceu desde a medição anterior é reportado antes de qualquer outra coisa.
8. Suposições são rotuladas como suposições, com o que as confirmaria.
9. O limite do método é declarado (por exemplo, correspondência exata dá um piso).
10. O achado nomeia a métrica que importa, não uma métrica de volume.
11. O achado se liga ao mecanismo documentado do próprio cliente ou da própria empresa, onde
    existe um.
12. Ações recomendadas carregam a classe de risco onde a metodologia define uma, e qualquer coisa
    que mova algo em produção é marcada para aprovação.

## Relatório ou entregável

1. O sinal verde explícito da pessoa para este documento está registrado.
2. O escopo bate com o que foi pedido: nada estreitado, alargado ou transformado em silêncio.
3. Todo número no texto bate com o arquivo de dados de onde veio, nesta execução.
4. Nenhum número arquivado, substituído ou anterior ao acesso é apresentado como atual.
5. Toda afirmação de estado é datada; o relatório declara a janela que cobre.
6. Efeitos sazonais ou estruturais são separados dos achados antes de uma tendência virar achado
   (ano contra ano, janelas comparáveis, mudanças de medição).
7. Limites e itens não verificáveis são declarados no documento, não omitidos.
8. Nada inferido é afirmado como fato.
9. O leitor consegue agir: cada achado tem um dono, um próximo passo ou uma decisão necessária.
10. Estilo da casa respeitado: idioma, dias corridos, terminologia dos documentos do próprio
    projeto.
11. A pessoa conseguiria explicar cada afirmação do documento em voz alta.
12. Todo achado no texto, incluindo uma frase dentro de um item maior, carrega severidade na
    escala do projeto, a consequência na métrica que paga, um dono, e um próximo passo ou uma
    pergunta.
13. Qualquer causa atribuída a uma classe (plataforma, CMS, tipo de página, plugin) foi checada
    em todo membro dessa classe presente nos dados.
14. Todo "eu pedi", "eu enviei", "eu avisei", "eu registrei" bate com um registro datado; senão
    está no futuro com prazo.
15. O texto checado é o artefato vivo que o destinatário vai ler, não o arquivo por trás.
16. Toda hora escrita foi lida do relógio da máquina no mesmo passo.

## Plano ou decisão (modo interrogatório)

1. A meta é explícita e mensurável; um alvo vago é falha.
2. As premissas estão listadas, e cada uma está verificada, contradita ou reconhecida como
   suposição.
3. Que evidência mudaria a decisão está declarado.
4. O que depende de outra pessoa está nomeado, e enquadrado como pedido de acesso ou de decisão.
5. Qualquer coisa que mude processo ou metodologia documentada é encaminhada ao dono desse
   processo, não decidida aqui.
6. O custo de estar errado está declarado, e se o passo é reversível.
7. A ordem dos passos segue o risco, não a conveniência.
8. Profundidade não é trocada por uma data.
9. O plano não depende de ferramenta, acesso ou pessoa que não está confirmada disponível.
10. A pessoa consegue explicar o plano e as razões dele em voz alta.
