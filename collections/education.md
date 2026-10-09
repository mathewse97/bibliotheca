---
id: education
image:                      # foto de fundo do cartão — interface-rules.md §5
  file: "images/collections/education.webp"
  subject: "Iluminura de Laurentius de Voltolina (séc. XIV): aula de Henricus de Alemannia na Universidade de Bolonha"
  supplied_by: mathews
  added: 2026-09-25
title_pt: "Educação"
question: "O que é formar um ser humano — que fins a educação deve perseguir,
           por que meios, e que respostas diferentes tradições e épocas deram
           a essa pergunta?"

# ---------------------------------------------------------------------------
# AS QUATRO CAMADAS — distintas, e nunca uma a definir a outra.
#
#   1. ESCOPO      o território que a coleção reivindica. Deriva da PERGUNTA.
#                  Não deriva, em nenhuma circunstância, do que já está aqui.
#   2. SCOPE_MAP   as regiões desse território, com o estado de cobertura de
#                  cada uma. É contra isto que a análise de lacunas mede.
#   3. MOVIMENTOS  como o que a coleção HOJE contém está organizado. Um
#                  movimento agrupa obras existentes; não reivindica território.
#   4. CAMINHOS    rotas alternativas sobre os membros atuais.
#
#   E, à parte das quatro: a LISTA DE BOOTSTRAP, que é uma amostra do
#   território — não a sua definição.
#
# CORREÇÃO DE MÉTODO (2026-09-05): a primeira versão deste arquivo derivou os
# inclusion_criteria das 9 obras importadas. Isso estava errado por construção:
# critérios inferidos do conteúdo descrevem o conteúdo, e uma coleção definida
# pelo que já contém não pode ter lacunas — a análise de cobertura passaria a
# confirmar a biblioteca em vez de a interrogar. Critérios derivam da pergunta.
# ---------------------------------------------------------------------------

source:
  origin: sua-lista
  imported: 2026-09-05
  archived_at: sources/lists/educacao.md
sequence_kind: intellectual

lineage:
  - event: refined
    from: education
    to: education
    proposal: education--sp01
    approved_by: voce
    date: 2026-10-05
    reason: "A coleção passa a admitir obras sobre os meios da educação
             sustentados por evidência empírica, mesmo sem tese sobre os fins;
             ganha a região ciencia-da-aprendizagem e o movimento VIII."
    reversible_by: "Remover o critério marcado 2026-10-05 em
                    inclusion_criteria, a região ciencia-da-aprendizagem do
                    scope_map e o movimento VIII com as suas duas participações;
                    devolver às duas obras o bloco pending_assignment (o texto
                    está no histórico do Git). Nenhuma outra participação foi
                    movida."

provisional:
  inferred_by_claude: [role, demand, movement.purpose, inclusion_criteria,
                       movement.grouping]
  authored_by_you: [sequence_rationale, why_here, sequence]
  pending_confirmation: true
  see: review/education.md

# ---------------------------------------------------------------------------
# A LÓGICA DA SEQUÊNCIA É SUA — literal, sem paráfrase.
# Primeira coleção em que o argumento da ordem veio escrito por você.
# ---------------------------------------------------------------------------
sequence_rationale:
  by: voce
  text: "o que era a educação clássica → como ela foi transformada pelo
         cristianismo → como sobreviveu na Idade Média → como mudou no
         Renascimento e na modernidade → por que Adler quer recuperá-la →
         como o trivium estrutura essa formação → como aplicá-la na prática."
  stages: 7
  note: "Agrupei os seus 7 estágios em 4 movimentos porque cinco deles teriam
         uma obra só. A cadeia acima fica literal; o agrupamento é meu e é
         reversível. Ver review/education.md §2.2."

