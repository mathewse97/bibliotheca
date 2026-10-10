# STATE.md — onde o trabalho está

Estado **operacional**: o que está em andamento, o que espera decisão, o que
ficou por fazer. Não é curadoria — a prosa curatorial vive em `review/`, as
lacunas em `review/gaps/`, as propostas em `review/structural/`. Este arquivo
é o resumo que faz alguém retomar sem reler tudo.

Não é uma segunda base de dados. Quando uma linha daqui divergir de um arquivo
canônico, **o arquivo canônico é o fato**.

**Atualizado em 2026-10-02.** Os números envelhecem; a contagem viva é a que
`python3 tools/build.py` imprime.

---

## Onde a biblioteca está

```
203 obras · 6 coleções · 154 publicações · 157 autores · 0 problemas
12 lacunas abertas · 5 obras sem coleção · 4 propostas estruturais (2 abertas)
```

Coleções: Política, Educação, Cultura, Religião, Cultura
Greco-Romana, Sobrevivência e Autossuficiência.

---

## Esperando decisão sua

A fila completa está em `review/decisions.yaml` e na tela **Decisões** da
interface — 12 itens. Os que têm consequência estrutural:

| o quê | onde | desde |
|---|---|---|
| Se uma regra deve proibir derivar o **propósito de um movimento** das obras que ele hoje contém | cartão `d-reg-proposito-movimento` | 2026-09-27 |
| O crescimento do movimento VII de Política (de 10 para 15 obras) pede subdivisão | registrado em `collections/political-thought.md` | 2026-09-28 |

---

## Pendências de pesquisa

- **Romances do movimento X: edições registradas em 2026-10-09** (Etapa 1).
  O caso difícil, Koestler, foi resolvido: a Sétimo Selo publicou em 2022
  *Escuridão ao meio-dia*, traduzida do manuscrito alemão redescoberto — não
  da versão inglesa de Daphne Hardy. Zamiátin e Huxley ficaram em cartão
  (`d-ed-zamiatin`, `d-ed-huxley`).
- **Lista original de Política ausente do repositório.** A coleção declara
  `archived_at: sources/lists/politica-formacao-geral.md`, mas o arquivo não
  foi enviado na migração (só as listas de Greco-Romana e Religião estão em
  `sources/lists/`). As `edition_pref` marcadas `by: voce` em Política não
  podem, por isso, ser conferidas contra o texto original. Se o Mathews tiver
  a lista, ela deve ser arquivada nesse caminho.
- **Curadoria das fotos de 2026-10-10 — duas decisões pendentes do Mathews.**
  Registradas: 11 obras (Bushcraft de Costa e Lorenzi e Matos em
  Sobrevivência; Cline em Greco-Romana; Ahrens em Educação; Krakauer, Leclerc,
  Stevenson, Defoe, London, Warburton e Cerbasi sem coleção, com
  pending_assignment). Pendentes: (1) *O Caibalion* — ele recusou a edição que
  tem; falta decidir se entra na edição comentada de Deslippe (Pensamento,
  2018) ou se não entra; (2) astronomia — *Turn Left at Orion* não cumpre o
  papel do *Manual do astrônomo* de Mourão (não ensina a construir
  telescópio); falta ele escolher. Não entraram, por decisão dele: Vasconcelos,
  Bukkyō Dendō Kyōkai, Mabbett (Pink Floyd), Christopherson, os dois Balbach,
  Da Vinci (Abril), O Pretoriano, Kleinman.
- **Relações ainda não escritas** para `dostoievski--besy`, `zamiatin--my` e
  `orwell--animal-farm`: nenhuma parceira defensável encontrada. Ausência
  honesta, não esquecimento.
- **Decidido em 2026-10-05:** Educação admite a ciência da aprendizagem
  (opção A de `d-edu-ciencia-aprendizagem`). Dehaene e Brown, Roediger e
  McDaniel entraram no movimento VIII novo. Ver `review/education.md` §11.
- **Classificação `work_type` pendente** em três obras — Hirsch, Brown/Roediger/
  McDaniel e Dehaene. O vocabulário tem cinco categorias do documento fundador
  e nenhuma descreve síntese de ciência empírica. Slug novo é decisão de
  classificação (`curation-rules.md` §6.8), não escolha de preenchimento.
- **Cinco conclusões `stale`** de revalidação (três em Educação, uma em
  Cultura, uma em Greco-Romana): a biblioteca mudou e parte da evidência
  deixou de valer. Nenhuma foi reexaminada.
- **ISBN do Dehaene não resolvido**: existem dois números válidos para a edição
  brasileira, `978-65-5541-165-2` e `978-65-5541-166-9`. O registro adotou o
  primeiro, que é o do objeto em papel nas livrarias, e guardou o outro.

---

## Decisões da migração para o Git — 2026-10-02

| decisão | quem | o quê |
|---|---|---|
| Repositório **público** | Mathews | Sabendo que o site do Pages é público na internet em qualquer plano fora do Enterprise Cloud, e que isso torna públicas também as fichas, a prosa de revisão e o estado pessoal |
| Capas **embutidas** no site | Mathews | As 118 capas continuam na interface publicada, como identificação bibliográfica |
| `_generated/` **fora** do repositório | claude, proposto | Derivado; versioná-lo somaria ~26 MB ao histórico por build |
| `Claude outputs/` fora, **sem apagar** | claude, proposto | Variante de interface nunca declarada canônica. Fica no disco à espera de decisão |
| Sem arquivo de licença | claude, proposto | Repositório público sem licença significa todos os direitos reservados, que é a postura certa enquanto houver 118 capas de terceiros embutidas |

---

## Frase de direitos das capas — corrigida em 2026-10-09

Os 118 registros que diziam "uso em acervo pessoal privado" em
`cover.rights_note`, mais o modelo `_TEMPLATE.md`, passaram a dizer
"Imagem de capa usada como identificação bibliográfica da edição." As capas
novas já entram com essa frase.

---

## O próximo passo

A migração para o GitHub está feita e o site publica pelo Actions. O cartão
`d-edu-ciencia-aprendizagem` foi decidido em 2026-10-05. Na fila de curadoria,
o próximo item estrutural é o cartão `d-reg-proposito-movimento`; a
classificação `work_type` de Hirsch, Dehaene e Brown, Roediger e McDaniel
continua devida.
