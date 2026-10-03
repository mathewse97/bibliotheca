---
kind: fonte-histórica-arquivada
document: "Bibliotheca Blueprint — Architecture proposal · 5 September 2026"
archived: 2026-09-06
archived_by: claude
provided_by: voce
precedence: 4
sections_archived: [C, E, F, I]
sections_not_archived: [A, B, D, G, H, J]
---

# Blueprint da Bibliotheca — seções C, E, F e I

**Isto é uma fonte histórica arquivada. NÃO é regra canônica.**

Este documento é o blueprint original da Bibliotheca. Ele viveu fora do
repositório e foi por isso que as seções `§C`, `§E`, `§F` e `§I` — citadas por
cerca de sessenta arquivos daqui — não resolviam. O Mathews forneceu-o em
2026-09-06 como material histórico para recuperação, e ele está arquivado aqui
para que cada citação `[recuperado do blueprint]` nas regras canônicas aponte
para um texto que existe dentro da biblioteca, e não para uma conversa.

## Precedência — leia antes de usar qualquer coisa daqui

Ordem estabelecida pelo Mathews em 2026-09-06:

1. Decisões diretas dele e regras aprovadas posteriores.
2. Dados canônicos atuais e arquitetura implementada.
3. `config/curation-rules.md` e a demais documentação atual.
4. **Este blueprint** — apenas para recuperar regras historicamente perdidas.
5. Inferência do agente, e só quando marcada como inferência.

Uma regra atual **não é substituída** porque este documento diz outra coisa.

## O que aqui já foi superado — não aplicar

| Neste documento | O que vale hoje |
|---|---|
| §F passo 4: "Portuguese, then Spanish, Italian, English" | **Superado** pela clarificação do Mathews de 2026-09-06. A hierarquia não é uma sequência fixa. Ver `config/bibliographic-rules.md` §F |
| §I, exemplo de registro de lacuna: `severity:` | O campo é `necessity`, com `context` separado — correção posterior. O próprio blueprint já usa `necessity` na sua prosa; só o exemplo ficou para trás |
| §I: registros de lacuna em `review/gaps/<colecao>.md` | São `.yaml`, com evidência `{claim, check}` revalidada a cada build — extensão posterior |
| §C: `state/personal.yaml` com a chave `editions:` e valores em inglês (`unread`, `reading`…) | A chave é `publications:` e os valores são portugueses, em `config/writable-fields.yaml` |
| §C: `ownership` com quatro valores | São cinco, com `nenhum` como padrão |
| §B: `vocab/`, `config/schema.yaml`, `review/pending.md`, `review/coverage.md` | Arquitetura nunca construída assim. Ver `README.md` §1 |

Uma observação sobre a idade do documento: apesar do cabeçalho "5 September
2026 · not yet built", ele **já incorpora** várias correções pós-importação —
critérios derivados da pergunta, `scope_map`, `structural_changes`, ★ contra
caminho, `pending_assignment`, a emenda de identificadores, `demand` na
participação, a ordem do arquivo como sequência. É um documento vivo, revisado
depois dos primeiros imports, e é por isso que concorda tanto com o cânone
atual.

## O que não foi arquivado

As seções **A** (diagnóstico), **B** (arquitetura), **D** (coleções como
currículos), **G** (interface), **H** (manutenção) e **J** (exemplo) não estão
aqui: nenhuma regra canônica as cita, e o `README.md` e o `curation-rules.md`
descrevem a arquitetura como ela de facto ficou. O documento completo está com
o Mathews.

---
---

# C · Data model

Five entities. Two get their own files, one is embedded, one is a vocabulary,
one is a junction.

