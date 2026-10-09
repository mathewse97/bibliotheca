---
id: pub--penguin-companhia--caixa-homero
title_as_published: "Box Homero — Ilíada e Odisseia"   # "Box", não "Caixa": correção sua (registrada só em 2026-09-23). O id continua o mesmo para não quebrar referências.
publisher: penguin-companhia
publisher_country: BR
series: null
year: null
language: pt-BR
bilingual: false
bilingual_pair: null
editor: null
introduction_by: null
register: null
framing: null
format: []
packaging: caixa               # valor do vocabulário (embalagem com vários volumes); o nome do produto é 'Box'. Dois volumes
                               # numa embalagem, não duas obras num tomo.
pages: null
isbn13: "978-85-6356-094-0"

availability_br: null
availability_checked: null
links:
  publisher: ""
  catalogue: ""

verified_fields: [title_as_published, publisher, isbn13]
research_status: partially_researched
missing: ["ano", pages, format, "número de edição",
          "aparato crítico, introdução e notas",
          "confirmação em fonte tier 1 (página da própria editora)"]
source_of_record: claude

contains:
  - work: homero--ilias
    verdict: unassessed
    reason: "Nenhuma edição alternativa foi pesquisada."
    translator: [frederico-lourenco]
    translated_from: direct
    source_text: null
    completeness: null
    apparatus: []
  - work: homero--odysseia
    verdict: unassessed
    reason: "Nenhuma edição alternativa foi pesquisada."
    translator: [frederico-lourenco]
    translated_from: direct
    source_text: null
    completeness: null
    apparatus: []
    # Objeto que você JÁ POSSUI (dito por você; posse só vale na interface,
    # em state/personal.yaml, que o agente não escreve). Você pretende comprar
    # também as edições bilíngues da Editora 34 (Ilíada e Odisseia).
    # Volume que você JÁ POSSUI. Um objeto, duas obras — e as duas obras t
    # êm também edição bilíngue pela Editora 34. Posse é estado pessoal e 
    # vive em state/personal.yaml, não aqui.


cover:
  file: covers/pub--penguin-companhia--caixa-homero.webp
  source: "https://m.media-amazon.com/images/I/A1qnARklYSL._SL1500_.jpg — imagem
           principal do anúncio https://www.amazon.com.br/dp/8563560948, baixada
           pelo navegador em 2026-09-23"
  source_type: retailer
  format_note: "Convertida para WebP (qualidade 80, mesmas dimensões) em 2026-09-23, por decisão do Mathews, para caber no artefato."
  represents: publication
  checked: 2026-09-23
  rights_note: "Imagem de capa usada como identificação bibliográfica da edição."

acquisition:
  - retailer: amazon-br
    url: "https://www.amazon.com.br/dp/8563560948"
    listing_id: "8563560948"
    match_basis: isbn13
    match_note: "O ASIN é o ISBN-10 que converte no isbn13 deste registro."
    format_listed: null
    price_band: null
    availability: null
    checked: 2026-09-23
    checked_by: claude

provenance:
  - claim: "O nome do produto é Box Homero, não Caixa Homero; você o possui e pretende
            comprar também as bilíngues da Editora 34."
    source: "informado pelo Mathews; reafirmado em 2026-09-23 porque a correção
             anterior não tinha chegado aos arquivos"
    source_tier: null
    retrieved: 2026-09-23
    confidence: reported
  - claim: "Título, editora, tradutor e ISBN-13 conforme o levantamento de
            edições que o Mathews fez na Amazon e forneceu em 2026-09-12."
    source: "levantamento do próprio Mathews a partir de anúncios da Amazon"
    source_tier: 7
    retrieved: 2026-09-12
    confidence: reported
    note: "Ele declarou que fez a curadoria das edições e que verificará
           manualmente os casos duvidosos, enviando ajustes. Nada aqui foi
           confirmado em catálogo de editora."

updated: 2026-09-23
---

## Avaliação

Identificação em nível de anúncio de varejo, feita pelo Mathews. Suficiente para registrar a publicação e o vínculo obra↔volume; insuficiente para qualquer veredito de qualidade de edição. Nenhuma alternativa foi pesquisada.
