---
collection: education
kind: import-report + curation
by: claude
date: 2026-09-05
status: "nada aplicado — tudo abaixo aguarda a sua decisão. Em 2026-09-10,
         depois da importação, duas obras entraram por decisão sua: A
         Inveja dos Anjos e Sociedade sem Escolas."
---

# 1 · Relatório de importação

**10 entradas → 9 obras. 4 movimentos. Ordem sua, intacta.**

| O que li | Resultado |
|---|---|
| Entradas numeradas | 10, das quais duas idênticas |
| Item 3 (Nunes, Idade Média) | Aparece **duas vezes**, texto integralmente idêntico. Deduplicado — 9 membros, não 10 |
| "Perspectiva" / "Temas" | Preservados em `perspective` e `subjects_stated`, literais |
| Terceira linha de cada item | 9 `why_here`, transcritos, marcados `voce` |
| A cadeia de setas no fim | `sequence_rationale`, **marcada `by: voce`** |
| Edições | **Zero**. Nenhuma entrada nomeia editora |

Duas diferenças em relação a Política que vale registrar:

**O argumento da ordem veio escrito por você.** Em Política tive de o
redigir a partir da estrutura; aqui a sua cadeia de sete setas é o argumento,
e está no arquivo literal. É a primeira coleção cujo `## Por que esta ordem`
é seu e não meu.

**Esta coleção é cumulativa, Política é dialética.** Em Política as obras
discordam e a ordem torna a discordância legível. Aqui cada elo depende do
anterior no sentido forte — Adler é incompreensível sem a história, porque
recuperar pressupõe conhecer. Consequência prática: esta coleção tem
prerequisitos reais, e não só uma ordem recomendada (ver §5).

---

# 2 · Perguntas

### 2.1 Tradutor ou coautor?
Duas entradas trazem dois nomes:

- **"Marshall McLuhan; Hugo Langone"**
- **"Irmã Miriam Joseph; Carlos Nougué"**

Leio ambos os segundos nomes como **tradutores**, no formato de livraria
brasileira, e não como coautores. Se estiver certo, isso importa mais do que
parece: **os dois nomes identificam implicitamente edições brasileiras
específicas** — é informação de edição escondida num campo de autoria, e a
pesquisa do §E deve partir dela em vez de recomeçar do zero.

Registrados provisoriamente como tradutores, sem entrar no campo `author`.
Confirme e eu fixo.

*(Nota: em "Susan Wise Bauer; Jessie Wise" os dois nomes **são** coautoras.
Interpretado assim.)*

### 2.2 Sete estágios, quatro movimentos
A sua cadeia tem 7 estágios; agrupei em 4 movimentos porque cinco deles
teriam uma obra só, e um movimento de uma obra é apenas um título com
legenda. A cadeia continua literal no arquivo, e cada movimento declara
quais estágios seus cobre (`covers_your_stages`). Se preferir os 7, é uma
troca de agrupamento e não perde nada.

### 2.3 Escopo — RESOLVIDO, e com uma correção de método minha

**Decisão sua:** Educação permanece a coleção larga. Educação clássica é uma
tradição *dentro* dela, como crítica libertária é uma tradição dentro de
Pensamento Político. Nenhuma tradição fica de fora por não estar na lista de
bootstrap.

**O erro era meu, e era de método, não de julgamento sobre esta coleção.**
Eu derivei os `inclusion_criteria` das 9 obras importadas. Critérios inferidos
do conteúdo descrevem o conteúdo — e uma coleção definida pelo que já contém
**não pode ter lacunas por construção**. A análise de cobertura passaria a
confirmar a biblioteca em vez de a interrogar, que é exatamente o oposto do
que o §I existe para fazer. Eu teria produzido um sistema que dizia "nada
falta" com toda a aparência de rigor.

A regra corrigida: **critérios derivam da pergunta da coleção, nunca dos seus
membros atuais.** E há um teste barato que a torna verificável — *este
critério excluiria uma obra que responde claramente à pergunta da coleção?*
Se sim, o critério está a descrever a amostra. Aplicado e registrado no
arquivo em `test_applied`.

**Nota sobre Pensamento Político:** os critérios daquela coleção foram
produzidos pelo mesmo método defeituoso. Saíram aceitáveis porque a sua lista
já era plural — o resultado foi bom por sorte do input, não por acerto do
método. Merecem uma revisão sob a regra corrigida quando você quiser; não a
fiz agora para não mexer numa coleção que você não pediu para mexer.

**Consequência estrutural:** entra um `scope_map` no arquivo da coleção — o
território reivindicado, dividido em regiões, cada uma com estado
`covered | thin | absent`. É contra ele que a cobertura mede. Sem um
território declarado não há contra o que medir, e foi por isso que a primeira
análise desta coleção encontrou tão pouco.

### 2.4 Weber — *A Ciência como Vocação*
A condição do `pending_assignment` era "Educação e Cultura importadas".
Educação chegou; Cultura não. Mantém-se pendente, mas deixou de ser
hipotético, então registro a leitura provisória:

Sob os critérios rascunhados, esta conferência **não pertence à linhagem** —
pertence ao seu interrogatório. Weber fala da universidade de pesquisa
moderna, do desencantamento e da neutralidade axiológica, que é quase o
oposto do ideal formativo que a coleção narra. Isso a qualificaria como
`critical-response` no fim da sequência, não como membro do corpo.

