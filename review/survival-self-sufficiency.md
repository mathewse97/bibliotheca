---
collection: survival-self-sufficiency
kind: import-report + avaliação curatorial
by: claude
date: 2026-09-06
status: "importada com as 11 obras da lista original. Em 2026-09-06 duas
         entraram por decisão sua, Strategic Relocation e Primeiros
         Socorros; uma foi registrada sem coleção, Dark Secrets of
         SHTF Survival; e uma saiu sem registro. Hoje são 13 obras."
---

# 1 · Relatório de importação

**12 entradas → 11 obras.** Uma descartada por decisão sua. Seis seções suas →
seis regiões e cinco movimentos.

| O que li | Resultado |
|---|---|
| Entradas | 12, das quais uma descartada |
| «Faça você mesmo (duas edições)» | **Descartada** (decisão sua, 2026-09-06). Sem registro de obra nem de publicação. Em `excluded` |
| Seções | 6 cabeçalhos seus, incluindo um vazio |
| Autoria | 4 entradas vieram sem autor; todas resolvidas por pesquisa |
| Publicações criadas | 9 nesta coleção — 4 escolhidas por você, 5 identificadas pela pesquisa |
| Lacunas registradas | **nenhuma** |
| Obras propostas | **nenhuma** |

Esta é a primeira importação feita inteiramente sob o §6.0: pesquisar antes de
perguntar. Nenhuma pergunta foi feita antes da pesquisa, e a única decisão que
lhe foi devolvida — as duas edições de «Faça você mesmo» — chegou-lhe depois de
esgotada a busca, e você resolveu-a descartando a entrada.

## 1.1 O que a pesquisa corrigiu

Três suposições óbvias que teriam entrado erradas se a lista fosse aceite como
está:

**Werner — o original é ESPANHOL.** `Donde no hay doctor` (1970) veio primeiro;
o inglês `Where There Is No Doctor` é tradução e adaptação. Pelo §C o id sai do
título original, e seria `werner--where-there-is-no-doctor` — errado — se eu
tivesse assumido o inglês.

**Van Lengen — o original também é ESPANHOL.** `Manual del arquitecto descalzo`,
escrito e publicado no México. O autor é neerlandês, o que torna a suposição
fácil e errada nos dois sentidos.

**Canterbury — «manual do mundo» não era coautoria da obra.** Era informação de
EDIÇÃO num campo de autoria — o mesmo padrão de «McLuhan; Hugo Langone» em
Educação. O Manual do Mundo é coautor da **adaptação brasileira**, e por isso
está na publicação e não na obra.

E quatro autorias que a sua lista não trazia foram estabelecidas, nenhuma
suposta: Lontro e Monteiro (Mini Manual), Kinupp e Lorenzi (PANC), NAEMT
(PHTLS), Pellegrini e Moraes já vinham.

---

# 2 · A estrutura, e por que ela é diferente das outras três

## 2.1 `sequence_kind: thematic` — o primeiro do acervo

Política, Educação e Cultura organizam **argumentos**, e a ordem nelas carrega
dependência intelectual: ler Adler antes de Marrou estraga Adler. Esta organiza
**domínios de competência**, e ler defesa antes de medicina não estraga nada.

O valor `thematic` existe no vocabulário recuperado do blueprint e nunca tinha
sido usado. É o que descreve isto sem forçar nada.

## 2.2 As regiões são SUAS — e é a primeira vez

Nas outras coleções o `scope_map` é meu: eu desenhei as regiões. Aqui os seis
nomes são os seus seis cabeçalhos. Eu não inventei território — **li os seus
cabeçalhos como território**, e essa leitura é a única que explica por que
`Energia:` foi escrita e deixada vazia.

O que é meu está marcado `reading_by: claude`; os nomes estão marcados
`regions_by: voce`. A distinção não é cosmética: significa que a análise de
cobertura desta coleção mede contra um mapa que você declarou, e não contra um
que eu propus.

## 2.3 Energia — a região que a lista mais informa

`coverage: absent`, `pursuit: open`, sem movimento. Um movimento vazio é
proibido pelo modelo e fabricar um seria fingir conteúdo; a região existe, e o
movimento entra com a primeira obra.

