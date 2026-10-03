#!/usr/bin/env python3
"""
scaffold.py — cria as camadas canônicas que ainda não existiam.

NÃO é curadoria. Só transcreve o que já estava nas listas importadas:
título em português e autoria. Tudo o que exigiria pesquisa (título original,
data, período, tradição, forma, tipo) fica NULO e research_status fica
not_researched — a incerteza tem de ficar visível, não ser preenchida.

Idempotente: nunca sobrescreve um arquivo de obra que já exista.
"""
import os, io, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = "2026-09-05"

# (work_id, title_pt, [author_ids], source_collection)
WORKS = [
    # ---- Política — Formação Geral (sua lista, 40 obras) ----
    ("platao--politeia", "A República", ["platao"], "political-thought"),
    ("aristoteles--politika", "Política", ["aristoteles"], "political-thought"),
    ("tucidides--historiai", "História da Guerra do Peloponeso", ["tucidides"], "political-thought"),
    ("cicero--de-re-publica", "Da República", ["cicero"], "political-thought"),
    ("confucio--lunyu", "Os Analectos", ["confucio"], "political-thought"),
    ("sunzi--bingfa", "A Arte da Guerra", ["sunzi"], "political-thought"),
    ("kautilya--arthashastra", "Arthashastra", ["kautilya"], "political-thought"),
    ("ibn-khaldun--muqaddimah", "Muqaddimah / Os Prolegômenos", ["ibn-khaldun"], "political-thought"),
    ("agostinho--de-civitate-dei", "A Cidade de Deus", ["agostinho"], "political-thought"),
    ("aquino--de-regno", "Do Governo dos Príncipes", ["aquino"], "political-thought"),
    ("maquiavel--il-principe", "O Príncipe", ["maquiavel"], "political-thought"),
    ("hobbes--leviathan", "Leviatã", ["hobbes"], "political-thought"),
    ("locke--second-treatise", "Segundo Tratado sobre o Governo", ["locke"], "political-thought"),
    ("montesquieu--de-lesprit-des-lois", "O Espírito das Leis", ["montesquieu"], "political-thought"),
    ("rousseau--du-contrat-social", "Do Contrato Social", ["rousseau"], "political-thought"),
    ("burke--reflections-france", "Reflexões sobre a Revolução na França", ["burke"], "political-thought"),
    ("tocqueville--de-la-democratie-en-amerique", "A Democracia na América", ["tocqueville"], "political-thought"),
    ("mill--on-liberty", "Sobre a Liberdade", ["mill"], "political-thought"),
    ("mill--representative-government", "Considerações sobre o Governo Representativo", ["mill"], "political-thought"),
    ("marx-engels--manifest-kommunistischen-partei", "Manifesto do Partido Comunista", ["marx", "engels"], "political-thought"),
    ("marx--achtzehnte-brumaire", "O 18 de Brumário de Luís Bonaparte", ["marx"], "political-thought"),
    ("michels--zur-soziologie-des-parteiwesens", "Sociologia dos Partidos Políticos", ["michels"], "political-thought"),
    ("schmitt--der-begriff-des-politischen", "O Conceito do Político", ["schmitt"], "political-thought"),
    ("arendt--origins-of-totalitarianism", "Origens do Totalitarismo", ["arendt"], "political-thought"),
    ("popper--the-open-society", "A Sociedade Aberta e Seus Inimigos", ["popper"], "political-thought"),
    ("berlin--two-concepts-of-liberty", "Dois Conceitos de Liberdade", ["berlin"], "political-thought"),
    ("aron--lopium-des-intellectuels", "O Ópio dos Intelectuais", ["aron"], "political-thought"),
    ("dahl--on-democracy", "Sobre a Democracia", ["dahl"], "political-thought"),
    ("rawls--a-theory-of-justice", "Uma Teoria da Justiça", ["rawls"], "political-thought"),
    ("rothbard--anatomy-of-the-state", "Anatomia do Estado", ["rothbard"], "political-thought"),
    ("rothbard--the-ethics-of-liberty", "A Ética da Liberdade", ["rothbard"], "political-thought"),
    ("hoppe--democracy-the-god-that-failed", "Democracia, o Deus que Falhou", ["hoppe"], "political-thought"),
    ("dostoievski--besy", "Os Demônios", ["dostoievski"], "political-thought"),
    ("zamiatin--my", "Nós", ["zamiatin"], "political-thought"),
    ("huxley--brave-new-world", "Admirável Mundo Novo", ["huxley"], "political-thought"),
    ("koestler--darkness-at-noon", "O Zero e o Infinito", ["koestler"], "political-thought"),
    ("orwell--animal-farm", "A Revolução dos Bichos", ["orwell"], "political-thought"),
    ("orwell--nineteen-eighty-four", "1984", ["orwell"], "political-thought"),
    ("orwell--politics-and-the-english-language", "A Política e a Língua Inglesa", ["orwell"], "political-thought"),
    # weber--politik-als-beruf já existe como arquivo próprio
    # ---- Educação (sua lista, 9 obras) ----
    ("marrou--histoire-de-leducation-dans-lantiquite", "História da Educação na Antiguidade", ["marrou"], "education"),
    ("nunes--historia-da-educacao-na-antiguidade-crista", "História da Educação na Antiguidade Cristã", ["nunes"], "education"),
    ("nunes--historia-da-educacao-na-idade-media", "História da Educação na Idade Média", ["nunes"], "education"),
    ("nunes--historia-da-educacao-no-renascimento", "História da Educação no Renascimento", ["nunes"], "education"),
    ("nunes--historia-da-educacao-no-seculo-xvii", "História da Educação no Século XVII", ["nunes"], "education"),
    ("adler--the-paideia-proposal", "A Proposta Paidéia", ["adler"], "education"),
    ("mcluhan--the-classical-trivium", "O Trivium Clássico", ["mcluhan"], "education"),
    ("miriam-joseph--the-trivium", "O Trivium: as artes liberais da lógica, da gramática e da retórica", ["miriam-joseph"], "education"),
    ("bauer-wise--the-well-trained-mind", "The Well-Trained Mind: A Guide to Classical Education at Home", ["bauer", "wise"], "education"),
]