Inclinação: **Cultura é a casa mais provável**, e Educação uma segunda opção
como voz crítica. Decisão fica para quando Cultura chegar, como combinado.

---

# 3 · Cobertura e lacunas — reexecutado sob o escopo largo

## 3.0 · O mapa, antes das propostas

Duas saídas diferentes, e mantê-las separadas é o que permite que o escopo
largo não produza uma enxurrada de sugestões:

| | O que é | Limite |
|---|---|---|
| **Cobertura** | Regiões do território com estado `covered/thin/absent`. Relatório. | Nenhum — o mapa é o mapa |
| **Propostas** | Obras concretas a acrescentar, com colocação e argumento | **3 abertas por coleção**, §I |

Sob o escopo largo, o mapa fica assim: **1 região densa, 5 rasas, 7 vazias.**

| Região | Estado | O que a ocupa |
|---|---|---|
| Educação clássica moderna | **covered** | Adler, McLuhan, Miriam Joseph, Bauer & Wise |
| Antiguidade clássica | thin | Marrou — história, sem fonte primária |
| Cristianismo antigo | thin | Nunes |
| Idade Média | thin | Nunes |
| Renascimento / humanismo | thin | Nunes |
| Século XVII | thin | Nunes |
| Iluminismo / séc. XVIII | **absent** | Rousseau (*Emílio*), Kant sobre pedagogia |
| Século XIX | **absent** | Newman, Humboldt, Herbart, Spencer |
| Educação progressista | **absent** | Dewey |
| Pedagogia crítica | **absent** | Freire |
| Psicologia do desenvolvimento | **absent** | Piaget, Vygotsky |
| Crítica da forma escolar | **absent** | Illich |
| Tradições não ocidentais | **absent** | confucionista, madraça, gurukula |

A leitura honesta: a coleção é **uma região de profundidade e treze de
largura**. Não é um defeito da sua lista — uma lista de bootstrap é uma
amostra, e esta amostra é excelente naquilo que amostra. É simplesmente o que
o escopo largo torna visível e o escopo estreito escondia.

Duas observações que só existem sob o escopo largo:

**`tensions` está vazio, e agora isso é um achado.** Em Política houve oito
tensões sem esforço. Aqui, zero — porque os nove membros pertencem todos à
mesma tradição e portanto não discordam entre si. Sob o escopo estreito isso
era uma propriedade da coleção; sob o largo é o sintoma central.

**As cinco regiões rasas são rasas do mesmo modo:** têm história e não têm
fonte. Isso é uma lacuna só, não cinco.

> **PROVISÓRIO — as duas observações acima.** Ambas dependem de cobertura
> cruzada que ainda não existe. Uma obra em Greco-Romana ou Religião pode já
> ocupar uma destas regiões, e nesse caso a região não está rasa: está
> coberta por uma *membership* que ninguém escreveu ainda. A conclusão "uma
> lacuna, cinco sintomas" só passa a firme depois da última importação.
> `recheck_after: outras-colecoes-importadas`.

---

## 3.1 · Propostas abertas

**Três, o teto do §I. Nenhuma aceita.**
`recheck_after: outras-colecoes-importadas`.

### Necessidade ≠ relevância contextual

Correção sua, e correta. Na volta anterior eu escrevi que Freire é "a
ausência mais conspícua num acervo brasileiro" — e deixei essa observação
encostar-se ao argumento de prioridade. São eixos diferentes e passam a ser
campos diferentes:

| Campo | O que mede | Pode determinar prioridade? |
|---|---|---|
| `necessity` | Quanto o argumento da coleção enfraquece sem a obra. Vem do sinal estrutural | **Sim. É o único que a determina** |
| `context` | Disponibilidade no Brasil, idioma, proximidade cultural, saliência local | **Não.** Registrado, nunca hierarquiza |

`context` só age como **desempate entre candidatos de necessidade igual** —
exatamente como a sua hierarquia de idiomas no §F, que decide dentro de uma
faixa de qualidade e nunca entre faixas. O princípio é o mesmo aplicado a
dois níveis: obra e edição. Um livro não sobe por ser fácil de comprar em
português, e não desce por ser difícil.

> Coleção 2 de N. Leia primeiro a §4: parte do que parece faltar **já está na
> biblioteca** e precisa de uma *membership*, não de uma compra.

---

### E-G1 · Uma tradição narrada inteiramente por terceiros
**Tipo:** type monoculture · **Necessidade:** alta
**Contexto (não hierarquiza):** Agostinho tem tradição editorial sólida em
português; Quintiliano e Hugo de São Vítor, muito menos. Isso não altera a
necessidade de nenhum dos três — entra só se dois deles empatarem.

**Sinal.** Mecânico: das 9 obras, **zero** têm `work_type: primary-source`.
Cinco são história, uma é manifesto, duas são estrutura, uma é método. A
coleção percorre dois mil anos de um ideal educativo sem conter um único
texto em que esse ideal é exercido. É a mesma assimetria que apontei em
Política com o marxismo, e aqui é total em vez de parcial.

