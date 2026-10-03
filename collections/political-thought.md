---
id: political-thought
image:                      # foto de fundo do cartão — interface-rules.md §5
  file: "images/collections/political-thought.webp"
  subject: "Frontispício do Leviatã de Thomas Hobbes (1651), gravura atribuída a Abraham Bosse"
  supplied_by: mathews
  added: 2026-09-25
title_pt: "Política — Formação Geral"
question: "Com que direito alguns homens governam outros, e sob que
           condições esse governo permanece legítimo?"

source:
  origin: sua-lista
  original_title: "Política — Formação Geral"
  imported: 2026-09-05
  archived_at: sources/lists/politica-formacao-geral.md
sequence_kind: intellectual

# ---------------------------------------------------------------------------
# PROVENIÊNCIA DOS CAMPOS
#   why_here      → literalmente suas palavras ("Por quê"), não parafraseadas
#   movement      → seus títulos de seção I–X, literais
#   sequence      → sua ordem, sem nenhuma alteração (ver order_changes: [])
#   editions_pref → literalmente sua indicação de edição, ainda NÃO verificada
#   role, demand  → inferidos por Claude nesta importação; aguardam confirmação
#   purpose, inclusion_criteria, excluded → rascunhos de Claude; aguardam sua decisão
# ---------------------------------------------------------------------------
provisional:
  inferred_by_claude: [role, demand, movement.purpose, inclusion_criteria,
                       tensions, structural_changes]
  pending_confirmation: true
  see: review/political-thought.md

# NOTA DE MODELO (2026-09-05): obras são unidades intelectuais, não livros.
# A forma bibliográfica (book | essay | lecture | dialogue | treatise | novel)
# vive no registro da obra, em works/. Publicações físicas são objetos
# próprios, em publications/, e uma publicação pode conter várias obras.
# Por isso este arquivo guarda publication_pref / edition_pref, e nunca uma
# edição embutida.

inclusion_criteria:            # RASCUNHO — inferido das suas 40 escolhas
  by: claude
  status: proposta
  criteria:
    - "Obras que argumentam sobre a origem, a legitimidade e os limites do
       poder político — não que apenas o descrevem ou administram."
    - "Fontes primárias e primeiras exposições de uma posição têm precedência
       sobre comentadores; comentador entra só quando muda a leitura da fonte."
    - "Tradições concorrentes devem estar presentes pelos seus próprios textos,
       e não apenas pelas críticas que receberam."
    - "Literatura entra quando trata um problema político que a teoria não
       alcança pela mesma via."
    - "Tradições não ocidentais entram por obras fundadoras próprias, não por
       apresentações comparativas."

excluded: []                   # nada registrado ainda — ver review/

