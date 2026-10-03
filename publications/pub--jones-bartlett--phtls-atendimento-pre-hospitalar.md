---
# PUBLICAÇÃO ESCOLHIDA POR VOCÊ.
# Sem ano no id, por não estar confirmado — mesmo tratamento já dado a
# pub--cultrix--ciencia-e-politica. O id não inventa o que não se sabe.
id: pub--jones-bartlett--phtls-atendimento-pre-hospitalar
title_as_published: "PHTLS: Atendimento Pré-hospitalar ao Traumatizado"
publisher: jones-bartlett
publisher_country: US
series: null
year: null                       # NÃO confirmado
language: pt
bilingual: false
bilingual_pair: null
editor: null
introduction_by: null
register: null
framing: null
format: []
pages: null
isbn13: "978-1-284-30069-7"
edition_statement: "10ª edição"

availability_br: null
availability_checked: null
links:
  publisher: "https://www.psglearning.com/catalog/productdetails/9781284300697"
  catalogue: ""

verified_fields: [isbn13, publisher, title_as_published]
research_status: partially_researched
missing: [year, pages, format, register, translator, translated_from,
          completeness, availability_br]
source_of_record: voce

# ---------------------------------------------------------------------------
# ANOMALIA REGISTRADA: livro em português com prefixo editorial NORTE-AMERICANO
# (978-1-284). Não é edição brasileira — é a edição em língua portuguesa
# publicada por editora dos EUA. Muda a leitura de aquisição e o raciocínio do
# §F, e explica por que nenhuma busca por "editora brasileira" a encontraria.
# ---------------------------------------------------------------------------

contains:
  - work: naemt--phtls-prehospital-trauma-life-support
    verdict: unassessed
    reason: "Não avaliada."
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

updated: 2026-09-06
---

## Avaliação

Identidade e editora confirmadas em tier 1; ano e páginas não. O `edition_statement`
vem do título do anúncio e da correspondência com a 10ª edição inglesa, e é a
razão de `source_text` estar preenchido com confiança `verified` enquanto `year`
continua nulo — são coisas diferentes e o registro não as mistura.