Vale dizer o que isto **não** é: não é lacuna, não é dívida, não é compra
devida (§2.1). É território reivindicado e vazio — e o cabeçalho que você
escreveu sem nada por baixo é a informação mais precisa da lista inteira, porque
diz que você sabe o que falta.

---

# 3 · Um problema de vocabulário, levantado e não decidido

**`role` está ausente nas onze participações originais — e continua ausente
nas duas acrescentadas em 2026-09-06** (`skousen--strategic-relocation`,
`silva-conforto--primeiros-socorros`), pela mesma razão, para não decidir em
silêncio uma questão que já estava em aberto. O vocabulário observado —
`foundational`, `critical-response`, `pivot`, `comparative`,
`literary-treatment`, `supplementary` — foi construído para obras que discutem
umas com as outras. Um guia de rastros não é `foundational` de nada, e não
responde criticamente a coisa nenhuma.

Inventar um slug (`reference`, `practical`, `manual`) seria decisão de
classificação tomada em silêncio, e o §6.8 manda levantar. **Está levantada
aqui.** Se você quiser um valor novo, ele entra em
`config/vocabularies.yaml` e as treze participações ganham-no de uma vez.

`demand` foi atribuída normalmente: mede o que a obra exige do leitor, e isso
aplica-se a um manual tão bem como a um tratado. Só o PHTLS levou `exigente`,
e por uma razão de destinatário — é formação técnica profissional, não guia
para leigos, ao contrário dos dois Hesperian ao lado. As duas novas
participações levaram `moderado`, pela mesma lógica.

**`work_type` ficou `null` nas treze.** É campo do §E e o vocabulário do
blueprint tem cinco categorias — fonte primária, teoria, sociologia,
literatura, comentário — e nenhuma delas é «manual prático». Mesma decisão:
levantar, não inventar.

---

# 4 · `tensions: []`, e por que aqui isso não significa nada

Em Educação, nove obras de uma só tradição sem nenhuma tensão foi o achado
central. Aqui o campo está igualmente vazio e **não é achado nenhum**: manuais
técnicos não se contradizem como argumentos. Um guia de rastros e um protocolo
de trauma não discordam — tratam de coisas diferentes.

Registrar isto evita que uma execução futura da análise leia o vazio como
sintoma.

---

# 5 · Estado bibliográfico, obra a obra

Confirmação em **tier 1** (página da própria editora):

| Obra | Publicação | Confirmado |
|---|---|---|
| Tiro de combate | Millennium, 2ª ed., 2022 | tudo |
| Canterbury | Sextante, 2022 | título, editora, ano, páginas, ISBN, tradutor |
| PANC | Plantarum, 2ª ed., 2021 | título, editora, ano, páginas, ISBN, autoria |
| PHTLS | Jones & Bartlett | ISBN, editora, título |

Sem confirmação em tier 1–5 — dados vindos de livrarias, citações
institucionais ou agregadores, e assim declarados:

| Obra | Publicação | Origem |
|---|---|---|
| Seymour | WMF Martins Fontes, 6ª ed., 2011 | livraria (tier 6) |
| Hoffmann | Cultrix, 2017 | livraria (tier 6) |
| Van Lengen | B4 Editores, 2014 | livraria (tier 6) |
| Rastros | Technical Books, 3ª ed., 2013 | citação científica |
| Mini Manual | Colecção Hipopótamo, 2012 | ficha técnica da colecção |

**Sem publicação registrada:** `dickson--where-there-is-no-dentist` e
`werner--donde-no-hay-doctor`. As obras estão identificadas; você não indicou
qual edição possui, e a edição em português não foi identificada. Nenhuma foi
inventada.

## 5.1 Duas anomalias que vale ter escritas

**O PHTLS é um livro em português com prefixo editorial norte-americano**
(978-1-284). Não é edição brasileira: é a edição em língua portuguesa de uma
editora dos EUA. Explica por que nenhuma busca por editora brasileira o
encontraria, e muda o raciocínio do §F.

**O Mini Manual é português de Portugal**, não brasileiro — daí «escutista» e
não «escoteiro». É distinção bibliográfica, não ortográfica, e afeta aquisição.

---

# 6 · Três questões de modelo que esta importação abriu

1. **Autor corporativo.** A NAEMT é o primeiro autor não-pessoa do acervo. Usei
   a sigla como sobrenome no id, porque é como a obra é citada, mas o §C não
   tem cláusula para isso. Reversível por `id_aliases`.
