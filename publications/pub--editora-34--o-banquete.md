---
id: pub--editora-34--o-banquete
title_as_published: "O banquete"
publisher: editora-34
publisher_country: BR
series: "Clássicos"
year: 2016                      # 1ª edição bilíngue (Coleção Clássicos)
language: pt-BR
bilingual: true
bilingual_pair: ["grc","pt-BR"]   # CORRIGIDO em 2026-09-17: a página da editora declara "Edição bilíngue - português/grego"
editor: null
introduction_by: [cavalcante-souza]
register: academic
framing: null
format: []
pages: 256
isbn13: "978-85-7326-647-4"

availability_br: null
availability_checked: null
links:
  publisher: "https://editora34.com.br/livro/926"   # página bibliográfica, tier 1
  catalogue: ""

verified_fields: [title_as_published, publisher, isbn13, year, pages, series, bilingual, translator]
research_status: partially_researched
missing: [format, "texto-base grego usado",
          "candidatos nas faixas espanhol/italiano/inglês",
          "disponibilidade em varejo datada"]
source_of_record: claude

contains:
  - work: platao--symposion
    verdict: recommended
    reason: "Tradução de especialista (tese de doutorado de 1961, a primeira em Língua e Literatura Grega no Brasil), com notas e ensaio, revista e bilíngue. Superior em aparato à alternativa EDUFPA (C. A. Nunes, introdução de V. S. Pinheiro), que também é bilíngue e está indisponível na loja da editora. Provisório até examinar faixas es/it/en."
    translator: [cavalcante-souza]
    translated_from: direct
    source_text: null
    completeness: null
    apparatus: [notas, ensaio]
    # [SUPERADO em 2026-09-17 — a edição É bilíngue] Único Platão fora da série bilíngue da EDUFPA que você escolheu para
    #  os outros diálogos. Não é erro — a tradução de José Cavalcante de S
    # ouza é referência —, mas é a única quebra de consistência de série n
    # o movimento VI. Observação, não correção.

cover:
  file: covers/pub--editora-34--o-banquete.webp
  source: "Imagem de capa fornecida pelo Mathews em 2026-09-17, da edição bilíngue da Editora 34 (ISBN 978-85-7326-647-4). Confere com a descrição da página da editora: título, subtítulo 'Edição bilíngue', crédito 'Tradução, posfácio e notas de José Cavalcante de Souza'."
  source_type: retailer
  format_note: "Convertida para WebP (qualidade 80, mesmas dimensões) em 2026-09-23, por decisão do Mathews, para caber no artefato."
  represents: publication
  checked: 2026-09-17
  rights_note: "Imagem de capa usada como identificação bibliográfica da edição."


acquisition:
  - retailer: amazon-br
    url: "https://www.amazon.com.br/dp/8573266473"
    listing_id: "8573266473"
    match_basis: isbn13
    match_note: "O ASIN é o ISBN-10 que converte no isbn13 deste registro."
    format_listed: null
    price_band: null
    availability: null
    checked: 2026-09-23
    checked_by: claude

provenance:
  - claim: "Tradução de José Cavalcante de Souza; edição bilíngue português/grego; Coleção Clássicos; 256 p.; 14 x 21 cm; ISBN 978-85-7326-647-4; 2016, 1ª edição; notas e ensaio; origem na tese de 1961."
    source: "https://editora34.com.br/livro/926"
    source_tier: 1
    retrieved: 2026-09-17
    confidence: verified
  - claim: "Alternativa: EDUFPA, O Banquete, Coleção Diálogos de Platão, bilíngue, 4ª ed., 2018, 200 p., ISBN 9788524705373, trad. C. A. Nunes, introdução de Victor Sales Pinheiro. Indisponível na loja."
    source: "https://vendasonline.editora.ufpa.br/filosofia/o-banquete-26/p"
    source_tier: 6
    retrieved: 2026-09-17
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

**Recomendada (provisório).** Confirmado na página bibliográfica da Editora 34 (tier 1): edição bilíngue grego–português, 2016, 256 p., tradução de José Cavalcante de Souza com notas e ensaio, originada na primeira tese de doutorado em grego do país (USP, 1961).

**Correção:** o registro dizia `bilingual: false`, e a revisão (§7.7) tratava esta edição como quebra da série bilíngue. Ela é bilíngue; a observação caiu.

Alternativa: a EDUFPA publica *O Banquete* na mesma série dos outros diálogos (bilíngue, 4ª ed., 2018, ISBN 9788524705373), com tradução de C. A. Nunes, hoje indisponível na loja. A Editora 34 vence em aparato e especialização do tradutor, não por disponibilidade.