| Entity | Lives in | Why there |
|---|---|---|
| **Work** | One file per work | The intellectual unit, and the anchor of identity. Not necessarily a book — a book, essay, lecture, speech, dialogue or treatise. Independent of language, translation and physical publication. |
| **Publication** | One file per publication | A physical object: this publisher, this translator, this year, this ISBN. It may contain several works, so it cannot live inside any one of them. Corrected — see below. |
| **Collection** | One file per collection | Holds its own description, intellectual question, ordered membership and declared tensions. |
| **Membership** | Entries in the collection's sequence | The junction, and the curriculum. It carries role, local prerequisites, demand and the argument for the placement — so it must be a thing, not a tag. Its order in the file is the reading order; no work anywhere holds a position number. See §D. |
| **Person** | `people/authors.yaml` | Authors and translators need normalised names and variants, but rarely need a document. Promote one to a file only when you want an essay about them. |

## Identity

Work ids are `<author-surname>--<short-title>`, lowercase ASCII, using the
original-language title: `platao--politeia`, `aristoteles--politika`,
`hobbes--leviathan`, `tocqueville--de-la-democratie-en-amerique`.

The original title is the only name that stays constant across every
translation you will ever consider — which is precisely what an identifier must
do. Amended after the first import: where an original title is unstable or
shared, the convention falls back to the standard scholarly short title.
Thucydides and Herodotus both wrote Ἱστορίαι; four of the first forty works
needed the fallback. Original title when stable and unambiguous, conventional
short title otherwise, `id_aliases` always. Portuguese titles vary between
publishers; English titles are a translation choice like any other. Ids are
never reused; a rename records the old value in `id_aliases`, and the validator
fails loudly on any dangling reference.

Publications get their own id space, since they no longer hang off a single
work: `pub--<publisher>--<short-title>--<year>`. Permanent, never recycled — a
rejected publication keeps its id so the rejection stays attached to something.

## The publication record — a correction

The first draft embedded editions inside the work file. The justification was
that an edition has no meaning apart from its work — and that justification was
simply wrong. A physical publication can carry several works: *Ciência e
Política* is two lectures, *Quatro Ensaios sobre a Liberdade* is four essays, an
Orwell collection is dozens. Embedding would mean storing the same book once
inside each work it contains, which is precisely the duplication this whole
architecture exists to prevent.

So publication becomes its own entity, and the relation is many-to-many: one
publication holds many works, one work appears in many publications. This is the
same shape as collection membership, and it wants the same treatment — a
junction that carries attributes. The recommendation verdict belongs on the
pair, not on the publication, because a volume can be the right vehicle for one
work it contains and the wrong one for another.

The cost is real and worth stating: a work with one edition now needs two files
instead of one. I accept that cost because the alternative is a model whose
shape depends on a fact that can change the day you add a second essay from the
same volume.

## Why `verdict: rejected` is a first-class value

You asked to track editions you rejected. Keeping the rejection on the
work–publication pair, with its reason, means the decision is made once. Next
year, when that edition surfaces again in a search, the record already says
"abridged, and translated via French — rejected 2026-09". Without this, every
rejected edition is silently reconsidered forever, which is the single most
wasteful failure mode of a library like this.

## Relations

A closed vocabulary, stored once, on the source work. The generator derives the
inverse — so `responds_to` automatically produces "responded to by" on the
target. Storing both directions by hand is how relation graphs become
self-contradictory.

| Type | Derived inverse | Use for |
|---|---|---|
| `prerequisite_for` | `requires` | Real dependency: you cannot follow B without A |
| `responds_to` | `answered_by` | Direct engagement with a named predecessor |
| `criticizes` | `criticized_by` | Sustained attack, not passing disagreement |
| `continues` | `continued_by` | Sequels and completions |
| `influenced_by` | `influenced` | Acknowledged formative debt |
| `same_tradition_as` | (symmetric) | Use sparingly — `traditions:` usually covers it |
| `opposing_tradition_to` | (symmetric) | The §20 relation. Structural disagreement, not personal |
| `complements` | (symmetric) | Better read together than apart |
| `literary_treatment_of` | `treated_literarily_by` | Orwell to the theory of totalitarianism |
| `primary_source_for` | `interprets` | Links a source to its commentary |
| `commentary_on` | `has_commentary` | Explicit scholarly commentary |
| `part_of` | `has_part` | A work inside a larger authored work — a volume of a multi-volume work. Not for an essay in a publisher's anthology: that is a publication holding several works, and it is a different relation entirely |

