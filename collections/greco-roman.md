---
id: greco-roman
title_pt: "Cultura e História Greco-Romana"
question: "Como a cultura grega se formou, como ela se converteu em pensamento,
           e como foi herdada, transformada e transmitida por Roma e pelo
           Ocidente?"
question_by: claude
question_status: proposta
image:                      # foto de fundo do cartão — interface-rules.md §5
  file: "images/collections/greco-roman.webp"
  subject: "Cariátides do Erecteion, Acrópole de Atenas"
  supplied_by: mathews
  added: 2026-09-24

# ---------------------------------------------------------------------------
# NOTA DE IMPORTAÇÃO — 2026-09-12
#
# A lista de origem tinha 57 entradas numeradas até 52: as seções VIII e IX
# reiniciavam a numeração em 40, de modo que os números 40 a 44 apareciam duas
# vezes. Corrigido na importação; nenhuma obra foi perdida ou duplicada por
# causa disso.
#
# ATUALIZAÇÃO 2026-09-22: a coleção passa a ter 75 membros. O 75º é
# pseudo-apolodoro--bibliotheke, que NÃO vem da lista de origem — entrou
# por pesquisa, no movimento II, com a sua aprovação nessa data.
#
# A coleção tem 74 membros, não 57. A diferença vem inteiramente da expansão
# de três entradas de VOLUME em obras individuais (decisão sua, 2026-09-12):
# ver `structural_changes`. Nenhuma obra foi acrescentada, nenhuma removida.
#
# Três membros NÃO são registros novos: A República, a Política e Tucídides já
# estavam na biblioteca, vindos de Política. Aqui eles ganham uma PARTICIPAÇÃO
# nova — papel, posição e argumento próprios — sobre o mesmo registro
# canônico. Ver curation-rules.md §2.7.
# ---------------------------------------------------------------------------

source:
  origin: sua-lista
  imported: 2026-09-12
  archived_at: sources/lists/greco-romana.md
sequence_kind: intellectual

provisional:
  inferred_by_claude: [question, inclusion_criteria, scope_map, role, demand,
                       movement.purpose, movement.grouping, paths, tensions]
  authored_by_you: [sequence, perspective, subjects_stated, why_here,
                    movement.titles]
  pending_confirmation: true
  see: review/greco-roman.md

inclusion_criteria:            # derivados da PERGUNTA, não do conteúdo atual
  by: claude
  status: proposta
  criteria:
    - "Fontes antigas gregas e romanas de qualquer gênero — épica, lírica,
       drama, história, filosofia, romance, tratado técnico — enquanto
       documentos de uma cultura que se pensa a si mesma."
    - "Obras históricas, filológicas, arqueológicas ou antropológicas modernas
       que interpretem essa cultura."
    - "Obras sobre a RECEPÇÃO do mundo greco-romano: como ele foi lido,
       apropriado e reinterpretado depois da Antiguidade."
    - "Uma obra não greco-romana entra apenas quando o seu objeto declarado é
       o material greco-romano, ou quando ela propõe uma teoria que o acervo
       usa para ler esse material — e nesse caso entra como objeto de
       avaliação, não como autoridade."
  out_of_scope:
    - "Antiguidade não mediterrânica estudada por si mesma."
    - "Cristianismo posterior a Constantino como assunto próprio."
    - "Manuais escolares e panoramas de divulgação sem argumento."
  test_applied: "Nenhum critério acima exclui uma obra que responda claramente
                 à pergunta. Em particular, os critérios NÃO exigem que uma
                 obra seja literária ou filosófica: arte, ciência, direito e
                 cultura material qualificam e hoje estão ausentes, o que é um
                 fato do mapa e não uma correção dos critérios."
  open_question: "A filosofia antiga mora aqui ou numa futura coleção de
                  Filosofia? Platão e Aristóteles já estão em Política por
                  outra razão, e as seções V–VI desta coleção são um curso de
                  filosofia antiga inteiro. Enquanto não houver coleção de
                  Filosofia a pergunta é teórica; quando houver, ela decide
                  participações, não posse. Ver review/greco-roman.md §2."