inclusion_criteria:            # derivados da PERGUNTA, não do conteúdo atual
  by: claude
  status: proposta
  criteria:
    - "Obras que argumentam sobre os fins da educação — o que um ser humano
       deve tornar-se e por que meios."
    - "Qualquer tradição, qualquer época, qualquer geografia. Clássica, cristã,
       humanista, iluminista, progressista, crítica, não ocidental: nenhuma
       está fora por ser o que é."
    - "Fontes primárias de uma tradição educativa e as obras históricas ou
       filosóficas que a interpretam, ambas."
    - "Defesas e críticas de uma mesma tradição pertencem ambas à coleção. A
       crítica de um ideal educativo é parte do estudo desse ideal."
    - "Fontes primárias têm precedência sobre comentadores; o comentador entra
       quando muda a leitura da fonte."
    - "Obras que argumentam sobre os MEIOS da educação a partir de evidência
       empírica — como se aprende, o que produz retenção, o que o cérebro faz
       ao aprender — ainda que não defendam uma tese sobre os fins. Entram pela
       pergunta, que reivindica os meios; não entram como manual de técnica.
       O que o out_of_scope exclui é mensuração sem argumento, não meios sem
       fins."
       # Acrescentado em 2026-10-05 por decisão sua (proposta education--sp01,
       # opção A do cartão d-edu-ciencia-aprendizagem). Ver `lineage`.
  out_of_scope:
    - "Administração e legislação escolar."
    - "Estudos empíricos de mensuração sem argumento sobre fins."
    - "Manuais de conteúdo (um livro de matemática não é uma obra sobre
       educação)."
  test_applied: "Nenhum critério acima exclui uma obra que responda claramente
                 à pergunta da coleção. Um critério que o fizesse estaria a
                 descrever a lista de bootstrap."

