---
id: pub--nova-fronteira--iniciacao-a-estetica--2023
title_as_published: "Iniciação à Estética"
publisher: nova-fronteira
publisher_country: BR
series: null
year: 2023
language: pt-BR
bilingual: false
bilingual_pair: null
editor: null
introduction_by: null
register: null
framing: null
format: [brochura]
packaging: volume
pages: null
isbn13: "978-65-5640-797-5"

availability_br: em-catalogo
availability_checked: 2026-09-23
links:
  publisher: "https://www.novafronteira.com.br/iniciacao-a-estetica-17-ed"
  catalogue: ""

verified_fields: [title_as_published, publisher, isbn13, year]
research_status: partially_researched
missing: [
          "pages: CONFLITO — o anúncio da Amazon diz 320 p.; a página da editora diz 240 p.",
          "número da edição (a editora e o anúncio dizem 17ª; falta catálogo)",
          "ano e editora da primeira edição (a obra é da década de 1970, não verificado)",
          "quem assina a apresentação ou o prefácio, se houver"]
source_of_record: claude

contains:
  - work: suassuna--iniciacao-a-estetica
    verdict: unassessed
    reason: "Original em português, sem tradução envolvida. Nenhuma edição alternativa foi comparada: reedições do mesmo texto não pedem comparação de tradução."
    translator: []
    translated_from: null  # original em português
    source_text: null
    completeness: null
    apparatus: []

cover:
  file: covers/pub--nova-fronteira--iniciacao-a-estetica--2023.webp
  source: "https://m.media-amazon.com/images/I/81MjIbA5XkL._SL1500_.jpg — imagem
           principal do anúncio https://www.amazon.com.br/dp/6556407976, baixada
           pelo navegador em 2026-09-23"
  source_type: retailer
  format_note: "Convertida para WebP (qualidade 80, mesmas dimensões) em 2026-09-23, por decisão do Mathews, para caber no artefato."
  represents: publication
  checked: 2026-09-23
  rights_note: "Imagem de capa usada como identificação bibliográfica em acervo
                pessoal privado."

acquisition:
  - retailer: amazon-br
    url: "https://www.amazon.com.br/dp/6556407976"
    listing_id: "6556407976"
    match_basis: isbn13
    match_note: "O ASIN é o ISBN-10 desta edição; o anúncio exibe o ISBN-13
                 978-65-5640-797-5."
    format_listed: brochura
    price_band: null
    availability: em-catalogo
    checked: 2026-09-23
    checked_by: claude

provenance:
  - claim: "Nova Fronteira, 17ª edição, 13/12/2023, 320 p., 15,5 × 1,7 × 23 cm, ISBN-13 978-6556407975. O anúncio credita Manuel Dantas Suassuna como ilustrador e Carlos Newton Júnior como artista."
    source: "https://www.amazon.com.br/dp/6556407976"
    source_tier: 7
    retrieved: 2026-09-23
    confidence: reported
  - claim: "Página da editora: Nova Fronteira, 17ª edição (dezembro 2023), capa comum, 240 páginas, ISBN-13 978-6556407975, 15,5 × 1,2 × 27,5 cm."
    source: "https://www.novafronteira.com.br/iniciacao-a-estetica-17-ed"
    source_tier: 1
    retrieved: 2026-09-23
    confidence: reported
    note: "CONFLITO PRESERVADO: páginas e dimensões divergem do anúncio. O
           bloco de detalhes da editora tem o mesmo formato do da Amazon, o
           que sugere cópia; nenhum dos dois números vence sem catálogo."
  - claim: "A capa mostra título, autor e selo da editora desta edição."
    source: "covers/pub--nova-fronteira--iniciacao-a-estetica--2023.jpg"
    source_tier: null
    retrieved: 2026-09-23
    confidence: verified
    note: "Exame direto da imagem: o selo impresso confere com a editora do
           registro. É isso que autoriza guardar uma capa de vendedor."

updated: 2026-09-23
---

## Avaliação

Sem veredito — e aqui não há o que comparar: a obra foi escrita em português, e as edições disponíveis são reedições do mesmo texto pela mesma casa. O que resta aberto é bibliográfico, não de escolha: o número de páginas diverge entre editora (240) e anúncio (320), e por isso `pages` fica nulo.