AUTHORS = [
    ("platao", "Platão"), ("aristoteles", "Aristóteles"), ("tucidides", "Tucídides"),
    ("cicero", "Cícero"), ("confucio", "Confúcio"), ("sunzi", "Sun Tzu"),
    ("kautilya", "Kautilya"), ("ibn-khaldun", "Ibn Khaldun"),
    ("agostinho", "Santo Agostinho"), ("aquino", "Tomás de Aquino"),
    ("maquiavel", "Nicolau Maquiavel"), ("hobbes", "Thomas Hobbes"),
    ("locke", "John Locke"), ("montesquieu", "Montesquieu"),
    ("rousseau", "Jean-Jacques Rousseau"), ("burke", "Edmund Burke"),
    ("tocqueville", "Alexis de Tocqueville"), ("mill", "John Stuart Mill"),
    ("marx", "Karl Marx"), ("engels", "Friedrich Engels"),
    ("weber", "Max Weber"), ("michels", "Robert Michels"),
    ("schmitt", "Carl Schmitt"), ("arendt", "Hannah Arendt"),
    ("popper", "Karl Popper"), ("berlin", "Isaiah Berlin"),
    ("aron", "Raymond Aron"), ("dahl", "Robert Dahl"), ("rawls", "John Rawls"),
    ("rothbard", "Murray Rothbard"), ("hoppe", "Hans-Hermann Hoppe"),
    ("dostoievski", "Fiódor Dostoiévski"), ("zamiatin", "Yevgeny Zamiátin"),
    ("huxley", "Aldous Huxley"), ("koestler", "Arthur Koestler"),
    ("orwell", "George Orwell"), ("marrou", "Henri-Irénée Marrou"),
    ("nunes", "Ruy Afonso da Costa Nunes"), ("adler", "Mortimer Adler"),
    ("mcluhan", "Marshall McLuhan"), ("miriam-joseph", "Irmã Miriam Joseph"),
    ("bauer", "Susan Wise Bauer"), ("wise", "Jessie Wise"),
    ("suassuna", "Ariano Suassuna"), ("vargas-llosa", "Mario Vargas Llosa"),
    ("scruton", "Roger Scruton"),
]