Isto não é uma preferência minha: a precedência das fontes primárias sobre os
comentadores é agora um critério explícito da própria coleção. Sob o escopo
largo a lacuna também **cresceu**: não é a antiguidade que carece de fonte
primária, são as cinco regiões rasas, todas do mesmo modo — história sem
texto. Uma lacuna, cinco sintomas.

**Candidato (fecha o elo mais forte):** **Agostinho — *A Doutrina Cristã***
(*De Doctrina Christiana*). O argumento vem das suas próprias palavras: a
sua justificativa do item 2 é "o cristianismo não simplesmente abandona a
tradição clássica, mas a incorpora, transforma e dá a ela uma nova
finalidade". Essa frase **é a tese** deste livro, e o Livro IV é o momento
exato em que a retórica clássica é batizada. Nunes narra o processo;
Agostinho é o processo.

**Por que preferível aos outros candidatos:**
- *Quintiliano — Institutio Oratoria*: fonte primária do estágio 1, e
  excelente, mas volumosa e o estágio 1 já tem Marrou como guia forte.
  `complementary`.
- *Hugo de São Vítor — Didascalicon*: o texto medieval sobre a ordem das
  artes; encaixa no estágio 3 e é curto. Segundo colocado real, e o melhor
  candidato se você quiser **duas** fontes primárias em vez de uma.
- *Comênio — Didática Magna*: pertence ao estágio 5 e é fonte primária, mas
  é já o modelo moderno que confronta a tradição, não a tradição.
  `complementary`.

**Colocação proposta:** logo após
`nunes--historia-da-educacao-na-antiguidade-crista` · role `primary-source` ·
demand `exigente` · `requires: [marrou--...]` · priority `core`.

---

### E-G2 · A sequência salta de 1700 para 1982
**Tipo:** period discontinuity · **Necessidade:** média
**Contexto (não hierarquiza):** disponibilidade de Newman em português a
verificar, e pode ser má. Se for, a necessidade continua média — muda apenas
o custo de a satisfazer, e isso é assunto do §F, não deste.

**Sinal.** Vem da sua própria cadeia. O estágio 4 diz "como mudou no
Renascimento **e na modernidade**", mas a modernidade termina no século XVII
com Nunes, e o elo seguinte é Adler, de 1982. Faltam os dois séculos em que
o ideal clássico foi de facto desmontado e defendido — e Adler escreve
contra esse desmonte, sem que a coleção mostre o que ele foi.

**Candidato:** **John Henry Newman — *A Ideia de uma Universidade***. É a
defesa mais forte do ideal de formação liberal escrita depois de ele ter
sido posto em causa, e é o elo direto que falta até Adler: Adler argumenta
para escolas o que Newman argumentou para a universidade.

**Por que preferível.** *Émile* de Rousseau é o outro candidato óbvio, mas é
a obra que **rompe** com a tradição, não a que a defende — e Rousseau já
está na biblioteca por Política, o que faz dele um caso da §4 e não desta.
Humboldt é mais influente institucionalmente e muito menos legível.

**Colocação proposta:** entre `nunes--historia-da-educacao-no-seculo-xvii` e
`adler--the-paideia-proposal` · role `foundational` · demand `moderado` ·
priority `secondary`.

---

### E-G3 · Adler argumenta contra um adversário que não está na coleção
**Tipo:** dangling interlocutor · **Necessidade:** alta
**Contexto (não hierarquiza):** há tradução histórica de Dewey em português,
o que é conveniente e irrelevante para a necessidade — que vem inteira do
facto de a coleção conter uma posição sem aquilo a que ela responde.
**Só visível sob o escopo largo.** Sob o escopo estreito, o adversário estava
fora de escopo por definição e a lacuna era invisível.

**Sinal.** Estruturalmente idêntico ao caso Rawls/Nozick em Política. A
posição de Adler — Grandes Livros, artes liberais, currículo único para
todos — constituiu-se historicamente **contra** a educação progressista, num
debate documentado que atravessa décadas. A coleção contém a posição e não
contém aquilo a que ela responde. `tensions: []` é a forma que esse vazio
toma no arquivo.

**Candidato.** **John Dewey — *Democracia e Educação***. É a exposição
sistemática da posição contrária, escrita por quem a formulou, e não uma
apresentação de segunda mão. Edição brasileira a verificar na pesquisa do §E;
há tradução histórica em português.

**Por que preferível aos outros candidatos:**
- *Freire — Pedagogia do Oprimido*: fecha uma região **diferente** —
  pedagogia crítica — e por isso não é candidato a esta proposta. Freire não
  é o interlocutor de Adler; é outro interlocutor, de outra pergunta.
  A sua necessidade própria é real e estrutural: uma tradição inteira que
  argumenta diretamente sobre os fins da educação, ausente do mapa.
  *Contexto, registrado e sem efeito na prioridade:* original em português e
  de altíssima saliência no Brasil. Na volta anterior deixei essa saliência
  encostar-se ao argumento de ordem e disse que ele seria "o primeiro a
  entrar"; retiro. Qual das regiões vazias tem precedência decide-se por
  necessidade comparada, e essa comparação não pode ser feita antes da
  cobertura cruzada.
- *Illich — Sociedade sem Escolas*: recusa a forma escolar inteira, incluindo
  a de Dewey. Terceira região, não esta.