# ===========================================================================
# SEQUÊNCIA — a ordem neste arquivo É a ordem. Nenhuma posição numérica.
# ===========================================================================
sequence:

  - movement: "I. Antiguidade: fundamentos da política"
    purpose: "Fixar as duas perguntas originais — o que é a justiça na cidade,
              e qual regime a realiza — e vê-las já sob pressão da prática."
    purpose_by: claude

  - work: platao--politeia
    core: true                                  # ★ seu
    role: foundational
    demand: exigente
    why_here: "Ponto de partida para justiça, cidade, educação, autoridade e
               formas de governo."
    why_here_by: voce
    edition_pref:
      text: "Fundação Calouste Gulbenkian, trad. Maria Helena da Rocha Pereira."
      by: voce
      verified: false
    publication_pref: pub--edufpa--a-republica   # decisão sua, 2026-09-27 (d-ed-republica): esta edição SUBSTITUI a indicação acima, que fica como registro

  - work: aristoteles--politika
    core: true
    role: foundational
    demand: exigente
    why_here: "Análise sistemática de cidadania, constituições, democracia,
               oligarquia, revolução e estabilidade política."
    why_here_by: voce
    edition_pref: {text: "Editora UnB, trad. Mário da Gama Kury.", by: voce, verified: false}
    publication_pref: pub--unb--politica   # escolha sua, 2026-09-27 (d-ed-politica): confirma a edição que já estava registrada

  - work: tucidides--historiai
    role: primary-source
    demand: exigente
    why_here: "Política como prática: guerra, imperialismo, liderança,
               interesse, propaganda e conflito."
    why_here_by: voce
    edition_pref: {text: "Madamu, trad. Mário da Gama Kury.", by: voce, verified: false}

  - work: cicero--de-re-publica
    role: foundational
    demand: moderado
    why_here: "Introduz republicanismo romano, lei, dever cívico e governo misto."
    why_here_by: voce
    edition_pref: {text: "Edipro, trad. Amador Cisneiros.", by: voce, verified: false}
    publication_pref: pub--edipro--da-republica--2021   # escolha sua (2026-09-23)

  # PARTICIPAÇÕES NOVAS — decisão sua de 2026-09-28. As duas já estavam na
  # biblioteca, vindas de Greco-Romana; aqui ganham papel e argumento próprios,
  # sem compra. Ficam no movimento I, e não junto de Aquino e de Hobbes, porque
  # os movimentos desta coleção são de período e um cabeçalho não pode passar a
  # afirmar algo falso sobre um membro. A ligação com o argumento que elas
  # encenam é feita pela relação registrada no arquivo da obra.
  - work: sofocles--antigone
    role: literary-treatment
    demand: leve
    why_here: "A lei da cidade contra a lei não escrita, encenada: é o caso que
               a tradição do direito natural cita há dois mil anos, e que
               Aquino e Hobbes discutem cada um à sua maneira."
    why_here_by: claude
    placement_status: a-confirmar
    inserted_by: claude
    publication_pref: pub--zahar--a-trilogia-tebana

  - work: esquilo--oresteia
    role: literary-treatment
    demand: exigente
    why_here: "Termina com a fundação de um tribunal: é o relato literário da
               passagem da vingança privada a uma instituição que julga — o
               problema que Hobbes formula como argumento."
    why_here_by: claude
    placement_status: a-confirmar
    inserted_by: claude
    publication_pref: pub--iluminuras--oresteia-i

  - movement: "II. Tradições políticas não ocidentais"
    purpose: "Mostrar que as perguntas da seção I foram feitas e respondidas
              fora da linhagem greco-europeia, com fundamentos distintos."
    purpose_by: claude

  - work: confucio--lunyu
    role: foundational
    demand: moderado
    why_here: "Apresenta uma concepção de ordem política fundada em virtude,
               educação, ritual e exemplaridade do governante."
    why_here_by: voce
    edition_pref:
      text: "Priorizar edição acadêmica traduzida diretamente do chinês,
             especialmente a de Giorgio Sinedino."
      by: voce
      kind: intencao          # nomeia tradutor, não edição
      verified: false

  - work: sunzi--bingfa
    role: primary-source
    demand: leve
    why_here: "Estratégia, conflito, informação, comando e relação de forças."
    why_here_by: voce
    edition_pref:
      text: "Martins Fontes, edição de Ralph D. Sawyer, trad. Ana Aguiar Cotrim."
      by: voce
      verified: false

  - work: kautilya--arthashastra
    role: primary-source
    demand: exigente
    why_here: "Estado, administração, tributação, espionagem, diplomacia e
               guerra em uma tradição independente da ocidental."
    why_here_by: voce
    edition_pref:
      text: "Tradução acadêmica integral diretamente do sânscrito, caso
             encontrada em português."
      by: voce
      kind: intencao
      verified: false

  - work: ibn-khaldun--muqaddimah
    role: foundational
    demand: exigente
    why_here: "Poder, coesão social, dinastias, Estado e ascensão e queda das
               sociedades."
    why_here_by: voce
    edition_pref:
      text: "Priorizar edição integral traduzida diretamente do árabe."
      by: voce
      kind: intencao
      verified: false

  - movement: "III. Cristianismo e política medieval"
    purpose: "Introduzir a fratura entre duas ordens — a cidade terrena e a
              lei divina — que a política moderna herdará e tentará resolver."
    purpose_by: claude

  - work: agostinho--de-civitate-dei
    role: foundational
    demand: exigente
    why_here: "Relação entre política, justiça, comunidade, império, história
               e cristianismo."
    why_here_by: voce
    edition_pref: {text: "Fundação Calouste Gulbenkian, trad. J. Dias Pereira.", by: voce, verified: false}
    publication_pref: pub--gulbenkian--a-cidade-de-deus-i   # vol. I de 3 (Gulbenkian); os três estão registrados

  - work: aquino--de-regno
    role: foundational
    demand: moderado
    why_here: "Lei natural, autoridade, bem comum e legitimidade do governo."
    why_here_by: voce
    edition_pref: {text: "Edipro, trad. Arlindo Veiga dos Santos.", by: voce, verified: false}
    publication_pref: pub--edipro--do-governo-dos-principes--2013   # escolha sua (2026-09-23)

  - movement: "IV. Formação da política moderna"
    purpose: "O eixo da coleção. A pergunta muda: deixa de ser qual o melhor
              regime e passa a ser de onde vem o poder e o que o obriga."
    purpose_by: claude

  - work: maquiavel--il-principe
    core: true
    role: pivot
    demand: moderado
    why_here: "Ruptura com a política como simples extensão da ética; poder,
               conquista, conservação e razão política."
    why_here_by: voce
    edition_pref: {text: "Penguin-Companhia das Letras, trad. Maurício Santana Dias.", by: voce, verified: false}
    publication_pref: pub--penguin-companhia--o-principe--2010   # escolha sua (2026-09-23)

  # PARTICIPAÇÕES NOVAS — decisão sua de 2026-09-28, com as duas caixas da
  # Nova Fronteira. As três ficam no movimento IV por período: são peças de
  # 1597 a 1608, entre Maquiavel (1513) e Hobbes (1651), e é ali que o
  # cabeçalho continua verdadeiro sobre elas. O argumento que cada uma encena
  # é ligado pela relação registrada no arquivo da obra.
  - work: shakespeare--richard-ii
    role: literary-treatment
    demand: moderado
    why_here: "A destruição da legitimidade, encenada: um rei legítimo depõe-se
               a si mesmo ao violar a regra de sucessão que o sustenta, e quem
               o substitui precisa inventar uma legitimidade nova. A cena da
               deposição foi censurada das primeiras impressões."
    why_here_by: claude
    placement_status: a-confirmar
    inserted_by: claude
    publication_pref: pub--nova-fronteira--grandes-obras-de-shakespeare--2017

  - work: shakespeare--julius-caesar
    role: literary-treatment
    demand: moderado
    why_here: "Tiranicídio preventivo — matar pelo que o governante poderia vir
               a ser — e a retórica como instrumento de poder, no discurso que
               fabrica um consenso sem precisar de uma mentira."
    why_here_by: claude
    placement_status: a-confirmar
    inserted_by: claude
    publication_pref: pub--nova-fronteira--grandes-obras-de-shakespeare--2017

  - work: shakespeare--coriolanus
    role: literary-treatment
    demand: exigente
    why_here: "Representação popular vista por quem a recusa: os plebeus
               conquistam tribunos e o herói militar considera intolerável que
               essa voz exista. É o problema de Mill e de Michels, encenado do
               lado de dentro do conflito."
    why_here_by: claude
    placement_status: a-confirmar
    inserted_by: claude
    publication_pref: pub--nova-fronteira--grandes-obras-de-shakespeare-2--2022

  - work: hobbes--leviathan
    core: true
    role: foundational
    demand: exigente
    why_here: "Estado de natureza, contrato, soberania, autoridade e
               necessidade de ordem política."
    why_here_by: voce
    edition_pref:
      text: "Martins Fontes, trad. João Paulo Monteiro e Maria Beatriz Nizza da Silva."
      by: voce
      verified: false
    publication_pref: pub--martins-fontes--leviata--2019   # escolha sua (2026-09-23)

  - work: locke--second-treatise
    core: true
    role: critical-response
    demand: moderado
    why_here: "Direitos naturais, propriedade, consentimento, governo limitado
               e resistência."
    why_here_by: voce
    edition_pref:
      text: "Martins Fontes, em Dois Tratados sobre o Governo, trad. Julio Fischer."
      by: voce
      verified: false
    publication_pref: pub--martins-fontes--dois-tratados-sobre-o-governo--2020   # escolha sua (2026-09-23)

  - work: montesquieu--de-lesprit-des-lois
    core: true
    role: foundational
    demand: exigente
    why_here: "Separação de poderes, instituições, leis, costumes e formas de
               governo."
    why_here_by: voce
    edition_pref:
      text: "Priorizar edição acadêmica brasileira da Martins Fontes."
      by: voce
      kind: intencao
      verified: false

  - work: rousseau--du-contrat-social
    core: true
    role: critical-response
    demand: moderado
    why_here: "Soberania popular, vontade geral, liberdade política e igualdade."
    why_here_by: voce
    edition_pref:
      text: "Edição física disponível em português; preferencialmente
             Penguin-Companhia das Letras, trad. Eduardo Brandão, quando disponível."
      by: voce
      kind: intencao
      verified: false
    publication_pref: pub--martin-claret--do-contrato-social--2013   # decisão sua, 2026-09-23: esta edição SUBSTITUI a indicação acima, que fica como registro

  - work: kant--grundlegung-zur-metaphysik-der-sitten
    role: foundational
    demand: exigente
    why_here: "A formulação moral que falta entre Rousseau e Burke, e de que
               Rawls depende declaradamente: autonomia da vontade, imperativo
               categórico, e a humanidade como fim em si. A coleção discutia a
               legitimidade do poder sem ter o termo moral que os dois lados
               disputam."
    why_here_by: claude
    closes_gap: political-thought--g05
    inserted_by: claude          # ver order_changes

  - movement: "V. Revolução, conservadorismo e democracia"
    purpose: "Submeter as construções da seção IV ao teste de um evento real —
              a Revolução — e ao teste de uma sociedade real: a América."
    purpose_by: claude

  - work: burke--reflections-france
    core: true
    role: critical-response
    demand: moderado
    why_here: "Tradição, prudência política, instituições e crítica ao
               racionalismo revolucionário."
    why_here_by: voce
    edition_pref: {text: "Fundação Calouste Gulbenkian, trad. Ivone Moreira.", by: voce, verified: false}

  - work: tocqueville--de-la-democratie-en-amerique
    core: true
    role: foundational
    demand: exigente
    why_here: "Democracia como regime e como sociedade: igualdade, costumes,
               associações, centralização e liberdade."
    why_here_by: voce
    edition_pref: {text: "Martins Fontes, trad. Eduardo Brandão.", by: voce, verified: false}
    publication_pref: pub--martins-fontes--a-democracia-na-america-livro-i--2019   # escolha sua (2026-09-23)

  - work: mill--on-liberty
    core: true
    role: foundational
    demand: leve
    why_here: "Liberdade individual, opinião, dissenso e limites da coerção
               social e estatal."
    why_here_by: voce
    edition_pref:
      text: "Priorizar edição acadêmica física em português."
      by: voce
      kind: intencao
      verified: false

  - work: mill--representative-government
    role: comparative
    demand: moderado
    why_here: "Representação, participação, competência política e
               funcionamento institucional da democracia."
    why_here_by: voce
    edition_pref: {text: "Edição acadêmica brasileira.", by: voce, kind: intencao, verified: false}

  - movement: "VI. Socialismo, marxismo e revolução"
    purpose: "Introduzir a tradição que fará a crítica mais radical de tudo
              o que veio das seções IV e V."
    purpose_by: claude

  - work: marx-engels--die-deutsche-ideologie
    role: foundational
    demand: exigente
    why_here: "A exposição da concepção materialista da história, que o
               Manifesto pressupõe e não expõe, e que Popper, 'A Sociedade
               Aberta e Seus Inimigos', e Aron, 'O Ópio dos Intelectuais',
               atacam nominalmente. Até aqui a coleção tinha os acusadores
               sem o texto acusado."
    why_here_by: claude
    closes_gap: political-thought--g03
    inserted_by: claude          # ver order_changes

  - work: marx-engels--manifest-kommunistischen-partei
    core: true
    role: foundational
    demand: leve
    why_here: "Crítica do capitalismo, classes sociais, burguesia, proletariado
               e revolução."
    why_here_by: voce
    edition_pref:
      text: "Penguin-Companhia das Letras, trad. Sérgio Tellaroli, revisão
             técnica de Ricardo Musse."
      by: voce
      verified: false
    publication_pref: pub--penguin-companhia--manifesto-comunista--2012   # escolha sua (2026-09-23)

  - work: marx--achtzehnte-brumaire
    core: true
    role: primary-source
    demand: moderado
    why_here: "Análise concreta de Estado, classes, representação, revolução
               e poder político."
    why_here_by: voce
    edition_pref: {text: "Boitempo, trad. Nélio Schneider.", by: voce, verified: false}
    publication_pref: pub--boitempo--o-18-de-brumario--2011   # escolha sua (2026-09-23)

  - work: dostoievski--besy
    core: true
    role: literary-treatment
    demand: exigente
    why_here: "Niilismo, radicalização, revolução, conspiração, violência
               política e ideologia."
    why_here_by: voce
    edition_pref: {text: "Editora 34, trad. Paulo Bezerra.", by: voce, verified: false}
    moved_by: claude             # vinha do movimento X — ver order_changes

  - work: lukacs--geschichte-und-klassenbewusstsein
    role: pivot
    demand: exigente
    why_here: "O elo que faltava entre Marx e a crítica da cultura: a
               reificação, formulada em 1923, é o que permite analisar a
               consciência e a cultura em termos materialistas sem falar de
               economia. É por aqui que a tradição se desloca para o terreno
               em que Frankfurt vai operar."
    why_here_by: claude
    requires: [marx-engels--die-deutsche-ideologie]
    inserted_by: claude          # ver order_changes

  - work: marcuse--one-dimensional-man
    role: critical-response
    demand: exigente
    why_here: "A voz da esquerda do século XX que a coleção só tinha pelo que
               os seus críticos diziam dela. Sustenta que a sociedade
               industrial avançada absorve a contestação e produz as
               necessidades que depois satisfaz — a tese que Popper e Aron
               nunca atacaram porque ela é posterior a eles."
    why_here_by: claude
    closes_gap: political-thought--g04
    inserted_by: claude          # ver order_changes

  - movement: "VII. Poder, partidos, massas e ideologia"
    purpose: "O século XX olhando para trás: o que a política moderna produziu
              quando aplicada, e o que na sua estrutura permitiu isso."
    purpose_by: claude

  # A sua entrada nomeava o volume; o volume são duas conferências distintas.
  # Divididas em duas obras (ver structural_changes). Desta coleção participa
  # apenas a conferência política — decisão sua, 2026-09-05. A conferência
  # sobre a ciência continua existindo na biblioteca, aguardando Educação /
  # Cultura, e as duas continuam a partilhar a mesma publicação física.
  - work: weber--politik-als-beruf
    core: true
    role: foundational
    demand: moderado
    why_here: "Poder, dominação, vocação política, ética da convicção e ética
               da responsabilidade."
    why_here_by: voce          # sua frase, escrita para o volume; cabe aqui
    publication_pref: pub--cultrix--ciencia-e-politica

  - work: michels--zur-soziologie-des-parteiwesens
    role: comparative
    demand: exigente
    why_here: "Partidos, organização e tendência à concentração oligárquica
               do poder."
    why_here_by: voce
    edition_pref:
      text: "Edição brasileira integral, preferencialmente acadêmica."
      by: voce
      kind: intencao
      verified: false

  - work: schmitt--der-begriff-des-politischen
    core: true
    role: critical-response
    demand: exigente
    why_here: "Conflito, amigo/inimigo, decisão e crítica ao liberalismo
               parlamentar."
    why_here_by: voce
    edition_pref:
      text: "Edição brasileira acadêmica, preferencialmente trad. Alexandre
             Franco de Sá."
      by: voce
      kind: intencao
      verified: false

  - work: zamiatin--my
    role: literary-treatment
    demand: moderado
    why_here: "Uma das origens da distopia política moderna e da reflexão
               ficcional sobre coletivização e controle."
    why_here_by: voce
    edition_pref:
      text: "Edição brasileira integral, preferencialmente traduzida
             diretamente do russo."
      by: voce
      kind: intencao
      verified: false
    moved_by: claude             # vinha do movimento X — ver order_changes

  - work: huxley--brave-new-world
    core: true
    role: literary-treatment
    demand: leve
    why_here: "Condicionamento, consumo, prazer, conformismo e engenharia
               social."
    why_here_by: voce
    edition_pref:
      text: "Edição brasileira física de referência, preferencialmente com
             boa tradução integral."
      by: voce
      kind: intencao
      verified: false
    moved_by: claude             # vinha do movimento X — ver order_changes

  - work: arendt--origins-of-totalitarianism
    core: true
    role: foundational
    demand: exigente
    why_here: "Antissemitismo, imperialismo, massas, ideologia e totalitarismo."
    why_here_by: voce
    edition_pref: {text: "Companhia das Letras, trad. Roberto Raposo.", by: voce, verified: false}

  - work: koestler--darkness-at-noon
    role: literary-treatment
    demand: moderado
    why_here: "Partido, confissão, disciplina ideológica e totalitarismo
               vistos a partir do interior do revolucionário."
    why_here_by: voce
    edition_pref:
      text: "Edição brasileira integral em tradução de qualidade."
      by: voce
      kind: intencao
      verified: false
    moved_by: claude             # vinha do movimento X — ver order_changes

  - work: popper--the-open-society
    core: true
    role: critical-response
    demand: exigente
    why_here: "Crítica ao historicismo e às concepções que pretendem descobrir
               e dirigir o curso necessário da história."
    why_here_by: voce
    edition_pref: {text: "Itatiaia, trad. Milton Amado.", by: voce, verified: false}

  - work: berlin--two-concepts-of-liberty
    core: true
    role: comparative
    demand: moderado
    why_here: "Liberdade negativa, liberdade positiva e pluralismo de valores."
    why_here_by: voce
    edition_pref:
      text: "Edição brasileira acadêmica de seus ensaios."
      by: voce
      kind: intencao
      verified: false
    # form: essay (no registro da obra). A publicação será provavelmente
    # "Quatro Ensaios sobre a Liberdade", que contém quatro obras.

  - work: aron--lopium-des-intellectuels
    core: true
    role: critical-response
    demand: moderado
    why_here: "Ideologia, mito revolucionário, intelectuais e crítica do
               fanatismo político."
    why_here_by: voce
    edition_pref: {text: "Três Estrelas, trad. Jorge Bastos.", by: voce, verified: false}
    publication_pref: pub--vide--o-opio-dos-intelectuais--2024   # decisão sua, 2026-09-23: esta edição SUBSTITUI a indicação acima, que fica como registro

  # ACRÉSCIMO PÓS-IMPORTAÇÃO — decisão sua de 2026-09-06, feita fora da lista
  # original de 40 (importada em 2026-09-05). `original_order`, abaixo, NÃO
  # foi tocado: continua a guardar exatamente a lista que você enviou naquela
  # data. Esta entrada existe só em `sequence`. Ver review/political-thought.md §6.
  - work: bezmenov--subversao-teoria-aplicacao-e-confissao-de-um-metodo
    role: primary-source
    demand: moderado
    why_here: "Guerra política, subversão ideológica, influência e
               transformação política das sociedades. Tem dimensão
               psicológica, mas você não considera esse o campo intelectual
               primário da obra."
    why_here_by: voce
    edition_pref:
      text: "ASIN/ISBN-10 6599245404 (Amazon). Editora e ano não
             identificados."
      by: claude
      verified: false

  - work: orwell--politics-and-the-english-language
    role: supplementary
    demand: leve
    why_here: "Relação entre linguagem, pensamento, eufemismo, propaganda
               e poder."
    why_here_by: voce
    edition_pref:
      text: "Preferencialmente em coletânea de ensaios de Orwell."
      by: voce
      kind: intencao
      verified: false
    # form: essay (no registro da obra). A publicação será uma coletânea
    # de ensaios de Orwell, contendo muitas obras.

  # PARTICIPAÇÃO NOVA — 2026-09-23; inclusão aprovada por você. POSIÇÃO a confirmar: logo depois do ensaio de Orwell — os dois
  # tratam da linguagem como instrumento de poder; Klemperer é o caso
  # documentado, dia a dia, sob o nazismo.
  - work: klemperer--lti-lingua-tertii-imperii
    role: supplementary
    demand: moderado
    why_here: "O que Orwell argumenta em ensaio, Klemperer registra como
               testemunha: como o regime nazista mudou o vocabulário comum e,
               com ele, o que as pessoas conseguiam pensar."
    why_here_by: claude
    placement_status: a-confirmar
    inserted_by: claude
    publication_pref: pub--contraponto--lti--2009

    moved_by: claude             # ver order_changes

  - work: orwell--animal-farm
    core: true
    role: literary-treatment
    demand: leve
    why_here: "Revolução, propaganda, corrupção dos ideais, revisionismo
               histórico e concentração de poder."
    why_here_by: voce
    edition_pref: {text: "Companhia das Letras, trad. Heitor Aquino Ferreira.", by: voce, verified: false}
    moved_by: claude             # vinha do movimento X — ver order_changes

  - work: orwell--nineteen-eighty-four
    core: true
    role: literary-treatment
    demand: moderado
    why_here: "Vigilância, propaganda, linguagem, memória e controle da
               realidade."
    why_here_by: voce
    edition_pref:
      text: "Companhia das Letras, trad. Heloisa Jahn e Alexandre Hubner."
      by: voce
      verified: false
    moved_by: claude             # vinha do movimento X — ver order_changes

  - movement: "VIII. Democracia e justiça contemporâneas"
    purpose: "Depois do diagnóstico do século XX, as duas tentativas de
              reconstrução: institucional (Dahl) e normativa (Rawls)."
    purpose_by: claude

  - work: habermas--strukturwandel-der-oeffentlichkeit
    role: critical-response
    demand: exigente
    why_here: "A terceira tentativa de reconstrução, ao lado da institucional
               de Dahl e da normativa de Rawls: reconstruir as condições de
               uma discussão pública argumentada, e mostrar como elas se
               degradam. Vem de dentro da própria tradição crítica e rompe
               com o pessimismo dela."
    why_here_by: claude
    requires: [marcuse--one-dimensional-man]
    inserted_by: claude          # ver order_changes

  - work: dahl--on-democracy
    core: true
    role: foundational
    demand: leve
    why_here: "Democracia como problema institucional: participação,
               competição, representação e pluralismo."
    why_here_by: voce
    edition_pref: {text: "Editora UnB, edição brasileira.", by: voce, verified: false}

  # PARTICIPAÇÃO NOVA — 2026-09-23; inclusão aprovada por você. POSIÇÃO a confirmar: logo depois de Dahl, que descreve como a
  # democracia funciona; este livro descreve como ela é desmontada por dentro.
  - work: levitsky-ziblatt--how-democracies-die
    role: supplementary
    demand: leve
    why_here: "O contraponto contemporâneo a Dahl: não o golpe, mas a erosão
               gradual das normas não escritas por governantes eleitos."
    why_here_by: claude
    placement_status: a-confirmar
    inserted_by: claude
    publication_pref: pub--zahar--como-as-democracias-morrem--2018

  - work: rawls--a-theory-of-justice
    core: true
    role: foundational
    demand: exigente
    why_here: "Justiça, liberdade, igualdade e desenho institucional do
               liberalismo contemporâneo."
    why_here_by: voce
    edition_pref:
      text: "Martins Fontes, trad. Jussara Simões, revisão técnica de
             Álvaro de Vita."
      by: voce
      verified: false

  - movement: "IX. Crítica libertária"
    purpose: "A recusa mais radical da premissa comum a quase toda a coleção:
              a de que o Estado é o quadro dentro do qual a pergunta se coloca."
    purpose_by: claude

  - work: rothbard--anatomy-of-the-state
    core: true
    role: critical-response
    demand: leve
    why_here: "Crítica concentrada da natureza e das funções coercitivas do
               Estado."
    why_here_by: voce
    edition_pref: {text: "Instituto Ludwig von Mises Brasil, trad. Tiago Chabert.", by: voce, verified: false}
    publication_pref: pub--vide--anatomia-do-estado--2019   # decisão sua, 2026-09-23: esta edição SUBSTITUI a indicação acima, que fica como registro

  - work: rothbard--the-ethics-of-liberty
    core: true
    role: foundational
    demand: exigente
    why_here: "Propriedade, direitos, coerção e fundamentação ética do
               libertarianismo."
    why_here_by: voce
    edition_pref: {text: "Instituto Ludwig von Mises Brasil.", by: voce, verified: false}
    publication_pref: pub--lvm--a-etica-da-liberdade--2010   # escolha sua (2026-09-23)

  - work: hoppe--democracy-the-god-that-failed
    core: true
    role: critical-response
    demand: moderado
    why_here: "Crítica libertária da democracia, do Estado e dos incentivos
               políticos."
    why_here_by: voce
    edition_pref:
      text: "Instituto Ludwig von Mises Brasil, trad. Marcelo Werlang de Assis."
      by: voce
      verified: false
    publication_pref: pub--lvm--democracia-o-deus-que-falhou--2014   # escolha sua (2026-09-23)