2. **A hierarquia de fontes não previu agregadores digitais.** Internet
   Archive, Google Books, Open Library e citações institucionais não são
   editora, catálogo universitário, biblioteca nacional, base acadêmica nem
   vendedor. Deixei `source_tier: null` com `tier_note` em cada caso, em vez de
   lhes atribuir um nível inventado.
3. **Exclusão antes da criação.** O campo `excluded` do esquema pressupõe uma
   obra já registrada (`work: <id>`). «Faça você mesmo» nunca teve id, e por
   isso a entrada usa `work: null` + `title_as_listed`. É a forma mínima que
   preserva a decisão sem inventar um registro só para o excluir.

---

# 7 · O que precisa de você

Nada é urgente, e a coleção funciona como está.

- **O vocabulário de `role`** para obras práticas (§3). É a única decisão que
  deixaria as treze participações mais completas de uma vez.
- **A pergunta e os critérios** da coleção são meus e estão `proposta`. A
  pergunta que escrevi tenta cobrir as seis regiões originais sem privilegiar
  nenhuma; a sétima região (`planejamento-risco-localizacao`) não foi
  incorporada ao texto da pergunta — outra pendência menor.
- **As edições de Dickson e Werner**, se você as tem — o colofão resolve as
  duas publicações que faltam.
- **Energia**, quando quiser. Não proponho nada: sem registro de lacuna não há
  recomendação (§I), e não há registro de lacuna porque uma região vazia não é
  uma ausência a corrigir.
- **Edição de Skousen, Bezmenov e "Dark Secrets"** — nenhuma pesquisa de
  editora/ano feita além do ASIN. Ver §8.

---

# 8 · Decisões pós-importação — 2026-09-06

Quatro decisões suas, aplicadas nesta data. Nenhuma foi inferida por Claude;
todas vieram diretamente da sua mensagem, com a implementação (forma dos
registros, colocação exata nos campos) decidida por Claude a partir das
regras existentes.

## 8.1 · Incluída — Skousen, *Strategic Relocation*

Nova região (`planejamento-risco-localizacao`) e novo movimento
("Planejamento, risco e localização"), com os nomes e a ideia que você deu.
Único membro por ora. Colocado ao final da `sequence` — não por juízo de
prioridade, mas porque é o acréscimo mais recente numa coleção `thematic`,
onde a posição não carrega dependência intelectual. `role` fica ausente, como
nos demais (§3). Bibliografia: só ASIN identificado (1735015407, 4ª edição);
editora e ano não pesquisados.

## 8.2 · Incluída — Silva & Conforto, *Primeiros Socorros*

Nova participação em `medicina-e-socorro`, entre Werner e o PHTLS — a posição
intermediária que você descreveu. Autoria (Evandro de Sena Silva, Cláudia
Conforto) veio diretamente de você; a pesquisa de Claude só alcançou tier 6
(catálogo de varejo da Di Livros), corroborado por uma segunda publicação da
mesma editora com o mesmo primeiro autor. Publicação criada:
`pub--di-livros--primeiros-socorros`, `research_status: partially_researched`.

## 8.3 · Excluída sem registro — Eda Gomes Lambert, *Guia Prático de Primeiros
Socorros*

Foi ao `excluded` de `survival-self-sufficiency`, `work: null` — mesma forma
de «Faça você mesmo», mas por razão diferente: ali a identificação tinha
falhado, aqui a identificação existe e a exclusão é por redundância frente ao
que a coleção já cobre (Werner, PHTLS, e agora Silva & Conforto). **Correção
de identificador:** o ASIN/ISBN-10 é 853392240X (dígito verificador X válido
pelo algoritmo padrão); o ISBN-13 correspondente é **978-85-3392-240-2**. Numa
conversa anterior eu tinha buscado por engano «9788533922404» — dígito final
errado — e essa string nunca chegou a um arquivo canônico. Fica corrigida
aqui, na primeira vez em que este candidato toca a Bibliotheca.

## 8.4 · Registrada sem coleção — Begovic & Luther, *The Dark Secrets of SHTF
Survival*