# ---------------------------------------------------------------------------
# SCOPE_MAP — o território reivindicado pela coleção.
#
# DUAS DIMENSÕES INDEPENDENTES, e é isso que impede que uma decisão sua seja
# lida como um defeito:
#
#   coverage: covered | thin | absent   — FATO. O que a coleção hoje contém.
#   pursuit:  open | not-pursued        — INTENÇÃO SUA. Se a região está ou
#                                         não sendo perseguida agora.
#
# Uma região `absent` + `not-pursued` não é uma falha nem uma pendência: é uma
# escolha registrada, e a análise de cobertura não a levanta. Uma região
# `absent` + `open` é apenas território ainda vazio — não uma compra devida.
# Nada aqui é uma fila de recomendações.
#
# `note` descreve o TERRITÓRIO — que perguntas caem nesta região. Nomes de
# obras candidatas não entram aqui: pertencem à camada de curadoria, em
# review/gaps/, e só quando existe um registro de lacuna que os justifique.
#
# Nenhuma região foi marcada `not-pursued`: essa decisão é sua, não minha.
# ---------------------------------------------------------------------------
scope_map:
  by: claude
  map_status: proposta
  regions:
    - {id: antiguidade-classica,     coverage: thin,   pursuit: open,
       held_by: [marrou--histoire-de-leducation-dans-lantiquite],
       note: "A paideía grega e a formação romana: ginásio, retórica, e o
              cidadão como produto da cidade."}
    - {id: cristianismo-antigo,      coverage: thin,   pursuit: open,
       held_by: [nunes--historia-da-educacao-na-antiguidade-crista],
       note: "A apropriação cristã da cultura clássica nos primeiros séculos:
              catequese, escolas cristãs, formação moral."}
    - {id: idade-media,              coverage: thin,   pursuit: open,
       held_by: [nunes--historia-da-educacao-na-idade-media,
                 jaeger--the-envy-of-angels],
       note: "Escolas monásticas e catedrais, universidades, escolástica, e as
              artes liberais como currículo."}
    - {id: renascimento-humanismo,   coverage: thin,   pursuit: open,
       held_by: [nunes--historia-da-educacao-no-renascimento],
       note: "Studia humanitatis: a redescoberta dos clássicos e a formação
              literária e moral do homem."}
    - {id: seculo-xvii,              coverage: thin,   pursuit: open,
       held_by: [nunes--historia-da-educacao-no-seculo-xvii],
       note: "Método, racionalismo e empirismo entram na educação; Reforma e
              Contrarreforma disputam a escola."}
    - {id: iluminismo-seculo-xviii,  coverage: thin, pursuit: open,
       note: "A ruptura ilustrada: natureza, autonomia, e a educação como
              formação do indivíduo contra a tradição herdada."}
    - {id: seculo-xix,               coverage: thin,   pursuit: open,
       held_by: [newman--the-idea-of-a-university, weber--wissenschaft-als-beruf],
       coverage_note: "2026-10-05: Newman é a defesa da formação liberal no
                       próprio século. `coverage` continua `thin` até você
                       revisar — detecção, não decisão.",
       note: "A universidade moderna e a escola nacional: o século em que o
              ideal de formação liberal foi defendido e desmontado. Weber
              entra pela ponta final dessa história — a universidade de
              pesquisa já consolidada, vista por dentro — e não pelo século
              XIX propriamente. Sustenta a região de raspão; não a fecha."}
    - {id: educacao-progressista,    coverage: thin, pursuit: open,
       held_by: [dewey--democracy-and-education],
       coverage_note: "2026-10-05: Dewey é a primeira obra que expõe a
                       posição por dentro. `coverage` continua `thin` até
                       você revisar — detecção, não decisão.",
       note: "Educação como experiência e como preparação para a democracia;
              crítica ao currículo transmitido."}
    - {id: pedagogia-critica,        coverage: thin, pursuit: open,
       note: "Educação como prática política: consciência, opressão e
              emancipação."}
    - {id: psicologia-do-desenvolvimento, coverage: thin, pursuit: open,
       note: "O aprender como processo psicológico — estágios, mediação,
              desenvolvimento — na medida em que argumenta sobre fins e não
              apenas mede."}
    - {id: critica-da-escola,        coverage: covered, pursuit: open,
       held_by: [illich--deschooling-society],
       note: "A recusa da forma escolar: desescolarização e crítica da escola
              como instituição."}
    - {id: tradicoes-nao-ocidentais, coverage: absent, pursuit: open,
       note: "Concepções de formação humana fora da linhagem greco-europeia."}
    - {id: ciencia-da-aprendizagem,  coverage: thin,   pursuit: open,
       held_by: [dehaene--how-we-learn, brown-roediger-mcdaniel--make-it-stick],
       note: "O estudo empírico de como se aprende: memória e recuperação,
              espaçamento, atenção, erro e consolidação, e o que disso tem
              consequência para ensinar e estudar. Distinta de
              psicologia-do-desenvolvimento, que é o aprender por estágios e
              mediação. Criada em 2026-10-05 (education--sp01). `thin`, e não
              `covered`: duas obras numa literatura grande, e uma região
              `thin` não é uma fila de compras."}
    - {id: educacao-classica-moderna, coverage: covered, pursuit: open,
       held_by: [adler--the-paideia-proposal, mcluhan--the-classical-trivium,
                 miriam-joseph--the-trivium, bauer-wise--the-well-trained-mind],
       note: "As recuperações contemporâneas do ideal clássico e das artes
              liberais como programa educativo."}

excluded: []                   # nada excluído por decisão — só por ausência

# ===========================================================================
# SEQUÊNCIA — a ordem neste arquivo É a ordem. Sua, sem alteração.
#
# Os movimentos ORGANIZAM o que a coleção hoje contém; não delimitam o que ela
# pode conter. Precedente estrutural: Política, onde fundações
# antigas, tradições não ocidentais, cristianismo medieval, marxismo, teoria
# democrática, crítica libertária e literatura política são subdivisões de uma
# coleção só. Aqui, "educação clássica" é uma tradição dentro de Educação,
# exatamente como "crítica libertária" é uma tradição dentro de Política.
#
# Regiões do scope_map sem movimento não estão fora de escopo: estão vazias.
# É essa a diferença que a análise de lacunas mede.
# ===========================================================================
sequence:

  - movement: "I. A linhagem clássica e cristã, narrada historicamente"
    purpose: "Percorrer o ideal clássico de formação humana: o que era, o que
              o cristianismo fez com ele, como sobreviveu, e como começou a
              ser confrontado. Tudo por via de história — o que é uma
              característica deste movimento, não da coleção."
    purpose_by: claude
    regions: [antiguidade-classica, cristianismo-antigo, idade-media,
              renascimento-humanismo, seculo-xvii]
    covers_your_stages: [1, 2, 3, 4]

  - work: marrou--histoire-de-leducation-dans-lantiquite
    role: foundational
    demand: exigente
    why_here: "É a melhor porta de entrada histórica para compreender como
               surgiu o ideal clássico de formação humana que posteriormente
               influenciaria a educação cristã e medieval."
    why_here_by: voce
    perspective: "História da educação grega e romana."
    subjects_stated: [paideia, educacao-ateniense, educacao-espartana,
                      retorica, filosofia, educacao-romana,
                      educacao-e-cidadania]

  - work: nunes--historia-da-educacao-na-antiguidade-crista
    role: foundational
    demand: moderado
    why_here: "Mostra como o cristianismo não simplesmente abandona a tradição
               clássica, mas a incorpora, transforma e dá a ela uma nova
               finalidade."
    why_here_by: voce
    perspective: "História da educação cristã nos primeiros séculos."
    subjects_stated: [cristianismo-e-cultura-classica, padres-da-igreja,
                      catequese, escolas-crists, formacao-intelectual-e-moral]

  - work: nunes--historia-da-educacao-na-idade-media
    role: foundational
    demand: moderado
    why_here: "É essencial para entender como a tradição clássica e cristã foi
               preservada, sistematizada e transmitida durante a formação da
               civilização medieval."
    why_here_by: voce
    perspective: "História da educação medieval."
    subjects_stated: [escolas-monasticas, escolas-catedrais, universidades,
                      escolastica, artes-liberais, fe-e-razao]
    # Esta entrada aparecia DUAS VEZES na sua lista, com texto idêntico.
    # Deduplicada na importação. Ver review/education.md §1.

  # ACRÉSCIMO PÓS-IMPORTAÇÃO — decisão sua de 2026-09-10. Colocado logo após
  # Nunes por ser aprofundamento do mesmo recorte (escolas catedrais,
  # 950–1200), não avanço cronológico. `original_order`, abaixo, NÃO foi
  # tocado.
  - work: jaeger--the-envy-of-angels
    role: supplementary
    demand: exigente
    why_here: "Aprofunda, com uma monografia acadêmica premiada, o recorte
               específico das escolas catedrais e dos ideais sociais que
               Nunes narra em panorama — mesma região do scope_map,
               profundidade diferente."
    why_here_by: claude
    publication_pref: pub--verbo-encarnado--a-inveja-dos-anjos

  - work: nunes--historia-da-educacao-no-renascimento
    role: foundational
    demand: moderado
    why_here: "Explica a passagem da educação medieval para o humanismo
               renascentista e ajuda a compreender a origem de muitos ideais
               educacionais modernos."
    why_here_by: voce
    perspective: "História da educação humanista."
    subjects_stated: [humanismo, studia-humanitatis, redescoberta-dos-classicos,
                      formacao-literaria, educacao-moral, retorica]

  - work: nunes--historia-da-educacao-no-seculo-xvii
    role: foundational
    demand: moderado
    why_here: "Completa a sequência histórica mostrando como a educação
               clássica e humanista começa a ser confrontada pelos novos
               modelos intelectuais da modernidade."
    why_here_by: voce
    perspective: "História da educação na transição para a modernidade."
    subjects_stated: [racionalismo, empirismo, reforma, contrarreforma,
                      metodo, educacao-jesuitica]

  - movement: "II. As posições em disputa: que filosofia sustenta cada programa educativo"
    purpose: "Fechada a narrativa histórica, a coleção deixa de contar e passa a
              comparar. Aqui estão as doutrinas — idealismo, realismo,
              pragmatismo, existencialismo, teoria crítica — e o que cada uma
              faz do currículo, do método e do papel do professor. É a camada
              que torna as outras legíveis: sem ela, um programa educativo
              parece a única forma possível de educar. NÃO é história das ideias
              pedagógicas, que é o movimento I, nem mais uma recuperação do
              ideal clássico, que são os movimentos III a V."
    purpose_by: claude
    regions: [iluminismo-seculo-xviii, educacao-progressista, pedagogia-critica,
              psicologia-do-desenvolvimento]
    # Criado em 2026-09-22 por instrução direta sua, que vence a regra §6.9.2
    # deste projeto ("nunca criar movimento para acomodar uma obra"). A ressalva
    # fica registrada, e o desenho responde a ela: o movimento nasce com quatro
    # regiões vazias legítimas a ocupar, não com uma obra e um cabeçalho.

  - work: ozmon-craver--philosophical-foundations-of-education
    role: comparative
    demand: moderado
    why_here: "Mapeia as escolas filosóficas e o que cada uma implica em sala de
               aula. Lido aqui, entrega o adversário que falta a Adler adiante."
    why_here_by: claude
    perspective: "Manual sistemático: doutrina filosófica e sua consequência
                  educacional, lado a lado."
    subjects_stated: [idealismo, realismo, pragmatismo, existencialismo,
                      teoria-critica, curriculo, metodo, papel-do-professor]
    subjects_stated_by: claude

  # -------------------------------------------------------------------------
  # PARTICIPAÇÃO NOVA — 2026-10-05, incluída por decisão sua (cartão
  # d-edu-dewey, opção A; fecha a lacuna education--g03). O cartão punha Dewey
  # no movimento II; a posição dentro dele é minha e está a confirmar: depois
  # de Ozmon, que apresenta o pragmatismo como uma das doutrinas, e antes de
  # Hirsch, para que a crítica dele se leia depois da posição que ela ataca.
  # -------------------------------------------------------------------------
  - work: dewey--democracy-and-education
    role: foundational
    demand: moderado
    why_here: "A posição progressista exposta por quem a formulou: educação
               como reconstrução contínua da experiência e como condição de
               uma sociedade democrática. Ozmon a apresenta entre as
               doutrinas; aqui ela fala por si. Adler a reivindica no ideal
               democrático e a recusa no método; Hirsch a ataca nos
               resultados."
    why_here_by: claude
    placement_status: a-confirmar
    inserted_by: claude
    publication_pref: pub--unesp--democracia-e-educacao--2026

  # -------------------------------------------------------------------------
  # PARTICIPAÇÃO NOVA — 2026-09-23, incluída por decisão sua. POSIÇÃO CONFIRMADA
  # por você em 2026-10-05 (cartão d-pos-hirsch; review/education.md §9.5). Entrou primeiro no movimento III, depois de
  # Adler — erro meu, apontado por você: o III é a recuperação do ideal
  # clássico, e Hirsch não é clássico. Movido para cá, depois de Ozmon: é uma
  # das posições em disputa, e a que ataca de frente a progressista.
  # -------------------------------------------------------------------------
  - work: hirsch--why-knowledge-matters
    role: critical-response
    demand: leve
    why_here: "Uma das posições que o manual de Ozmon apresenta, agora
               defendida por dentro: o conhecimento partilhado vem antes das
               'habilidades', e a pedagogia progressista e centrada no
               desenvolvimento natural é a causa da queda dos resultados. O
               argumento é de ciência cognitiva e de dados escolares, não de
               tradição — por isso fica aqui, e não com Adler."
    why_here_by: claude
    inserted_by: claude

  - movement: "III. A recuperação do ideal clássico no século XX"
    purpose: "Fechada a narrativa histórica, a pergunta muda de tempo verbal:
              deixa de ser o que a tradição foi e passa a ser por que alguém
              a quereria de volta. Adler reivindica o ideal democrático de
              Dewey, lido no movimento II, e recusa o método da escola
              progressista que saiu dele."
    # Texto corrigido em 2026-10-05: dizia "Adler argumenta contra um
    # adversário que a coleção ainda não contém". Dewey entrou, e a Paideia é
    # dedicada a ele — ver review/education.md §12.
    purpose_by: claude
    regions: [educacao-classica-moderna]
    covers_your_stages: [5]

  - work: adler--the-paideia-proposal
    role: pivot
    demand: leve
    why_here: "É o elo entre a história que você acabou de estudar e a
               recuperação moderna do ideal clássico de educação como formação
               integral do ser humano."
    why_here_by: voce
    perspective: "Filosofia da educação e defesa da educação liberal."
    subjects_stated: [paideia, educacao-democratica, artes-liberais,
                      grandes-livros, pensamento-critico, igualdade-intelectual]


  - movement: "IV. A arquitetura: o trivium"
    purpose: "Do porquê para o como. As três artes da linguagem tratadas
              primeiro como objeto histórico, depois como instrumento."
    purpose_by: claude
    regions: [educacao-classica-moderna]
    covers_your_stages: [6]

  - work: mcluhan--the-classical-trivium
    role: comparative
    demand: exigente
    why_here: "Ajuda a compreender o trivium não como uma simples técnica
               escolar, mas como uma arquitetura tradicional para ordenar e
               desenvolver a mente."
    why_here_by: voce
    perspective: "História e estrutura intelectual do trivium clássico."
    subjects_stated: [gramatica, dialetica, retorica, tradicao-medieval,
                      linguagem, logica, artes-liberais]

  - work: miriam-joseph--the-trivium
    role: foundational
    demand: exigente
    why_here: "É uma passagem da história para a prática intelectual: depois
               de conhecer a tradição do trivium, você começa a ver como essas
               três artes podem efetivamente estruturar o aprendizado."
    why_here_by: voce
    perspective: "Educação clássica e formação do intelecto pelo trivium."
    subjects_stated: [gramatica, logica, dialetica, retorica, argumentacao,
                      composicao, comunicacao]

  - movement: "V. A prática"
    purpose: "O último passo da sua cadeia, e o único operacional: o que fazer
              na segunda de manhã. Prática de UM modelo, não da educação."
    purpose_by: claude
    regions: [educacao-classica-moderna]
    covers_your_stages: [7]

  - work: bauer-wise--the-well-trained-mind
    role: supplementary
    demand: leve
    why_here: "Transforma os princípios da educação clássica em um método
               concreto de organização curricular e de formação intelectual."
    why_here_by: voce
    perspective: "Aplicação prática da educação clássica."
    subjects_stated: [tres-estagios, grammar-stage, logic-stage, rhetoric-stage,
                      curriculo, leitura, escrita, organizacao-do-estudo]
    publication_pref: pub--klasika-liber--a-mente-bem-treinada--2021   # decisão sua, 2026-09-23: a edição em português

  # MOVIMENTO E REGIÃO NOVOS — decisão sua de 2026-09-10, pós-importação. A
  # região `critica-da-escola` já estava declarada `absent` desde a
  # importação original (2026-09-05) e já tinha esta obra citada como
  # candidata em review/gaps/education.yaml, gap education--g03. Colocado ao
  # final da sequência: a cadeia original (§ "Por que esta ordem") é
  # estritamente cumulativa e é dela, não minha, para inserir no meio.
  - movement: "VI. A crítica radical da escola"
    purpose: "A posição oposta a Adler sobre a mesma pergunta: não se a
              escola deve recuperar o cânone clássico, mas se a forma
              escolar deveria existir."
    purpose_by: claude
    regions: [critica-da-escola]

  - work: illich--deschooling-society
    role: foundational
    demand: moderado
    why_here: "Recusa a forma escolar inteira, incluindo a do próprio Adler
               — não apenas o currículo que a escola ensina, mas a
               instituição que ensina."
    why_here_by: claude
    publication_pref: pub--vozes--sociedade-sem-escolas

  # -------------------------------------------------------------------------
  # PARTICIPAÇÃO NOVA — 2026-09-19. Obra JÁ no acervo desde a importação de
  # Política, de onde saiu por decisão sua (2026-09-05); estava
  # `pending_assignment` à espera de que Educação e Cultura tivessem critérios
  # declarados. Ambas têm agora, e a pesquisa sobre a conferência decidiu entre
  # as duas. Não é compra: é participação de um registro canônico existente.
  # Argumento em review/education.md §8.
  #
  # Colocada no fim, em movimento próprio, pela mesma razão de Illich: a cadeia
  # original é cumulativa e é sua, não minha, para partir pelo meio.
  # -------------------------------------------------------------------------
  - movement: "VII. O limite do que a universidade pode formar"
    purpose: "Se a instituição que herdou a tarefa de formar pode, ela mesma,
              ensinar quais fins valem a pena — ou apenas método, clareza e
              consciência das consequências."
    purpose_by: claude
    regions: [seculo-xix]

  # -------------------------------------------------------------------------
  # PARTICIPAÇÃO NOVA — 2026-10-05, incluída por decisão sua (cartão
  # d-edu-newman, opção A; fecha a lacuna education--g02). O cartão dizia
  # movimento I, depois de Nunes; você corrigiu para cá, antes de Weber: o I é
  # narrado por história, e Newman é fonte primária. Aqui ele é a resposta
  # afirmativa à pergunta do movimento, e Weber a negativa.
  # -------------------------------------------------------------------------
  - work: newman--the-idea-of-a-university
    role: foundational
    demand: moderado
    why_here: "A defesa mais forte de que a universidade pode formar: o
               conhecimento liberal como fim em si, e a universidade como
               lugar do saber universal. Vem antes de Weber porque é a tese
               que ele, sessenta anos depois e de dentro da universidade de
               pesquisa, diz que a instituição já não pode cumprir."
    why_here_by: claude
    inserted_by: claude
    publication_pref: pub--ecclesiae--a-ideia-de-uma-universidade--2020

  - work: weber--wissenschaft-als-beruf
    role: critical-response
    demand: moderado
    why_here: "A coleção narra a formação como transmissão de um ideal: a
               paideía, as artes liberais, o trivium, a proposta de Adler.
               Weber descreve a instituição que herdou essa tarefa — a
               universidade de pesquisa moderna — e diz que ela não pode
               cumpri-la: pode dar método, clareza e consciência das
               consequências de uma escolha, nunca a escolha. E proíbe ao
               professor pregar da cátedra. É a interrogação da premissa da
               coleção, feita de dentro da instituição."
    why_here_by: claude
    publication_pref: pub--cultrix--ciencia-e-politica

  # -------------------------------------------------------------------------
  # MOVIMENTO NOVO — 2026-10-05, por decisão sua (proposta education--sp01,
  # opção A). Não é a exceção que a §6.9 regra 2 proíbe: o movimento não nasce
  # para acomodar duas obras, nasce de um critério e de uma região que a
  # decisão acrescentou à coleção. A ordem interna — mecanismo antes de
  # prática — é sugestão sua, de 2026-10-01.
  # -------------------------------------------------------------------------
  - movement: "VIII. Como se aprende: a ciência da aprendizagem"
    purpose: "Os movimentos anteriores discutem para que se educa e que forma
              a educação deve ter. Este pergunta o que acontece quando alguém
              aprende — e o que a evidência empírica sobre isso implica para
              ensinar e estudar. É a parte da pergunta da coleção que fala de
              meios, tratada pela ciência e não pela doutrina."
    purpose_by: claude
    regions: [ciencia-da-aprendizagem]

  - work: dehaene--how-we-learn
    role: foundational
    demand: moderado
    why_here: "O mecanismo: atenção, engajamento ativo, feedback de erro e
               consolidação, os quatro pilares com que o autor descreve o que
               o cérebro faz ao aprender. Vem primeiro porque é dele que saem
               as afirmações sobre como ensinar — e porque explica por que as
               práticas da obra seguinte funcionam."
    why_here_by: claude
    publication_pref: pub--contexto--e-assim-que-aprendemos--2022

  - work: brown-roediger-mcdaniel--make-it-stick
    role: supplementary
    demand: leve
    why_here: "A prática: recuperação, espaçamento, intercalação e dificuldades
               desejáveis, cada uma sustentada por pesquisa experimental, no
               nível de quem estuda. Depois de Dehaene, as técnicas deixam de
               ser receitas e passam a ser consequências do mecanismo."
    why_here_by: claude
    publication_pref: pub--penso--fixe-o-conhecimento--2018

paths: []                      # nenhum ainda — 12 obras não pedem compressão

tensions:
  - {a: newman--the-idea-of-a-university, b: weber--wissenschaft-als-beruf,
     about: "Se a universidade pode formar — o conhecimento liberal como fim
             em si, que aperfeiçoa o intelecto — ou se a universidade moderna
             só entrega método e clareza, e a escolha dos fins fica fora do
             seu alcance."}
  - {a: adler--the-paideia-proposal, b: weber--wissenschaft-als-beruf,
     about: "Se a educação pode formar o caráter e indicar fins — a premissa
             que a cadeia inteira pressupõe e que Adler torna programa — ou se
             a instituição moderna só pode entregar método e clareza, deixando
             a escolha dos fins fora do seu alcance."}
  - {a: adler--the-paideia-proposal, b: illich--deschooling-society,
     about: "Se a formação humana exige a instituição escolar, redirecionada
             para o cânone clássico, ou se a escola é, ela mesma, o
             obstáculo à formação que promete dar."}
# Deixou de ser [] com esta adição. Ver review/education.md §3 — o achado
# registrado ali (zero tensões porque os 9 membros originais pertenciam a
# uma só tradição) continua descrevendo corretamente a lista original; esta
# é a primeira tensão real da coleção, e chega de fora dela.

# ===========================================================================
# ORDEM ORIGINAL E DESVIOS
# ===========================================================================
original_order: [marrou--histoire-de-leducation-dans-lantiquite,
  nunes--historia-da-educacao-na-antiguidade-crista,
  nunes--historia-da-educacao-na-idade-media,
  nunes--historia-da-educacao-no-renascimento,
  nunes--historia-da-educacao-no-seculo-xvii,
  adler--the-paideia-proposal,
  mcluhan--the-classical-trivium,
  miriam-joseph--the-trivium,
  bauer-wise--the-well-trained-mind]

order_changes: []              # nada movido

structural_changes:
  - kind: add-movement
    from: "Seis movimentos, do histórico (I) ao limite da universidade (VI)"
    into: ["II. As posições em disputa: que filosofia sustenta cada programa educativo"]
    reason: "A coleção narrava e prescrevia, mas não comparava. Faltava a camada
             sistemática — que doutrinas existem e o que cada uma faz da escola.
             O movimento repara dois buracos declarados: o texto do movimento de
             Adler dizia que ele argumenta contra um adversário que a coleção não
             contém, e entre o fim do movimento histórico (séc. XVII) e Weber
             (séc. XIX) havia um vazio cronológico com o Iluminismo ausente do
             mapa. Entra como II, e os movimentos II a VI passam a III a VII."
    by: claude
    approved_by: voce
    approved_on: 2026-09-22
    reversible: true
    library_effect: "Nenhum registro de obra criado ou alterado por esta mudança."
    membership_effect: "A coleção ganha 1 membro: Ozmon & Craver."
    note: "A regra §6.9.2 proíbe criar movimento para acomodar uma obra. A
           instrução dele vence a regra (precedência declarada em
           curation-rules.md), e o desenho responde à objeção: o movimento traz
           quatro regiões do mapa de escopo que nenhum movimento cobria."

  - kind: add-movement
    from: "Sete movimentos, do histórico (I) ao limite da universidade (VII)"
    into: ["VIII. Como se aprende: a ciência da aprendizagem"]
    reason: "Consequência da proposta education--sp01, aprovada em 2026-10-05:
             a coleção ganhou um critério e uma região que nenhum movimento
             cobria. Entra no fim, sem renumerar nada — a cadeia I a V é sua,
             e VI e VII são contrapesos que respondem a ela; o VIII não
             responde à cadeia, trata da outra metade da pergunta."
    by: claude
    approved_by: voce
    approved_on: 2026-10-05
    reversible: true
    library_effect: "Nenhum registro de obra criado. As duas obras perderam o
                     bloco pending_assignment."
    membership_effect: "A coleção ganha 2 membros: Dehaene e Brown, Roediger e
                        McDaniel."

  - kind: deduplicate
    from: "Item 3 — Nunes, História da Educação na Idade Média (duas entradas
           idênticas na sua lista)"
    into: [nunes--historia-da-educacao-na-idade-media]
    reason: "Texto integralmente idêntico nas duas ocorrências: mesma
             perspectiva, mesmos temas, mesma justificativa. Duplicação de
             transcrição, não duas obras."
    by: claude
    reversible: true
    library_effect: "Nenhum. Uma obra, não duas."
    membership_effect: "A coleção tem 9 membros, não 10."
    status: aguarda-sua-confirmacao

# ===========================================================================
# EDIÇÕES
# ===========================================================================
# Nenhuma das 9 entradas nomeia editora. Esta coleção está inteiramente por
# pesquisar no nível de edição — ao contrário de Política, onde 25 de 40
# vinham identificadas.
#
# Dois nomes na sua lista precisam de confirmação de papel:
#   "Marshall McLuhan; Hugo Langone"     → Langone é tradutor, não coautor?
#   "Irmã Miriam Joseph; Carlos Nougué"  → Nougué é tradutor, não coautor?
# Se sim, os dois nomes identificam implicitamente edições brasileiras
# específicas, e isso é informação de edição escondida num campo de autoria.
# Ver review/education.md §2.1.
#
# RESPONDIDO em 2026-09-23 pelos anúncios de varejo (tier 7, a confirmar
# na editora): Hugo Langone é o TRADUTOR de McLuhan; Carlos Nougué assina o
# PRÓLOGO de Miriam Joseph, e o tradutor é Henrique Paul Dmyterko. Ver
# review/education.md §9.

updated: 2026-10-05
---

## Por que esta ordem

O centro da coleção é uma cadeia em sete passos:

> o que era a educação clássica → como ela foi transformada pelo cristianismo
> → como sobreviveu na Idade Média → como mudou no Renascimento e na
> modernidade → por que Adler quer recuperá-la → como o trivium estrutura
> essa formação → como aplicá-la na prática.

**Aqui a ordem importa de verdade.** Cada passo depende do anterior: Adler só
faz sentido depois da história, porque a proposta dele é recuperar algo, e não
se recupera o que não se conhece. Ler fora de ordem atrapalha.

**A cadeia muda de gênero três vezes**, e é por isso que os movimentos caem
onde caem: primeiro história (I), depois as doutrinas em disputa (II), depois o
argumento para recuperar o ideal clássico (III), a estrutura do trivium (IV) e
o método na prática (V).

**Dois contrapesos no fim.** Illich (VI) questiona se a escola deveria existir;
Weber (VII) pergunta se a universidade pode ensinar quais fins valem a pena, ou
só método — depois de Newman, que defendeu que ela pode. Vêm depois da cadeia
porque respondem a ela.

**E a outra metade da pergunta.** O movimento VIII, de 2026-10-05, não responde
à cadeia: trata dos meios pela ciência — o que acontece quando alguém aprende.
Primeiro o mecanismo (Dehaene), depois a prática (Brown, Roediger e McDaniel),
na ordem que você sugeriu.

A cadeia segue uma tradição, a clássica. A coleção é mais larga do que ela: as
outras correntes (por exemplo, a educação progressista) ainda têm poucas obras.

## Lacunas e observações

Ver `review/education.md`. Nada dali foi aplicado a este arquivo.

**Nota de 2026-09-10:** a descrição acima é da sua lista original, de nove
obras. Duas participações entraram depois, fora daquela lista —
`jaeger--the-envy-of-angels`, dentro do movimento I, logo após Nunes —
Idade Média, e `illich--deschooling-society`, em movimento e região novos
("V. A crítica radical da escola") — e `original_order`, abaixo, continua a
guardar só as nove, exatamente como estavam.