# ===========================================================================
# CAMINHOS ALTERNATIVOS
# ===========================================================================
paths:
  - id: nucleo-duro
    title_pt: "O esqueleto fundamental da coleção"
    by: voce                   # seu, integralmente — inclusive a ordem interna
    for: "Se os 40 títulos forem transformados em um currículo de núcleo duro."
    declares: "Espinha ocidental comprimida do pensamento político moderno.
               NÃO é uma afirmação de que as seções II e III sejam
               dispensáveis — a coleção completa inclui as tradições não
               ocidentais deliberadamente."
    declares_by: voce
    excludes_by_design: [movimento-II-nao-ocidentais, movimento-III-medieval]
    note: "A ordem interna deste caminho difere da sequência completa no bloco
           de literatura: aqui Huxley vem DEPOIS de 1984. Diferença sua,
           preservada como está."
    # ★ e pertencer a este caminho são conceitos separados e não se reconciliam.
    # Três obras estreladas ficam de fora; duas delas são sinalizadas abaixo
    # como distorção potencial. Sinalizar, não corrigir.
    flagged_omissions:
      - {work: burke--reflections-france,
         concern: "Sem Burke, a sequência Rousseau → Tocqueville perde a
                   objeção conservadora e a Revolução aparece sem contestação."}
      - {work: schmitt--der-begriff-des-politischen,
         concern: "Sem Schmitt, o caminho critica o liberalismo apenas a partir
                   do libertarianismo e do marxismo, e não a partir da recusa
                   da premissa parlamentar."}
      - {work: berlin--two-concepts-of-liberty,
         concern: "Baixa. Mill e Rawls cobrem boa parte do terreno."}
    accepted_omissions: []     # mova para cá o que decidir manter de fora
    future_paths_note: "Um caminho comparativo/não ocidental sobre os mesmos
                        membros é aditivo: não altera este caminho nem a
                        coleção."
    works:
      - platao--politeia
      - aristoteles--politika
      - maquiavel--il-principe
      - hobbes--leviathan
      - locke--second-treatise
      - montesquieu--de-lesprit-des-lois
      - rousseau--du-contrat-social
      - tocqueville--de-la-democratie-en-amerique
      - mill--on-liberty
      - marx-engels--manifest-kommunistischen-partei
      - marx--achtzehnte-brumaire
      - weber--politik-als-beruf
      - arendt--origins-of-totalitarianism
      - popper--the-open-society
      - aron--lopium-des-intellectuels
      - dahl--on-democracy
      - rawls--a-theory-of-justice
      - rothbard--anatomy-of-the-state
      - rothbard--the-ethics-of-liberty
      - hoppe--democracy-the-god-that-failed
      - dostoievski--besy
      - orwell--animal-farm
      - orwell--nineteen-eighty-four
      - huxley--brave-new-world

# ===========================================================================
# TENSÕES — renderizadas como oposição, nunca como sequência
# ===========================================================================
tensions:                      # RASCUNHO de Claude, a partir das suas escolhas
  by: claude
  status: proposta
  pairs:
    - {a: hobbes--leviathan, b: locke--second-treatise,
       about: "Se o poder soberano pode ser legitimamente resistido."}
    - {a: locke--second-treatise, b: rousseau--du-contrat-social,
       about: "Se a liberdade se preserva limitando o soberano ou constituindo-o."}
    - {a: rousseau--du-contrat-social, b: burke--reflections-france,
       about: "Se a ordem política pode ser refundada pela razão."}
    - {a: marx--achtzehnte-brumaire, b: tocqueville--de-la-democratie-en-amerique,
       about: "Se a igualdade democrática liberta ou dissolve."}
    - {a: marx-engels--manifest-kommunistischen-partei, b: popper--the-open-society,
       about: "Se a história tem um curso que se possa conhecer e dirigir."}
    - {a: rawls--a-theory-of-justice, b: rothbard--the-ethics-of-liberty,
       about: "Se a redistribuição é exigência da justiça ou violação de direito."}
    - {a: arendt--origins-of-totalitarianism, b: schmitt--der-begriff-des-politischen,
       about: "Se o político se define pela ação em comum ou pela distinção
               amigo/inimigo."}
    - {a: orwell--nineteen-eighty-four, b: huxley--brave-new-world,
       about: "Se o controle se impõe pela dor ou pelo prazer."}

# ===========================================================================
# ORDEM ORIGINAL E DESVIOS
# ===========================================================================
original_order: [platao--politeia, aristoteles--politika, tucidides--historiai,
  cicero--de-re-publica, confucio--lunyu, sunzi--bingfa, kautilya--arthashastra,
  ibn-khaldun--muqaddimah, agostinho--de-civitate-dei, aquino--de-regno,
  maquiavel--il-principe, hobbes--leviathan, locke--second-treatise,
  montesquieu--de-lesprit-des-lois, rousseau--du-contrat-social,
  burke--reflections-france, tocqueville--de-la-democratie-en-amerique,
  mill--on-liberty, mill--representative-government,
  marx-engels--manifest-kommunistischen-partei, marx--achtzehnte-brumaire,
  weber--politik-als-beruf, michels--zur-soziologie-des-parteiwesens,
  schmitt--der-begriff-des-politischen, arendt--origins-of-totalitarianism,
  popper--the-open-society, berlin--two-concepts-of-liberty,
  aron--lopium-des-intellectuels, dahl--on-democracy, rawls--a-theory-of-justice,
  rothbard--anatomy-of-the-state, rothbard--the-ethics-of-liberty,
  hoppe--democracy-the-god-that-failed, dostoievski--besy, zamiatin--my,
  huxley--brave-new-world, koestler--darkness-at-noon, orwell--animal-farm,
  orwell--nineteen-eighty-four, orwell--politics-and-the-english-language]

# ---------------------------------------------------------------------------
# ORDER_CHANGES — deixou de estar vazio em 2026-09-19, com a sua aprovação.
# É a primeira vez em todo o acervo que a ordem de uma coleção é alterada.
# As três entradas abaixo são reversíveis: cada uma diz de onde a obra veio.
#
# Nenhuma das 40 obras da sua lista original mudou de posição relativa entre
# si, exceto a última — o ensaio de Orwell, que estava no movimento errado.
# `original_order` continua a guardar a sua lista verbatim.
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# SINAL ESTRUTURAL REGISTRADO — 2026-09-28, por decisão sua (opção B).
# Com a dissolução do movimento X, o movimento VII passou de 10 para 15 obras,
# quase um terço da coleção. A dispersão prevista pela convenção quase não
# dispersou: cinco das seis obras foram para o mesmo lugar, porque cinco das
# seis tratam de ideologia do século XX. Isto NÃO foi resolvido agora — fica
# registrado como sinal a reavaliar, e a resposta, se houver, é subdivisão
# interna do VII (degrau 1 da escada), não um movimento de gênero de volta.
# ---------------------------------------------------------------------------

order_changes:

  # ---------------------------------------------------------------------
  # SHAKESPEARE ENTRA — decisão sua de 2026-09-28. Você optou pelas duas
  # caixas da Nova Fronteira, e as três peças entram como participações novas
  # no movimento IV. Reversível: remover as três entradas; os registros de
  # obra e as duas publicações continuam na biblioteca.
  # ---------------------------------------------------------------------
  - work: shakespeare--richard-ii
    kind: insert
    from: "fora da biblioteca — obra registrada em 2026-09-28"
    to: "movimento IV, depois de maquiavel--il-principe"
    approved_by: voce
    date: 2026-09-28
    reason: "Peça de 1597, entre Maquiavel e Hobbes também pela cronologia. A
             coleção não tinha nada, teórico nem literário, sobre o momento em
             que um rei legítimo é deposto."
    reversible_by: "Remover a entrada do movimento IV."

  - work: shakespeare--julius-caesar
    kind: insert
    from: "fora da biblioteca — obra registrada em 2026-09-28"
    to: "movimento IV, depois de shakespeare--richard-ii"
    approved_by: voce
    date: 2026-09-28
    reason: "Peça possivelmente de 1599. Traz o tiranicídio preventivo, que a
             coleção discutia só por Maquiavel e pelo lado da conservação do
             poder."
    reversible_by: "Remover a entrada do movimento IV."

  - work: shakespeare--coriolanus
    kind: insert
    from: "fora da biblioteca — obra registrada em 2026-09-28"
    to: "movimento IV, depois de shakespeare--julius-caesar"
    approved_by: voce
    date: 2026-09-28
    reason: "Única das três sobre representação popular, e a única vinda da
             segunda caixa. Data de composição não estabelecida; a posição
             segue a ordem editorial das outras duas e fica a confirmar."
    reversible_by: "Remover a entrada do movimento IV."

  # ---------------------------------------------------------------------
  # DISSOLUÇÃO DO MOVIMENTO X — decisão sua de 2026-09-28, opção B.
  # O cabeçalho "X. Literatura como crítica política" deixou de existir: pela
  # convenção de 27/09, literatura é colocada junto do argumento que ela
  # encena, e um movimento que agrupava literatura por gênero perdeu a razão
  # de ser. As seis obras foram pesquisadas em 28/09 antes de qualquer
  # colocação. Reversível: recriar o cabeçalho no fim da sequência e devolver
  # as seis, na ordem em que estão listadas aqui.
  # ---------------------------------------------------------------------
  - work: dostoievski--besy
    kind: move
    from: "movimento X (Literatura como crítica política), 1ª posição"
    to: "movimento VI, depois de marx--achtzehnte-brumaire"
    approved_by: voce
    date: 2026-09-28
    reason: "É a única das seis que muda de vizinhança de verdade. O romance
             trata da célula revolucionária por dentro, e o movimento VI é
             onde a tradição revolucionária é apresentada. A posição é também
             cronológica: 1872, entre o 18 de Brumário (1852) e Lukács (1923)."
    reversible_by: "Remover do movimento VI e devolver ao fim da sequência."

  - work: zamiatin--my
    kind: move
    from: "movimento X, 2ª posição"
    to: "movimento VII, depois de schmitt--der-begriff-des-politischen"
    approved_by: voce
    date: 2026-09-28
    reason: "Escrito por volta de 1920, contra o projeto soviético no momento
             em que ele começava — anterior a tudo o que a coleção tem sobre o
             assunto, e por isso abre a série de tratamentos ficcionais dentro
             do movimento VII."
    reversible_by: "Remover do movimento VII e devolver ao fim da sequência."

  - work: huxley--brave-new-world
    kind: move
    from: "movimento X, 3ª posição"
    to: "movimento VII, depois de zamiatin--my"
    approved_by: voce
    date: 2026-09-28
    reason: "Distopia do controle brando, e não do terror. Fica ao lado de Nós
             porque as duas antecipam por ficção o que o movimento VII depois
             analisa por teoria."
    reversible_by: "Remover do movimento VII e devolver ao fim da sequência."

  - work: koestler--darkness-at-noon
    kind: move
    from: "movimento X, 4ª posição"
    to: "movimento VII, imediatamente depois de arendt--origins-of-totalitarianism"
    approved_by: voce
    date: 2026-09-28
    reason: "Partido, confissão e disciplina ideológica vistos de dentro do
             revolucionário. É o que Arendt analisa de fora, encenado de
             dentro — daí a adjacência imediata."
    reversible_by: "Remover do movimento VII e devolver ao fim da sequência."

  - work: orwell--animal-farm
    kind: move
    from: "movimento X, 5ª posição"
    to: "movimento VII, depois de klemperer--lti-lingua-tertii-imperii"
    approved_by: voce
    date: 2026-09-28
    reason: "Revolução traída, propaganda e reescrita do passado. Fecha o
             movimento junto do ensaio de Orwell sobre linguagem e do registro
             de Klemperer."
    reversible_by: "Remover do movimento VII e devolver ao fim da sequência."

  - work: orwell--nineteen-eighty-four
    kind: move
    from: "movimento X, 6ª posição"
    to: "movimento VII, depois de orwell--animal-farm"
    approved_by: voce
    date: 2026-09-28
    reason: "Vigilância, linguagem e controle da memória. Fica ao lado do
             ensaio de Orwell e do diário de Klemperer: os três tratam do
             mesmo objeto por argumento, testemunho e ficção."
    reversible_by: "Remover do movimento VII e devolver ao fim da sequência."

  - work: sofocles--antigone
    kind: insert
    from: "fora da coleção — participava apenas de greco-roman"
    to: "movimento I, depois de cicero--de-re-publica"
    approved_by: voce
    date: 2026-09-28
    reason: "Participação nova, sem compra. Vai ao movimento I, e não junto de
             Aquino, porque os movimentos desta coleção são de período: uma
             tragédia do século V a.C. dentro de Cristianismo e política
             medieval faria o cabeçalho afirmar algo falso. A ligação com o
             argumento do direito natural é feita pela relação registrada."
    reversible_by: "Remover a entrada do movimento I; a obra continua em
                    Greco-Romana, intacta."

  - work: esquilo--oresteia
    kind: insert
    from: "fora da coleção — participava apenas de greco-roman"
    to: "movimento I, depois de sofocles--antigone"
    approved_by: voce
    date: 2026-09-28
    reason: "Mesma razão da Antígona. A relação registrada aponta para Hobbes,
             e não para Montesquieu como eu havia sugerido antes: o argumento
             da Oresteia é a substituição da vingança privada por uma
             instituição, que é o problema de Hobbes, e não a divisão de
             poderes."
    reversible_by: "Remover a entrada do movimento I; a obra continua em
                    Greco-Romana, intacta."
  - work: kant--grundlegung-zur-metaphysik-der-sitten
    kind: insert
    from: "fim da sequência, em movimento próprio (XI), criado por mim"
    to: "movimento IV, depois de rousseau--du-contrat-social"
    approved_by: voce
    date: 2026-09-19
    reason: "O movimento IV pergunta de onde vem o poder e o que o limita.
             Kant (1785) dá o fundamento moral do limite, e a posição é também
             cronológica: entre Rousseau (1762) e Burke (1790)."
    reversible_by: "Remover a entrada do movimento IV; a obra volta ao fim."

  - work: marcuse--one-dimensional-man
    kind: insert
    from: "fim da sequência, em movimento próprio (XII), criado por mim"
    to: "movimento VI, depois de marx--achtzehnte-brumaire"
    approved_by: voce
    date: 2026-09-19
    reason: "O movimento VI nomeia a tradição — socialismo, marxismo e
             revolução. Marcuse (1964) é a releitura dessa tradição depois de
             a previsão falhar, e é dentro dela que a assimetria apontada em
             political-thought--g04 se corrige."
    reversible_by: "Remover a entrada do movimento VI; a obra volta ao fim."

  - work: orwell--politics-and-the-english-language
    kind: move
    from: "movimento X, Literatura como crítica política"
    to: "movimento VII, Poder, partidos, massas e ideologia — no fim dele"
    approved_by: voce
    date: 2026-09-19
    reason: "A obra não é literatura: é um ensaio de 1946, publicado na
             revista Horizon, sobre a degradação da linguagem política. Já
             estava registrada com role `supplementary`, diferente das seis
             ficções do movimento X, todas `literary-treatment`. O movimento
             VII trata do que a política moderna produziu quando aplicada —
             propaganda, eufemismo e ideologia —, que é o assunto do ensaio."
    reversible_by: "Devolver a entrada ao fim do movimento X."
    note: "A sua ordem relativa das seis ficções do movimento X não mudou."

  - work: marx-engels--die-deutsche-ideologie
    kind: insert
    from: "não estava na biblioteca"
    to: "movimento VI, antes de marx-engels--manifest-kommunistischen-partei"
    approved_by: voce
    date: 2026-09-19
    reason: "Colocação já registrada como proposta em political-thought--g03
             desde 2026-09-05, com esta posição exata. A exposição vem antes
             do panfleto que a pressupõe."
    reversible_by: "Remover a entrada; a lacuna g03 volta a `open`."

  - work: lukacs--geschichte-und-klassenbewusstsein
    kind: insert
    from: "não estava na biblioteca"
    to: "movimento VI, depois de marx--achtzehnte-brumaire e antes de
         marcuse--one-dimensional-man"
    approved_by: voce
    date: 2026-09-19
    reason: "Ordem cronológica e lógica dentro do movimento: 1846, 1848, 1852,
             1923, 1964. Lukács é o intermediário entre Marx e Marcuse, e sem
             ele o salto de um para o outro é de quase oitenta anos."
    reversible_by: "Remover a entrada."

  - work: habermas--strukturwandel-der-oeffentlichkeit
    kind: insert
    from: "não estava na biblioteca"
    to: "movimento VIII, antes de dahl--on-democracy"
    approved_by: voce
    date: 2026-09-19
    reason: "O movimento VIII são as tentativas de reconstrução depois do
             diagnóstico do século XX. Habermas (1962) é anterior a Dahl e a
             Rawls e abre a série. NÃO foi posto no movimento VI, da tradição
             marxista, porque o que ele faz é responder a ela — e a SEP
             adverte que tratá-lo como membro da Escola de Frankfurt é
             enganoso."
    reversible_by: "Remover a entrada."

# Movimentos XI e XII, que eu havia criado para acomodar Kant e Marcuse,
# foram REMOVIDOS. A coleção volta a ter os seus dez movimentos.

# Importar também pode mudar a CARDINALIDADE, não só a ordem — e isso
# tampouco pode acontecer em silêncio. Registro separado:
structural_changes:
  - kind: split
    from: "Weber — Ciência e Política: Duas Vocações (uma entrada sua)"
    into: [weber--politik-als-beruf, weber--wissenschaft-als-beruf]
    reason: "Duas conferências intelectualmente distintas. A publicação
             continua sendo uma só e contém as duas."
    by: claude
    approved_by: voce
    approved: 2026-09-05
    reversible: true
    # CONTABILIDADE — a distinção importa e não é um detalhe:
    library_effect: "+1 obra na biblioteca (weber--wissenschaft-als-beruf)."
    membership_effect: "Nenhum. A coleção permanece com 40 membros: a entrada
                        original representava as duas conferências e o que ela
                        significava para ESTA coleção era a conferência
                        política, que continua sendo o membro."
    resolved_by: "Sua decisão de 2026-09-05: A Ciência como Vocação sai de
                  Pensamento Político; casa provável em Educação e/ou Cultura,
                  a decidir pelos critérios dessas coleções quando importadas."
    status: aplicado

updated: 2026-09-23
---

## Por que esta ordem

A coleção não avança pela cronologia: avança por uma pergunta que muda de
forma três vezes.

**Qual é o melhor regime? (I–III)** Platão e Aristóteles fixam a pergunta em
termos de justiça e constituição; Tucídides mostra o que a guerra faz com ela;
Cícero a traduz para o vocabulário jurídico que a Europa vai herdar. A seção II
interrompe de propósito: Confúcio, Kautilya e Ibn Khaldun fazem as mesmas
perguntas com outros fundamentos, e por estarem aqui, e não no fim, impedem que
o resto pareça a única história possível. A seção III traz a divisão entre
duas ordens e duas lealdades, de onde a modernidade vai nascer.

**De onde vem o poder, e o que o obriga? (IV–V)** Este é o eixo da coleção.
Com Maquiavel a política deixa de ser um ramo da ética; Hobbes leva isso até a
soberania absoluta; Locke aceita o contrato e recusa a conclusão; Montesquieu
passa da origem para a arquitetura do poder; Rousseau devolve a soberania ao
povo. Em V, tudo isso é testado: Burke diante da Revolução, Tocqueville diante
da América, e Mill perguntando o que resta do indivíduo.

**O que deu errado, e como reconstruir? (VI–X)** VI e VII são um par: Marx
faz a crítica mais radical do que veio antes, e VII mostra o que o século XX
viu na política moderna — poder, partidos, massas e ideologia (Weber, Michels,
Schmitt, Arendt, Popper, Berlin, Aron) — e termina no que a ideologia faz à
linguagem (Orwell, Klemperer). VIII volta à democracia: como ela funciona
(Dahl), como é desmontada por dentro (Levitsky e Ziblatt) e o que a tornaria
justa (Rawls). IX recusa a premissa comum a quase toda a coleção, a de que o
Estado é o quadro da pergunta; vindo depois de Rawls, funciona como objeção. X
não é ilustração: mostra, em romances, como a ideologia é vivida por dentro
(Dostoiévski, Zamiátin, Huxley, Koestler, Orwell).

## Lacunas e observações

Ver `review/political-thought.md`. Nada dali foi aplicado a este arquivo.
