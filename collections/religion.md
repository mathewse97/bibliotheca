---
id: religion
image:                      # foto de fundo do cartão — interface-rules.md §5
  file: "images/collections/religion.webp"
  subject: "Grande Rolo de Isaías, manuscrito do Mar Morto (Qumran)"
  supplied_by: mathews
  added: 2026-09-25
title_pt: "Religião"
question: "O que é o fenômeno religioso, como as suas grandes tradições se
           formaram historicamente, e com que instrumentos — comparação,
           arqueologia, crítica textual, sociologia — é possível estudá-lo
           sem adotar a perspectiva de nenhuma delas?"
question_by: claude
question_status: proposta

# ---------------------------------------------------------------------------
# NOTA DE IMPORTAÇÃO — 2026-09-20
#
# A lista tem 30 entradas numeradas de 1 a 30, e a numeração está correta:
# nenhuma se repete, nenhuma falta. A ordem canônica é a DELE.
#
# As sete seções são dele e são os movimentos. As frases em itálico sob cada
# cabeçalho também são dele e entram como `purpose`, com `purpose_by: voce`,
# pelo mesmo critério aplicado em collections/greco-roman.md. Elas NÃO são
# descrições do conteúdo atual: várias nomeiam tradições que a coleção ainda
# não cobre (hinduísmo, islamismo, judaísmo, Padres da Igreja, escolástica,
# Reforma, cultos de mistério). É por isso que várias regiões do scope_map
# estão `absent` com `pursuit: open` — a intenção é declarada por ele.
#
# A ENTRADA 30 (Bíblia de Jerusalém) NÃO ESTÁ EM NENHUMA DAS SETE SEÇÕES.
# Ela aparece depois do mapa narrativo de fecho e do separador final, e é a
# única das trinta sem Perspectiva, sem Temas e sem frase de justificativa —
# traz apenas os dois ISBNs. Colocá-la no movimento VII por ser a última
# seria exatamente o que a §6.9 regra 3 proíbe. Ela entra em
# `unplaced_members`, e a colocação é decisão dele. Ver review/religion.md §3.
#
# Dois membros NÃO são registros novos: A ética protestante (entrada 10),
# vinda de Cultura, e O Herói de mil faces (entrada 29), vindo de
# Greco-Romana. Aqui recebem PARTICIPAÇÃO nova — papel, posição e argumento
# próprios — sobre o mesmo registro canônico. Ver curation-rules.md §2.7.
#
# Os três volumes da História das crenças e das ideias religiosas entram
# como TRÊS obras ligadas por `continues`, e não como uma obra com três
# publicações, porque ele escreveu Perspectiva, Temas e justificativa
# SEPARADOS para cada volume — três argumentos exigem três participações.
# A alternativa (uma obra, três publicações) está levantada em
# review/religion.md §4 e é reversível.
# ---------------------------------------------------------------------------

source:
  origin: sua-lista
  imported: 2026-09-20
  archived_at: sources/lists/religiao.md
sequence_kind: intellectual

provisional:
  inferred_by_claude: [question, inclusion_criteria, scope_map, role, demand,
                       paths, tensions]
  authored_by_you: [sequence, perspective, subjects_stated, why_here,
                    movement.titles, movement.purpose]
  pending_confirmation: true
  see: review/religion.md

