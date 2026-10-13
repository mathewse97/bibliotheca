---
id: ancient-near-east-egypt
title_pt: "Oriente Próximo e Egito antigos"
title_by: claude
title_approved_by: voce
question: "Como surgiram e funcionaram as civilizações do Oriente Próximo e do
           Egito — Estado, sociedade, economia, escrita e crença — e o que
           delas passou à Grécia, a Israel e ao Ocidente?"
question_by: claude
question_status: estabelecida
question_approved_by: voce
question_approved_on: 2026-10-12
# Sem foto de fundo: a interface usa o mosaico das capas (interface-rules.md §5).

source:
  origin: pedido-seu
  created: 2026-10-13
  note: "Nasceu de uma pergunta do Mathews sobre O Egito antigo, de Ciro
         Flamarion Cardoso (2026-10-11), e da série Blackwell History of the
         Ancient World. Criada por decisão dele em 2026-10-13. A pergunta foi
         DELIMITADA de propósito: 'primeiras civilizações' prometeria Indo,
         China e Mesoamérica, que ele não pediu. Nenhuma coleção foi criada
         para essas regiões; se o interesse vier, ela nasce dele. Ver
         review/ancient-near-east-egypt.md."
sequence_kind: intellectual

provisional:
  inferred_by_claude: [title_pt, question, inclusion_criteria, scope_map,
                       sequence, movement.titles, movement.purpose, role,
                       demand, why_here]
  authored_by_you: []
  approved_by_you: [title_pt, question, membership]
  pending_confirmation: true
  see: review/ancient-near-east-egypt.md

inclusion_criteria:
  by: claude
  status: proposta
  criteria:
    - "Histórias modernas do Oriente Próximo antigo (Mesopotâmia, Anatólia,
       Levante, Irã) e do Egito, de c. 3500 a.C. até Alexandre."
    - "Fontes antigas dessas civilizações, em tradução."
    - "Obras sobre escrita, direito, saber e religião dessas sociedades
       enquanto parte do funcionamento delas."
    - "Obras sobre a passagem dessa herança à Grécia, a Israel e ao
       Ocidente."
  out_of_scope:
    - "O mundo grego e romano em si, e o Egito ptolemaico e romano: são da
       Greco-Romana."
    - "Indo, China, Mesoamérica e outras civilizações antigas: fora da
       pergunta, sem coleção por enquanto."

