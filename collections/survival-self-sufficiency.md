---
id: survival-self-sufficiency
image:                      # foto de fundo do cartão — interface-rules.md §5
  file: "images/collections/survival-self-sufficiency.webp"
  subject: "Cabanas do Lost Creek Ranch, Jackson Hole, Wyoming"
  supplied_by: mathews
  added: 2026-09-25
title_pt: "Sobrevivência/Autossuficiência"
title_by: voce
question: "Como um ser humano se sustenta, se cura, se abriga, se defende e se
           orienta quando os sistemas que normalmente fazem isso por ele não
           estão disponíveis?"
question_by: claude
question_status: proposta

source:
  origin: sua-lista
  imported: 2026-09-06
  archived_at: sources/lists/sobrevivencia-autossuficiencia.md
  note: "Você declarou explicitamente que a coleção NÃO está completa. Isso não
         é defeito nem pendência (§0.1)."
sequence_kind: thematic
# ^ PRIMEIRA coleção não-`intellectual` do acervo. As outras três organizam
#   ARGUMENTOS, e a ordem nelas carrega dependência intelectual. Esta organiza
#   DOMÍNIOS DE COMPETÊNCIA, e a ordem entre eles não é dependência: ninguém
#   precisa de ler sobre defesa antes de ler sobre medicina. O valor `thematic`
#   existe no vocabulário recuperado do blueprint e é o que descreve isto.

provisional:
  inferred_by_claude: [question, inclusion_criteria, demand,
                       movement.purpose, scope_map.reading]
  authored_by_you: [title_pt, sequence, scope_map.regions]
  pending_confirmation: true
  see: review/survival-self-sufficiency.md

# ---------------------------------------------------------------------------
# UMA COLEÇÃO DE MANUAIS, NÃO DE ARGUMENTOS — e isso tem consequências.
# `role` está AUSENTE em todas as participações. O vocabulário observado
# (foundational, critical-response, pivot, comparative, literary-treatment,
# supplementary) foi construído para obras que discutem uma com a outra. Um
# guia de campo não é `foundational` nem `critical-response` de coisa nenhuma.
# Inventar um slug — `reference`, `practical` — seria decisão de classificação
# tomada em silêncio, que o §6.8 manda levantar. Está levantada em review/ §3.
# `demand` foi atribuída: mede o que a obra exige do leitor, e isso aplica-se
# a um manual tão bem como a um tratado.
# ---------------------------------------------------------------------------

inclusion_criteria:            # derivados da PERGUNTA, não das onze obras
  by: claude
  status: proposta
  criteria:
    - "Obras que ensinam a produzir, manter, curar, construir, defender ou
       orientar-se sem depender da infraestrutura que normalmente faz isso."
    - "Manuais, guias de campo e obras de referência prática, de qualquer país
       e qualquer época."
    - "Obras de doutrina ou de política sobre autossuficiência pertencem
       igualmente, se argumentarem sobre a pergunta da coleção."
  out_of_scope:
    - "Literatura de sobrevivência e relatos de expedição sem conteúdo
       técnico transmissível."
    - "Manuais de equipamento de marca ou catálogos comerciais."
  test_applied: "Nenhum critério acima exclui uma obra que responda claramente
                 à pergunta da coleção. O segundo critério descreve FORMA e não
                 tema, e o terceiro existe exatamente para o primeiro não se
                 fechar sobre a amostra de manuais que você enviou."