inclusion_criteria:            # derivados da PERGUNTA, não do conteúdo atual
  by: claude
  status: proposta
  criteria:
    - "Obras que descrevam, comparem ou narrem historicamente tradições
       religiosas, de qualquer época ou região."
    - "Obras que proponham teoria ou método para o estudo do fenômeno
       religioso — fenomenologia, sociologia, antropologia, psicologia,
       filosofia da religião."
    - "Fontes primárias religiosas de qualquer tradição — escrituras,
       cosmogonias, corpora doutrinais, cartas e documentos de prática — lidas
       como documentos da tradição que as produziu, e não como autoridade."
    - "Obras de crítica histórica, arqueológica, filológica ou textual sobre
       essas fontes."
    - "Correntes religiosas não instituídas — hermetismo, cultos de mistério,
       esoterismo antigo — quando tratadas como pensamento religioso e não
       como prática atual."
  out_of_scope:
    - "Teologia normativa que argumenta a verdade de uma tradição PARA o
       leitor. Uma obra confessional entra como fonte primária, nunca como
       autoridade — é a distinção que mantém a entrada 26 dentro do escopo."
    - "Religião grega e romana estudada como parte da cultura antiga: isso é
       greco-roman, cuja região `religiao-e-culto` já está `covered`."
    - "Espiritualidade prática, autoajuda e literatura devocional de uso."
  test_applied: "Os critérios não exigem que uma tradição seja instituída: a
                 seção VII é dele e nomeia hermetismo e cultos de mistério, e
                 os critérios têm de acomodá-los sem os converter em curiosidade.
                 Também não exigem distância confessional da FONTE, só do
                 tratamento — sem isso a entrada 26 cairia fora do escopo do
                 próprio dono da lista."
  open_question: "A fronteira com greco-roman. As entradas 19, 20 e 21
                  (evangelhos, Ehrman, Vermes) tratam do cristianismo
                  primitivo, que é anterior a Constantino e portanto DENTRO do
                  escopo declarado de greco-roman, cuja região
                  `religiao-romana-e-cristianismo-antigo` está `absent` e cujo
                  arquivo de lacunas já previu que Religião a cobriria por
                  participação. Isso é proposta, não aplicação: ver
                  review/religion.md §7."