`works/begovic-luther--dark-secrets-of-shtf-survival.md` criado com
`pending_assignment: true` — mesmo mecanismo de
`weber--wissenschaft-als-beruf.md`. Não é membro de nenhuma coleção; está
isenta da checagem de órfãs. `candidate_collections` fica **vazio**, por
instrução sua explícita de não criar uma coleção futura a partir desta
mensagem — os quatro títulos que você mencionou (*Why Nations Fail*, *The End
Is Always Near*, *Collapse*, *Guns, Germs, and Steel*) estão citados em prosa,
como razão da preservação, e **não** como registros da Bibliotheca. Nenhum
dos quatro foi criado.

## 8.5 · Não tocada — *Entre a Honra e o Nada*

Instrução explícita sua: não mudar agora. Continua em `Cultura`, com o
raciocínio curatorial que já lá estava. Nenhum arquivo relacionado foi lido
nem editado nesta rodada.

## 9 · Medicina sem médico: há obras melhores que Werner e Dickson? (2026-10-10)

Pesquisa pedida pelo Mathews depois que a Etapa 1 mostrou que as edições
brasileiras de *Onde não há médico* e *Onde não há dentista* são de décadas
atrás. Ele disse que não precisa manter essas obras se houver outras melhores
sobre os mesmos pontos. A decisão está no cartão `d-sob-medicina`.

**O que Werner e Dickson fazem na coleção.** São os únicos membros de
"Medicina e socorro" sobre cuidado **continuado** sem médico — doenças comuns,
infecções, medicamentos, parto, dentes. Silva e Conforto e o PHTLS supõem que
haverá atendimento depois; Hoffmann trata de ervas. Uma substituta tem de
cobrir esse mesmo terreno, não o dos primeiros socorros.

**Contra Werner.** Babu e Eisenberg fizeram uma avaliação sistemática do livro
e concluíram que, sendo um grande recurso, ele "contém problemas consideráveis
nas recomendações de diagnóstico e tratamento", e que não está claro quanto ele
melhora a saúde de quem não tem formação médica
(faculty.washington.edu/dtae/manuscripts/wtind complete PDF March 9 2010.pdf,
lido pelo resumo da busca; edição avaliada não conferida). O livro foi escrito
para agentes de saúde em vilas pobres; a coleção pergunta pelo que fazer
quando o sistema some.

**Candidatas encontradas** (anúncios da Amazon, tier 7, salvo indicação):

| Obra | Dados | Leitura |
|---|---|---|
| Alton e Alton, *The Survival Medicine Handbook*, 4ª ed. | Doom and Bloom, 2021, 694 p., ISBN 978-0988872509 | Parte do princípio de que hospitais e médicos não estarão disponíveis; trauma, primeiros socorros, doenças crônicas, procedimentos, plantas medicinais; 300+ tópicos e ilustrações. Resenha da OFFGRID elogia a revisão da 4ª ed. **Substituta direta de Werner.** |
| Hubbard, *The Survival Doctor's Complete Handbook* | Trusted Media Brands, 2016, 288 p., ISBN 978-1621453055 | Mesma proposta, mais curta; médico de família com 30 anos de prática. |
| Schlaad e Schlaad (org.), *Medicina em áreas remotas no Brasil* | Manole, 2019, 544 p., ISBN 978-8578683733 | Primeiro livro brasileiro de medicina de expedições e áreas remotas; escrito para profissionais de saúde. Único com o contexto brasileiro. |
| Paulo Willian, *Medicina de Emergência em Áreas Remotas* | Dialética, 2025, 332 p., capa dura, ISBN 978-6527074922 | Protocolos de emergência adaptados aos biomas brasileiros; foco em emergência. |
| Schimelpfenig, *NOLS Wilderness Medicine*, 7ª ed. | Stackpole, 2021, 392 p. (há edição em espanhol de 2016) | Primeiros socorros até a evacuação. Fora do terreno de Werner. |
| Auerbach e outros, *Medicine for the Outdoors*, 7ª ed. | Elsevier, 2023, 576 p. | Idem; traz emergências dentárias. |
| Met Clark, *Emergency Dentistry Handbook* | Paladin Press, 2011, 80 p. | Única alternativa específica a Dickson; curta demais para substituí-lo. |

**Conclusão.** Para Werner há substituta melhor: Alton. Para Dickson não há —
a edição inglesa revista em 2018 continua a melhor obra sobre o tema. Nenhuma
obra em português cobre o cuidado continuado sem médico; Schlaad é a melhor
fonte brasileira e complementa pelo contexto local.

