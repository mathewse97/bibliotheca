---
# ---------------------------------------------------------------------------
# MODELO DE PUBLICAÇÃO — não é uma publicação. O prefixo `_` faz a build
# ignorar este arquivo.
#
# A publicação é o OBJETO FÍSICO. Pode conter várias obras, e por isso não
# vive dentro de nenhuma delas. Blocos, em ordem:
#   1. propriedades do objeto      — bibliográficas
#   2. contains                    — a junção: como este volume entrega cada obra
#   3. cover                       — a capa DESTE objeto
#   4. acquisition                 — onde comprar. NÃO é evidência bibliográfica
#   5. provenance                  — de onde veio cada afirmação
#
# Campos sem verificação ficam `null`. Preencher sem pesquisa é inventar.
# ---------------------------------------------------------------------------
id: pub--<editora>--<titulo-curto>--<ano>
title_as_published: "<título como impresso na capa de rosto>"
publisher: <editora>
publisher_country: BR
series: null
year: null
language: pt-BR
bilingual: false
bilingual_pair: null            # ex.: grc-pt. Verificado no livro, nunca no título
editor: null
introduction_by: null
register: null                  # critical | academic | popular | escolar
framing: null                   # orientação da introdução, à parte da tradução
format: []                      # capa-dura | brochura | bolso
packaging: volume               # volume | caixa — o OBJETO é um tomo ou uma
                                # embalagem com vários? Separa "no mesmo volume"
                                # de "na mesma caixa" na interface.
pages: null
isbn13: null

availability_br: null           # em-catalogo | esgotado | importacao | usado
availability_checked: null      # juízo geral sobre ESTA edição ser obtenível
links:                          # referências BIBLIOGRÁFICAS (tiers 1–5)
  publisher: ""                 # página da editora
  catalogue: ""                 # catálogo de biblioteca nacional/universitária

verified_fields: []             # o que foi CHECADO, não o que foi suposto
research_status: not_researched
source_of_record: null          # voce | claude

# ---- 2 · a junção -----------------------------------------------------------
# Tradutor, texto-base, completude e veredito vivem AQUI, no par obra–publicação,
# porque variam entre as obras do mesmo volume.
# also_contains: obras do volume que NÃO estão em nenhuma coleção (sem registro
# de obra). Uma linha por obra: {title, author}. A página da edição as mostra,
# para que o conteúdo do livro físico apareça inteiro. interface-rules §8.
contains:
  - work: <work-id>
    verdict: unassessed         # recommended | alternative | rejected | unassessed
    reason: null
    translator: []
    translated_from: null       # direct | via:<lang> | unknown
    source_text: null
    completeness: null          # complete | abridged | selections
    apparatus: []

# ---- 3 · capa ---------------------------------------------------------------
# A capa é deste OBJETO, não da obra. Uma obra não tem capa.
# Omita o bloco inteiro quando não houver fonte confiável — ausência de capa
# não é defeito. Esquema em config/acquisition.yaml.
#
# cover:
#   file: covers/<publication-id>.jpg
#   source: "<URL ou descrição literal de onde a imagem veio>"
#   source_type: publisher      # publisher | catalogue | retailer | scan
#   represents: publication     # obrigatório, e sempre este valor
#   checked: <AAAA-MM-DD>
#   rights_note: "Imagem de capa usada como identificação bibliográfica da edição."

# ---- 4 · aquisição ----------------------------------------------------------
# Lista aberta de fontes. NÃO é evidência bibliográfica: vendedores são tier
# 6–7 e estabelecem apenas que o livro existe e pode ser comprado.
#
# `match_basis` é o campo que impede a fabricação: diz COMO se sabe que o
# anúncio é desta edição. Marketplaces fundem edições rotineiramente.
# `unconfirmed` guarda a pista e a interface não a apresenta como opção de
# compra desta edição.
#
# Omita o bloco quando não houver anúncio confiável. Isso não é defeito.
#
# acquisition:
#   - retailer: amazon-br       # ver retailers em config/acquisition.yaml
#     url: "<URL do anúncio, literal>"
#     listing_id: "<ASIN / ISBN do anúncio>"
#     match_basis: isbn13       # isbn13 | publisher-translator-year |
#                               # publisher-year | unconfirmed
#     match_note: "Como a correspondência foi estabelecida."
#     format_listed: brochura
#     price_band: null          # faixa, nunca preço exato. Desempate final
#     availability: em-catalogo
#     checked: <AAAA-MM-DD>
#     checked_by: claude

# ---- 5 · proveniência -------------------------------------------------------
provenance: []
#   - claim: "..."
#     source: "https://…"
#     source_tier: 1            # 1–5 bibliográfico · 6–7 só disponibilidade
#     retrieved: <AAAA-MM-DD>
#     confidence: verified      # verified | reported | inferred | unverified

updated: <AAAA-MM-DD>
---

## Avaliação

A prosa sobre esta publicação: o que a torna recomendável ou não, para cada
obra que ela contém. Disponibilidade e preço não entram aqui — são contexto,
não juízo.