# ---------------------------------------------------------------------------
# SCOPE_MAP — e aqui há uma diferença que vale registrar.
#
# Nas outras coleções as regiões são MINHAS. Aqui as seis regiões são SUAS:
# são os seis cabeçalhos que você escreveu. Eu não inventei território — li os
# seus cabeçalhos como território, que é a única leitura que explica por que
# `Energia:` veio escrita e vazia. O que é meu é a LEITURA; os nomes são seus.
#
# `Energia` fica `absent` + `open`: território que você declarou e ainda não
# ocupou. Não é dívida, não é lacuna, e a análise de cobertura não a levanta
# como defeito (§2.1).
# ---------------------------------------------------------------------------
scope_map:
  regions_by: voce
  reading_by: claude
  map_status: proposta
  regions:
    - {id: sobrevivencia, coverage: covered, pursuit: open,
       held_by: [lontro-monteiro--mini-manual-de-tecnica-escutista,
                 seymour--guia-pratico-da-autossuficiencia,
                 becker-dalponte--rastros-de-mamiferos-silvestres-brasileiros,
                 canterbury--bushcraft-101],
       note: "Técnica de campo, autossuficiência doméstica e leitura do
              terreno: o que fazer com o que existe à volta."}
    - {id: medicina-e-socorro, coverage: covered, pursuit: open,
       held_by: [dickson--where-there-is-no-dentist,
                 werner--donde-no-hay-doctor,
                 silva-conforto--primeiros-socorros,
                 naemt--phtls-prehospital-trauma-life-support,
                 hoffmann--the-complete-herbs-sourcebook],
       note: "Cuidado do corpo sem hospital à mão: emergência, atenção
              continuada e recursos vegetais."}
    - {id: defesa, coverage: thin, pursuit: open,
       held_by: [pellegrini-moraes--tiro-de-combate-pistola],
       note: "Proteção da vida e uso de força defensiva."}
    - {id: construcao, coverage: thin, pursuit: open,
       held_by: [van-lengen--manual-del-arquitecto-descalzo],
       note: "Abrigo: construir e reparar com meios locais."}
    - {id: agricultura, coverage: thin, pursuit: open,
       held_by: [kinupp-lorenzi--plantas-alimenticias-nao-convencionais-no-brasil],
       note: "Alimento: cultivar, identificar e aproveitar o que se come."}
    - {id: energia, coverage: absent, pursuit: open,
       note: "Geração, armazenamento e uso de energia fora da rede. REGIÃO
              DECLARADA POR VOCÊ E VAZIA — você escreveu o cabeçalho e não pôs
              nada por baixo. É território reivindicado, não esquecimento."}
    # REGIÃO NOVA, pós-importação — proposta por você em 2026-09-06, não parte
    # dos seis cabeçalhos originais. Mesma leitura de Claude sobre o nome que
    # você deu, mesmo mecanismo das seis primeiras.
    - {id: planejamento-risco-localizacao, coverage: covered, pursuit: open,
       held_by: [skousen--strategic-relocation],
       note: "Avaliar ameaças, escolher o terreno e decidir onde
              estabelecer-se — risco geográfico, geopolítico e ambiental como
              critério de localização, e não apenas como fundo de outra
              competência."}

# ---------------------------------------------------------------------------
# EXCLUÍDA POR DECISÃO SUA
# ---------------------------------------------------------------------------
excluded:
  - work: werner--donde-no-hay-doctor
    title_as_listed: "Onde não há médicos"
    reason: "Substituída por Alton, The Survival Medicine Handbook (4ª ed.,
             2021), que trata do mesmo cuidado continuado sem médico, é atual
             e parte do cenário da coleção (a ajuda não vem). Werner foi
             escrito em 1970 para agentes de saúde em vilas pobres; uma
             avaliação sistemática (Babu e Eisenberg) apontou problemas
             consideráveis nas recomendações de diagnóstico e tratamento; e a
             edição brasileira tem décadas. Pesquisa em
             review/survival-self-sufficiency.md §9."
    by: voce
    date: 2026-10-10
    card: d-sob-medicina
    note: "O registro da obra e as três publicações (Terracota, Hesperian,
           Paulus) continuam no acervo, sem coleção."

  - work: null
    title_as_listed: "Faça você mesmo (duas edições)"
    reason: "Nem você nem eu conseguimos identificar de forma confiável quais
             seriam as duas edições. Decisão sua de 2026-09-06: descartar da
             importação, não tratar como pendência, e não criar registro de
             obra nem de publicação."
    by: voce
    date: 2026-09-06
    note: "`work: null` porque nunca existiu registro a que apontar — o campo
           `excluded` do esquema pressupõe uma obra já registrada, e este é o
           primeiro caso de exclusão ANTES da criação. Fica aqui para que a
           entrada não volte a ser proposta."

  - work: null
    title_as_listed: "Guia Prático de Primeiros Socorros"
    author_as_listed: "Eda Gomes Lambert"
    reason: "Decisão sua de 2026-09-06: valor marginal baixo demais frente ao
             que a coleção já cobre em medicina-e-socorro — especialmente
             Werner (Onde não há médico), PHTLS, e Primeiros Socorros
             (Silva & Conforto, incluída na mesma decisão). Exclusão
             curatorial por redundância (curation-rules.md §2.3), não falha de
             identificação bibliográfica."
    by: voce
    date: 2026-09-06
    note: "Identificadores corrigidos nesta decisão: ASIN/ISBN-10 853392240X
           (dígito verificador X válido). O ISBN-13 correspondente, calculado
           pelo algoritmo padrão a partir desse ISBN-10, é 978-85-3392-240-2 —
           NÃO 9788533922404, que foi uma tentativa de busca incorreta de
           Claude numa conversa anterior e nunca chegou a ser gravada em
           arquivo canônico. Nenhum registro de obra ou de publicação foi
           criado para esta entrada."

  - work: begovic-luther--dark-secrets-of-shtf-survival
    title_as_listed: "The Dark Secrets of SHTF Survival: The Brutal Truth
                       About Violence, Death, & Mayhem You Must Know to
                       Survive"
    reason: "Decisão sua de 2026-09-06: não é manual técnico de sobrevivência
             transmissível — cai no critério de exclusão desta coleção
             ('literatura de sobrevivência... sem conteúdo técnico
             transmissível'). Relevância bibliográfica preservada: a obra TEM
             registro em works/, com `pending_assignment`, para
             reconsideração quando um corpo de obras sobre colapso e
             fragilidade social existir na biblioteca."
    by: voce
    date: 2026-09-06
    note: "Diferente do caso 'Faça você mesmo' acima: ali não havia registro
           possível; aqui há um registro completo em
           works/begovic-luther--dark-secrets-of-shtf-survival.md, apenas sem
           coleção. Ver review/survival-self-sufficiency.md §6."

# ===========================================================================
# SEQUÊNCIA — a sua ordem, e as suas seções como movimentos.
# ===========================================================================
sequence:

  - movement: "Sobrevivência"
    purpose: "Técnica de campo e autossuficiência: orientar-se, ler o terreno,
              produzir e manter."
    purpose_by: claude
    regions: [sobrevivencia]

  - work: lontro-monteiro--mini-manual-de-tecnica-escutista
    demand: leve
    why_here: "Técnica escutista em formato de bolso: o repertório básico de
               campo, condensado."
    why_here_by: claude

  - work: seymour--guia-pratico-da-autossuficiencia
    demand: moderado
    why_here: "A obra mais ampla da coleção em escopo: cultivo, criação,
               conservação, ofícios e energia doméstica num só volume."
    why_here_by: claude

  - work: becker-dalponte--rastros-de-mamiferos-silvestres-brasileiros
    demand: moderado
    why_here: "Guia de campo brasileiro. Ler rastros é saber o que partilha o
               território — caça, risco e presença animal."
    why_here_by: claude

  - work: canterbury--bushcraft-101
    demand: leve
    why_here: "Bushcraft: abrigo, fogo, água e ferramenta com o que a mata dá."
    why_here_by: claude

  # PARTICIPAÇÃO NOVA — decisão sua de 2026-10-10 (curadoria das fotos).
  - work: costa--bushcraft-habilidades-na-natureza
    demand: leve
    why_here: "O mesmo ofício de Canterbury, por autor brasileiro: ferramentas
               de corte, abrigo, água, fogo, nós e escultura em madeira, com o
               mato daqui."
    why_here_by: claude
    inserted_by: claude          # ver order_changes
    publication_pref: pub--bonilaure--bushcraft-habilidades-na-natureza--2022   # seu exemplar

  - work: gooley--the-lost-art-of-reading-natures-signs
    role: foundational
    demand: leve
    why_here: "Ensina a deduzir direção, clima, água e presença de animais a
               partir do que o ambiente mostra, sem instrumento nenhum."
    why_here_by: claude
    perspective: "Leitura do ambiente como método de dedução."
    subjects_stated: [orientacao, clima, agua, rastros, paisagem, observacao]
    subjects_stated_by: claude
    # Entrou em 2026-09-23. Repertório calibrado para o hemisfério norte
    # temperado: o método transfere, boa parte dos sinais específicos não.
    # Ele sabe disso e aceitou — está registrado na obra.

  - work: gooley--the-secret-world-of-weather
    role: supplementary
    demand: leve
    why_here: "Aprofunda só a parte climática: ler nuvem, vento e microclima
               para saber o que o tempo está fazendo agora e o que vem."
    why_here_by: claude
    perspective: "Meteorologia observacional e microclima."
    subjects_stated: [nuvens, vento, chuva, temperatura, umidade, microclimas]
    subjects_stated_by: claude
    # Único aprofundamento escolhido entre os cinco livros do autor que ele
    # trouxe. Os outros três foram examinados e recusados por sobreposição.

  - movement: "Medicina e socorro"
    purpose: "Cuidar do corpo sem hospital à mão — da emergência traumática ao
              cuidado continuado."
    purpose_by: claude
    regions: [medicina-e-socorro]

  - work: dickson--where-there-is-no-dentist
    demand: moderado
    why_here: "Cuidado odontológico onde não há dentista. A Hesperian escreve
               para quem tem de agir sem estrutura."
    why_here_by: claude
    publication_pref: pub--hesperian--where-there-is-no-dentist--2021   # decisão sua, 2026-10-10 (d-ed-dickson)

  # PARTICIPAÇÃO NOVA — decisão sua de 2026-10-10 (cartão d-sob-medicina,
  # opção A): ocupa o lugar de Werner, que saiu da coleção (ver `excluded`).
  - work: alton--the-survival-medicine-handbook
    demand: moderado
    why_here: "O manual de medicina para quando a ajuda não vem: parte do
               princípio de que hospital e médico não estão disponíveis, e
               cobre o cuidado continuado — infecções, doenças crônicas,
               medicamentos, procedimentos, dentes, plantas medicinais. Toma o
               lugar de Werner, escrito para agentes de saúde em vilas pobres
               nos anos 1970 e com recomendações apontadas como problemáticas
               numa avaliação sistemática."
    why_here_by: claude
    inserted_by: claude          # ver order_changes
    publication_pref: pub--doom-and-bloom--the-survival-medicine-handbook--2021   # decisão sua, 2026-10-10 (d-sob-medicina)

  # ACRÉSCIMO PÓS-IMPORTAÇÃO — decisão sua de 2026-09-06. Posicionada aqui,
  # entre Werner e o PHTLS, por raciocínio seu explícito de posição
  # intermediária entre os dois.
  # NOTA 2026-10-10: Werner saiu da coleção e Alton ocupa o lugar dele. O seu
  # `why_here` abaixo continua citando Werner e foi preservado como escrito;
  # a posição intermediária vale igualmente entre Alton e o PHTLS.
  - work: silva-conforto--primeiros-socorros
    demand: moderado
    why_here: "Posição intermediária entre Onde não há médico (cuidado de
               saúde comunitário amplo, sem médico) e o PHTLS (protocolo
               profissional de trauma pré-hospitalar): procedimentos gerais
               de primeiros socorros para o leigo, mais focados que Werner e
               muito menos técnicos que o PHTLS."
    why_here_by: voce
    publication_pref: pub--di-livros--primeiros-socorros

  - work: naemt--phtls-prehospital-trauma-life-support
    demand: exigente
    why_here: "O protocolo profissional de trauma pré-hospitalar. Difere dos
               dois anteriores em destinatário: é formação técnica, não guia
               leigo."
    why_here_by: claude

  # PARTICIPAÇÃO NOVA — decisão sua de 2026-10-10 (cartão d-sob-medicina,
  # opção A). Posição minha, a confirmar: depois do PHTLS, porque também é
  # escrita para profissionais e supõe evacuação; antes de Hoffmann.
  - work: schlaad--medicina-em-areas-remotas-no-brasil
    demand: exigente
    why_here: "A única obra em português sobre medicina longe dos centros
               médicos, e a única com o que é próprio do Brasil: biomas,
               animais peçonhentos, doenças tropicais. Escrita para
               profissionais de saúde; complementa Alton pelo contexto local."
    why_here_by: claude
    inserted_by: claude          # ver order_changes
    publication_pref: pub--manole--medicina-em-areas-remotas-no-brasil--2019   # decisão sua, 2026-10-10 (d-sob-medicina)

  - work: hoffmann--the-complete-herbs-sourcebook
    demand: moderado
    why_here: "Recurso vegetal medicinal, de A a Z. Complementa os manuais de
               emergência pelo lado do que se cultiva e se colhe."
    why_here_by: claude

  # PARTICIPAÇÃO NOVA — decisão sua de 2026-10-10 (curadoria das fotos), no
  # lugar dos livros de Balbach, que não entraram.
  - work: lorenzi-matos--plantas-medicinais-no-brasil
    demand: moderado
    why_here: "As plantas medicinais da flora brasileira com base técnica:
               química, fitoterapia e etnofarmacologia. Complementa Hoffmann,
               que é de tradição europeia, pelo que cresce aqui."
    why_here_by: claude
    inserted_by: claude          # ver order_changes
    publication_pref: pub--plantarum--plantas-medicinais-no-brasil--2021   # decisão sua, 2026-10-10

  - movement: "Defesa"
    purpose: "Proteção da vida e uso de força defensiva."
    purpose_by: claude
    regions: [defesa]

  - work: pellegrini-moraes--tiro-de-combate-pistola
    demand: moderado
    why_here: "Fundamentos e habilidades de tiro defensivo com pistola,
               incluindo segurança e manuseio."
    why_here_by: claude

  - movement: "Construção"
    purpose: "Abrigo: construir e reparar com meios locais."
    purpose_by: claude
    regions: [construcao]

  - work: van-lengen--manual-del-arquitecto-descalzo
    demand: moderado
    why_here: "Arquitetura de baixo custo com técnica e material local — o
               abrigo como coisa que se faz, não que se compra."
    why_here_by: claude

  - movement: "Agricultura"
    purpose: "Alimento: cultivar, identificar e aproveitar."
    purpose_by: claude
    regions: [agricultura]

  - work: kinupp-lorenzi--plantas-alimenticias-nao-convencionais-no-brasil
    demand: moderado
    why_here: "Identificação e uso alimentar de plantas não convencionais no
               Brasil — o alimento que já está no terreno."
    why_here_by: claude

  # MOVIMENTO E REGIÃO NOVOS — decisão sua de 2026-09-06, pós-importação.
  # Colocado ao final da sequência por ser o acréscimo mais recente, não por
  # juízo de prioridade intelectual: a coleção é `thematic`, e nela a ordem
  # não carrega dependência (ver "Por que esta ordem", abaixo).
  - movement: "Planejamento, risco e localização"
    purpose: "Avaliar ameaças, escolher o terreno e decidir onde
              estabelecer-se."
    purpose_by: voce
    regions: [planejamento-risco-localizacao]

  - work: skousen--strategic-relocation
    demand: moderado
    why_here: "Avaliação de risco geográfico, geopolítico e ambiental para a
               escolha e a mudança de local de residência, como forma de
               reduzir exposição a ameaças."
    why_here_by: voce
    edition_pref:
      text: "ASIN/ISBN-10 1735015407, 4ª edição (Amazon). Editora e ano não
             identificados."
      by: claude
      verified: true
    publication_pref: pub--joel-skousen-designs--strategic-relocation--2020   # escolhida em 2026-10-10 (Etapa 1): 4ª edição, a do ISBN já registrado; pesquisa na obra

# `Energia` NÃO tem movimento. Um movimento vazio é proibido pelo modelo, e
# fabricar um seria fingir conteúdo. A região existe no scope_map; o movimento
# entra quando entrar a primeira obra.

paths: []

tensions: []
# Vazio, e AQUI isso não é achado nenhum. Manuais técnicos não se contradizem
# como argumentos: um guia de rastros e um manual de trauma não discordam,
# tratam de coisas diferentes. Diferente de Educação, onde o vazio era sintoma.

# ===========================================================================
# ORDEM ORIGINAL
# ===========================================================================
original_order: [lontro-monteiro--mini-manual-de-tecnica-escutista,
  seymour--guia-pratico-da-autossuficiencia,
  becker-dalponte--rastros-de-mamiferos-silvestres-brasileiros,
  canterbury--bushcraft-101,
  dickson--where-there-is-no-dentist,
  werner--donde-no-hay-doctor,
  naemt--phtls-prehospital-trauma-life-support,
  hoffmann--the-complete-herbs-sourcebook,
  pellegrini-moraes--tiro-de-combate-pistola,
  van-lengen--manual-del-arquitecto-descalzo,
  kinupp-lorenzi--plantas-alimenticias-nao-convencionais-no-brasil]
# NOTA: a sua lista tinha DOZE entradas; esta ordem tem onze. A décima segunda
# — «Faça você mesmo (duas edições)» — foi descartada por decisão sua e está em
# `excluded`. Não entra aqui porque nunca teve id.

order_changes:
  - work: costa--bushcraft-habilidades-na-natureza
    kind: insert
    from: "não estava na biblioteca"
    to: "movimento Sobrevivência, depois de canterbury--bushcraft-101"
    approved_by: voce
    date: 2026-10-10
    reason: "Exemplar seu; inclusão decidida por você na curadoria das fotos.
             Ao lado de Canterbury por tratar do mesmo ofício."
    reversible_by: "Remover a participação e o registro da obra."

  - work: lorenzi-matos--plantas-medicinais-no-brasil
    kind: insert
    from: "não estava na biblioteca"
    to: "movimento Medicina e socorro, depois de hoffmann--the-complete-herbs-sourcebook"
    approved_by: voce
    date: 2026-10-10
    reason: "Recomendação de Claude no lugar dos livros de Balbach, aprovada
             por você na curadoria das fotos."
    reversible_by: "Remover a participação e o registro da obra."

  - work: alton--the-survival-medicine-handbook
    kind: insert
    from: "não estava na biblioteca"
    to: "movimento Medicina e socorro, no lugar de werner--donde-no-hay-doctor"
    approved_by: voce
    date: 2026-10-10
    reason: "Substitui Werner; cartão d-sob-medicina, opção A."
    reversible_by: "Remover a participação e devolver Werner à mesma posição."

  - work: schlaad--medicina-em-areas-remotas-no-brasil
    kind: insert
    from: "não estava na biblioteca"
    to: "movimento Medicina e socorro, depois de naemt--phtls-prehospital-trauma-life-support"
    approved_by: voce
    date: 2026-10-10
    reason: "Referência brasileira; cartão d-sob-medicina, opção A. A posição é
             de Claude e fica a confirmar."
    reversible_by: "Remover a participação e o registro da obra."
structural_changes: []

updated: 2026-09-23
---

## Por que esta ordem

Aqui a ordem é **por tema**, não por dependência: ler sobre defesa antes de
medicina não atrapalha nada. Os movimentos podem ser lidos na ordem que a
necessidade pedir.

A sequência vai do **geral ao específico** e do **corpo ao território**:
começa pelo repertório de campo mais amplo (Sobrevivência), passa ao cuidado
do corpo, que é a competência que não admite espera (Medicina e socorro), e só
então chega às competências que pedem instalação e prática longa: Defesa,
Construção, Agricultura. Termina em Planejamento, risco e localização:
decidir onde se estabelecer e contra o quê se preparar.

Energia ainda não tem nenhuma obra na coleção.

## Avaliação curatorial

Ver `review/survival-self-sufficiency.md`.