scope_map:
  by: claude
  map_status: proposta
  regions:
    - {id: mesopotamia, coverage: covered, pursuit: open,
       held_by: [van-de-mieroop--a-history-of-the-ancient-near-east,
                 bottero--au-commencement-etaient-les-dieux],
       note: "Suméria, Acádia, Babilônia e Assíria: cidade, Estado, escrita
              cuneiforme e religião."}
    - {id: egito, coverage: covered, pursuit: open,
       held_by: [van-de-mieroop--a-history-of-ancient-egypt,
                 shaw--the-egyptian-myths],
       note: "Do Estado faraônico à conquista de Alexandre."}
    - {id: levante-e-israel, coverage: covered, pursuit: open,
       held_by: [kaefer--a-biblia-a-arqueologia-e-a-historia-de-israel-e-juda,
                 finkelstein-romer--aux-origines-de-la-torah,
                 smith--the-memoirs-of-god],
       note: "Canaã, Israel e Judá no mundo dos impérios do Oriente Próximo."}
    - {id: anatolia-e-mediterraneo-oriental, coverage: thin, pursuit: open,
       held_by: [cline--1177-bc],
       note: "Hititas e o sistema internacional da Idade do Bronze tardia,
              até o colapso."}
    - {id: persia, coverage: covered, pursuit: open,
       held_by: [brosius--a-history-of-ancient-persia],
       note: "O império aquemênida, que reúne a região e fecha o período."}

excluded: []

sequence:

  - movement: "I. Estados, sociedades e economias"
    purpose: "Como as civilizações da região surgiram, se organizaram e se
              sucederam, da Mesopotâmia à Pérsia."
    purpose_by: claude
    regions: [mesopotamia, egito, anatolia-e-mediterraneo-oriental, persia]

  - work: van-de-mieroop--a-history-of-the-ancient-near-east
    role: foundational
    demand: moderado
    why_here: "O panorama de toda a região, de c. 3000 a.C. a Alexandre:
               política, sociedade, economia e fontes. É a base da coleção."
    why_here_by: claude

  - work: van-de-mieroop--a-history-of-ancient-egypt
    role: foundational
    demand: moderado
    why_here: "O mesmo método aplicado ao Egito, a civilização que o livro
               anterior trata só de passagem."
    why_here_by: claude

  # PARTICIPAÇÃO NOVA sobre registro existente (Greco-Romana).
  - work: cline--1177-bc
    role: supplementary
    demand: leve
    why_here: "O momento em que o sistema internacional da Idade do Bronze
               (Egito, hititas, Babilônia, Assíria, Micenas) entra em colapso.
               Aqui é o fim de um mundo; na Greco-Romana, o ponto de partida
               da Grécia."
    why_here_by: claude
    publication_pref: pub--avis-rara--1177-ac--2023   # seu exemplar

  - work: brosius--a-history-of-ancient-persia
    role: foundational
    demand: moderado
    why_here: "O último império da região, que a unifica até a conquista de
               Alexandre."
    why_here_by: claude

  - movement: "II. Escrita, crença e mito"
    purpose: "Como essas sociedades pensaram o divino, o mundo e a si mesmas."
    purpose_by: claude
    regions: [mesopotamia, egito]

  # PARTICIPAÇÃO NOVA sobre registro existente (Religião).
  - work: bottero--au-commencement-etaient-les-dieux
    role: foundational
    demand: moderado
    why_here: "A religião mesopotâmica lida a partir dos textos cuneiformes:
               a crença como parte do funcionamento da sociedade que o
               movimento I descreve."
    why_here_by: claude

  # PARTICIPAÇÃO NOVA sobre registro existente (Religião).
  - work: shaw--the-egyptian-myths
    role: comparative
    demand: leve
    why_here: "Os mitos egípcios ao lado dos mesopotâmicos: duas maneiras de
               pensar a ordem do mundo."
    why_here_by: claude

  - movement: "III. Israel e a passagem ao Ocidente"
    purpose: "Como Israel se formou dentro desse mundo e transmitiu parte dele
              ao Ocidente."
    purpose_by: claude
    regions: [levante-e-israel]

  # PARTICIPAÇÃO NOVA sobre registro existente (Religião).
  - work: kaefer--a-biblia-a-arqueologia-e-a-historia-de-israel-e-juda
    role: foundational
    demand: moderado
    why_here: "Israel e Judá como reinos do Levante, à luz da arqueologia e dos
               impérios vizinhos."
    why_here_by: claude

  # PARTICIPAÇÃO NOVA sobre registro existente (Religião).
  - work: finkelstein-romer--aux-origines-de-la-torah
    role: pivot
    demand: exigente
    why_here: "Como a Torá foi composta no contexto dos impérios assírio,
               babilônico e persa: o texto que leva essa herança ao Ocidente."
    why_here_by: claude

  # PARTICIPAÇÃO NOVA sobre registro existente (Religião).
  - work: smith--the-memoirs-of-god
    role: supplementary
    demand: exigente
    why_here: "Como o monoteísmo de Israel se formou a partir das tradições
               cananeias."
    why_here_by: claude

updated: 2026-10-13
---

## Por que esta ordem

Primeiro as civilizações, depois o que elas pensaram, e por fim o que
passou adiante. O movimento I segue a cronologia: o panorama geral, o Egito,
o colapso do fim da Idade do Bronze e o império persa. O II trata da crença
como parte do funcionamento dessas sociedades. O III segue Israel, por onde
boa parte dessa herança chegou ao Ocidente. A passagem à Grécia está na
Greco-Romana, onde o *1177 a.C.* e Brosius também participam.

## Avaliação curatorial

Ver `review/ancient-near-east-egypt.md`.