- *Kilpatrick, e outros progressistas de segunda linha*: mais fáceis de
  refutar. Pelo princípio do §I, o adversário a incluir é o mais forte
  disponível, não o mais conveniente.

**Colocação proposta:** imediatamente **antes** de
`adler--the-paideia-proposal` · role `foundational` · demand `moderado` ·
`requires: []` · priority `core` · nova tensão
`adler ⇄ dewey — sobre se a formação comum liberta ou exclui`.

Colocado antes, Adler passa a ler-se como resposta, que é o que é. Colocado
depois, Dewey pareceria um apêndice crítico — o que inverteria a história.

---

# 4 · Não são lacunas — são *memberships*

Isto é exatamente o caso que o §I previu, e ele apareceu na segunda coleção.
Três obras que E-G1 pediria estão **já na biblioteca**, vindas de Política.
Nenhuma delas é uma compra: são novas participações do mesmo registro
canônico, com papel, posição e escopo próprios nesta coleção.

| Obra | Escopo em Educação | Papel proposto |
|---|---|---|
| `platao--politeia` | Livros II–III e VII | `primary-source` — a paideía sendo argumentada, não descrita |
| `aristoteles--politika` | Livros VII–VIII | `primary-source` — a formação do cidadão como função da cidade |
| `agostinho--de-civitate-dei` | seletivo | `complementary` — contexto para *A Doutrina Cristã*, se E-G1 for aceito |

Se aceitar as duas primeiras, **E-G1 muda de severidade**: a coleção deixa de
ter zero fontes primárias e passa a ter duas, ambas no estágio 1. O que
sobra é a lacuna cristã e medieval, que é onde Agostinho ou Hugo de São
Vítor entram — e aí a proposta fica mais estreita e mais forte.

Recomendo decidir a §4 antes da §3. É mais barato e altera a §3.

---

# 5 · Prerequisitos propostos

Diferente de Política, onde deixei `requires` vazio por não haver base sua.
Aqui a sua própria cadeia é uma afirmação de dependência — "recuperá-la"
pressupõe conhecê-la — e por isso proponho estes:

| Obra | requires | Razão |
|---|---|---|
| `nunes--...-antiguidade-crista` | `marrou--...` | A transformação exige o que foi transformado |
| `nunes--...-idade-media` | `nunes--...-antiguidade-crista` | Cadeia sua, elos consecutivos |
| `nunes--...-renascimento` | `nunes--...-idade-media` | idem |
| `nunes--...-seculo-xvii` | `nunes--...-renascimento` | idem |
| `adler--the-paideia-proposal` | toda a sequência histórica | "Por que Adler quer recuperá-la" só é resposta depois do que se recupera |
| `miriam-joseph--the-trivium` | `mcluhan--the-classical-trivium` | Sua ordem: história do trivium antes do trivium como instrumento |
| `bauer-wise--the-well-trained-mind` | `miriam-joseph--the-trivium` | Método pressupõe a estrutura |

Se aplicados, esta é a primeira coleção com uma cadeia de prerequisitos
completa — o que a torna o melhor caso de teste para a checagem topológica
do validador.

---

# 6 · Nota de edições

Zero das 9 entradas nomeiam editora, contra 25 de 40 em Política. A pesquisa
do §E terá aqui muito mais trabalho por obra.

Um dado favorável: **quatro das nove são originais em português** — Nunes
escreveu em português, e as suas quatro obras não têm questão de tradução
nenhuma. Marrou é francês; Adler, McLuhan e Miriam Joseph têm edição
brasileira implícita pelos tradutores; Bauer & Wise é a **única** entrada
dada em inglês, e provavelmente a única em que a sua hierarquia de idiomas
não poderá ser satisfeita em português.

---

# 7 · Obras acrescentadas após a importação — 2026-09-10

Duas decisões suas, fora do fluxo de importação da lista original de nove.
Você forneceu título e ISBN de cada uma; a pesquisa (identidade da obra,
edição brasileira, colocação) e a implementação são de Claude.

## 7.1 · Jaeger, *A Inveja dos Anjos* (*The Envy of Angels*)

Monografia acadêmica de 1994 sobre as escolas catedrais medievais
(950–1200), University of Pennsylvania Press; edição brasileira pela Verbo
Encarnado, confirmada em fonte tier 1 (página da própria editora) — a
primeira confirmação tier 1 de editora nesta coleção desde a importação
original, que não tinha nenhuma.

Colocada na região `idade-media`, ao lado de
`nunes--historia-da-educacao-na-idade-media`, como aprofundamento de um
recorte que Nunes narra em panorama. Não muda a classificação `thin` da
região — acrescenta um segundo título a ela, mais especializado. `role:
supplementary`, pela mesma lógica de `bauer-wise--the-well-trained-mind`:
aprofunda um elo já presente, não estabelece um novo.

## 7.2 · Illich, *Sociedade sem Escolas* (*Deschooling Society*)

**Não é uma obra nova para esta coleção — é uma lacuna que se fechou.** A
região `critica-da-escola` estava `absent` desde 2026-09-05, e esta obra já
estava nomeada como candidata em `review/gaps/education.yaml`, gap
`education--g03`, com o veredito `different-region`: fecharia essa região,
não a de Dewey/educação-progressista que g03 persegue. Isso permanece
exato — g03 continua `open`, sobre um interlocutor diferente (Dewey, ainda
ausente).

