---
# ---------------------------------------------------------------------------
# PUBLICAÇÃO — objeto físico. Pode conter várias obras.
# Nada aqui foi verificado. Sua indicação foi "edição brasileira de
# referência da Cultrix" (intenção, não edição identificada).
# ---------------------------------------------------------------------------
id: pub--cultrix--ciencia-e-politica
title_as_published: "Ciência e Política: Duas Vocações"
publisher: cultrix
publisher_country: BR
series: null
year: null                       # a verificar
language: pt-BR
bilingual: false
bilingual_pair: null
editor: null
introduction_by: null
register: null                   # a verificar: academic | popular | escolar
framing: null                    # orientação da introdução, se houver —
                                 # registrada à parte da qualidade da tradução
format: []                       # a verificar
pages: 160                       # anúncio da Amazon (tier 7); ver provenance
isbn13: "978-85-316-0047-0"     # anúncio da Amazon (tier 7); ver provenance
availability_br: null
availability_checked: null
links: {publisher: "", catalogue: "", retailer: ""}

verified_fields: []              # explicitamente vazio. Nada foi checado.
research_status: partially_researched
missing:
  - "Ano da impressão à venda: o anúncio diz 18ª edição e data de 21/10/2003,
     o que pode ser a data do cadastro, não a da tiragem"
  - "Tradutor(es), texto-base alemão e completude das duas conferências"
  - "Confirmação em fonte de nível 1 (página da Cultrix/Pensamento)"
source_of_record: voce           # veio da sua lista, como intenção

# ---------------------------------------------------------------------------
# A JUNÇÃO — como ESTA publicação entrega CADA obra que contém.
# O veredito vive aqui, e não na publicação, porque um volume pode ser
# o veículo certo para uma obra e o errado para outra que ele carrega.
# ---------------------------------------------------------------------------
contains:
  - work: weber--politik-als-beruf
    why: "Sua indicação: as duas conferências de Weber, sobre a ciência e a política, num volume em catálogo."
    verdict: unassessed
    reason: "Pesquisa de 2026-10-10: tradução de Leonidas Hegenberg e Octany Silveira da Mota; a ficha cita os títulos alemães, mas nenhuma fonte diz de que língua traduziram. Alternativas: Editora UnB (2003, trad. Maurício Tragtenberg, revisão técnica do germanista Oliver Tolle; só A política como vocação); Martin Claret (2015, trad. Marco Antônio Casanova, tradutor do alemão; ISBN não confirmado); em Portugal, Artur Morão (2017). Mantida por ser sua indicação e estar em catálogo; ver a seção Edições da obra."
    translator: [leonidas-hegenberg, octany-silveira-da-mota]
    translated_from: unknown     # direct | via:<lang> | unknown
    source_text: null            # qual edição alemã segue
    completeness: null           # complete | abridged | selections
    apparatus: []

  - work: weber--wissenschaft-als-beruf
    verdict: unassessed
    reason: null
    translator: [leonidas-hegenberg, octany-silveira-da-mota]
    translated_from: null
    source_text: null
    completeness: null
    apparatus: []

cover:
  file: covers/pub--cultrix--ciencia-e-politica.webp
  source: "https://m.media-amazon.com/images/I/516sfhDf9vL._SL1179_.jpg — imagem
           principal do anúncio https://www.amazon.com.br/dp/8531600472, baixada
           pelo navegador em 2026-10-09"
  source_type: retailer
  format_note: "Convertida para WebP (qualidade 80, mesmas dimensões) em 2026-10-09, conforme config/acquisition.yaml."
  represents: publication
  checked: 2026-10-09
  rights_note: "Imagem de capa usada como identificação bibliográfica da edição."

acquisition:
  - retailer: amazon-br
    url: "https://www.amazon.com.br/dp/8531600472"
    listing_id: "8531600472"
    match_basis: isbn13
    match_note: "O registro não tinha ISBN: a indicação do Mathews era a edição
                 da Cultrix com este título. A busca na Amazon devolve uma só
                 edição física da Cultrix com ele, e o isbn13 do registro foi
                 tomado deste anúncio — a correspondência é por construção, não
                 independente."
    format_listed: brochura
    price_band: null
    availability: em-catalogo
    checked: 2026-10-09
    checked_by: claude

provenance:
  - claim: "Cultrix, 18ª edição, 160 páginas, ISBN-10 8531600472, ISBN-13
            978-8531600470, 14 × 0,9 × 21 cm, em português; data no anúncio:
            21 de outubro de 2003."
    source: "https://www.amazon.com.br/dp/8531600472"
    source_tier: 7
    retrieved: 2026-10-09
    confidence: reported
    note: "O anúncio não nomeia tradutor. Varejo: estabelece o objeto, não a
           qualidade."
  - claim: "A capa mostra título, autor e selo da Cultrix."
    source: "covers/pub--cultrix--ciencia-e-politica.webp"
    source_tier: null
    retrieved: 2026-10-09
    confidence: verified
    note: "Exame direto da imagem: o selo impresso confere com a editora do registro."
updated: 2026-10-09
---

## Avaliação

Ainda não pesquisada. Quando o §E rodar sobre este volume, cada obra em
`contains` recebe o seu próprio veredito — as duas conferências podem
perfeitamente ter destinos diferentes: esta edição ser a recomendada para
*A política como vocação* e apenas uma alternativa para *A ciência como
vocação*, se existir uma edição melhor da segunda.

Nenhuma outra estrutura da biblioteca permitiria dizer isso. Com edições
embutidas na obra, este volume existiria duas vezes, e as duas cópias
divergiriam na primeira correção.