# ---------------------------------------------------------------------------
# SCOPE_MAP — território reivindicado pela PERGUNTA.
#   coverage: covered | thin | absent   — FATO.
#   pursuit:  open | not-pursued        — INTENÇÃO SUA.
# Nenhuma região está `not-pursued`: essa decisão é sua. Uma região `absent`
# não é uma compra devida (§7, §2.3).
# ---------------------------------------------------------------------------
scope_map:
  by: claude
  map_status: proposta
  regions:
    - {id: historia-comparada-das-religioes, coverage: covered, pursuit: open,
       note: "Panoramas e histórias comparadas que percorrem várias tradições e
             as põem numa sequência histórica única."}
    - {id: teoria-e-metodo-do-fenomeno-religioso, coverage: covered, pursuit: open,
       note: "Fenomenologia, morfologia do sagrado e os instrumentos
             conceituais com que a religião é estudada como objeto."}
    - {id: sociologia-da-religiao, coverage: covered, pursuit: open,
       note: "A religião como fato social: legitimação, instituição,
             secularização e efeito histórico das éticas religiosas."}
    - {id: antropologia-e-etnografia-da-religiao, coverage: absent, pursuit: open,
       note: "O estudo da religião por trabalho de campo e comparação
             etnográfica, distinto da fenomenologia e da sociologia. A seção
             II declara antropologia; o acervo não a cobre."}
    - {id: religiao-mesopotamica, coverage: covered, pursuit: open,
       note: "Cosmogonia, panteão, culto e literatura religiosa da Mesopotâmia,
             em fonte primária e em síntese moderna."}
    - {id: religiao-egipcia, coverage: thin, pursuit: open,
       note: "Mitos, deuses e concepções do cosmos do Egito antigo. Presente
             por um único guia moderno."}
    - {id: religiao-cananeia-e-israel-antigo, coverage: covered, pursuit: open,
       note: "A religião de Israel antes e durante a formação do monoteísmo,
             lida por arqueologia e história comparada."}
    - {id: biblia-hebraica-formacao, coverage: covered, pursuit: open,
       note: "Como a Torá e a Bíblia hebraica se formaram: composição, redação,
             arqueologia e crítica histórica."}
    - {id: novo-testamento-e-jesus-historico, coverage: covered, pursuit: open,
       note: "Os evangelhos como texto e como fonte histórica; crítica textual
             e reconstrução da figura de Jesus."}
    - {id: judaismo-pos-biblico, coverage: absent, pursuit: open,
       note: "O judaísmo como tradição viva depois da Bíblia: rabinismo,
             halachá, cabala, modernidade. Declarado na seção V; ausente."}
    - {id: islamismo, coverage: absent, pursuit: open,
       note: "Corão, tradição profética, direito, teologia e história do islã.
             Declarado na seção V; ausente."}
    - {id: hinduismo, coverage: absent, pursuit: open,
       note: "Vedas, Upanixades, épica, darshanas e prática hindu. Declarado na
             seção V; ausente."}
    - {id: budismo, coverage: covered, pursuit: open,
       note: "Doutrina budista em exposição moderna e em fonte primária do
             cânone páli."}
    - {id: cristianismo-historico-e-teologia, coverage: absent, pursuit: open,
       note: "Padres da Igreja, história institucional, escolástica, Reforma e
             teologia cristã como assunto próprio. Declarado na seção VI;
             ausente."}
    - {id: missao-e-expansao-crista, coverage: thin, pursuit: open,
       note: "O cristianismo em encontro com outras culturas, em fonte
             primária. Presente por um único corpus."}
    - {id: hermetismo, coverage: covered, pursuit: open,
       note: "O corpus hermético e os seus textos emblemáticos, lidos como
             pensamento religioso do helenismo tardio e da sua transmissão."}
    - {id: mitologia-comparada, coverage: thin, pursuit: open,
       note: "Teoria do mito e comparação de estruturas narrativas entre
             tradições. Presente por uma única obra, e ela mesma objeto de
             avaliação."}
    - {id: cultos-de-misterio, coverage: absent, pursuit: open,
       note: "Elêusis, orfismo, mitraísmo e as religiões de iniciação do mundo
             antigo como assunto próprio. Declarado na seção VII; ausente."}

excluded: []

# ===========================================================================
# SEQUÊNCIA
#
# A ordem dele, de 1 a 30, preservada. `order_changes` está vazio: nenhuma
# alteração foi aplicada. A avaliação da ordem, com as duas propostas que ela
# gerou, está em review/religion.md §5 — propor não é aplicar (§6.9, §5).
# ===========================================================================
sequence:

  - movement: "I. História comparada das religiões"
    purpose: "Eliade, Noss, Armstrong e outras obras panorâmicas."
    purpose_by: voce
    regions: [historia-comparada-das-religioes]

  - work: armstrong--a-history-of-god       # entrada 2 da lista dele
    role: foundational
    demand: leve
    why_here: "É uma excelente introdução às três grandes tradições
                monoteístas abraâmicas e ajuda a estabelecer um eixo histórico
                em torno da ideia de Deus."
    why_here_by: voce
    perspective: "história comparada das concepções de Deus."
    subjects_stated: [judaismo, cristianismo, islamismo, monoteismo, teologia,
                      mistica, filosofia, modernidade,
                      transformacoes-da-ideia-de-deus]

  - work: noss-grangaard--a-history-of-the-worlds-religions       # entrada 1 da lista dele
    role: foundational
    demand: moderado
    why_here: "Funciona como grande mapa comparativo para situar as
                principais tradições religiosas antes de aprofundar cada uma
                delas."
    why_here_by: voce
    perspective: "história geral e comparada das religiões."
    subjects_stated: [religioes-do-mundo, mitologia, ritos, crencas,
                      instituicoes-religiosas,
                      tradicoes-orientais-e-ocidentais,
                      desenvolvimento-historico-das-religioes]

  - work: eliade--histoire-des-croyances-i       # entrada 3 da lista dele
    role: foundational
    demand: exigente
    why_here: "Permite transformar o panorama geral em uma narrativa
                histórica das religiões antigas, situando civilizações e
                tradições dentro de uma sequência mais ampla."
    why_here_by: voce
    perspective: "história comparada das religiões antigas."
    subjects_stated: [pre-historia-religiosa, sociedades-arcaicas,
                      mesopotamia, egito, religioes-indo-europeias,
                      grecia-antiga, misterios-de-eleusis]

  - work: eliade--histoire-des-croyances-ii       # entrada 4 da lista dele
    role: foundational
    demand: exigente
    why_here: "Amplia o quadro histórico para as grandes tradições religiosas
                que se desenvolvem entre a Antiguidade clássica e o surgimento
                do cristianismo."
    why_here_by: voce
    perspective: "história comparada das religiões da Antiguidade clássica e
                   tardia."
    subjects_stated: [hinduismo, budismo, religioes-iranianas, judaismo,
                      cristianismo-primitivo, mundo-greco-romano,
                      transformacoes-religiosas-da-antiguidade]

  - work: eliade--histoire-des-croyances-iii       # entrada 5 da lista dele
    role: foundational
    demand: exigente
    why_here: "Fecha a grande narrativa histórica de Eliade e leva o percurso
                das religiões até a formação do mundo medieval e moderno."
    why_here_by: voce
    perspective: "história comparada das religiões na Idade Média e início da
                   modernidade."
    subjects_stated: [islamismo, cristianismo-medieval, judaismo,
                      tradicoes-asiaticas, reforma,
                      transformacoes-religiosas-do-ocidente]

  - work: eliade-culianu--dictionnaire-des-religions       # entrada 6 da lista dele
    role: supplementary
    demand: leve
    why_here: "Deve funcionar principalmente como obra de consulta ao longo
                de toda a formação, consolidando nomes, conceitos e tradições
                encontrados nas demais leituras."
    why_here_by: voce
    perspective: "referência comparativa e conceitual."
    subjects_stated: [divindades, conceitos-religiosos, mitos, ritos, escolas,
                      tradicoes, personagens, terminologia-das-religioes]

  - movement: "II. Teoria do fenômeno religioso"
    purpose: "Eliade, Berger, Weber, antropologia, sociologia, fenomenologia,
              filosofia."
    purpose_by: voce
    regions: [teoria-e-metodo-do-fenomeno-religioso, sociologia-da-religiao]

  - work: eliade--das-heilige-und-das-profane       # entrada 8 da lista dele
    role: foundational
    demand: moderado
    why_here: "É uma síntese mais concentrada das ideias de Eliade e uma boa
                passagem do conhecimento histórico para a compreensão
                conceitual da experiência religiosa."
    why_here_by: voce
    perspective: "fenomenologia da religião."
    subjects_stated: [sagrado-e-profano, espaco-sagrado, tempo-sagrado,
                      simbolos, mitos, ritos, experiencia-religiosa]

  - work: eliade--traite-dhistoire-des-religions       # entrada 7 da lista dele
    role: pivot
    demand: exigente
    why_here: "Depois do panorama histórico, introduz uma maneira sistemática
                de investigar as estruturas e manifestações recorrentes do
                fenômeno religioso."
    why_here_by: voce
    perspective: "fenomenologia e história comparada das religiões."
    subjects_stated: [manifestacoes-do-sagrado, simbolos, mitos, ritos,
                      hierofanias, espaco-e-tempo-sagrados,
                      estruturas-fundamentais-da-experiencia-religiosa]

  - work: weber--die-protestantische-ethik       # entrada 10 da lista dele
    role: comparative
    demand: exigente
    why_here: "Permite compreender de maneira mais concreta como Weber
                relaciona sistemas religiosos, comportamento social e formação
                da modernidade ocidental."
    why_here_by: voce
    perspective: "sociologia histórica da religião."
    subjects_stated: [protestantismo, ascetismo, vocacao, racionalizacao,
                      etica-economica, capitalismo-moderno,
                      ideias-religiosas-e-transformacoes-sociais]

  - work: berger--the-sacred-canopy       # entrada 9 da lista dele
    role: comparative
    demand: exigente
    why_here: "Introduz uma perspectiva sociológica complementar à
                fenomenologia, mostrando como a religião também estrutura e
                legitima uma determinada visão de mundo."
    why_here_by: voce
    perspective: "sociologia da religião."
    subjects_stated: [construcao-social-da-realidade, legitimacao,
                      instituicoes, universo-simbolico, religiao-e-sociedade,
                      secularizacao, funcao-social-da-religiao]

  - movement: "III. Mundo religioso do antigo Oriente"
    purpose: "Mesopotâmia, Egito, Canaã, Israel."
    purpose_by: voce
    regions: [religiao-mesopotamica, religiao-egipcia, religiao-cananeia-e-israel-antigo]

  - work: epopeia-de-gilgamesh       # entrada 11 da lista dele
    role: primary-source
    demand: moderado
    why_here: "É uma das melhores portas de entrada para conhecer o
                imaginário religioso do antigo Oriente Próximo diretamente
                através de uma de suas grandes obras literárias."
    why_here_by: voce
    publication_pref: pub--autentica--ele-que-o-abismo-viu--2017   # decisão sua, 2026-10-05 (d-ed-gilgamesh): confirma a edição acadêmica, com aparato, que eu tinha proposto em 2026-09-25; a de 2021 continua registrada
    perspective: "literatura, religião e cosmovisão da Mesopotâmia antiga."
    subjects_stated: [criacao, mortalidade, amizade, realeza,
                      relacao-entre-homens-e-deuses, diluvio, destino,
                      busca-pela-imortalidade]

  - work: enuma-elis       # entrada 12 da lista dele
    role: primary-source
    demand: moderado
    why_here: "Complementa *Gilgámesh* mostrando de forma mais direta como os
                mesopotâmios concebiam a origem do mundo, dos deuses e da
                ordem cósmica."
    why_here_by: voce
    perspective: "cosmogonia e religião da Mesopotâmia antiga."
    subjects_stated: [criacao-do-cosmos, genealogia-divina,
                      conflito-entre-deuses, marduque, ordem-cosmica,
                      soberania-divina, origem-da-humanidade]

  - work: bottero--au-commencement-etaient-les-dieux       # entrada 14 da lista dele
    role: foundational
    demand: moderado
    why_here: "É um passo importante da leitura de mitos para a compreensão
                da religião mesopotâmica como sistema cultural completo."
    why_here_by: voce
    perspective: "religião e civilização da antiga Mesopotâmia."
    subjects_stated: [concepcao-mesopotamica-dos-deuses, religiao-cotidiana,
                      ritos, humanidade, cosmos, culto,
                      organizacao-da-sociedade-em-torno-do-sagrado]

  - work: shaw--the-egyptian-myths       # entrada 13 da lista dele
    role: comparative
    demand: leve
    why_here: "Amplia o horizonte do antigo Oriente Próximo e permite
                comparar a religião egípcia com as tradições mesopotâmicas que
                você acabou de conhecer."
    why_here_by: voce
    perspective: "mitologia e religião do Egito antigo."
    subjects_stated: [deuses-egipcios, cosmogonias, mitos-de-criacao,
                      morte-e-ressurreicao, osiris, isis, horus, ra,
                      concepcoes-egipcias-do-cosmos]

  - work: kaefer--a-biblia-a-arqueologia-e-a-historia-de-israel-e-juda       # entrada 15 da lista dele
    role: pivot
    demand: moderado
    why_here: "Faz a transição fundamental entre as religiões do antigo
                Oriente Próximo e o contexto histórico no qual surge a
                tradição bíblica de Israel."
    why_here_by: voce
    perspective: "arqueologia bíblica e história do antigo Israel e Judá."
    subjects_stated: [formacao-de-israel, monarquia, juda, arqueologia,
                      fontes-historicas, tradicao-biblica,
                      reconstrucao-historica]

  - movement: "IV. Bíblia e formação das tradições abraâmicas"
    purpose: "Bíblia de Jerusalém, história de Israel, formação da Torá, Novo
              Testamento, Jesus histórico etc."
    purpose_by: voce
    regions: [biblia-hebraica-formacao, novo-testamento-e-jesus-historico]

  - work: biblia       # entrada 30 da lista dele
    role: primary-source
    demand: exigente
    why_here: null                 # ele não escreveu justificativa para esta entrada
    why_here_by: null
    perspective: null
    subjects_stated: []
    note: "Obra de CONSULTA, não leitura corrida: 2208 páginas. O uso
           proveitoso são as introduções gerais e por livro — algumas
           dezenas de páginas que já são uma formação em história
           literária de Israel — mais os blocos narrativos, deixando o
           resto como referência permanente. Colocada aqui por decisão
           dele em 2026-09-20; ver review/religion.md §9, P1."

  - work: finkelstein-romer--aux-origines-de-la-torah       # entrada 17 da lista dele
    role: pivot
    demand: exigente
    why_here: "Aprofunda a questão central de como a tradição bíblica se
                formou historicamente e prepara o terreno para uma leitura
                mais crítica das Escrituras."
    why_here_by: voce
    perspective: "história crítica, arqueologia e formação da Torá."
    subjects_stated: [composicao-da-tora, israel-antigo, arqueologia,
                      tradicoes-patriarcais, exodo, monarquia, exilio,
                      formacao-literaria-da-biblia-hebraica]

  - work: smith--the-memoirs-of-god       # entrada 16 da lista dele
    role: foundational
    demand: exigente
    why_here: "Ajuda a compreender o desenvolvimento histórico da religião
                israelita antes de entrar diretamente nas interpretações dos
                textos bíblicos."
    why_here_by: voce
    perspective: "história da religião israelita e formação do monoteísmo
                   bíblico."
    subjects_stated: [religiao-do-antigo-israel, memoria, identidade,
                      monoteismo, tradicoes-cananeias,
                      desenvolvimento-da-concepcao-de-deus-de-israel]

  - work: kugel--how-to-read-the-bible       # entrada 18 da lista dele
    role: foundational
    demand: exigente
    why_here: "É o momento adequado para aprender a ler a Bíblia levando
                simultaneamente em conta seu mundo antigo e a longa tradição
                de interpretação que se desenvolveu em torno dela."
    why_here_by: voce
    perspective: "interpretação bíblica e história da exegese."
    subjects_stated: [leitura-da-biblia, contexto-antigo,
                      interpretacao-judaica-tradicional,
                      critica-biblica-moderna, autoria, composicao,
                      significado-dos-textos]

  - work: evangelhos-canonicos       # entrada 19 da lista dele
    role: primary-source
    demand: moderado
    why_here: "Depois de estudar a formação do contexto bíblico, você chega
                às fontes centrais para o estudo histórico e literário do
                cristianismo."
    why_here_by: voce
    perspective: "leitura direta e filológica dos Evangelhos."
    subjects_stated: [mateus, marcos, lucas, joao, texto-grego, traducao,
                      narrativa-evangelica, vida-e-ensinamentos-de-jesus]

  - work: ehrman--misquoting-jesus       # entrada 20 da lista dele
    role: critical-response
    demand: moderado
    why_here: "Ensina a distinguir entre aquilo que os textos preservam e
                aquilo que pode ter sido introduzido ou modificado durante sua
                transmissão."
    why_here_by: voce
    publication_pref: pub--harpercollins-brasil--o-que-jesus-disse--2015   # escolha sua (2026-09-25)
    perspective: "crítica textual e história do cristianismo primitivo."
    subjects_stated: [transmissao-dos-evangelhos, alteracoes-textuais,
                      tradicao-manuscrita, palavras-atribuidas-a-jesus,
                      formacao-dos-textos-cristaos]

  - work: vermes--the-authentic-gospel-of-jesus       # entrada 21 da lista dele
    role: critical-response
    demand: exigente
    why_here: "Complementa Ehrman deslocando o foco da transmissão textual
                para a reconstrução histórica da figura de Jesus."
    why_here_by: voce
    perspective: "estudo histórico de Jesus no contexto judaico do século I."
    subjects_stated: [jesus-historico, judaismo-do-segundo-templo,
                      ensinamentos-de-jesus, reino-de-deus, contexto-judaico,
                      interpretacao-historica-dos-evangelhos]

  - movement: "V. Religiões específicas"
    purpose: "Budismo, hinduísmo, islamismo, judaísmo etc."
    purpose_by: voce
    regions: [budismo, hinduismo, islamismo, judaismo-pos-biblico]

  - work: rahula--what-the-buddha-taught       # entrada 22 da lista dele
    role: foundational
    demand: leve
    why_here: "Depois da perspectiva histórica de Eliade, fornece uma
                apresentação mais diretamente interna da doutrina budista."
    why_here_by: voce
    publication_pref: pub--motilal-banarsidass--what-the-buddha-taught--2017   # escolha sua (2026-09-25)
    perspective: "introdução doutrinal ao budismo."
    subjects_stated: [quatro-nobres-verdades, caminho-octuplo, sofrimento,
                      desejo, impermanencia, nao-eu, nirvana,
                      ensinamentos-fundamentais-de-buda]

  - work: dhammapada       # entrada 23 da lista dele
    role: primary-source
    demand: leve
    why_here: "Deve ser lido como texto religioso primário, permitindo
                confrontar a apresentação moderna de Rahula com uma fonte
                tradicional de ensinamentos budistas."
    why_here_by: voce
    perspective: "fonte primária budista."
    subjects_stated: [etica, disciplina-mental, sofrimento, sabedoria,
                      desapego, meditacao, caminho-espiritual]

  - movement: "VI. Cristianismo"
    purpose: "Cristianismo primitivo, Padres da Igreja, história da Igreja,
              escolástica, Reforma, teologia etc."
    purpose_by: voce
    regions: [cristianismo-historico-e-teologia, missao-e-expansao-crista]

  - work: jefferson--the-life-and-morals-of-jesus-of-nazareth       # entrada 24 da lista dele
    role: primary-source
    demand: leve
    why_here: "É especialmente útil depois dos estudos históricos sobre Jesus
                porque mostra como um pensador moderno reinterpretou os
                Evangelhos segundo seus próprios pressupostos filosóficos."
    why_here_by: voce
    perspective: "leitura racionalista e moderna dos Evangelhos."
    subjects_stated: [ensinamentos-morais-de-jesus, selecao-dos-evangelhos,
                      racionalismo-religioso, etica-crista,
                      distincao-entre-ensinamento-moral-e-elementos-sobrenaturais]

  - work: xavier--epistolae       # entrada 25 da lista dele
    role: primary-source
    demand: exigente
    why_here: "É uma leitura histórica importante para observar como uma
                tradição religiosa já consolidada se apresenta diante de
                outras culturas e religiões fora da Europa."
    why_here_by: voce
    perspective: "fonte primária da expansão missionária cristã."
    subjects_stated: [evangelizacao, missao, encontro-intercultural,
                      cristianismo, pratica-missionaria, asia,
                      expansao-global-da-igreja]

  - work: joao-paulo-ii--varcare-la-soglia-della-speranza       # entrada 26 da lista dele
    role: primary-source
    demand: leve
    why_here: "Fecha a sequência deslocando o estudo da religião histórica,
                comparativa e sociológica para a reflexão existencial e
                confessional sobre a fé cristã."
    why_here_by: voce
    perspective: "reflexão cristã contemporânea sobre fé e esperança."
    subjects_stated: [fe, esperanca, deus, jesus-cristo, sofrimento, oracao,
                      moral, igreja, sentido-da-existencia]

  - movement: "VII. Mitologia, hermetismo e pensamento religioso antigo"
    purpose: "Hermetismo, mitologia comparada, cultos de mistério etc."
    purpose_by: voce
    regions: [hermetismo, mitologia-comparada, cultos-de-misterio]

  - work: corpus-hermeticum       # entrada 27 da lista dele
    role: primary-source
    demand: exigente
    why_here: "Introduz diretamente uma das principais correntes religiosas e
                filosóficas do helenismo tardio e prepara a leitura de seus
                textos herméticos específicos."
    why_here_by: voce
    perspective: "fonte primária da tradição hermética."
    subjects_stated: [cosmologia, divindade, intelecto, criacao, conhecimento,
                      regeneracao-espiritual, relacao-entre-homem-e-cosmos]

  - work: tabula-smaragdina       # entrada 28 da lista dele
    role: primary-source
    demand: leve
    why_here: "É melhor lida depois do *Corpus Hermeticum*, pois então seus
                símbolos deixam de aparecer como fórmulas isoladas e passam a
                fazer parte de um universo intelectual compreensível."
    why_here_by: voce
    perspective: "texto emblemático da tradição hermética."
    subjects_stated: [correspondencia-entre-macrocosmo-e-microcosmo, unidade,
                      transformacao, conhecimento, linguagem-simbolica]

  - work: campbell--the-hero-with-a-thousand-faces       # entrada 29 da lista dele
    role: comparative
    demand: moderado
    why_here: "Depois de estudar várias tradições religiosas concretas, você
                pode avaliar a tentativa de Campbell de encontrar estruturas
                comuns por trás de seus mitos."
    why_here_by: voce
    perspective: "mitologia comparada e teoria do mito."
    subjects_stated: [jornada-do-heroi, mitos-de-iniciacao, simbolos,
                      arquetipos, transformacao,
                      estruturas-narrativas-recorrentes]

# ---------------------------------------------------------------------------
# A ENTRADA 30 FOI COLOCADA NO MOVIMENTO IV
#
# Ela estava fora das sete seções na lista de origem, sem Perspectiva, Temas
# nem justificativa. Ele decidiu em 2026-09-20 colocá-la abrindo o movimento
# IV, cujo próprio texto de abertura, escrito por ele, começa nomeando a
# Bíblia de Jerusalém. Os campos que ele não escreveu continuam nulos.
# ---------------------------------------------------------------------------

order_changes:

  - work: armstrong--a-history-of-god
    kind: move
    from: "posição 2, depois de Noss"
    to: "posição 1, abrindo o movimento I"
    approved_by: voce
    date: 2026-09-20
    reason: "Noss tem 840 páginas, é descritivo e sem tese: é obra de consulta
             e quase ninguém a lê inteira. Armstrong tem um fio narrativo e uma
             tese, e dá ao leitor uma razão para continuar. O manual passa a ser
             consulta permanente a partir daqui."
    reversible_by: "Trocar as duas de volta; nada mais depende disto."

  - work: eliade--das-heilige-und-das-profane
    kind: move
    from: "posição 8, depois do Tratado"
    to: "posição 7, abrindo o movimento II"
    approved_by: voce
    date: 2026-09-20
    reason: "O sagrado e o profano (198 p.) é a versão condensada e didática do
             Tratado (496 p.), escrita para divulgação. Na ordem anterior o
             leitor enfrentava o livro mais difícil da coleção antes de ter os
             conceitos que o organizam."
    reversible_by: "Trocar as duas de volta."

  - work: weber--die-protestantische-ethik
    kind: move
    from: "posição 10, depois de Berger"
    to: "posição 9, antes de Berger"
    approved_by: voce
    date: 2026-09-20
    reason: "Berger é weberiano declarado, e a discussão de racionalização e
             secularização de O Dossel Sagrado pressupõe A ética protestante
             conhecida."
    reversible_by: "Trocar as duas de volta."

  - work: bottero--au-commencement-etaient-les-dieux
    kind: move
    from: "posição 14, depois dos mitos egípcios"
    to: "posição 13, logo depois do Enūma Eliš"
    approved_by: voce
    date: 2026-09-20
    reason: "Mantém contíguo o bloco mesopotâmico — os dois poemas e depois a
             síntese que os sistematiza e faz a ponte da Suméria a Jerusalém,
             entrando direto em Kaefer. Os mitos egípcios são digressão
             comparativa e funcionam igualmente bem depois."
    reversible_by: "Trocar as duas de volta."

  - work: smith--the-memoirs-of-god
    kind: move
    from: "movimento III, posição 16, antes de Finkelstein-Römer"
    to: "movimento IV, depois de Finkelstein-Römer"
    approved_by: voce
    date: 2026-09-20
    reason: "Kaefer dá a cronologia, Finkelstein e Römer dão o solo arqueológico
             e a datação dos textos, e só então O memorial de Deus — que é o
             mais técnico do bloco, com material ugarítico e teoria da memória
             coletiva, e o que efetivamente responde como surgiu o monoteísmo —
             rende o que pode. É também mudança de movimento: a obra trata da
             formação da tradição bíblica, que é o assunto do movimento IV."
    reversible_by: "Devolver a obra ao movimento III, antes de Kaefer."

  - work: biblia
    kind: place
    from: "fora das sete seções da lista de origem, `pending_assignment: true`"
    to: "movimento IV, primeira posição"
    approved_by: voce
    date: 2026-09-20
    reason: "Três razões convergentes. O texto de abertura do movimento IV,
             escrito por ele, começa nomeando a Bíblia de Jerusalém. É
             pré-requisito direto da entrada 24, a Bíblia de Jefferson, que é
             feita de recortes dos evangelhos e cujo argumento está todo nas
             ausências. E é a edição através da qual as demais obras do
             movimento são lidas. A entrada não traz Perspectiva, Temas nem
             justificativa porque ele não as escreveu; os campos ficam nulos."
    reversible_by: "Remover do movimento IV e devolver `pending_assignment: true`
                    ao registro works/biblia.md."

structural_changes: []

updated: 2026-09-20
---

## Por que esta ordem

A ordem segue este caminho:

> mapa geral das religiões → teoria do fenômeno religioso → mundo religioso do
> antigo Oriente → formação de Israel e da Bíblia → Jesus e Novo Testamento →
> religiões específicas → cristianismo → mitologia, hermetismo e pensamento
> religioso antigo

**Primeiro o instrumento, depois o objeto.** A coleção não começa pela religião
mais antiga: começa pelo mapa comparativo (I) e pela teoria que diz o que se
está olhando (II). Só então passa às religiões concretas, em ordem
aproximadamente cronológica (III a VII). Ensina a olhar antes de mostrar o que
olhar.

**O custo:** os três volumes de Eliade percorrem a história inteira das
religiões, incluindo Mesopotâmia, Egito, Israel, cristianismo e islã, antes de
a coleção chegar a qualquer uma delas nas fontes. Você vai ler o resumo de
Gilgámesh antes de ler Gilgámesh. É o preço de pôr o panorama primeiro.

## Avaliação curatorial

Ver `review/religion.md`. A importação corrigiu uma autoria errada e treze
confusões entre autor, tradutor e editora, todas herdadas do catálogo da Amazon
e nenhuma delas dele. Três registros de lacuna foram abertos como detecção.
Cinco decisões aguardam ele.
