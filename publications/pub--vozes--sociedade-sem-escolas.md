---
id: pub--vozes--sociedade-sem-escolas
title_as_published: "Sociedade sem Escolas"
publisher: vozes
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
isbn13: "978-85-3265-891-3"

availability_br: null
availability_checked: null
links:
  publisher: ""
  catalogue: ""

verified_fields: [title_as_published, isbn13]
research_status: partially_researched
missing: ["ano — fontes de varejo divergem entre uma primeira edição de 1982
          e reimpressões posteriores (uma cita 2018); não ficou claro a qual
          este ISBN corresponde", tradutor, "número de edição", format,
          pages, "confirmação em fonte tier 1 (página da própria Vozes)"]
source_of_record: claude

contains:
  - work: illich--deschooling-society
    verdict: unassessed
    reason: "Único candidato identificado até agora — não há comparação com
             alternativas porque nenhuma foi pesquisada."
    translator: []
    translated_from: direct
    source_text: null
    completeness: null
    apparatus: []

cover:
  file: covers/pub--vozes--sociedade-sem-escolas.webp
  source: "https://m.media-amazon.com/images/I/71GGN5gpLGL._SL1500_.jpg — imagem
           principal do anúncio https://www.amazon.com.br/dp/8532658911, baixada
           pelo navegador em 2026-10-09"
  source_type: retailer
  format_note: "Convertida para WebP (qualidade 80, mesmas dimensões) em 2026-10-09, conforme config/acquisition.yaml."
  represents: publication
  checked: 2026-10-09
  rights_note: "Imagem de capa usada como identificação bibliográfica da edição."

acquisition:
  - retailer: amazon-br
    url: "https://www.amazon.com.br/Sociedade-sem-escolas-IVAN-ILLICH/dp/8532658911"
    listing_id: "8532658911"
    match_basis: isbn13
    match_note: "ASIN é o ISBN-10 desta publicação, consistente com o
                 ISBN-13 978-85-3265-891-3 que você forneceu."
    format_listed: brochura
    price_band: null
    availability: em-catalogo
    checked: 2026-10-09
    checked_by: claude

provenance:
  - claim: "Publicado pela Editora Vozes (Petrópolis); catálogos de varejo
            citam uma edição de 1982 e reimpressões posteriores, sem que se
            possa atribuir com segurança qual delas tem o ISBN
            978-85-3265-891-3."
    source: "múltiplos catálogos de varejo (Mercado Livre, Estante Virtual,
             Portal dos Livreiros) — nenhuma página da própria Vozes foi
             lida diretamente"
    source_tier: 6
    retrieved: 2026-09-10
    confidence: reported

  - claim: "Para este ISBN, o anúncio dá: Editora Vozes, 1ª edição, 7 de
            novembro de 2018, 152 páginas, ISBN-13 978-8532658913, 20,8 × 13,4
            × 0,6 cm; tradução de Lúcia Mathilde Endlich Orth."
    source: "https://www.amazon.com.br/dp/8532658911"
    source_tier: 7
    retrieved: 2026-10-09
    confidence: reported
    note: "Aponta 2018 como o ano deste ISBN, o que resolveria a dúvida anotada
           em `missing` — mas é varejo; ano, páginas e tradutora não foram
           gravados nos campos até haver confirmação da Vozes."
  - claim: "A capa mostra título, autor e selo da Editora Vozes."
    source: "covers/pub--vozes--sociedade-sem-escolas.webp"
    source_tier: null
    retrieved: 2026-10-09
    confidence: verified
    note: "Exame direto da imagem: o selo impresso confere com a editora do registro."

updated: 2026-10-09
---

## Avaliação

Identificação em nível de varejo. Suficiente para registrar a publicação;
insuficiente para atribuir ano ou tradutor com confiança, ou para qualquer
veredito de qualidade de edição.