WORK_TMPL = """---
id: {wid}
id_aliases: []
title_pt: "{title}"
title_original: null            # a pesquisar (§E)
title_en: null
alt_titles: []
authors: [{authors}]
original_language: null
form: null                      # book | essay | lecture | dialogue | treatise | novel …
work_type: null                 # primary-source | political-theory | … (§E)
date_written: null
date_sort: null
period: null
traditions: []
subjects: []

research_status: not_researched
priority_library: null          # curatorial; ★ da lista é escopo de coleção, não daqui
obsidian_notes: []

relations: []
provenance: []

derived_from:
  source: bootstrap-import
  collection: {coll}
  transcribed: [title_pt, authors]
  note: "Título e autoria vieram da sua lista. Tudo o mais está nulo de
         propósito: preencher sem pesquisa seria inventar."
updated: {date}
---

## Fatos

Não pesquisado. Nada neste registro foi verificado.

## Avaliações acadêmicas

—

## Síntese

—
"""


def w(path, content, overwrite=False):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    if os.path.exists(full) and not overwrite:
        return False
    with io.open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def main():
    created = skipped = 0
    for wid, title, authors, coll in WORKS:
        body = WORK_TMPL.format(wid=wid, title=title.replace('"', "'"),
                                authors=", ".join(authors), coll=coll, date=DATE)
        if w("works/%s.md" % wid, body):
            created += 1
        else:
            skipped += 1

    lines = ["# Normalização de nomes. Um registro por pessoa.",
             "# name_display é o nome como aparece nas suas listas.", ""]
    for aid, name in AUTHORS:
        lines.append("%s:" % aid)
        lines.append('  name_display: "%s"' % name)
        lines.append("  name_variants: []")
        lines.append("  dates: null                 # a pesquisar")
        lines.append("  note: null")
        lines.append("")
    w("people/authors.yaml", "\n".join(lines), overwrite=True)

    w("config/writable-fields.yaml", WRITABLE, overwrite=True)
    w("state/personal.yaml", STATE)
    print("obras criadas: %d | já existiam: %d | autores: %d"
          % (created, skipped, len(AUTHORS)))


WRITABLE = """# ---------------------------------------------------------------------------
# A LISTA BRANCA DE ESCRITA.
# A interface só pode escrever campos declarados aqui, e só no arquivo
# indicado. Nada fora desta lista é editável pela interface em nenhuma
# circunstância — nem por engano, nem por um toque distraído no telemóvel.
#
# Acrescentar um campo editável no futuro é acrescentar uma linha aqui.
# A interface lê este arquivo e desenha os controles a partir dele; não há
# nenhuma lista de campos codificada na interface.
# ---------------------------------------------------------------------------
version: 1
state_file: state/personal.yaml

targets:

  # Estado de LEITURA pertence à OBRA — você lê uma obra, não um volume.
  work:
    key: works
    fields:
      - name: reading_status
        label_pt: "Leitura"
        type: enum
        values: [nao-lido, lendo, lido, relendo, abandonado]
        default: nao-lido
      - name: started
        label_pt: "Início"
        type: date
      - name: finished
        label_pt: "Conclusão"
        type: date
      - name: priority_personal
        label_pt: "Prioridade sua"
        type: enum
        values: [alta, media, baixa, nenhuma]
        note: "Sua. Distinta de priority_library, que é curatorial e não é
               editável aqui."
      - name: note_ref
        label_pt: "Nota no Obsidian"
        type: string
        note: "Apenas um caminho. A interface nunca lê nem escreve o conteúdo
               da nota."

  # POSSE pertence à PUBLICAÇÃO — você compra um objeto físico, e esse objeto
  # pode conter várias obras. Consequência direta da separação obra/publicação.
  publication:
    key: publications
    fields:
      - name: ownership
        label_pt: "Posse"
        type: enum
        values: [nenhum, quero-comprar, encomendado, tenho, dispensei]
        default: nenhum
      - name: acquired
        label_pt: "Adquirido em"
        type: date
      - name: acquired_where
        label_pt: "Onde"
        type: string

# Campos explicitamente NÃO editáveis pela interface, por serem curatoriais
# ou bibliográficos. Ficam aqui nomeados para que a fronteira seja legível:
locked:
  - "tudo em works/ exceto o que está acima"
  - "tudo em collections/ — sequência, papel, why_here, movimentos, caminhos"
  - "tudo em publications/ — editora, tradutor, ISBN, veredito"
  - "review/ e review/gaps/ — lacunas, necessidade, contexto"
"""

STATE = """# Estado pessoal. O ÚNICO arquivo que a interface escreve.
# Nenhum arquivo bibliográfico ou curatorial é tocado por ela.
works: {}
publications: {}
"""

if __name__ == "__main__":
    main()