## Classification dimensions — what earns a field

| Dimension | Verdict | Reasoning |
|---|---|---|
| Collection | Keep — junction | Curated, ordered, many-to-many. The spine of the system. |
| Subject | Keep — many per work | Cheap, validated against a vocabulary, answers cross-cutting questions. |
| Period | Keep — one per work | Fixed ladder. Makes chronological views and historical-gap analysis possible. |
| Tradition | Keep — 0–2 per work | The dimension that keeps disagreement visible. Without it, §20 has no mechanism. |
| Work type | Keep — one per work | Primary source / theory / sociology / literature / commentary. Drives balance analysis. |
| Form | New — one per work | Book, essay, lecture, speech, dialogue, treatise, novel, play. Separate from work type, which is the intellectual kind. Collapsing the two is exactly what forces every intellectual unit to be a "book", and it is why Weber's two lectures nearly became one record. |
| Role | Keep — on the membership, not the work | *Leviathan* is foundational in Political Thought and a primary source in a Modernity collection. Roles are relative to a collection, so a per-work field would be simply false. |
| Priority | Keep — but split in two | `priority_library` (curatorial, mine) and `priority_personal` (your intent, yours). Merging them means my judgement silently overwrites yours. |
| Reading status | Keep — personal state | Cheap, and it is what turns a reading sequence from a diagram into a plan. |
| Difficulty | Drop as a work field — keep as `demand` on the membership | A global difficulty number is subjective and unstable. But difficulty is real and it is relative to where you are in a curriculum: Aristotle after Plato is demanding, Aristotle after nothing is punishing. |
| Importance score | Drop | Meaningless across domains, and it invites false precision. Role plus priority already carries the signal. |

---

# E · Research workflow

What happens when you type "Leviathan".

1. **Resolve, don't guess.** Match the string against ids, aliases, original and
   translated titles. One match, proceed. Several, ask. None, offer to create
   the work and run the full curation pipeline in §H.
2. **Load what already exists.** Prior research, prior verdicts, previously
   rejected editions and their reasons, your notes, current collection
   memberships, existing relations. Research never starts from zero, and never
   silently repeats a decision you already made.
3. **Establish the bibliographic facts.** Original language, date and
   circumstances of composition, textual transmission, and the standard critical
   edition of the original text. These go under `## Fatos`.
4. **Enumerate candidates** across Portuguese, Spanish, Italian and English,
   plus original-language and bilingual options. Enumerate before judging — the
   ranking comes later, and letting it come early is how a language preference
   quietly becomes a filter.
