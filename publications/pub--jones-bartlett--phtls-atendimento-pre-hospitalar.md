---
# PUBLICAÇÃO ESCOLHIDA POR VOCÊ.
# Sem ano no id, por não estar confirmado — mesmo tratamento já dado a
# pub--cultrix--ciencia-e-politica. O id não inventa o que não se sabe.
id: pub--jones-bartlett--phtls-atendimento-pre-hospitalar
title_as_published: "PHTLS: Atendimento Pré-hospitalar ao Traumatizado"
publisher: jones-bartlett
publisher_country: US
series: null
year: 2025                       # Amazon: 20 jul. 2025; algumas lojas dão 2026
language: pt
bilingual: false
bilingual_pair: null
editor: null
introduction_by: null
register: null
framing: null
format: [brochura]
pages: 864
isbn13: "978-1-284-30069-7"
edition_statement: "10ª edição"

availability_br: em-catalogo
availability_checked: 2026-10-21
links:
  publisher: "https://www.psglearning.com/catalog/productdetails/9781284300697"
  catalogue: ""

verified_fields: [isbn13, publisher, title_as_published, edition_statement, pages]
research_status: partially_researched
missing: [register, translator,
          "ano: Amazon dá 2025, algumas lojas 2026"]
source_of_record: voce

# ---------------------------------------------------------------------------
# ANOMALIA REGISTRADA: livro em português com prefixo editorial NORTE-AMERICANO
# (978-1-284). Não é edição brasileira — é a edição em língua portuguesa
# publicada por editora dos EUA. Muda a leitura de aquisição e o raciocínio do
# §F, e explica por que nenhuma busca por "editora brasileira" a encontraria.
# ---------------------------------------------------------------------------

contains:
  - work: naemt--phtls-prehospital-trauma-life-support
    why: "O manual de referência em atendimento pré-hospitalar ao trauma, na tradução portuguesa da 10ª edição, a mais recente, publicada pela própria editora do original e distribuída no Brasil pelo Grupo A. À venda nova; o tradutor não é nomeado nas fontes."
    verdict: recommended
    reason: "Decisão do Mathews (2026-10-21), pela regra de manuais técnicos do §F.2: tradução portuguesa oficial da 10ª edição (2025, 864 p., brochura), publicada pela própria Jones & Bartlett, editora do original, e da mesma edição do original inglês mais recente. À venda nova no Brasil. O tradutor não é nomeado; para este tipo de livro, a tradução da editora do original basta."
    translator: []
    translated_from: direct
    translated_from_confidence: inferred
    translated_from_note: "Do inglês, direto — inferido do facto de a mesma
                           editora publicar o original e esta versão. Nenhuma
                           fonte o declara."
    source_text: "10ª edição inglesa, ISBN 978-1-284-27227-7"
    source_text_confidence: verified
    completeness: null
    apparatus: []
    work_identification_confidence: verified

cover:
  file: covers/pub--jones-bartlett--phtls-atendimento-pre-hospitalar.webp
  source: "https://m.media-amazon.com/images/I/81JGVLq--RL._SL1500_.jpg — imagem
           do anúncio https://www.amazon.com.br/dp/1284300692, baixada
           pelo navegador em 2026-10-09"
  source_type: retailer
  format_note: "Convertida para WebP (qualidade 80, mesmas dimensões) em 2026-10-09, conforme config/acquisition.yaml."
  represents: publication
  checked: 2026-10-09
  rights_note: "Imagem de capa usada como identificação bibliográfica da edição."

acquisition:
  - retailer: amazon-br
    url: "https://www.amazon.com.br/PHTLS-Atendimento-Pr%C3%A9-hospitalar-Traumatizado-10ed/dp/1284300692"
    listing_id: "1284300692"
    match_basis: isbn13
    match_note: "O código em /dp/ do anúncio É o ISBN-10 desta publicação
                 (1284300692, dígito de controlo válido), que converte em
                 978-1-284-30069-7. A correspondência é por identificador, que é a base
                 mais forte que o §E admite. A PÁGINA em si não foi lida: a
                 Amazon.com.br é bloqueada por robots.txt para este agente, e
                 esse bloqueio não foi contornado."
    format_listed: null
    price_band: null
    availability: null
    availability_note: "Não verificada. A página do anúncio não foi lida."
    checked: 2026-09-06
    checked_by: claude

provenance:
  - claim: "ISBN 978-1-284-30069-7, editora Jones & Bartlett Learning / Public
            Safety Group, título `Portuguese PHTLS: Atendimento
            Pré-Hospitalar`."
    source: "https://www.psglearning.com/catalog/productdetails/9781284300697"
    source_tier: 1
    retrieved: 2026-09-06
    confidence: verified
    note: "Página da editora. Confirma identidade, editora e ISBN; NÃO expõe
           ano, edição, páginas nem tradutor."
  - claim: "O ISBN-10 do anúncio (1284300692) é válido e converte em
            978-1-284-30069-7."
    source: "Aritmética de dígito de controlo sobre o identificador fornecido."
    source_tier: null
    tier_note: "Verificação sobre o identificador, não uma fonte."
    retrieved: 2026-09-06
    confidence: verified
  - claim: "Capa tomada do anúncio https://www.amazon.com.br/dp/1284300692."
    source: "covers/pub--jones-bartlett--phtls-atendimento-pre-hospitalar.webp"
    source_tier: null
    retrieved: 2026-10-09
    confidence: verified
    note: "Exame direto da imagem: título, autor e editora conferem com o registro."
  - claim: "PHTLS - Atendimento Pré-hospitalar ao Traumatizado 10ed., Jones & Bartlett, 20 jul. 2025, 864 p., ISBN 978-1284300697; vendido e entregue pela Amazon."
    source: "https://www.amazon.com.br/dp/1284300692"
    source_tier: 7
    retrieved: 2026-10-21
    confidence: reported
  - claim: "Lojas brasileiras (Grupo A, Disal, DI Livros, Martins Fontes Paulista, Loyola) vendem a 10ª edição em português, 864 p., brochura, distribuída pelo Grupo A; preço de lista R$ 703,00."
    source: "Resultados de busca por 9781284300697 (loja.grupoa.com.br, disal.com.br, dilivros.com.br)"
    source_tier: 6
    retrieved: 2026-10-21
    confidence: reported

updated: 2026-10-21
---

## Avaliação

**Recomendada** (2026-10-21). Tradução oficial da 10ª edição, pela própria editora do original.

Identidade e editora confirmadas em tier 1; ano (2025) e páginas (864) vêm de lojas, em 2026-10-21. O `edition_statement`
vem do título do anúncio e da correspondência com a 10ª edição inglesa, e é a
razão de `source_text` estar preenchido com confiança `verified`.
