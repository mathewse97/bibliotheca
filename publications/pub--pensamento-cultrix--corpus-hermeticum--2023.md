---
id: pub--pensamento-cultrix--corpus-hermeticum--2023
title_as_published: "Corpus hermeticum græcum"
publisher: "Pensamento-Cultrix"
publisher_country: BR
series: null
year: 2023
language: pt-BR
bilingual: false
bilingual_pair: null           # não verificado no livro (§E.2 passo 5)
editor: null
introduction_by: null
register: academic
framing: null
format: []
pages: null
isbn13: "9786557362600"

availability_br: em-catalogo
availability_checked: 2026-09-19
links:
  publisher: ""
  catalogue: ""

verified_fields: [publisher, year, isbn13, translator, translated_from]
research_status: partially_researched
source_of_record: voce

contains:
  - work: corpus-hermeticum
    verdict: unassessed         # o §F não foi percorrido — ver review/religion.md §6
    reason: null
    translator: [pessoa-de-lira]
    translated_from: direct
    source_text: "grego"
    completeness: null
    apparatus: []

cover:
  file: covers/pub--pensamento-cultrix--corpus-hermeticum--2023.webp
  source: "https://m.media-amazon.com/images/I/A1tUhsiVDtL.jpg — imagem
           principal do anúncio https://www.amazon.com.br/dp/6557362607, baixada
           pelo navegador em 2026-09-25"
  source_type: retailer
  format_note: "Convertida para WebP (qualidade 80, mesmas dimensões) em 2026-09-25, conforme config/acquisition.yaml."
  represents: publication
  checked: 2026-09-25
  rights_note: "Imagem de capa usada como identificação bibliográfica da edição."

acquisition:
  - retailer: amazon-br
    url: "https://www.amazon.com.br/dp/6557362607"
    listing_id: "6557362607"
    match_basis: isbn13
    match_note: "O ASIN é o ISBN-10 desta edição e converte no ISBN-13
                 verificado."
    format_listed: null
    price_band: null
    availability: em-catalogo
    checked: 2026-09-19
    checked_by: claude

provenance:
  - claim: "Editora Pensamento-Cultrix, 2023; ISBN impresso 9786557362600,
            digital 9786557362624; prefácio, introdução, tradução direta do
            grego e glossário grego-português de David Pessoa de Lira."
    source: "Ficha do e-book em distribuidor"
    source_tier: 6
    retrieved: 2026-09-20
    confidence: reported
updated: 2026-09-20
---

## Avaliação

O BILINGUISMO NÃO ESTÁ VERIFICADO como o §E.2 passo 5 exige, e o título traz 'græcum' — a armadilha que o §E.1b nomeia. `bilingual` fica false até reverificação em tier 1–3.

Nenhum veredito foi emitido para esta publicação. O §F é um procedimento
ordenado — portão textual, portão físico, faixas de mérito, e só então
idioma — e ele não foi percorrido: os candidatos não foram enumerados antes
de julgar, como o §E.2 passo 4 exige. `verdict: unassessed` é o estado
correto, não uma omissão.