5. **Verify field by field.** Publisher pages, national library catalogues
   (Brazil's ISBN agency, BNP, BNE, BNCF, LoC, DNB), university catalogues,
   WorldCat. Each verified field is recorded as verified; each unverified field
   is recorded as unverified. Bilingualism is confirmed from a catalogue or a
   page description, never inferred from a Greek word in the title.
6. **Assess quality.** Translator's credentials, which source text was used,
   direct versus intermediary translation, completeness, apparatus, the
   introduction, scholarly reception where it exists. These go under
   `## Avaliações acadêmicas`, attributed.
7. **Check Brazilian availability** and the physical format, with the date of
   the check recorded — availability is the fastest-decaying fact in the whole
   system.
8. **Apply the §F framework** and write verdicts onto the editions, including
   rejections with reasons.
9. **Write the fit.** What this prepares, what answers it, which works in your
   library contest it, where it sits in each sequence, what gap it fills. Under
   `## Lugar na biblioteca`.
10. **Set status, record provenance, commit.** Every claim gets a source, a tier
    and a retrieval date.

## Source tiers

Your hierarchy, stored on every claim as `source_tier`:

1. publisher and scholarly edition information
2. university library catalogues
3. national libraries
4. scholarly databases and reviews
5. original-language bibliographic sources
6. reputable booksellers, for availability only
7. retailers, for purchasing verification only

Tiers 6 and 7 can establish that a book exists and can be bought. They can never
establish that it is good. A retailer's review count is not evidence and will
not appear in an assessment.

## Four assumptions this workflow refuses to make

Popularity is not quality. A distinguished publisher's imprint is not a
guarantee about this translator — imprints are uneven, and the claim to check is
the translator's, not the house's. A newer translation is not automatically
better than an older one; several standing translations are old and unsurpassed,
and several recent ones are commercial reissues of public-domain text. And a
Greek or Latin title on a cover is not evidence of a bilingual edition. Each of
these is checked against a source or recorded as unverified.

```yaml
- claim: "Tradução direta do grego; texto-base é a OCT de Ross."
  source: "https://…"
  source_tier: 1
  retrieved: 2026-09-05
  confidence: verified        # verified | reported | inferred | unverified
```

## When is a work "fully researched"

You asked that this not be a box I tick to feel finished. It is a checklist, and
all of it must hold: original language, date and transmission established · at
least one candidate examined in each language tier that has one · for the
recommended edition, publisher, translator, year, format, ISBN, completeness,
source text and direct-versus-intermediary all verified against tier 1–5 ·
apparatus and introduction assessed · Brazilian availability checked and dated ·
rejected candidates recorded with reasons · every claim sourced.

Anything short of that is `partially_researched`, with the missing items named.
A work whose availability was last checked more than a year ago goes to
`needs_review` automatically — the assessment is still good, the shopping
information is not.

---

# F · Edition-selection framework

A decision procedure, run in this order. The order is the argument: gates first,
quality second, language third. Your language hierarchy is powerful but it is a
tiebreaker, and running it earlier would let a mediocre Portuguese edition beat
a decisive English one — which is precisely the outcome you told me to avoid.

1. **Gate: textual adequacy.** Complete unless you asked for selections; based
   on a defensible source text; translated directly from the original when any
   direct translation exists. An edition translated through an intermediary
   language is rejected whenever a direct one is available, in any language.
   Failures are recorded as `rejected` with the reason, not quietly dropped.
2. **Gate: physical existence.** It must be a physical book you can obtain. If
   the best scholarly edition exists only electronically, that is stated in the
   open, never substituted silently.
3. **Rank the survivors on merit.** Scholarly authority of translator and
   editor; fidelity; apparatus; quality of the introduction; readability;
   register. This produces quality bands, not a single winner.
4. **Now apply language preference — within a band.** *(Portuguese, then
   Spanish, Italian, English.)* It decides between editions of comparable
   quality and nothing else. When the best Portuguese edition sits a band lower,
   the superior edition wins and I show you the trade-off explicitly rather than
   announcing a conclusion.
   **⚠ A formulação entre parênteses foi SUPERADA em 2026-09-06. Ver
   `config/bibliographic-rules.md` §F.**
5. **Ancient Greek rule.** A bilingual Greek–Portuguese edition is preferred
   within its band, never for being bilingual. When the best bilingual edition is
   weak, the better answer is almost always two books: the superior reading
   edition, plus an inexpensive facing-text or Greek-only text (an OCT, a
   Teubner, a Loeb) as your study companion. That serves your Greek better than a
   compromised translation would, and it costs less than it sounds. Same
   reasoning for Greek–English.
6. **Disclose framing separately.** The orientation of an introduction or
   accompanying essays is recorded as its own field and never blended into
   translation quality. An excellent edition with a strongly positioned
   introduction stays excellent — you are simply told. Framing disqualifies an
   edition only when it contaminates the text itself: tendentious renderings,
   silent excisions, an apparatus that argues instead of informing.
7. **Output only the verdicts that genuinely differ.** Best overall scholarly
   edition, best Portuguese edition, best practically obtainable in Brazil. When
   two coincide, they are reported as one. No manufactured alternatives.

## Your stated priority order, encoded

scholarly quality → translation quality → textual reliability → editorial
quality → suitability for your languages → physical availability → price. Steps
1–3 cover the first four, step 4 the fifth, step 2 the sixth. Price appears only
as a band, and only as a tiebreaker of last resort — which is what
"approximately this order" ought to mean in practice.

---

# I · Curation and gap analysis

The library is not a catalogue of the books you have already chosen. Keeping
each curriculum intellectually complete is a standing responsibility of the
system, and it needs its own machinery.

It also has an obvious failure mode, and the whole design of this section is
aimed at it: an assistant that produces plausible book lists forever.
Suggestions are cheap to generate and expensive to evaluate, so a system that
emits them freely quietly transfers all the work to you. Three rules prevent
that.

## 1 · A gap is defined against the collection's own criteria

Nothing is missing in the abstract. A work is missing only relative to a
question a collection has declared and criteria it has stated — which is why
`inclusion_criteria` from §D is load-bearing rather than decorative. Without it,
"gap" collapses into "book I happened to think of", and there is no principled
way to tell the two apart.

## 2 · Detection is structural, not generative

Candidates are proposed only where the library's own graph shows a hole. Each
gap type has a signal in the data, and the signal comes first — the argument
second.

| Gap type | Signal in the data | Judgement needed |
|---|---|---|
| Dangling interlocutor | A `responds_to`, `criticizes` or `opposing_tradition_to` edge whose target is not in the library | None to detect. The library already asserts the work matters |
| Broken prerequisite | A `requires:` pointing at a work absent from the collection | None to detect — either add the work or the dependency was a universal claim in disguise |
| One-sided tradition | A tradition that appears only as the target of `opposing_tradition_to` and never as a work's own `traditions:` | Low. The count is mechanical; which work best represents the tradition is not |
| Orphan foundational | A `role: foundational` work with no `critical-response` anywhere in the same collection | Low. Some foundations genuinely have no serious answer in scope |
| Period discontinuity | A span inside the collection's period range with no member | Medium. A silence can be deliberate |
| Type monoculture | `work_type` distribution skewed past a threshold — all theory and no empirical, historical or literary treatment | Medium. Some questions really are purely theoretical |
| Unanswered movement | A movement whose stated purpose is not achievable by the works it contains | High. This one is genuinely mine to argue |

Two of these are fully computable, four are computable as a flag that then needs
judgement, and one is judgement supported by counts. None of them is "here are
ten more books about politics." That distinction is the entire point of the
table.

## 3 · Four verdicts, and only one produces a proposal

| Verdict | Meaning | What happens to it |
|---|---|---|
| Genuine gap | An absence that weakens the collection's intellectual completeness | A proposal, with a full placement attached. Surfaced. |
| Complementary | Valuable, but the collection is not incomplete without it | Recorded against the gap as a considered candidate. Not proposed. |
| Enriching | Interesting; does not belong to the core curriculum | Kept in a per-collection list you can open when you want more. Never surfaced unprompted. |
| Redundant | A good or famous book whose contribution the library already covers | Recorded permanently, with the reason and the works that cover it. |

The fourth verdict is the least obvious and the most useful. A recorded
redundancy works exactly like `verdict: rejected` on an edition: it stops a
decision being silently reopened. "We considered Rawls's *Political Liberalism*;
the library already carries its contribution through *A Theory of Justice* and
the Rothbard–Nozick exchange" is a durable fact about your library, and writing
it down means neither of us reconsiders it every year.

## Two rules that keep the volume honest

**No gap record, no recommendation.** Every proposal must name the gap it
closes, by id. A book I merely find interesting has nowhere to go — there is no
field for it. That single constraint removes most of the noise before it is
written.

**Coverage and proposals are different outputs, and only one is capped.**
Coverage reports the scope map — every region, with its state — and is uncapped,
because the map is the map and a broad collection honestly has many empty
regions. Proposals name specific works to add, and stay capped at three. Without
that split, broadening a collection's scope would produce a flood of suggestions
and the cap would have to be abandoned; with it, Education can report seven
absent regions while still putting only three books in front of you.

**Three open proposals per collection, maximum.** A budget forces ranking. If a
fourth candidate matters more than one already open, something must be closed or
demoted first — which is a harder and far more useful question than "is this book
good?" Nearly every book worth proposing is good; the question is whether it is
more necessary than the three already waiting.

## The strongest opponent, not the most convenient one

Where a collection holds a position without its opposition, the work to propose
is the best available statement of the other side, not the easiest one to argue
against. Recommending a weak critic is worse than recommending nothing: it lets
a collection look balanced while remaining one-sided, and it is the exact
mechanism by which a library flatters its owner. This applies in both directions
and regardless of which side the collection currently leans.

## Necessity is not relevance

Two axes, two fields, and only one of them ranks. `necessity` measures how much
the collection's argument weakens without the work, and it comes from the
structural signal. `context` records availability in Brazil, language, cultural
proximity, local salience — and never sets priority. It breaks a tie between
candidates of equal necessity, exactly as the language hierarchy in §F decides
within a quality band and never across bands: the same principle applied at two
levels, work and edition. A book does not rise because it is easy to buy in
Portuguese, and does not fall because it is hard to find.

What this prevents is subtle enough to be worth naming, because it would never
announce itself: a library slowly reshaping itself around what its owner's
market happens to stock, with every individual decision looking perfectly
reasonable at the time.

## A proposal is a placement, not a title

Each candidate arrives with everything needed to judge it as a decision rather
than as a suggestion: which collections it belongs to, its role in each, its
priority, where it enters the sequence, its prerequisites, its relations to works
already present, and why it is preferable to the alternatives considered. A work
with no obtainable edition in your languages is flagged as such at proposal time,
since that changes whether the proposal is actionable at all. Accepting one is a
single decision, and it feeds straight into the §H pipeline.

```yaml
# review/gaps/political-thought.md — an open gap record
- id: political-thought--g03
  type: one-sided-tradition
  severity: alta                # ← superado: o campo é `necessity`
  statement: "A coleção contém três críticas ao marxismo e nenhuma
              exposição marxista de primeira mão. A tradição aparece
              somente pelos seus adversários."
  evidence:
    - "marxismo: 3× como alvo de opposing_tradition_to,
       0× como tradição própria de uma obra da coleção."
  candidates:
    - work: marx--das-kapital
      verdict: gap-filler
      argument: "… fundamentado, com fontes …"
      over: "O Manifesto é mais lido, porém insuficiente como exposição
             da teoria — panfleto, não argumento."
      placement:
        collection: political-thought
        after: tocqueville--de-la-democratie-en-amerique
        role: foundational
        requires: […]
        demand: exigente
        priority_library: core
    - work: …
      verdict: complementary
      argument: "… por que não fecha a lacuna sozinho …"
  status: open              # open | proposed | accepted | dismissed
  raised: 2026-09-05
```

## Redundancy in the other direction

The same analysis runs inwards: two works covering the same contribution where
one would do, a member that no longer meets its collection's stated criteria, a
period or tradition carrying disproportionate weight. The output is a demotion
or removal proposal with an argument. Nothing is ever removed, demoted or
reordered without your decision.

## A work may legitimately belong to no collection

Coverage flags works that sit in no collection, because an orphan is usually a
mistake. Sometimes it is not: a work can be correctly in the library and
correctly waiting — the second Weber lecture belongs to Education or Culture, and
neither has been imported yet. Left undeclared, that work would be flagged as an
orphan on every run, forever, and a check that cries wolf is a check you learn to
ignore.

So the state gets declared rather than inferred: `pending_assignment` records why
the work has no collection, which collections are candidates, and the condition
under which the question becomes answerable. It exempts the work from the orphan
check until then — and the moment the condition is met, it becomes a real
question again rather than a permanently silenced one.

## A gap found in one collection is provisional

Coverage analysis over a single collection produces false positives, because part
of what looks absent will be sitting in a collection not yet imported — and a
work already in the library needs a new membership, not a purchase. So a gap
raised before library-wide coverage exists carries `recheck_after`, a deferral
condition rather than a date, and stays open until it has been re-tested against
the whole library. Nothing is proposed for acquisition on the strength of one
collection's view of itself.

## When it runs

Automatically as a check after any structural change to a collection, and as a
deliberate audit whenever you ask for one. Findings accumulate in `review/gaps/`.
They do not interrupt, they do not edit, and they are there when you want them —
which is the difference between a system that curates and one that nags.