# ---------------------------------------------------------------------------
# SCOPE_MAP — território reivindicado pela PERGUNTA.
#   coverage: covered | thin | absent   — FATO.
#   pursuit:  open | not-pursued        — INTENÇÃO SUA.
# Nenhuma região está marcada `not-pursued`: essa decisão é sua, não minha.
# Uma região `absent` não é uma compra devida.
# ---------------------------------------------------------------------------
scope_map:
  by: claude
  map_status: proposta
  regions:
    - {id: formacao-da-grecia, coverage: covered, pursuit: open,
       note: "Idade do Bronze, colonização, nascimento da pólis, e as
              estruturas sociais e políticas que antecedem a cultura clássica."}
    - {id: mito-e-poesia-arcaica, coverage: covered, pursuit: open,
       note: "Cosmogonia, épica e a poesia que fixou o imaginário heroico e
              divino antes da prosa."}
    - {id: lirica-e-poesia-nao-epica, coverage: thin, pursuit: open,
       note: "Lírica monódica e coral, elegia, iambo: a voz individual e a
              poesia de ocasião, distintas da épica e do drama."}
    - {id: religiao-e-culto, coverage: covered, pursuit: open,
       note: "Culto, sacrifício, santuário, festival, mistérios — a religião
              praticada, distinta da religião narrada."}
    - {id: teatro-e-drama, coverage: covered, pursuit: open,
       note: "Tragédia e comédia como instituições cívicas e como forma de
              pensamento sobre justiça, poder e o divino."}
    - {id: filosofia-grega, coverage: covered, pursuit: open,
       note: "Da cosmologia pré-socrática à metafísica, ética e política
              clássicas."}
    - {id: historiografia-grega, coverage: covered, pursuit: open,
       note: "A invenção da investigação histórica e a análise antiga da
              guerra, do poder e da decisão política."}
    - {id: instituicoes-e-democracia, coverage: covered, pursuit: open,
       note: "Como as instituições da pólis funcionavam de fato: magistraturas,
              assembleia, tribunais, cidadania."}
    - {id: arte-arquitetura-cultura-material, coverage: absent, pursuit: open,
       note: "Escultura, arquitetura, cerâmica, urbanismo, arqueologia: a
              cultura que sobrevive em objetos e não em textos."}
    - {id: ciencia-e-medicina-antigas, coverage: absent, pursuit: open,
       note: "Matemática, astronomia, medicina e história natural como parte
              da mesma transformação intelectual que produziu a filosofia."}
    - {id: helenismo, coverage: thin, pursuit: open,
       note: "A expansão macedônica, os reinos sucessores, e as escolas
              filosóficas que respondem à perda do mundo da pólis."}
    - {id: roma-republicana-fontes-antigas, coverage: absent, pursuit: open,
       note: "Fontes antigas sobre a República: historiografia, oratória e
              pensamento político romanos escritos por romanos."}
    - {id: roma-imperial-fontes-antigas, coverage: absent, pursuit: open,
       note: "Historiografia e biografia imperiais antigas: o Império narrado
              de dentro."}
    - {id: literatura-latina, coverage: covered, pursuit: open,
       note: "Épica, poesia mitológica e prosa de ficção latinas."}
    - {id: filosofia-romana, coverage: covered, pursuit: open,
       note: "A apropriação romana da filosofia grega como disciplina moral e
              prática de vida."}
    - {id: religiao-romana-e-cristianismo-antigo, coverage: absent, pursuit: open,
       note: "Culto romano, religiões do Império, e o cristianismo enquanto
              fenômeno do mundo antigo."}
    - {id: tecnica-e-materialidade-romanas, coverage: thin, pursuit: open,
       note: "Guerra, engenharia, agronomia, administração e direito: a
              infraestrutura técnica e jurídica que sustentou o Império.
              Região criada por decisão sua em 2026-09-12, ao decidir que
              Vegécio não devia ser lido como literatura."}
    - {id: recepcao-e-tradicao-classica, coverage: covered, pursuit: open,
       note: "Como a Antiguidade foi lida, apropriada e reinterpretada depois
              de si mesma — e as teorias modernas que a usam como material."}

excluded: []

# ===========================================================================
# SEQUÊNCIA
#
# Sua ordem e os seus títulos de seção, preservados. Três desvios, todos
# aprovados por você em 2026-09-12 e registrados em `order_changes`.
#
# Sobre as entradas expandidas de volume: o argumento que você escreveu era do
# VOLUME, não da peça. Ele está preservado verbatim no comentário que abre cada
# grupo, atribuído a você. As entradas individuais não recebem um `why_here`
# seu, porque você não escreveu um — inventá-lo seria pôr palavras suas onde
# elas não estão.
# ===========================================================================
sequence:

  - movement: "I. Contexto histórico e formação da Grécia"
    purpose: "Formação do mundo grego, pólis, sociedade, educação e passagem
              para a cultura clássica."
    purpose_by: voce
    regions: [formacao-da-grecia]

  - work: guarinello--historia-antiga
    role: foundational
    demand: leve
    why_here: "É um bom enquadramento inicial para situar a Grécia e Roma
               dentro do mundo antigo antes de aprofundar suas histórias
               particulares."
    why_here_by: voce
    perspective: "Panorama geral das civilizações antigas e do mundo
                  mediterrânico."
    subjects_stated: [formacao-das-sociedades-antigas, estruturas-politicas,
                      economia, guerra, religiao, cultura,
                      transformacoes-historicas]

  - work: osborne--greece-in-the-making
    role: foundational
    demand: exigente
    why_here: "Aprofunda a formação histórica da Grécia e fornece o contexto
               necessário para compreender o surgimento de sua cultura
               literária, religiosa e política."
    why_here_by: voce
    perspective: "História da formação da Grécia arcaica."
    subjects_stated: [idade-do-bronze, comunidades-gregas, polis, colonizacao,
                      transformacoes-sociais, desenvolvimento-politico,
                      guerras-persas]

  - work: finley--the-ancient-greeks
    role: foundational
    demand: moderado
    why_here: "Oferece uma visão sintética da sociedade grega e ajuda a
               transformar o cenário histórico em realidade social concreta."
    why_here_by: voce
    perspective: "História social, política e cultural da Grécia antiga."
    subjects_stated: [polis, cidadania, escravidao, guerra, economia,
                      sociedade, politica, organizacao-da-vida-grega]

  - work: everitt--the-rise-of-athens
    role: foundational
    demand: leve
    why_here: "Concentra o panorama na pólis que se tornaria o principal centro
               político, artístico e intelectual da Grécia clássica."
    why_here_by: voce
    perspective: "História política e cultural de Atenas."
    subjects_stated: [formacao-da-cidade, guerras, democracia, imperio,
                      cultura, politica, desenvolvimento-ateniense]

  - work: jaeger-werner--paideia
    role: foundational
    demand: exigente
    why_here: "É fundamental para compreender a paideía como projeto de
               formação integral e perceber como literatura, política,
               filosofia e educação fazem parte de uma mesma tradição
               cultural."
    why_here_by: voce
    perspective: "História cultural e intelectual da formação grega."
    subjects_stated: [educacao, poesia, homero, formacao-moral, politica,
                      filosofia, arte, cidadania, ideal-de-homem-grego]
    # OBSERVAÇÃO MINHA, não desvio: Paideia comenta obras que, nesta ordem,
    # ainda não foram lidas. Você decidiu mantê-la aqui, e a razão é boa — ela
    # é o único item da lista que declara a TESE da coleção, e as seções II a
    # VI são o teste dessa tese. O custo fica registrado, e o caminho
    # cronológico oferece a leitura alternativa. Ver review/greco-roman.md §5.

  - movement: "II. Poesia, mito e religião na Grécia arcaica"
    purpose: "Cosmogonia, deuses, heróis, destino, culto e formação do
              imaginário religioso grego."
    purpose_by: voce
    regions: [mito-e-poesia-arcaica, lirica-e-poesia-nao-epica]

  - work: hesiodo--theogonia
    role: primary-source
    demand: moderado
    why_here: "É a principal porta de entrada literária para compreender como
               os gregos narravam a origem do cosmos e a estrutura do mundo
               divino."
    why_here_by: voce
    perspective: "Cosmogonia, genealogia divina e religião grega."
    subjects_stated: [origem-do-cosmos, genealogia-dos-deuses, gaia, urano,
                      cronos, zeus, sucessao-divina, organizacao-do-universo]

  - work: hesiodo--erga-kai-hemerai
    role: primary-source
    demand: moderado
    why_here: "Complementa a Teogonia mostrando como a visão religiosa grega se
               relacionava com a vida cotidiana, a moral e a condição humana."
    why_here_by: voce
    perspective: "Poesia didática, moral e religiosa."
    subjects_stated: [trabalho, justica, moralidade, idades-do-homem,
                      prometeu, pandora, deuses-e-homens,
                      organizacao-da-vida-humana]

  - work: homero--ilias
    role: primary-source
    demand: exigente
    why_here: "Mostra os deuses em ação dentro do mundo humano e constitui uma
               das bases literárias da cultura grega posterior."
    why_here_by: voce
    perspective: "Épica, religião e cultura heroica grega."
    subjects_stated: [guerra-de-troia, honra, gloria, destino, heroismo,
                      colera, deuses-intervenientes, valores-aristocraticos]
    publication_pref: pub--penguin-companhia--caixa-homero   # decisão sua, 2026-09-23: mostrar a edição que você tem (o Box)

  - work: homero--odysseia
    role: primary-source
    demand: exigente
    why_here: "Expande o mundo homérico para além da guerra e apresenta uma
               forma diferente de heroísmo, baseada sobretudo na inteligência,
               resistência e adaptação."
    why_here_by: voce
    perspective: "Épica, religião e narrativa heroica."
    subjects_stated: [retorno, identidade, astucia, hospitalidade, deuses,
                      monstros, viagens, provas, destino-e-acao-humana]
    publication_pref: pub--penguin-companhia--caixa-homero   # decisão sua, 2026-09-23: mostrar a edição que você tem (o Box)

  - work: pindaro--olympionikai
    role: supplementary
    demand: exigente
    why_here: "É uma leitura complementar que mostra como a poesia grega
               transformava feitos humanos em memória heroica e religiosa."
    why_here_by: voce
    perspective: "Poesia lírica e construção da memória heroica."
    subjects_stated: [herois, jogos, genealogia, gloria, honra, deuses,
                      destino, memoria]

  # ENTRADA NOVA — 2026-09-22. Não vem da sua lista de origem: entrou por
  # pesquisa, a partir da comparação de edições Frazer/Valla. Colocada aqui, e
  # não no fim da sequência, por curation-rules.md §6.9 regra 3. Proposta por
  # mim, aprovada por você em 2026-09-22, neste movimento.
  - work: pseudo-apolodoro--bibliotheke
    role: primary-source
    demand: leve
    publication_pref: pub--loeb--library-i--1921
    # Escolha dele, 2026-09-22: a edição desta coleção é a Loeb, que é a
    # obtenível. NÃO altera o veredito — a Valla continua `recommended` em
    # mérito. Preferência é exibição; veredito é juízo.
    publication_pref_by: voce
    why_here: "É o que o Grimal é na forma antiga: um catálogo de histórias e
               variantes, para consulta durante a leitura dos poetas."
    why_here_by: claude
    perspective: "Compêndio mitográfico antigo — fonte, não interpretação."
    subjects_stated: [genealogias-divinas, herois, ciclos-miticos,
                      variantes-narrativas, epitome, tradicao-mitografica]
    subjects_stated_by: claude
    # TENSÃO DECLARADA, não escondida: este movimento é arcaico e a Biblioteca
    # é um compêndio de época imperial (datação disputada — ver o registro da
    # obra). Ela está aqui pela FUNÇÃO, não pela data. A alternativa examinada
    # e descartada foi o movimento III, que é erudição moderna sobre religião
    # vivida; a Biblioteca não trata de culto nem de crença.

  - work: grimal--dictionnaire-de-la-mythologie-grecque-et-romaine
    role: reference
    demand: leve
    why_here: "Funciona melhor como instrumento de consulta permanente durante
               a leitura dos autores antigos, e não como leitura linear."
    why_here_by: voce
    perspective: "Obra de referência sobre a tradição mitológica clássica."
    subjects_stated: [deuses, herois, genealogias, ciclos-miticos, personagens,
                      variantes-narrativas, tradicoes-gregas-e-romanas]

  - movement: "III. Religião grega e transformação do mito"
    purpose: "Religião, culto, rito, mito, crença e relação entre o imaginário
              religioso e a pólis."
    purpose_by: voce
    regions: [religiao-e-culto]

  - work: mikalson--ancient-greek-religion
    role: foundational
    demand: moderado
    why_here: "É uma introdução sistemática à religião grega propriamente dita
               e ajuda a distinguir religião vivida, mito e literatura."
    why_here_by: voce
    perspective: "Estudo histórico da religião grega antiga."
    subjects_stated: [deuses, culto, sacrificio, festivais, sacerdocio, oracao,
                      praticas-religiosas, religiao-e-sociedade]

  - work: burkert--griechische-religion
    role: foundational
    demand: exigente
    why_here: "É uma das obras centrais para compreender a religião grega como
               sistema histórico e ritual, indo muito além das narrativas
               mitológicas."
    why_here_by: voce
    perspective: "Estudo acadêmico da religião grega."
    subjects_stated: [deuses, ritos, sacrificios, culto, santuarios, iniciacao,
                      morte, praticas-religiosas, estrutura-da-religiao-grega]

  - work: vernant--mythe-et-religion-en-grece-ancienne
    role: critical-response
    demand: exigente
    why_here: "Depois de conhecer a religião em seus aspectos históricos,
               permite compreender como mito, religião e estrutura social
               estavam profundamente entrelaçados."
    why_here_by: voce
    perspective: "Antropologia histórica e interpretação estrutural da religião
                  grega."
    subjects_stated: [mito, rito, deuses, sacrificio, polis,
                      organizacao-social, pensamento-religioso-grego]

  - work: veyne--les-grecs-ont-ils-cru-a-leurs-mythes
    role: critical-response
    demand: moderado
    why_here: "Leva a investigação um passo adiante ao questionar o que
               realmente significa dizer que os gregos “acreditavam” em seus
               mitos."
    why_here_by: voce
    perspective: "História das mentalidades e análise da crença no mundo
                  antigo."
    subjects_stated: [mito, crenca, verdade, imaginacao, narrativa-historica,
                      formas-antigas-de-compreender-a-realidade]

  - movement: "IV. Tragédia, comédia e a crise da pólis"
    purpose: "O mito transformado em reflexão sobre justiça, destino, religião,
              poder, educação e vida política."
    purpose_by: voce
    regions: [teatro-e-drama]

  - work: esquilo--oresteia
    role: primary-source
    demand: exigente
    why_here: "É uma das obras fundamentais para compreender a transformação do
               mito em reflexão sobre justiça, religião, violência e
               organização da pólis."
    why_here_by: voce
    perspective: "Tragédia grega e transformação da justiça arcaica."
    subjects_stated: [maldicao-familiar, vinganca, sacrificio, culpa,
                      justica-divina, formas-antigas-e-novas-de-justica,
                      fundacao-da-ordem-civica]
    publication_pref: pub--iluminuras--oresteia-i   # 2026-10-10: a obra vem em três volumes (Torrano); o vol. I representa o conjunto, como em Política. Vols. II e III: pub--iluminuras--oresteia-ii e -iii

  # -------------------------------------------------------------------------
  # EXPANSÃO DE VOLUME — "Ésquilo, Tragédias" (Iluminuras, trad. Torrano);
  # inclusão aprovada por você em 2026-09-23.
  # Quatro peças de um volume. POSIÇÃO CONFIRMADA por você em 2026-10-05
  # (cartão d-pos-esquilo, opção A): logo depois da Oresteia, que continua a
  # porta de entrada de Ésquilo. A ordem de composição — Os Persas é de 472
  # a.C., anterior à Oresteia — foi considerada e recusada: a coleção não é
  # cronológica.
  # -------------------------------------------------------------------------
  - work: esquilo--persai
    role: primary-source
    demand: exigente
    why_here: "Completa o Ésquilo da coleção além da Oresteia, no mesmo
               tradutor e em edição bilíngue."
    why_here_by: claude
    inserted_by: claude
    publication_pref: pub--iluminuras--esquilo-tragedias--2009

  - work: esquilo--hepta-epi-thebas
    role: primary-source
    demand: exigente
    why_here: "Completa o Ésquilo da coleção além da Oresteia, no mesmo
               tradutor e em edição bilíngue."
    why_here_by: claude
    inserted_by: claude
    publication_pref: pub--iluminuras--esquilo-tragedias--2009

  - work: esquilo--hiketides
    role: primary-source
    demand: exigente
    why_here: "Completa o Ésquilo da coleção além da Oresteia, no mesmo
               tradutor e em edição bilíngue."
    why_here_by: claude
    inserted_by: claude
    publication_pref: pub--iluminuras--esquilo-tragedias--2009

  - work: esquilo--prometheus-desmotes
    role: primary-source
    demand: exigente
    why_here: "Completa o Ésquilo da coleção além da Oresteia, no mesmo
               tradutor e em edição bilíngue."
    why_here_by: claude
    inserted_by: claude
    publication_pref: pub--iluminuras--esquilo-tragedias--2009


  # -------------------------------------------------------------------------
  # EXPANSÃO DE VOLUME — "Sófocles, A Trilogia Tebana" (item 17 da sua lista).
  # Não é uma trilogia autoral: são três peças independentes, compostas com
  # cerca de 35 anos de intervalo e em ordem inversa à narrativa (Antígona
  # ~441, Édipo Rei ~429, Édipo em Colono ~401). "A Trilogia Tebana" é o nome
  # de uma PUBLICAÇÃO (Zahar, trad. Mário da Gama Kury) — registrada em
  # publications/. A ordem abaixo é a ordem narrativa da publicação, que é a
  # ordem em que você as receberia ao abrir o volume.
  #
  # O SEU texto, verbatim, sobre a entrada inteira:
  #   Perspectiva: "Tragédia grega e investigação da condição humana."
  #   Temas: "destino, conhecimento, cegueira, culpa, família, lei divina, lei
  #           humana, poder, morte e conflito entre indivíduo e cidade."
  #   Porquê: "É uma das melhores expressões da capacidade da tragédia de
  #            transformar o mito em investigação filosófica e política."
  # -------------------------------------------------------------------------
  - work: sofocles--oidipous-tyrannos
    role: primary-source
    demand: exigente
    why_here: "Entrou pela expansão do volume A Trilogia Tebana. O argumento é
               seu e vale para as três peças; está acima, verbatim."
    why_here_by: claude

  - work: sofocles--oidipous-epi-kolonoi
    role: primary-source
    demand: exigente
    why_here: "Idem — expansão do mesmo volume."
    why_here_by: claude

  - work: sofocles--antigone
    role: primary-source
    demand: exigente
    why_here: "Idem — expansão do mesmo volume."
    why_here_by: claude

  - work: euripides--medeia
    role: primary-source
    demand: moderado
    why_here: "Reinterpreta o mito de Medeia como uma investigação radical
               sobre paixão, humilhação e vingança."
    why_here_by: voce
    perspective: "Tragédia psicológica e crítica das relações humanas."
    subjects_stated: [paixao, vinganca, casamento, abandono,
                      condicao-feminina, poder, ira, racionalidade, violencia]
    # Nota de publicação, não de currículo: na série da Editora 34 (trad. Jaa
    # Torrano) Medeia está no Teatro Completo I, volume que a sua lista não
    # inclui. Não é redundância — é uma questão de por qual edição adquiri-la.

  - work: euripides--bakchai
    role: primary-source
    demand: exigente
    why_here: "É particularmente importante para compreender a dimensão
               extática da religião grega e seus conflitos com as pretensões
               da razão e da ordem política."
    why_here_by: voce
    perspective: "Tragédia, religião e experiência do divino."
    subjects_stated: [dioniso, extase, loucura, identidade, poder, sacrificio,
                      repressao, limites-da-racionalidade]
    publication_pref: pub--editora-34--euripides-teatro-completo-vi--2026   # decisão sua, 2026-10-10 (d-ed-bacantes)
    # As Bacantes ainda não saiu na série da Editora 34 (os volumes publicados
    # vão de I a V). Questão de edição, registrada em review/greco-roman.md §7.

  # -------------------------------------------------------------------------
  # EXPANSÃO DE VOLUME — "Eurípides, Teatro Completo II" (Editora 34, trad.
  # Jaa Torrano, 2022): Os Heráclidas, Hipólito, Andrômaca, Hécuba.
  # SEU texto, verbatim:
  #   Perspectiva: "Tragédia grega e diversidade do pensamento trágico de
  #                 Eurípides."
  #   Temas: "guerra, família, desejo, honra, sofrimento, religião, poder e
  #           condição humana."
  #   Porquê: "Amplia o contato com Eurípides e mostra que os problemas de
  #            Medeia não são um caso isolado, mas parte de uma investigação
  #            recorrente sobre a sociedade e o indivíduo."
  # -------------------------------------------------------------------------
  - {work: euripides--herakleidai, role: primary-source, demand: exigente,
     why_here: "Expansão do volume Teatro Completo II; argumento seu, acima.",
     why_here_by: claude}
  - {work: euripides--hippolytos, role: primary-source, demand: exigente,
     why_here: "Expansão do volume Teatro Completo II; argumento seu, acima.",
     why_here_by: claude}
  - {work: euripides--andromache, role: primary-source, demand: exigente,
     why_here: "Expansão do volume Teatro Completo II; argumento seu, acima.",
     why_here_by: claude}
  - {work: euripides--hekabe, role: primary-source, demand: exigente,
     why_here: "Expansão do volume Teatro Completo II; argumento seu, acima.",
     why_here_by: claude}

  # -------------------------------------------------------------------------
  # EXPANSÃO DE VOLUME — "Teatro Completo III": As Suplicantes, Electra,
  # Héracles.
  # SEU texto, verbatim:
  #   Perspectiva: "Tragédia grega, guerra e conflito moral."
  #   Temas: "justiça, guerra, família, vingança, loucura, violência e
  #           responsabilidade humana."
  #   Porquê: "Aprofunda a variedade temática de Eurípides e amplia a percepção
  #            da relação entre mito, política e ética."
  # -------------------------------------------------------------------------
  - {work: euripides--hiketides, role: primary-source, demand: exigente,
     why_here: "Expansão do volume Teatro Completo III; argumento seu, acima.",
     why_here_by: claude}
  - {work: euripides--elektra, role: primary-source, demand: exigente,
     why_here: "Expansão do volume Teatro Completo III; argumento seu, acima.",
     why_here_by: claude}
  - {work: euripides--herakles, role: primary-source, demand: exigente,
     why_here: "Expansão do volume Teatro Completo III; argumento seu, acima.",
     why_here_by: claude}

  # -------------------------------------------------------------------------
  # EXPANSÃO DE VOLUME — "Teatro Completo IV": As Troianas, Ifigênia em
  # Táurida, Íon.
  # SEU texto, verbatim:
  #   Perspectiva: "Tragédia, guerra, religião e identidade."
  #   Temas: "destruição, exílio, sacrifício, guerra, origem, família, deuses e
  #           identidade."
  #   Porquê: "Acrescenta uma dimensão histórica e política particularmente
  #            forte à leitura do teatro de Eurípides."
  # -------------------------------------------------------------------------
  - {work: euripides--troades, role: primary-source, demand: exigente,
     why_here: "Expansão do volume Teatro Completo IV; argumento seu, acima.",
     why_here_by: claude}
  - {work: euripides--iphigeneia-he-en-taurois, role: primary-source,
     demand: exigente,
     why_here: "Expansão do volume Teatro Completo IV; argumento seu, acima.",
     why_here_by: claude}
  - {work: euripides--ion, role: primary-source, demand: exigente,
     why_here: "Expansão do volume Teatro Completo IV; argumento seu, acima.",
     why_here_by: claude}

  # -------------------------------------------------------------------------
  # EXPANSÃO DE VOLUME — "Teatro Completo V": Helena, As Fenícias, Orestes.
  # SEU texto, verbatim:
  #   Perspectiva: "Tragédia tardia e revisão dos mitos tradicionais."
  #   Temas: "guerra, identidade, aparência, verdade, família, violência, poder
  #           e destino."
  #   Porquê: "Completa o panorama de Eurípides e evidencia como o autor
  #            reelabora criticamente os mitos tradicionais."
  # -------------------------------------------------------------------------
  - {work: euripides--helene, role: primary-source, demand: exigente,
     why_here: "Expansão do volume Teatro Completo V; argumento seu, acima.",
     why_here_by: claude}
  - {work: euripides--phoinissai, role: primary-source, demand: exigente,
     why_here: "Expansão do volume Teatro Completo V; argumento seu, acima.",
     why_here_by: claude}
  - {work: euripides--orestes, role: primary-source, demand: exigente,
     why_here: "Expansão do volume Teatro Completo V; argumento seu, acima.",
     why_here_by: claude}

  - work: aristofanes--nephelai
    role: primary-source
    demand: moderado
    why_here: "Mostra como a transformação intelectual da Atenas clássica era
               percebida e satirizada no próprio ambiente político e cultural
               da pólis."
    why_here_by: voce
    perspective: "Comédia política e intelectual da Atenas clássica."
    subjects_stated: [socrates, sofistas, educacao, retorica, novas-ideias,
                      tradicao-e-inovacao, critica-social]

  - movement: "V. Do mito ao logos"
    purpose: "Nascimento da filosofia, investigação racional da natureza e
              transformação das antigas perguntas religiosas."
    purpose_by: voce
    regions: [filosofia-grega]

  - work: vernant--les-origines-de-la-pensee-grecque
    role: foundational
    demand: moderado
    why_here: "É o principal elo conceitual entre o mundo mítico que você
               acabou de estudar e o nascimento histórico da filosofia grega."
    why_here_by: voce
    perspective: "História intelectual da Grécia arcaica."
    subjects_stated: [polis, pensamento-racional, politica, secularizacao,
                      organizacao-social, do-mito-a-explicacao]

  - work: kirk-raven-schofield--the-presocratic-philosophers
    role: foundational
    demand: exigente
    why_here: "Apresenta diretamente os filósofos que transformaram a reflexão
               sobre o cosmos em investigação racional da realidade."
    why_here_by: voce
    perspective: "História da filosofia pré-socrática."
    subjects_stated: [arche, natureza, cosmos, mudanca, ser, numero, materia,
                      primeiros-modelos-racionais]

  - work: mckirahan--philosophy-before-socrates
    role: supplementary
    demand: moderado
    why_here: "Complementa Kirk, Raven e Schofield com uma abordagem
               introdutória e comentada baseada diretamente nos textos dos
               primeiros filósofos."
    why_here_by: voce
    perspective: "Introdução histórica e textual à filosofia anterior a
                  Sócrates."
    subjects_stated: [pre-socraticos, cosmologia, ontologia,
                      argumentos-filosoficos, fragmentos]

  - movement: "VI. Sócrates, Platão e Aristóteles"
    purpose: "Ética, política, conhecimento, metafísica, arte e formação do
              homem."
    purpose_by: voce
    regions: [filosofia-grega]

  - work: platao--apologia-sokratous
    role: primary-source
    demand: leve
    why_here: "É a melhor porta de entrada para a figura de Sócrates e para a
               filosofia como modo de vida orientado pela busca da verdade."
    why_here_by: voce
    perspective: "Filosofia socrática e defesa da vida filosófica."
    subjects_stated: [justica, verdade, virtude, sabedoria,
                      consciencia-moral, educacao, missao-filosofica]

  - work: platao--kriton
    role: primary-source
    demand: leve
    why_here: "Aprofunda o problema da relação entre consciência individual,
               justiça e ordem política."
    why_here_by: voce
    perspective: "Ética e filosofia política socrática."
    subjects_stated: [justica, lei, dever, cidadania, obediencia,
                      individuo-e-cidade]

  - work: platao--phaidon
    role: primary-source
    demand: moderado
    why_here: "Marca a passagem da figura histórica de Sócrates para os
               problemas metafísicos centrais do pensamento platônico."
    why_here_by: voce
    perspective: "Filosofia socrática e metafísica platônica."
    subjects_stated: [morte, alma, imortalidade, conhecimento, filosofia,
                      purificacao, corpo-e-alma]

  # PARTICIPAÇÃO NOVA sobre registro existente. A República já estava na
  # biblioteca, vinda de Política, onde o papel dela é outro. Um arquivo,
  # duas participações. Ver curation-rules.md §2.7.
  - work: platao--politeia
    role: foundational
    demand: exigente
    why_here: "É o grande centro do projeto intelectual platônico e reúne
               educação, política, ética, conhecimento e metafísica."
    why_here_by: voce
    perspective: "Filosofia política, ética e metafísica."
    subjects_stated: [justica, cidade, educacao, filosofo-rei, conhecimento,
                      formas, alegoria-da-caverna, regimes-politicos]
    scope: "Aqui ela é lida como o centro do projeto platônico inteiro; em
            Política ela entra como fonte do pensamento político ocidental."
    publication_pref: pub--edufpa--a-republica   # decisão sua, 2026-09-27 (d-ed-republica), válida nas duas coleções

  - work: platao--symposion
    role: primary-source
    demand: moderado
    why_here: "Complementa a República mostrando como o desejo e a beleza podem
               conduzir à busca filosófica."
    why_here_by: voce
    perspective: "Filosofia do amor e da beleza."
    subjects_stated: [eros, beleza, desejo, alma, conhecimento,
                      amor-e-filosofia]

  - work: aristoteles--poietike
    role: primary-source
    demand: moderado
    why_here: "Permite voltar às tragédias gregas que você já leu e
               compreendê-las agora a partir de uma teoria filosófica da arte."
    why_here_by: voce
    perspective: "Filosofia da arte e teoria da tragédia."
    subjects_stated: [poesia, imitacao, tragedia, enredo, personagem,
                      reconhecimento, peripecia, catarse]
    requires: [esquilo--oresteia, sofocles--oidipous-tyrannos]

  - work: aristoteles--ethika-nikomacheia
    role: foundational
    demand: exigente
    why_here: "Sistematiza uma das bases da ética ocidental e transforma em
               teoria filosófica questões morais já presentes na literatura e
               na vida política grega."
    why_here_by: voce
    perspective: "Filosofia moral e teoria da virtude."
    subjects_stated: [felicidade, virtude, habito, prudencia, amizade, justica,
                      finalidade-da-vida-humana]

  # PARTICIPAÇÃO NOVA sobre registro existente (Política).
  - work: aristoteles--politika
    role: foundational
    demand: exigente
    why_here: "É a continuação natural da Ética a Nicômaco e permite
               compreender filosoficamente a estrutura política que aparece na
               história grega."
    why_here_by: voce
    perspective: "Filosofia política e análise da pólis."
    subjects_stated: [cidade, cidadania, constituicoes, justica, escravidao,
                      educacao, familia, formas-de-governo]
    requires: [aristoteles--ethika-nikomacheia]
    scope: "Aqui ela fecha o par ética→política dentro do percurso grego; em
            Política ela é fonte fundadora da teoria política ocidental."
    publication_pref: pub--unb--politica   # escolha sua, 2026-09-27 (d-ed-politica), válida nas duas coleções

  - work: aristoteles--ta-meta-ta-physika
    role: primary-source
    demand: exigente
    why_here: "É a etapa mais abstrata do percurso e consolida a transformação
               da antiga pergunta sobre o cosmos em investigação ontológica
               sistemática."
    why_here_by: voce
    perspective: "Metafísica e investigação dos princípios fundamentais da
                  realidade."
    subjects_stated: [ser, substancia, causas, ato-e-potencia, essencia,
                      primeiro-motor]

  - movement: "VII. História, política e mundo grego clássico"
    purpose: "Historiografia, democracia, guerra, poder, instituições e
              interpretação da experiência política grega."
    purpose_by: voce
    regions: [historiografia-grega, instituicoes-e-democracia]
    # Este movimento perdeu duas obras na importação: Finley (O Legado da
    # Grécia) e Highet foram para o movimento XI, por decisão sua de
    # 2026-09-12. Ver `order_changes`.

  - work: herodoto--historiai
    role: primary-source
    demand: exigente
    why_here: "É uma das fontes primárias fundamentais para perceber como os
               próprios gregos começaram a investigar historicamente homens,
               povos e acontecimentos."
    why_here_by: voce
    perspective: "Historiografia grega e investigação do passado."
    subjects_stated: [guerras-medicas, povos, costumes, religiao, politica,
                      memoria, gregos-e-persas, explicacao-historica]

  # PARTICIPAÇÃO NOVA sobre registro existente (Política).
  - work: tucidides--historiai
    role: foundational
    demand: exigente
    why_here: "É a principal obra histórica para compreender a crise da pólis
               clássica e oferece uma análise particularmente rigorosa da
               guerra, do poder e do comportamento político."
    why_here_by: voce
    perspective: "Historiografia política e militar da Grécia clássica."
    subjects_stated: [guerra-do-peloponeso, atenas, esparta, imperialismo,
                      democracia, estrategia, poder, diplomacia,
                      faccoes-politicas, decisoes-coletivas]
    scope: "Aqui ele é a história da crise que a tragédia e a filosofia desta
            coleção estão respondendo; em Política ele entra como fonte do
            realismo político."

  - work: xenofonte--hellenika
    role: primary-source
    demand: exigente
    why_here: "Continua a narrativa interrompida por Tucídides e conduz a
               leitura para as profundas transformações políticas que antecedem
               a ascensão da Macedônia."
    why_here_by: voce
    perspective: "Historiografia grega e continuidade da história política do
                  século V e IV a.C."
    subjects_stated: [fim-da-guerra-do-peloponeso, derrota-de-atenas,
                      hegemonia-espartana, conflitos-politicos, guerras,
                      transformacoes-do-mundo-grego]
    requires: [tucidides--historiai]
    publication_pref: pub--loeb--hellenica-i   # 2026-10-10: a obra vem em dois volumes Loeb; o vol. I representa o conjunto. Vol. II: pub--loeb--hellenica-ii

  - work: aristoteles--athenaion-politeia
    role: primary-source
    demand: moderado
    why_here: "Complementa a Política mostrando concretamente como as
               instituições atenienses se desenvolveram historicamente e como
               funcionava a democracia."
    why_here_by: voce
    perspective: "História institucional e política de Atenas."
    subjects_stated: [formacao-da-democracia, reformas-politicas, solon,
                      clistenes, instituicoes, magistraturas, assembleia,
                      tribunais, cidadania, estado-ateniense]
    requires: [aristoteles--politika]

  - work: hansen--the-athenian-democracy-in-the-age-of-demosthenes
    role: supplementary
    demand: exigente
    why_here: "Oferece uma reconstrução sistemática do funcionamento da
               democracia ateniense e fornece o contexto histórico necessário
               para compreender sua estrutura política."
    why_here_by: voce
    perspective: "Estudo histórico e institucional da democracia ateniense."
    subjects_stated: [cidadania, assembleia, conselho, tribunais,
                      magistraturas, participacao-politica,
                      organizacao-territorial, sociedade-ateniense]

  # -------------------------------------------------------------------------
  # EXPANSÃO DE VOLUME — "Plutarco, Vidas Paralelas (seleção grega)".
  # Sete biografias, portanto sete obras. A sua nota rotulava a seleção como
  # "grega" e incluía César; por decisão sua (2026-09-12) César fica, e o
  # rótulo é que foi corrigido: Plutarco escreveu as Vidas em PARES
  # grego/romano, e Alexandre é pareado justamente com César. A ordem abaixo é
  # a sua, e a sua glosa de cada Vida está preservada em `why_here` — ela é o
  # único caso de expansão em que você escreveu uma linha por obra.
  #
  # SEU texto sobre a entrada: Perspectiva: "Biografia histórica e memória
  # política da Grécia antiga." Porquê: "Permite observar a história grega
  # através das trajetórias individuais de seus principais personagens e mostra
  # como a memória política da Antiguidade foi construída."
  # -------------------------------------------------------------------------
  - {work: plutarco--solon, role: primary-source, demand: moderado,
     why_here: "formação da democracia", why_here_by: voce,
     publication_pref: pub--coimbra--vidas-paralelas-solon-e-publicola--2012}   # escolhida em 2026-10-10 (Etapa 1): série de Coimbra, como as outras Vidas; pesquisa na obra
  - {work: plutarco--themistokles, role: primary-source, demand: moderado,
     why_here: "Guerras Médicas", why_here_by: voce,
     publication_pref: pub--gredos--vidas-paralelas-ii--2024}   # decisão sua, 2026-10-10 (d-ed-plutarco-temistocles)
  - {work: plutarco--perikles, role: primary-source, demand: moderado,
     why_here: "auge de Atenas", why_here_by: voce,
     publication_pref: pub--annablume--vidas-paralelas-pericles-e-fabio-maximo--2012}   # escolhida em 2026-10-10 (Etapa 1): série de Coimbra, edição brasileira; pesquisa na obra
  - {work: plutarco--alkibiades, role: primary-source, demand: moderado,
     why_here: "crise e Guerra do Peloponeso", why_here_by: voce,
     publication_pref: pub--annablume--vidas-paralelas-alcibiades-e-coriolano--2011}   # escolhida em 2026-10-10 (Etapa 1): série de Coimbra, edição brasileira; pesquisa na obra
  - {work: plutarco--demosthenes, role: primary-source, demand: moderado,
     why_here: "crise do século IV e Macedônia", why_here_by: voce}
  - {work: plutarco--alexandros, role: primary-source, demand: moderado,
     why_here: "conquista e expansão helenística", why_here_by: voce}
  - {work: plutarco--kaisar, role: primary-source, demand: moderado,
     why_here: "transição para o mundo romano", why_here_by: voce,
     scope: "Par de Alexandre. É o único ponto da coleção em que a passagem
             Grécia → Roma acontece dentro de uma fonte antiga."}

  - movement: "VIII. Alexandre e o mundo helenístico"
    purpose: "Expansão da cultura grega, transformação do mundo mediterrânico
              e surgimento de novas formas de filosofia e cultura."
    purpose_by: voce
    regions: [helenismo]
    # Este movimento perdeu Epicteto para o movimento X, por decisão sua de
    # 2026-09-12. O par Epicuro–Epicteto que ele formava aqui — as duas escolas
    # helenísticas como respostas à perda do mundo político da pólis — passa a
    # existir como RELAÇÃO entre obras, não como adjacência na sequência. Ver
    # `order_changes` e review/greco-roman.md §5.

  - work: martin-blackwell--alexander-the-great
    role: foundational
    demand: leve
    why_here: "É a ponte histórica entre a pólis clássica e o mundo ampliado no
               qual a cultura grega se espalha por todo o Oriente."
    why_here_by: voce
    perspective: "História de Alexandre e do mundo macedônico."
    subjects_stated: [macedonia, conquista-persa, expansao-grega, imperio,
                      guerra, politica, mundo-helenistico]

  - work: epicuro--epistole-pros-menoikea
    role: primary-source
    demand: leve
    why_here: "Introduz a filosofia helenística como uma resposta à busca
               individual pela felicidade em um mundo politicamente
               transformado."
    why_here_by: voce
    perspective: "Filosofia helenística e ética epicurista."
    subjects_stated: [prazer, felicidade, morte, deuses, medo, prudencia,
                      vida-filosofica]

  - movement: "IX. Roma: formação, sociedade e poder"
    purpose: "Do mundo republicano ao Império e a transformação romana da
              herança grega."
    purpose_by: voce
    regions: [literatura-latina, tecnica-e-materialidade-romanas]

  - work: beard--spqr
    role: foundational
    demand: moderado
    why_here: "É a melhor transição geral para Roma porque apresenta a
               civilização romana em sua estrutura política e social antes do
               aprofundamento de suas fontes literárias e filosóficas."
    why_here_by: voce
    perspective: "História política, social e cultural de Roma."
    subjects_stated: [fundacao, republica, imperio, sociedade, politica,
                      religiao, cidadania, guerra, expansao]

  - work: woolf--rome-an-empires-story
    role: supplementary
    demand: moderado
    why_here: "Complementa SPQR deslocando o foco para o funcionamento e a
               diversidade do Império Romano."
    why_here_by: voce
    perspective: "História social e cultural do Império Romano."
    subjects_stated: [expansao, integracao-imperial, cidades, povos, religiao,
                      administracao, cultura, transformacao-do-mediterraneo]

  - work: virgilio--aeneis
    role: primary-source
    demand: exigente
    why_here: "É a grande apropriação romana da tradição épica grega e
               estabelece um contraponto latino à Ilíada e à Odisseia."
    why_here_by: voce
    perspective: "Épica romana e construção da identidade de Roma."
    subjects_stated: [troia, eneias, destino, deuses, fundacao, guerra, dever,
                      familia, missao-historica]
    requires: [homero--ilias, homero--odysseia]

  - work: ovidio--metamorphoses
    role: primary-source
    demand: exigente
    why_here: "Funciona como uma enorme síntese literária da tradição
               mitológica clássica e como uma das principais pontes entre a
               mitologia antiga e a cultura ocidental posterior."
    why_here_by: voce
    perspective: "Poesia mitológica e literatura romana."
    subjects_stated: [transformacao, deuses, herois, amor, violencia, destino,
                      criacao, mitos-gregos-e-romanos]

  - work: apuleio--metamorphoses-asinus-aureus
    role: primary-source
    demand: moderado
    why_here: "Amplia o estudo da literatura romana para além da épica e mostra
               como o imaginário religioso funcionava na cultura cotidiana do
               Império."
    why_here_by: voce
    perspective: "Romance latino, religião e cultura popular do Império
                  Romano."
    subjects_stated: [transformacao, magia, iniciacao, religiao, erotismo,
                      deuses, moralidade, experiencia-humana]

  - work: vegecio--epitoma-rei-militaris
    role: primary-source
    demand: moderado
    why_here: "É uma fonte especializada que permite observar uma dimensão
               fundamental da civilização romana: a organização militar que
               sustentou sua expansão e poder imperial."
    why_here_by: voce
    perspective: "Tratado romano sobre arte militar."
    subjects_stated: [organizacao-do-exercito, treinamento, disciplina,
                      estrategia, logistica, guerra]
    scope: "Único membro da região `tecnica-e-materialidade-romanas`, criada
            por decisão sua em 2026-09-12. Posição na sequência inalterada:
            o que mudou foi a região a que ele responde, não onde ele é lido."
    publication_pref: pub--annablume--vegecio-compendio-da-arte-militar--2011   # escolhida em 2026-10-10 (Etapa 1): única tradução em português, bilíngue; edição brasileira do texto de Coimbra; pesquisa na obra

  - movement: "X. Filosofia moral romana"
    purpose: "Transformação da filosofia grega em disciplina moral e prática de
              vida no mundo romano."
    purpose_by: voce
    regions: [filosofia-romana]

  - work: cicero--de-officiis
    role: primary-source
    demand: moderado
    why_here: "Mostra como conceitos filosóficos gregos foram apropriados e
               transformados pela cultura política e moral romana."
    why_here_by: voce
    perspective: "Filosofia moral romana com forte influência estoica."
    subjects_stated: [dever, virtude, justica, honra, prudencia,
                      responsabilidade-publica, bem-comum]

  - work: seneca--epistulae-morales-ad-lucilium
    role: primary-source
    demand: moderado
    why_here: "Apresenta o estoicismo como disciplina cotidiana voltada para a
               formação moral do indivíduo."
    why_here_by: voce
    perspective: "Estoicismo romano e filosofia como prática de vida."
    subjects_stated: [morte, tempo, riqueza, amizade, sofrimento, virtude,
                      autocontrole, serenidade]

  # DESLOCADO da seção VIII por decisão sua de 2026-09-12. Ver `order_changes`.
  - work: epicteto--encheiridion
    role: primary-source
    demand: leve
    why_here: "Apresenta o estoicismo como exercício cotidiano de formação
               moral e domínio de si."
    why_here_by: voce
    perspective: "Estoicismo e ética prática."
    subjects_stated: [liberdade-interior, o-que-depende-de-nos, paixoes,
                      disciplina, sofrimento, racionalidade]
    scope: "Colocado entre Sêneca e Marco Aurélio porque é a única dependência
            direta entre dois autores visível na própria ordem da coleção: as
            Meditações são, em parte, um exercício sobre Epicteto."

  - work: marco-aurelio--ta-eis-heauton
    role: primary-source
    demand: leve
    why_here: "Fecha o desenvolvimento do estoicismo romano mostrando sua
               aplicação prática por um indivíduo situado no centro do poder
               imperial."
    why_here_by: voce
    perspective: "Estoicismo romano e exercício pessoal de reflexão."
    subjects_stated: [dever, morte, natureza, razao, impermanencia,
                      autocontrole, destino, responsabilidade]
    requires: [epicteto--encheiridion]

  - movement: "XI. Legado e interpretação moderna do mundo greco-romano"
    purpose: "Como a cultura clássica passou a ser estudada, reinterpretada e
              incorporada pela tradição ocidental."
    purpose_by: voce
    regions: [recepcao-e-tradicao-classica]
    # Este movimento ganhou duas obras na importação — Finley (O Legado da
    # Grécia) e Highet —, que na sua lista fechavam a seção VII. Decisão sua de
    # 2026-09-12. Ver `order_changes`.

  # DESLOCADO da seção VII.
  - work: finley--the-legacy-of-greece
    role: supplementary
    demand: moderado
    why_here: "Mostra como a experiência grega foi reinterpretada e incorporada
               pelas civilizações posteriores."
    why_here_by: voce
    perspective: "Interpretação histórica da herança grega."
    subjects_stated: [politica, sociedade, pensamento, cultura, democracia,
                      economia, instituicoes, influencia-grega-no-ocidente]
    scope: "Volume COLETIVO organizado por Finley, não uma obra dele. Ver o
            registro da obra."

  # DESLOCADO da seção VII.
  - work: highet--the-classical-tradition
    role: supplementary
    demand: exigente
    why_here: "É o primeiro grande passo para perceber que estudar Grécia e
               Roma também significa compreender a longa tradição ocidental que
               se formou a partir delas."
    why_here_by: voce
    perspective: "História da recepção da Antiguidade na cultura ocidental."
    subjects_stated: [literatura, educacao, humanismo, renascimento,
                      classicismo, transmissao-greco-romana]

  - work: campbell--the-hero-with-a-thousand-faces
    role: critical-response
    demand: moderado
    why_here: "Funciona melhor depois das fontes clássicas porque permite
               avaliar criticamente sua tentativa de encontrar padrões
               universais nos mitos."
    why_here_by: voce
    perspective: "Mitologia comparada e teoria do mito."
    subjects_stated: [jornada-do-heroi, iniciacao, simbolos, arquetipos,
                      transformacao, estruturas-narrativas-recorrentes]
    scope: "Único membro cujo objeto não é greco-romano. Entra pelo quarto
            critério de inclusão — teoria que o acervo usa para ler o material
            —, e a sua própria nota já o trata como objeto de avaliação e não
            como autoridade."

# ===========================================================================
# CAMINHOS
# ===========================================================================
paths:
  - id: cronologico
    title_pt: "Caminho cronológico"
    by: claude
    approved_by_you: 2026-09-12
    declares: "Os mesmos 74 membros, na ordem aproximada em que o mundo que
               eles descrevem aconteceu — não na ordem em que a sua sequência
               principal os argumenta. Existe para resolver uma coisa
               específica: na sequência principal, As Nuvens e a Apologia são
               lidas antes da Guerra do Peloponeso que as explica, e Paideia é
               lida antes das obras que ela comenta. Aqui não."
    excludes_by_design: []
    note: "A ordem é aproximada por construção. Datas de composição não estão
           pesquisadas (todos os 71 registros novos são `not_researched`), e
           várias são disputadas. Este caminho é uma HIPÓTESE de ordenação e
           deve ser revisto quando a pesquisa de datas existir."
    works: [guarinello--historia-antiga, osborne--greece-in-the-making,
            homero--ilias, homero--odysseia,
            hesiodo--theogonia, hesiodo--erga-kai-hemerai,
            pindaro--olympionikai,
            finley--the-ancient-greeks, everitt--the-rise-of-athens,
            kirk-raven-schofield--the-presocratic-philosophers,
            mckirahan--philosophy-before-socrates,
            herodoto--historiai,
            esquilo--oresteia,
            sofocles--antigone, sofocles--oidipous-tyrannos,
            euripides--medeia, euripides--herakleidai, euripides--hippolytos,
            euripides--andromache, euripides--hekabe, euripides--hiketides,
            euripides--elektra, euripides--herakles, euripides--troades,
            euripides--iphigeneia-he-en-taurois, euripides--ion,
            euripides--helene, euripides--phoinissai, euripides--orestes,
            tucidides--historiai,
            aristofanes--nephelai,
            euripides--bakchai, sofocles--oidipous-epi-kolonoi,
            platao--apologia-sokratous, platao--kriton, platao--phaidon,
            platao--symposion, platao--politeia,
            xenofonte--hellenika,
            aristoteles--poietike, aristoteles--ethika-nikomacheia,
            aristoteles--politika, aristoteles--athenaion-politeia,
            aristoteles--ta-meta-ta-physika,
            martin-blackwell--alexander-the-great,
            epicuro--epistole-pros-menoikea,
            virgilio--aeneis, ovidio--metamorphoses,
            cicero--de-officiis, seneca--epistulae-morales-ad-lucilium,
            epicteto--encheiridion, marco-aurelio--ta-eis-heauton,
            plutarco--solon, plutarco--themistokles, plutarco--perikles,
            plutarco--alkibiades, plutarco--demosthenes, plutarco--alexandros,
            plutarco--kaisar,
            apuleio--metamorphoses-asinus-aureus,
            vegecio--epitoma-rei-militaris,
            mikalson--ancient-greek-religion, burkert--griechische-religion,
            vernant--les-origines-de-la-pensee-grecque,
            vernant--mythe-et-religion-en-grece-ancienne,
            veyne--les-grecs-ont-ils-cru-a-leurs-mythes,
            jaeger-werner--paideia,
            hansen--the-athenian-democracy-in-the-age-of-demosthenes,
            beard--spqr, woolf--rome-an-empires-story,
            grimal--dictionnaire-de-la-mythologie-grecque-et-romaine,
            finley--the-legacy-of-greece, highet--the-classical-tradition,
            campbell--the-hero-with-a-thousand-faces]

# ===========================================================================
# TENSÕES — desacordos reais entre membros, preservados e não sintetizados
# ===========================================================================
tensions:
  - {a: veyne--les-grecs-ont-ils-cru-a-leurs-mythes,
     b: burkert--griechische-religion,
     about: "Se a religião grega pode ser descrita como um sistema de crenças e
             ritos reconstituível historicamente, ou se a própria categoria de
             'acreditar' é uma projeção moderna sobre um mundo que organizava a
             verdade de outro modo."}
  - {a: vernant--mythe-et-religion-en-grece-ancienne,
     b: burkert--griechische-religion,
     about: "Se o que explica a religião grega é a estrutura social e mental que
             o mito articula, ou a continuidade histórica e ritual do culto —
             estruturalismo contra história das religiões."}
  - {a: campbell--the-hero-with-a-thousand-faces,
     b: vernant--les-origines-de-la-pensee-grecque,
     about: "Se os mitos gregos são instâncias de um padrão narrativo universal,
             ou produtos de uma configuração social e histórica específica que
             se dissolve quando universalizada."}
  - {a: aristofanes--nephelai,
     b: platao--apologia-sokratous,
     about: "Quem era Sócrates: um sofista que ensinava a fazer o argumento mais
             fraco parecer o mais forte, ou o seu oposto exato. As duas fontes
             são contemporâneas e incompatíveis, e a Apologia responde
             nominalmente à comédia."}

# ===========================================================================
# ORDEM ORIGINAL E DESVIOS
#
# `original_order` é a sua lista verbatim, com as 57 entradas como você as
# escreveu — incluindo as três entradas de volume, que aqui NÃO estão
# expandidas. É esse o ponto do campo: ele preserva o que você enviou, não o
# que a biblioteca fez com isso.
# ===========================================================================
original_order: [guarinello--historia-antiga, osborne--greece-in-the-making,
  finley--the-ancient-greeks, everitt--the-rise-of-athens,
  jaeger-werner--paideia,
  hesiodo--theogonia, hesiodo--erga-kai-hemerai, homero--ilias,
  homero--odysseia, pindaro--olympionikai,
  grimal--dictionnaire-de-la-mythologie-grecque-et-romaine,
  mikalson--ancient-greek-religion, burkert--griechische-religion,
  vernant--mythe-et-religion-en-grece-ancienne,
  veyne--les-grecs-ont-ils-cru-a-leurs-mythes,
  esquilo--oresteia,
  "VOLUME: Sófocles — A Trilogia Tebana",
  euripides--medeia, euripides--bakchai,
  "VOLUME: Eurípides — Teatro Completo II",
  "VOLUME: Eurípides — Teatro Completo III",
  "VOLUME: Eurípides — Teatro Completo IV",
  "VOLUME: Eurípides — Teatro Completo V",
  aristofanes--nephelai,
  vernant--les-origines-de-la-pensee-grecque,
  kirk-raven-schofield--the-presocratic-philosophers,
  mckirahan--philosophy-before-socrates,
  platao--apologia-sokratous, platao--kriton, platao--phaidon,
  platao--politeia, platao--symposion,
  aristoteles--poietike, aristoteles--ethika-nikomacheia,
  aristoteles--politika, aristoteles--ta-meta-ta-physika,
  herodoto--historiai, tucidides--historiai, xenofonte--hellenika,
  aristoteles--athenaion-politeia,
  hansen--the-athenian-democracy-in-the-age-of-demosthenes,
  "VOLUME: Plutarco — Vidas Paralelas (seleção)",
  finley--the-legacy-of-greece, highet--the-classical-tradition,
  martin-blackwell--alexander-the-great, epicuro--epistole-pros-menoikea,
  epicteto--encheiridion,
  beard--spqr, woolf--rome-an-empires-story, virgilio--aeneis,
  ovidio--metamorphoses, apuleio--metamorphoses-asinus-aureus,
  vegecio--epitoma-rei-militaris,
  cicero--de-officiis, seneca--epistulae-morales-ad-lucilium,
  marco-aurelio--ta-eis-heauton,
  campbell--the-hero-with-a-thousand-faces]

order_changes:
  - work: finley--the-legacy-of-greece
    from: "fim da seção VII (História, política e mundo grego clássico)"
    to: "início da seção XI (Legado e interpretação moderna)"
    reason: "É uma obra de recepção, e a seção XI existe declaradamente para
             isso. Na sua ordem, a coleção tinha duas seções de legado
             separadas por quatro seções de fontes antigas, e a seção VII
             terminava com dois livros sobre o Ocidente moderno."
    by: claude
    approved_by: voce
    approved_on: 2026-09-12

  - work: highet--the-classical-tradition
    from: "fim da seção VII"
    to: "seção XI, depois de Finley"
    reason: "Mesma razão. A seção XI passa a ler-se Finley (o que a Grécia
             legou) → Highet (como a literatura ocidental o recebeu) →
             Campbell (uma teoria universalizante a avaliar criticamente)."
    by: claude
    approved_by: voce
    approved_on: 2026-09-12

  - work: epicteto--encheiridion
    from: "seção VIII (Alexandre e o mundo helenístico), depois de Epicuro"
    to: "seção X (Filosofia moral romana), entre Sêneca e Marco Aurélio"
    reason: "Epicteto é do Império Romano (séc. I–II d.C.), POSTERIOR a Sêneca,
             e Marco Aurélio o leu. Na sua ordem, a seção X apresentava o
             estoicismo romano com um vazio exatamente entre o autor que
             antecede Epicteto e o autor que o cita. Custo declarado: o par
             Epicuro–Epicteto da seção VIII deixa de ser adjacência e passa a
             ser relação."
    by: claude
    approved_by: voce
    approved_on: 2026-09-12

structural_changes:
  - kind: expand
    from: "Item 17 — Sófocles, A Trilogia Tebana"
    into: [sofocles--oidipous-tyrannos, sofocles--oidipous-epi-kolonoi,
           sofocles--antigone]
    reason: "Não é uma trilogia autoral: são três peças independentes,
             compostas com cerca de 35 anos de intervalo e em ordem inversa à
             narrativa. 'A Trilogia Tebana' é o nome de uma publicação (Zahar,
             trad. Mário da Gama Kury), não de uma obra."
    by: claude
    approved_by: voce
    approved_on: 2026-09-12
    reversible: true
    library_effect: "Três registros de obra, não um."
    membership_effect: "A coleção ganha 2 membros em relação à sua lista."

  - kind: expand
    from: "Itens 20 a 23 — Eurípides, Teatro Completo II, III, IV e V"
    into: [euripides--herakleidai, euripides--hippolytos,
           euripides--andromache, euripides--hekabe, euripides--hiketides,
           euripides--elektra, euripides--herakles, euripides--troades,
           euripides--iphigeneia-he-en-taurois, euripides--ion,
           euripides--helene, euripides--phoinissai, euripides--orestes]
    reason: "São publicações da Editora 34 (trad. Jaa Torrano) que contêm 13
             tragédias. Mantidas como quatro entradas, treze tragédias teriam
             uma única posição de leitura e nenhuma relação individual com o
             resto da coleção."
    by: claude
    approved_by: voce
    approved_on: 2026-09-12
    reversible: true
    library_effect: "Treze registros de obra, não quatro."
    membership_effect: "A coleção ganha 9 membros em relação à sua lista."

  - kind: expand
    from: "Item 42 — Plutarco, Vidas Paralelas (seleção grega)"
    into: [plutarco--solon, plutarco--themistokles, plutarco--perikles,
           plutarco--alkibiades, plutarco--demosthenes, plutarco--alexandros,
           plutarco--kaisar]
    reason: "Sete biografias, portanto sete obras — e a sua própria nota já
             dava uma linha de justificativa por Vida, o que é um argumento por
             obra e não por volume. O rótulo 'seleção grega' foi corrigido: a
             Vida de César é romana e permanece na seleção por decisão sua,
             como par de Alexandre."
    by: claude
    approved_by: voce
    approved_on: 2026-09-12
    reversible: true
    library_effect: "Sete registros de obra, não um."
    membership_effect: "A coleção ganha 6 membros em relação à sua lista."

  - kind: renumber
    from: "Numeração da sua lista: 57 entradas numeradas até 52, com os números
           40 a 44 repetidos entre as seções VII, VIII e IX"
    into: []
    reason: "Erro de transcrição, não decisão intelectual. Nenhuma obra foi
             perdida nem duplicada."
    by: claude
    reversible: true
    library_effect: "Nenhum."
    membership_effect: "Nenhum."

updated: 2026-10-05
---

## Por que esta ordem

A ordem segue um caminho em treze etapas:

> contexto histórico → formação da Grécia → poesia e mito → religião grega →
> tragédia → nascimento da filosofia → Sócrates, Platão e Aristóteles →
> historiografia e política → Alexandre e Helenismo → Roma → literatura e
> religiões romanas → estoicismo romano → legado clássico e interpretações
> modernas

**A ordem não é cronológica: mostra como uma coisa nasce da outra.** O mito
vira religião praticada, a religião vira drama, o drama vira pergunta
filosófica, a pergunta vira sistema, o sistema é herdado por Roma e Roma é
herdada pelo Ocidente. Por isso a historiografia chega tarde: ela não move a
sequência, documenta o mundo em que ela acontece.

**O custo:** *As Nuvens* e a *Apologia* vêm antes da Guerra do Peloponeso que
as explica, e *Paideia* vem antes das obras que comenta. Reordenar desfaria o
argumento. Se preferir ler na ordem dos acontecimentos, use o **caminho
cronológico** no seletor do topo da coleção.

## Avaliação curatorial

Ver `review/greco-roman.md`. Três registros de lacuna foram abertos, todos como
detecção pura e sem candidatos. Uma proposta estrutural está em aberto, em
`review/structural/greco-roman.yaml`: a divisão Grécia/Roma, com gatilho
declarado.
