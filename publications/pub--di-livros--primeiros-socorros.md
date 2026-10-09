---
id: pub--di-livros--primeiros-socorros
title_as_published: "Primeiros Socorros"
publisher: di-livros
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
pages: null
isbn13: "978-85-8116-091-7"

availability_br: null
availability_checked: null
links:
  publisher: ""
  catalogue: ""

verified_fields: [title_as_published, isbn13]
research_status: partially_researched
missing: ["publisher — tier 1 não confirmado, apenas catálogo de varejo",
          year, format, pages, register]
source_of_record: claude

contains:
  - work: silva-conforto--primeiros-socorros
    verdict: unassessed
    reason: "Identificação em tier 6 apenas. Falta confirmação em fonte
             bibliográfica (tier 1-5) antes de qualquer veredito de edição."
    translator: []
    translated_from: null
    source_text: null
    completeness: null
    apparatus: []

cover:
  file: covers/pub--di-livros--primeiros-socorros.webp
  source: "https://m.media-amazon.com/images/I/61CVIQaRuBL._SL1500_.jpg — imagem
           do anúncio https://www.amazon.com.br/dp/8581160913, baixada
           pelo navegador em 2026-10-09"
  source_type: retailer
  format_note: "Convertida para WebP (qualidade 80, mesmas dimensões) em 2026-10-09, conforme config/acquisition.yaml."
  represents: publication
  checked: 2026-10-09
  rights_note: "Imagem de capa usada como identificação bibliográfica da edição."

acquisition:
  - retailer: amazon-br
    url: "https://www.amazon.com.br/Primeiros-Socorros-Evandro-Cl%C3%A1udia-Conforto/dp/8581160913"
    listing_id: "8581160913"
    match_basis: isbn13
    match_note: "O código em /dp/ do anúncio é o ISBN-10 desta publicação
                 (8581160913), consistente com o ISBN-13 978-85-8116-091-7
                 visto nas listagens consultadas."
    format_listed: null
    price_band: null
    availability: null
    availability_note: "Não verificada."
    checked: 2026-09-06
    checked_by: claude

provenance:
  - claim: "ISBN-13 9788581160917, título 'Primeiros Socorros', publicado
            pela Di Livros Editora e Livraria."
    source: "https://www.dilivros.com.br/livro-primeiros-socorros-9788581160917,c57170.html
             (título e ISBN vistos em resultado de busca; página não foi lida
             diretamente)"
    source_tier: 6
    retrieved: 2026-09-06
    confidence: reported
  - claim: "Capa tomada do anúncio https://www.amazon.com.br/dp/8581160913."
    source: "covers/pub--di-livros--primeiros-socorros.webp"
    source_tier: null
    retrieved: 2026-10-09
    confidence: verified
    note: "DIVERGÊNCIA: o selo impresso na capa é o da MARTINARI, e o anúncio também dá Editora Martinari; o registro diz Di Livros. O ISBN confere. Não corrigido: decisão do Mathews."

updated: 2026-10-09
---

## Avaliação

Identificação em nível de varejo/catálogo, não de fonte bibliográfica
primária. Suficiente para registrar a publicação e a aquisição;
insuficiente para emitir qualquer veredito de qualidade de edição.