**Duas consequências que vale registrar:**

1. **`tensions` deixou de ser `[]`.** Registrei um par novo:
   `adler--the-paideia-proposal` × `illich--deschooling-society` — se a
   formação humana exige a instituição escolar redirecionada para o cânone
   clássico, ou se a escola é, ela mesma, o obstáculo. O achado de §3 (zero
   tensões porque os nove membros originais pertenciam a uma só tradição)
   continua descrevendo corretamente **a lista original**; esta tensão
   chega de fora dela, e o campo vazio deixou de ser um traço da coleção
   inteira.
2. **A evidência de `education--g01` mudou de estado.** g01 mede
   `work_type: primary-source` entre os membros e espera 0. Classifiquei
   `illich--deschooling-society` como `work_type: primary-source` — não é
   história nem comentário de uma tradição, é a própria posição sendo
   argumentada, o que é exatamente o que g01 registra como ausente. A
   contagem real passa a 1. Não editei o predicado `check` nem o `status`
   de g01 — quem revalida isso é o próximo build, ou a próxima leitura
   humana da lacuna — mas a afirmação em prosa de g01 ("zero são fonte
   primária") já não é exata sem esta nota, e por isso ela está aqui. g01
   continua substantivamente aberta: é sobre a Antiguidade e a Idade Média,
   e Illich é do século XX — não a fecha, só deixa de ser um zero limpo.

Movimento novo criado — "V. A crítica radical da escola" — porque a cadeia
original (§"Por que esta ordem" em `collections/education.md`) é
estritamente cumulativa e é sua; inserir Illich no meio dela teria mudado o
que ela argumenta. Colocado ao final, como aconteceu com Jaeger e como
aconteceu na coleção de Sobrevivência com as duas participações de
2026-09-06.

---

# 8 · Weber, *A Ciência como Vocação* — colocação decidida por pesquisa (2026-09-19)

A conferência estava sem coleção desde 2026-09-05, quando você a retirou de
Pensamento Político: partilhar volume com *A Política como Vocação* não faz
dela membro daquela coleção. O `pending_assignment` dizia que a decisão
esperaria Educação e Cultura terem critérios declarados. As duas têm agora.

Em 2026-09-19 você delegou a escolha explicitamente, por não conhecer a obra,
pedindo que ela fosse decidida por pesquisa e não por palpite. **Decisão:
Educação, como `critical-response`.** Minha inclinação anterior, registrada no
§2.4, era Cultura — e a pesquisa a reverteu.

## 8.1 O que a conferência argumenta

Quatro passos, nesta ordem:

1. A ciência moderna tornou-se **especializada** e institucionalizada; a
   carreira acadêmica depende de acaso tanto quanto de mérito.
2. O progresso científico é **inacabável por natureza**: toda obra nasce para
   ser superada, e isso distingue a ciência da arte.
3. A racionalização produz o **desencantamento do mundo** e não devolve
   sentido no lugar do que dissolveu.
4. Portanto a ciência **não pode dizer como se deve viver**. Pode dar clareza
   sobre meios, consequências e coerência de uma escolha; nunca fazer a
   escolha. Daí a proibição final: o professor não deve pregar da cátedra,
   porque a sala de aula não é um púlpito.

Fonte: [SEP, *Max Weber*](https://plato.stanford.edu/entries/weber/), tier 4,
consultada em 2026-09-19. A pesquisa de edição do §E **não** foi feita, e a
publicação da Cultrix continua não verificada.

## 8.2 Por que Educação, e não Cultura

O argumento decisivo é o objeto declarado da conferência. Ela não fala da
cultura em geral: fala da **universidade** e do que um professor pode e não
pode fazer em sala. Isso é uma tese sobre os fins e os limites da formação —
que é a pergunta desta coleção, e não a de Cultura.

O segundo argumento é estrutural. A cadeia de Educação narra a formação como
transmissão de um ideal, da paideía ao trivium, e culmina em Adler, *A
Proposta Paideia*, que quer recuperá-lo. Weber descreve a instituição que
herdou essa tarefa e diz que ela não pode cumpri-la. **É a interrogação da
premissa da coleção, feita de dentro da instituição** — e é por isso que ela
vale mais aqui do que em Cultura, onde seria apenas mais um diagnóstico da
modernidade ao lado de três outros.

O terceiro é de cobertura: a região `seculo-xix` — a universidade moderna —
estava `absent` e passou a `thin`. Em Cultura, a conferência não sustentaria
nenhuma região melhor do que as obras que já lá estão.

Contra-argumento honesto, registrado para não se perder: o desencantamento e o
politeísmo de valores **são** temas de crítica da cultura moderna, e uma
participação futura em Cultura continua possível — obra é uma, participações
são várias. Não a criei agora porque uma segunda participação deve ter papel
próprio, e o papel dela aqui é claro enquanto o de lá seria redundante com o
que Han e Vargas Llosa já fazem.

## 8.3 O que mudou no arquivo

- Movimento novo no fim da sequência: **VI. O limite do que a universidade
  pode formar**. A cadeia original, que é sua e é cumulativa, não foi partida
  — mesma solução usada para Illich, *Sociedade sem Escolas*.
- Região `seculo-xix`: de `absent` para `thin`, com a ressalva escrita de que
  Weber a sustenta de raspão e não a fecha.
- **Tensão nova:** Adler × Weber — se a educação pode formar o caráter e
  indicar fins, ou se a instituição moderna só entrega método e clareza. A
  coleção passa a ter duas tensões.
- A lacuna `education--g02` continua **aberta**, e o seu predicado foi
  atualizado para `thin` em vez de ficar stale afirmando o que já não é
  verdade. Falta ali a voz que defendeu que a universidade podia formar —
  Newman, *A Ideia de uma Universidade*, é o candidato já registrado.

---

# 9 · Edições, capas e links de compra — 2026-09-23

Dados de anúncio de varejo são tier 7: entrada, não autoridade bibliográfica.

## 9.1 Edições registradas — 11 publicações, todas com capa e link de compra

| Obra | Edição | Registro |
|---|---|---|
| Marrou | Kírion, 2017 (trad. Mário Leônidas Casanova) | `pub--kirion--historia-da-educacao-na-antiguidade--2017` |
| Nunes, Antiguidade Cristã | Kírion, 2018 | `pub--kirion--historia-da-educacao-na-antiguidade-crista--2018` |
| Nunes, Idade Média | Kírion, 2018, 2ª ed. | `pub--kirion--historia-da-educacao-na-idade-media--2018` |
| Nunes, Renascimento | Kírion, 2018 | `pub--kirion--historia-da-educacao-no-renascimento--2018` |
| Nunes, Século XVII | Kírion, 2018 | `pub--kirion--historia-da-educacao-no-seculo-xvii--2018` |
| Adler | Kírion, 2021 | `pub--kirion--a-proposta-paideia--2021` |
| McLuhan | É Realizações, 2012 (trad. Hugo Langone) | `pub--e-realizacoes--o-trivium-classico--2012` |
| Miriam Joseph | É Realizações, 2018 (trad. H. P. Dmyterko) | `pub--e-realizacoes--o-trivium--2018` |
| Bauer & Wise | Klasiká Liber, 2021 (PT) | `pub--klasika-liber--a-mente-bem-treinada--2021` |
| Bauer & Wise | Norton, 4ª ed., 2016 (EN) | `pub--norton--the-well-trained-mind--2016` |
| Hirsch | Kírion, 2023 | `pub--kirion--por-que-o-conhecimento-importa--2023` |

Ozmon & Craver já tinha registro (Artmed/Penso) e não mudou.

## 9.2 A dúvida do §2.1, respondida

Pelos anúncios: **Langone é tradutor** de McLuhan, e **Nougué não é
tradutor** de Miriam Joseph — assina o prólogo; o tradutor é Henrique Paul
Dmyterko. Tier 7: vale até a editora confirmar.

## 9.3 Inclusões e exclusões — decisões suas

- **Hirsch, *Por que o conhecimento importa*** — incluído por decisão sua.
  Posição **a confirmar**: movimento III, depois de Adler. Alternativa: o
  movimento II, como voz de uma das posições em disputa. Nota de cobertura:
  Hirsch é o primeiro crítico direto da educação progressista na coleção; a
  região `educacao-progressista` continua `thin` — ele a comenta de fora, não
  a representa. A lacuna `education--g03` (Dewey) continua aberta: Hirsch é
  adversário de Dewey, não substituto.
- **Joel Jota, *Pai, não amigo*** — não entra na coleção, por decisão sua.

## 9.4 Edições que pedem decisão ou pesquisa

1. **Bauer & Wise — duas edições registradas.** Tradução brasileira de 2021 e
   original americano (4ª ed., 2016). Não se sabe de qual edição americana a
   tradução foi feita. E existe uma **Essential Edition** mais nova, que tira
   as listas de material do livro e as põe num portal pago.
2. **Marrou** — tradução histórica de Casanova, não avaliada; o candidato
   alternativo é o original francês.
3. **Adler** — o volume brasileiro (442 p.) é bem maior que o livro original;
   parece reunir outros textos do programa Paideia. Tradutor não creditado.
4. **Hirsch, Klasiká Liber** — tradutor não identificado.

## 9.5 Correção — Hirsch estava no movimento errado (apontado por você)

Coloquei Hirsch no movimento III olhando só o vizinho (Adler) e não o
propósito do movimento, que é a recuperação do **ideal clássico**. Hirsch não
é clássico: argumenta com ciência cognitiva e resultados escolares, e a
coleção já dizia no propósito do movimento II que ele NÃO é "mais uma
recuperação do ideal clássico". Movido para o **II**, logo depois de Ozmon:
é uma das posições em disputa, a que responde de frente à educação
progressista (região `educacao-progressista`, que continua `thin` — ele a
critica, não a representa). A posição segue `a-confirmar`.

**Confirmada por você em 2026-10-05** (cartão `d-pos-hirsch`, opção A): Hirsch
fica no movimento II, depois de Ozmon.

## 9.6 Edição preferida — decisão sua

*The Well-Trained Mind*: as duas edições ficam registradas; a coleção lê pela
**tradução brasileira** (`publication_pref`). Isso é preferência de coleção,
não veredito de pesquisa: `verdict` continua `unassessed` nas duas.

---

## 10 · Duas obras de ciência da aprendizagem — 2026-10-01

Você pediu para acrescentar *Fixe o Conhecimento* (Brown, Roediger e McDaniel)
e *É assim que aprendemos* (Dehaene), com a pesquisa bibliográfica já feita e
os links de compra. As duas estão na biblioteca. **Nenhuma está em coleção**, e
isso é deliberado: ver §10.3.

### 10.1 O que foi conferido, e o que a conferência achou

Conferi campo a campo contra a editora antes de gravar, em vez de transcrever.

**Fixe o Conhecimento** — a loja do Grupo A expõe a ficha inteira, e tudo
coincidiu: Penso, 2018, 256 p., brochura, 16 × 23 cm, tradução de Henrique de
Oliveira Guerra, revisão técnica de Claudio de Moura Castro, ISBN impresso
9788584291243 e e-book 9788584291250, sumário em oito capítulos. O original
ficou conferido na Harvard: Belknap, 14/04/2014, 336 p., ISBN 9780674729018 —
é a contagem da editora, e as de 268 e 313 ficam registradas como divergência
de catálogo. Um único campo seu não tem fonte: **o número da edição**. A página
da editora não declara "1ª edição".

**É assim que aprendemos** — aqui a conferência achou dois problemas.

1. **O ISBN que você trouxe não fecha.** A ficha dá ISBN-10 `65-5541-165-1` e
   ISBN-13 `978-65-5541-166-9`, e esses dois números não se correspondem: o
   165-1 converte para **978-65-5541-165-2**, e o 166-9 converte para
   `65-5541-166-X`. São duas publicações registradas, não um número em dois
   formatos. As livrarias, a Editora UnB e a Amazon dão 165-2 para o livro em
   papel; o Google Books dá 166-9; uma plataforma de biblioteca digital afirma
   o inverso. O registro adota **165-2**, que é o número do objeto que o seu
   link vende, e guarda o outro. Qual é o digital não ficou estabelecido.
2. **A página da própria Contexto não respondeu** em duas tentativas, só a do
   autor. Então o objeto está sustentado por livrarias — nível 6 —, e não por
   fonte de nível 1. Editora, ano, páginas e tradutor coincidem entre a
   livraria e a sua ficha, o que lhes dá duas vias independentes; o ISBN não.

Achado menor, mas vale: a **edição britânica tem outro subtítulo** — *The New
Science of Education and the Brain*. Não são duas obras; está em `alt_titles`.

### 10.2 Os links de compra foram normalizados

Os dois links que você mandou carregavam parâmetros de busca e uma **etiqueta
de afiliado de terceiro** (`tag=rodrigoleaobr-20`). Guardei na forma canônica
`/dp/<ASIN>`: é estável, não envelhece com os parâmetros, e não credita as suas
compras a outra pessoa. A correspondência dos dois está declarada por ISBN,
com o dígito verificador conferido por cálculo.

### 10.3 Por que nenhuma das duas entrou em Educação

A pergunta da coleção reivindica os meios — "que fins a educação deve
perseguir, **por que meios**". Mas os critérios de inclusão amarram os meios
aos fins numa frase só, o mapa de escopo não tem região para o estudo empírico
de como se aprende, e nenhum dos sete movimentos recebe estas duas sem deixar
de ser verdadeiro. *Fixe o Conhecimento* é o caso puro: práticas de estudo
apoiadas em experimentos, e nenhuma tese sobre o que um ser humano deve
tornar-se. Dehaene está no meio — pelos quatro pilares, chega a afirmações
sobre como ensinar.

Pela §6.9 regra 2, uma obra que não cabe em nenhum movimento é **sinal de
escopo** e vai à escada do §4 — não se resolve com um cabeçalho novo. Registrei
a proposta `education--sp01` (tipo `refine`, estado `open`) e o cartão
`d-edu-ciencia-aprendizagem`. As duas obras ficaram com `pending_assignment`
declarado, exatamente como *A Ciência como Vocação* ficou até esta coleção ter
critérios (§8).

O precedente que mais se aproxima é **Hirsch**, que entrou com argumento de
ciência cognitiva — mas para defender uma posição de currículo, e é a posição
que o põe no movimento II. Não é o mesmo gênero.

### 10.4 Classificação pendente

As duas ficaram com `work_type: null`, com o candidato anotado. O vocabulário
tem cinco categorias do documento fundador — fonte primária, teoria,
sociologia, literatura, comentário — e nenhuma descreve síntese de ciência
empírica. Slug novo é decisão de classificação e vai a revisão pela §6.8, como
já está o de Hirsch. **São três obras esperando a mesma decisão agora**, e isso
é mais sinal do que uma.

## 11 · Decisão: Educação admite a ciência da aprendizagem — 2026-10-05

Você escolheu a **opção A** do cartão `d-edu-ciencia-aprendizagem`. A proposta
`education--sp01` passou a `approved` e foi aplicada como estava escrita:

- **Critério novo** em `inclusion_criteria`: obras que argumentam sobre os
  meios da educação a partir de evidência empírica entram mesmo sem tese sobre
  os fins. Manual de técnica continua fora, e o `out_of_scope` não mudou.
- **Região nova** no mapa, `ciencia-da-aprendizagem`, declarada `thin`: duas
  obras numa literatura grande. Não é fila de compras.
- **Movimento VIII**, "Como se aprende: a ciência da aprendizagem", no fim da
  sequência. Dehaene vem primeiro (mecanismo), Brown, Roediger e McDaniel
  depois (prática), na ordem que você sugeriu em 2026-10-01. Os papéis e as
  justificativas de posição são meus (`why_here_by: claude`) e estão abertos a
  correção.
- **Linhagem** registrada na coleção, com o que desfaz a mudança.
- As duas obras **perderam o `pending_assignment`**: agora são membros.

O que não mudou: a pergunta da coleção, a sua ordem, os sete movimentos
anteriores e nenhuma outra participação.

**O que continua pendente.** As duas obras seguem com `work_type: null` (§10.4).
A §6.9 regra 4 diz que uma obra sem `work_type` não tem colocação defensável;
aqui a colocação vem da sua decisão, e não de inferência minha, mas a
classificação continua devida — e são três obras esperando o mesmo slug novo,
com Hirsch.

A ressalva da recomendação vale daqui em diante: o critério abre a coleção para
um gênero com muita divulgação fraca, e a proteção é a análise de necessidade
obra a obra, não o critério.

## 12 · Dewey entra em Educação — 2026-10-05

Você escolheu a **opção A** do cartão `d-edu-dewey`, com a edição que pesquisou:
*Democracia e educação: uma introdução à filosofia da educação*, Editora Unesp,
2026, tradução de Guilherme Mirage Umeda, apresentação de Carlota Boto.

**O que foi feito.** Registros novos: a obra (`dewey--democracy-and-education`),
a publicação (`pub--unesp--democracia-e-educacao--2026`) e três pessoas (Dewey,
Umeda, Boto). Dewey entrou no movimento II, **entre Ozmon e Hirsch** — Ozmon
apresenta o pragmatismo como doutrina, Dewey o expõe por dentro, Hirsch o ataca.
A posição é minha e está `a-confirmar`. A lacuna `education--g03` passou a
`accepted`.

**O que a conferência achou.** A página da Unesp não abriu deste ambiente. Pelos
trechos dela devolvidos pela busca, confirmam-se título, ano, a parceria com a
SBHE, o tradutor e a apresentação. O ISBN fecha por cálculo. Páginas, formato,
dimensões e número da edição ficam como informados por você.

**Uma correção à premissa do cartão.** O cartão dizia que a Paideia "nasceu
contra a educação progressista". Não é exato: *The Paideia Proposal* é
**dedicada a Horace Mann, John Dewey e Robert Hutchins**, e invoca *Democracia
e Educação* para ligar educação e democracia. Adler reivindica o ideal
democrático de Dewey e recusa o método da escola progressista. Por isso não
gravei uma tensão Adler × Dewey; gravei a relação `responds_to`, do lado de
Adler. Quem ataca a posição progressista de frente, na coleção, é Hirsch.

**O que continua pendente.**
- Confirmar a posição de Dewey no movimento II.
- `coverage` de `educacao-progressista` continua `thin` — revisão sua.
- A tradução histórica de Godofredo Rangel e Anísio Teixeira (Companhia
  Editora Nacional) não foi comparada; a edição está sem veredito.
- `traditions`: o candidato é `pragmatismo`, que não existe no vocabulário.

## 13 · Newman entra em Educação — 2026-10-05

Você escolheu a **opção A** do cartão `d-edu-newman`, com a edição que pesquisou:
*A Idéia de uma Universidade*, Ecclesiae, 2020.

**A colocação mudou em relação ao cartão.** O cartão (texto meu) dizia
"movimento I, depois de Nunes". Estava errado: o movimento I é narrado por
história, e Newman é fonte primária — o cabeçalho ficaria falso (§6.9.1). Você
escolheu o **movimento VII, antes de Weber**. Ali a pergunta do movimento é se
a universidade pode formar; Newman responde que sim, Weber que não. A tensão
entre os dois foi gravada, e é a primeira em que as duas pontas são vozes
sobre a mesma instituição.

**O que foi feito.** Registros novos: a obra
(`newman--the-idea-of-a-university`), a publicação
(`pub--ecclesiae--a-ideia-de-uma-universidade--2020`) e duas pessoas (Newman e
o tradutor). A região `seculo-xix` ganhou Newman em `held_by`; `coverage`
continua `thin` até você revisar. A lacuna `education--g02` passou a
`accepted`.

**O que a conferência achou.** Editora, data (3/5/2020), 444 páginas,
16 × 23 cm e ISBN coincidem em várias livrarias e catálogos, e os dois dígitos
verificadores fecham. **O tradutor não aparece em nenhuma fonte** que eu
consegui consultar — Bruno Alexander fica como informado por você.

**O que continua pendente.**
- Confirmar o tradutor e se a edição traz só os Discursos ou também as
  Palestras.
- A EDUSC publicou em 2001 um *Newman e a ideia de uma universidade*, não
  pesquisado.
- O salto cronológico que motivou a lacuna continua visível no movimento I:
  Newman não está na cadeia histórica, está no VII. E o século XVIII
  (`iluminismo-seculo-xviii`) continua sem obra própria.
