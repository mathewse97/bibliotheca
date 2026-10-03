# Regras de curadoria da Bibliotheca

Documentação canônica de **como um agente deve raciocinar sobre esta
biblioteca e modificá-la**. O `README.md` descreve a mecânica — estrutura de
pastas, build, interface, gravação de estado. Este documento descreve o
julgamento: o que pode ser decidido sozinho, o que precisa de aprovação, e o
que nunca pode ser feito em silêncio.

**Precedência.** Uma instrução direta do Mathews vence este documento; este
documento vence o julgamento do agente. Quando este documento e um arquivo
canônico discordarem, o arquivo é o fato e a regra é aqui — e a divergência
deve ser **relatada**, nunca resolvida em silêncio.

Onde uma regra já tem um mecanismo, o mecanismo é citado em vez de reexplicado.

---

## 0 · Postura

### 0.1 Listas de bootstrap são hipóteses, não estrutura autoritativa

Uma lista fornecida pelo Mathews é uma seleção inicial e uma hipótese de
trabalho — não uma afirmação de completude nem uma taxonomia final. O agente
avalia criticamente nome, pergunta, escopo, critérios, coerência interna e
relação com as coleções existentes, em vez de assumir que estão corretos.

**Uma coleção pode ser pequena, parcial e deliberadamente incompleta.** O
número de obras nunca é, por si só, um defeito. Não existe obrigação de
"completar" uma coleção.

### 0.2 Coleções também são hipóteses

Nome, pergunta, escopo, critérios — e mesmo a suposição de que um conjunto de
obras pertence a **uma** coleção — são provisórios enquanto não forem
explicitamente estabelecidos. Reavaliar isso à medida que a evidência se
acumula é parte do trabalho normal, e o resultado da reavaliação é uma
**proposta**, nunca uma mudança aplicada. Ver §4 e §5.

O gatilho é evidência, **não tamanho**. Uma coleção pode estar errada com três
obras: a pergunta de escopo em aberto de `culture` foi detectada com três.

### 0.3 A incerteza permanece visível

Uma conclusão provisória nunca é convertida em certeza pela sua apresentação.
Isto não é estilo: é a regra que impede a biblioteca de mentir sobre o que
sabe.

| O que | Como fica visível |
|---|---|
| Dados não pesquisados | `research_status: not_researched`; campos ficam `null`, e a interface escreve *não pesquisado* em vez de deixar em branco |
| Conclusão que pode envelhecer | `check:` em `evidence`, revalidado a cada build; `revalidation.status` ∈ `current \| stale \| unverifiable` |
| Afirmação que depende de julgamento | `check: null` + `checkable: false` + `reason`. Fingir um predicado é pior do que assumir o limite |
| Lacuna dependente de cobertura cruzada | `provisional: true` + `recheck_after` |
| Campo inferido pelo agente | `provisional.inferred_by_claude`, e `*_by: claude \| voce` no campo |
| Obra sem coleção por decisão | `pending_assignment` — declarada, e por isso isenta da checagem de órfãs |

Corolário: **a interface não interpreta um campo vazio.** Um `tensions: []` é
um fato; se significa algo, quem o diz é a revisão da coleção.

---

## 1 · As distinções sobre as quais o modelo se apoia

Nenhuma delas é terminologia. Cada uma existe porque colapsá-la destrói
informação que a biblioteca precisa.

| Distinção | O que separa | Mecanismo |
|---|---|---|
| **Obra × Publicação** | A obra é a unidade **intelectual** — livro, ensaio, conferência, diálogo, tratado (`form`). A publicação é o **objeto físico**, e pode conter várias obras | `works/*.md` e `publications/*.md`; a junção é `contains`, e o veredito de recomendação vive **no par**, não na publicação — um volume pode ser o veículo certo para uma obra que carrega e o errado para outra |
| **Coleção × Participação** | A coleção é um argumento; a participação é a entrada de uma obra nele, e carrega atributos próprios | Entradas de `sequence`: `role`, `demand`, `requires`, `why_here`, `scope`. Um registro canônico de obra, várias participações — papel e posição mudam por coleção |
| **Movimento × Caminho** | O movimento **organiza** o que a coleção contém, em unidades com propósito declarado. O caminho é uma **rota alternativa** sobre os mesmos membros | Entradas `movement:` dentro de `sequence`; `paths:` à parte, com `declares` e `excludes_by_design` |
| **★ core × núcleo-duro** | `core` marca importância **dentro da coleção completa**; o caminho é uma rota comprimida. Uma obra estrelada fora de um caminho é normal | `core: true` na participação; `paths[].works`. **Os dois nunca são reconciliados** — o sistema pode *sinalizar* (`flagged_omissions`) e nunca corrigir; ao dispensar um sinal ele vai para `accepted_omissions` e não volta |
| **Escopo × Cobertura × Prosseguimento** | O escopo é o que a coleção **reivindica**; a cobertura é o que ela **contém**; o prosseguimento é o que o Mathews **está perseguindo** | `question` + `inclusion_criteria`; `scope_map.regions[].coverage` ∈ `covered\|thin\|absent`; `.pursuit` ∈ `open\|not-pursued`. Ver §2.1 |
| **Estado pessoal × estado curatorial** | Leitura, posse, prioridade pessoal e nota são do Mathews. Bibliografia, sequência, papel, veredito e lacunas são curatoriais | `state/personal.yaml` é o **único** arquivo que a interface escreve; os campos editáveis vêm de `config/writable-fields.yaml`. Leitura pertence à **obra**; posse pertence à **publicação** |
| **Necessidade × contexto** | A necessidade mede quanto o argumento da coleção enfraquece sem a obra. O contexto é disponibilidade, idioma, proximidade cultural, saliência local | `necessity:` e `context:` nos registros de lacuna. Ver §2.4 |

---

## 2 · Regras derivadas dessas distinções

### 2.1 Escopo, cobertura e prosseguimento

Os critérios de inclusão derivam da **pergunta** da coleção — **nunca** dos
seus membros atuais. Critérios inferidos do conteúdo descrevem o conteúdo, e
tornam a coleção infalsificável: ela não pode ter lacunas porque tudo o que
qualifica já está lá.

Teste obrigatório, registrado em `inclusion_criteria.test_applied`:
> *Este critério excluiria uma obra que responde claramente à pergunta da
> coleção?* Se sim, o critério está descrevendo a amostra.

O `scope_map` é o território reivindicado, e é contra ele que a cobertura
mede. Três consequências:

- Uma região **vazia não está fora de escopo** — está vazia. Fora de escopo é
  uma afirmação dos critérios; vazio é um fato do mapa.
- Uma região `absent` **não é uma obra em falta**, e a soma das regiões não
  cobertas não é uma dívida. A interface apresenta cobertura **neutramente**,
  sem contagens em cor de alerta.
- `pursuit: not-pursued` registra uma decisão do Mathews. Não é defeito nem
  pendência, e a cobertura não a levanta.

Descrições de região explicam **que perguntas caem ali**. Nomes de obras
candidatas não entram no mapa: pertencem à camada de curadoria, em
`review/gaps/`, e só quando existe um registro que os justifique.

Uma coleção sem escopo declarado **não recebe um `scope_map` especulativo**
(`scope_map: null`). Inventar território antes de o escopo ser decidido produz
a fila de recomendações que a §2.2 proíbe.

### 2.2 As quatro operações, e o que é automático

| Operação | O que é | Automática? |
|---|---|---|
| **Importação** | Preservar e estruturar a seleção do Mathews | Sim, quando ele envia uma lista |
| **Avaliação curatorial** | Avaliar se a coleção, a pergunta, o escopo, os critérios, a coerência interna e a relação com as outras coleções fazem sentido | **Sim, em todo import e em toda obra nova** |
| **Detecção e revalidação de lacunas** | Identificar ausências estruturalmente significativas; reexecutar a evidência das lacunas existentes | **Sim, a cada build** |
| **Preenchimento e recomendação** | Propor obras concretas para uma lacuna | **Não. Só quando o fluxo de curadoria exigir ou o Mathews pedir** |

Reavaliação automática **não é expansão automática**. Depois de reavaliar, a
coleção fica deliberadamente incompleta quando nada mais foi pedido.

Uma lacuna pode existir como **detecção pura**, com `candidates: []`. Isso é um
estado normal e não um registro incompleto.

Nenhuma lista grande de recomendações é produzida proativamente. Quando uma
lacuna ou candidato emerge e nenhuma ação foi pedida, o registro é provisório.

**O teto: 3 propostas abertas por coleção.** Cobertura e proposta são saídas
diferentes, e mantê-las separadas é o que impede um escopo largo de produzir
uma enxurrada de sugestões: o mapa de cobertura não tem limite — o mapa é o
mapa — e as propostas de obra concreta têm. [recuperado de
`review/education.md` §3.0 e §3.1, que citam o teto como regra do §I]

### 2.3 Quatro coisas conceitualmente distintas

Nunca colapsar:

1. **Lacuna genuína** — ausência que compromete a completude intelectual da coleção.
2. **Obra complementar** — valiosa, mas a coleção não fica incompleta sem ela.
3. **Leitura opcional / enriquecedora** — interessante, fora do currículo central.
4. **Redundância** — obra boa ou famosa cuja contribuição a biblioteca já cobre.

A quarta é a mais útil e a menos óbvia: um veredito de redundância registrado
impede que a mesma sugestão volte todo ano — como `verdict: rejected` numa
publicação. E é julgada **contra o currículo, não contra o catálogo**: duas
obras que pareceriam redundantes em abstrato deixam de o ser quando a ordem
do Mathews faz de uma a porta de entrada da outra.

Toda recomendação traz: por que acrescentar, que lacuna ou função atende, e
por que é preferível aos outros candidatos considerados.

E na sua forma estrita: **sem registro de lacuna, não há recomendação.** Toda
proposta nomeia a lacuna que fecha **pelo id**. Um livro que o agente apenas
ache interessante não tem onde ir — não existe campo para ele, e é essa única
restrição que remove a maior parte do ruído antes de ele ser escrito. A forma
completa de uma proposta está em `config/gap-records.yaml`, `volume_rules`.
[recuperado do blueprint §I — ver §9]

A mesma análise corre **para dentro**: duas obras cobrindo a mesma contribuição
onde uma bastaria, um membro que deixou de satisfazer os critérios declarados da
própria coleção, um período ou uma tradição com peso desproporcional. A saída é
uma proposta de rebaixamento ou remoção **com argumento** — e nada é removido,
rebaixado ou reordenado sem a decisão do Mathews. [idem]

### 2.4 Necessidade hierarquiza; contexto não

`necessity` vem do sinal estrutural e é a **única** coisa que determina
prioridade. `context` — disponibilidade no Brasil, idioma, proximidade
cultural, saliência local — é registrado e **nunca** hierarquiza. Atua apenas
como **desempate entre candidatos de necessidade comparável**, exatamente como
a hierarquia de idiomas decide dentro de uma faixa de qualidade e nunca entre
faixas.

Uma obra não sobe por ser fácil de comprar em português nem desce por ser
difícil de encontrar. A falha que isto previne é silenciosa: uma biblioteca
que se remodela em torno do que o mercado do dono estoca, com cada decisão
individual parecendo razoável.

### 2.5 Aquisição e capa — onde vivem, e o que nunca fazem

Capa e fonte de compra pertencem à **publicação**. Uma obra não tem capa nem
preço: *A República* não tem capa, a edição da Gulbenkian tem. Como a
publicação já é uma entidade própria (§1), não foi preciso mecanismo paralelo —
os dois blocos entram nela.

Aquisição é uma instância concreta de **contexto** (§2.4) e obedece à mesma
regra: registra-se, e não hierarquiza. Vendedores são fonte de nível 6–7 da
hierarquia de fontes do **§E** (`config/bibliographic-rules.md`): estabelecem
que um livro existe e pode ser comprado, e nada mais. Nem disponibilidade, nem preço, nem popularidade, nem avaliações tocam
`verdict`, `necessity` ou prioridade.

**Ausência de anúncio não é defeito bibliográfico.** Ausência de capa também
não. A interface apresenta as duas ausências neutramente, e a build não as
reporta como problema.

O campo que impede a fabricação é `match_basis`: um anúncio só significa algo
se soubermos **como** se sabe que é desta edição. Marketplaces fundem edições
rotineiramente — mesmo título, outra editora, outro tradutor, avaliações
somadas. `unconfirmed` guarda a pista e a interface **não** a apresenta como
opção de compra desta edição. Link, ASIN, ISBN, correspondência ou fonte de
capa **nunca** são inventados ou deduzidos: na dúvida o campo fica vazio.

A imagem de capa vive no repositório (`covers/`), não como link remoto: um
link de vendedor quebra, troca de edição sem aviso e não funciona offline.

Disponibilidade é o dado que envelhece mais depressa da biblioteca, e por isso
cada fonte carrega a sua própria `checked`, com frescor derivado a cada build.
Esquema e vocabulário de vendedores em `config/acquisition.yaml`; forma do
registro em `publications/_TEMPLATE.md`.

### 2.6 Ao propor o interlocutor de uma posição

Quando uma coleção contém uma posição sem a sua oposição, a obra a propor é a
**melhor** exposição do outro lado, não a mais fácil de refutar. Recomendar um
crítico fraco é pior do que não recomendar: deixa a coleção parecer
equilibrada continuando unilateral. Vale nos dois sentidos, independentemente
do lado para o qual a coleção pende.

### 2.7 Uma ausência pode ser uma participação em falta, e não uma compra

Antes de tratar uma ausência como obra a adquirir, verificar se a obra **já
está na biblioteca**, vinda de outra coleção. Se estiver, o que falta é uma
participação — uma entrada nova do mesmo registro canônico, com papel, posição
e escopo próprios nesta coleção — e não uma aquisição. Uma obra em três
coleções continua sendo um arquivo.

Duas consequências práticas, ambas já observadas no acervo: uma análise de
lacunas feita com poucas coleções importadas produz **falsos positivos**,
porque parte do que parece ausente está nas listas que ainda faltam — é o que
`recheck_after: outras-colecoes-importadas` registra. E decidir as
participações **antes** das lacunas é mais barato e altera-as: aceitar uma
participação pode reduzir a severidade de uma lacuna, ou dissolvê-la.

Forma do registro: o bloco `memberships_not_gaps` de `review/gaps/*.yaml`.

[recuperado de `review/political-thought.md` §2.5 e §3, e de
`review/education.md` §4, que o nomeia como o caso previsto pelo §I]

### 2.8 Literatura entra junto do que ela ilumina — decisão do Mathews, 2026-09-27

Vale para **todas** as coleções, não só para Política.

Uma obra literária que trata o mesmo problema de uma obra teórica, histórica ou
técnica do acervo é colocada **dentro do movimento que ela complementa**, e não
agrupada com as outras obras literárias por serem literatura. O agrupamento por
gênero é uma etiqueta; a colocação junto do que a obra ilumina é o argumento.

Três camadas, e as três são exigidas quando se aplica esta regra:

1. **Posição** — a participação entra no movimento da obra que ela trata, com
   `role: literary-treatment`. O papel diz que a obra está ali como tratamento
   literário, e é por isso que o movimento não deixa de ser verdadeiro.
2. **Aresta** — o registro canônico da obra literária recebe uma relação
   `literary_treatment_of` apontando para a obra tratada. A build deriva a
   inversa, e a tela da obra teórica passa a mostrar por quem ela é tratada
   literariamente. Sem a aresta a colocação fica muda: quem chega pela obra
   teórica não descobre a literária.
3. **Caminho**, quando couber — se o par vale como roteiro de leitura, um
   `path` o declara. É degrau 2 da §4, desenvolvimento interno normal.

Isto **não** afrouxa nada. A colocação continua sendo conclusão de pesquisa e
não de impressão (§6.9 regra 4): uma obra literária com `form` e `work_type`
nulos não tem colocação defensável aqui tampouco. E a regra não autoriza
realocar em silêncio membro nenhum: mover uma obra que já está numa sequência é
mudança de ordem, exige aprovação explícita e fica registrada em
`order_changes` (§3, §7).

Consequência conhecida e aceita por ele na mesma decisão: um movimento cuja
única razão de existir era agrupar literatura por gênero deixa de ter razão de
existir. O caso é `political-thought`, movimento X — e a redistribuição dos seus
seis membros é obra a obra, com pesquisa antes e aprovação dele em cada uma.
Ver o cartão `d-pol-movimento-x` em `review/decisions.yaml`.

---

## 3 · Preservação

A seleção e a ordem do Mathews são preservadas **exatamente**, salvo mudança
estrutural que ele tenha aprovado.

| Mecanismo | O que garante |
|---|---|
| `original_order` | A lista dele, verbatim, permanentemente |
| `order_changes` | Todo desvio, **com razão** — um desvio sem razão falha na validação |
| `structural_changes` | Mudanças de **cardinalidade** (split, merge, deduplicação), com os efeitos declarados **em separado**: efeito na biblioteca ≠ efeito na coleção. Confundi-los faz a biblioteca mentir sobre o próprio tamanho |
| `why_here` + `why_here_by` | O raciocínio dele fica marcado como dele. O agente pode propor alternativa em `review/`, nunca sobrescrever |
| `provisional.authored_by_you` | Que campos são literalmente dele |

O agente **não reordena, não acrescenta e não remove** para melhorar a
aparência de uma coleção. Nenhuma obra entra para deixar a coleção mais
completa.

**Atualização — decisão do Mathews, 2026-09-25.** A coleção como definida em
conjunto (obras, ordem, movimentos, depois de curadoria e pesquisa) é o
**registro principal**. `original_order` e `order_changes` deixam de ser
obrigatórios: os que existem ficam nos arquivos como histórico, não aparecem na
interface e não precisam ser mantidos em coleções novas. Continua valendo: o
agente não reordena, não acrescenta e não remove sem aprovação dele.

---

## 4 · A escada de escalonamento

Quando a evidência se acumula, responder no **degrau mais baixo que resolva**.
O desenvolvimento interno é a forma normal e preferida de uma coleção evoluir.

| Degrau | Resposta | Quando |
|---|---|---|
| 1 | Reorganizar **movimentos** — por período, tradição, problema, escola | Primeira resposta ao crescimento. Quase sempre suficiente |
| 2 | Acrescentar um **caminho** | Quando existe uma rota alternativa útil sobre os mesmos membros |
| 3 | **Refinar** pergunta, escopo ou critérios, mantendo a coleção | Quando a coleção continua uma, mas se descreve mal |
| 4 | **Renomear** | Quando o nome deixou de representar a pergunta |
| 5 | **Dividir** | Quando os membros se tornaram perguntas genuinamente distintas que uma coleção não representa coerentemente |
| 6 | **Fundir** | Quando a distinção entre duas coleções deixou de ser intelectualmente significativa |

**A exceção à preferência pelo interno.** Preferir subdivisão interna **exceto
quando a ambiguidade não resolvida corrompe a maquinaria de escopo**: se uma
coleção contém de fato duas perguntas, toda análise de cobertura mede contra a
**união** de dois territórios e o `scope_map` fica sem sentido para ambas.
Nesse ponto, não dividir é a escolha mais destrutiva.

O sistema não otimiza para preservar a taxonomia inicial nem para criar
coleções novas. Otimiza para a taxonomia mais coerente que a biblioteca
acumulada sustenta.

---

## 5 · Aprovação e reversibilidade

Os degraus 3 a 6 são **propostas curatoriais**, nunca mudanças automáticas. O
agente **não renomeia, não divide, não funde e não redefine em silêncio**. Ele:

1. registra o problema estrutural;
2. explica a evidência que o sustenta;
3. mostra a alternativa proposta;
4. **espera a decisão do Mathews.**

Mecanismo: `config/structural-proposals.yaml` define o esquema, os tipos, os
estados e o portão de aprovação; as propostas vivem em
`review/structural/<colecao>.yaml`, com modelo em `_TEMPLATE.yaml`. Os degraus
1 e 2 — movimentos e caminhos — **não** são propostas estruturais: são
desenvolvimento interno normal e não passam por este registro.

**Estados:** `open` (registrada, nada aplicado) · `approved` (o Mathews
aprovou; a mudança pode ser aplicada) · `rejected` (recusada, e fica no arquivo
para que a mesma proposta não volte — como um veredito de redundância).

**O portão.** A build não aplica nada, mas garante que nada foi aplicado sem
decisão registrada. São erros de integridade: uma proposta `approved` ou
`rejected` sem bloco `decision`; uma `decision.by` que não seja `voce`; e uma
entrada de `lineage` numa coleção que cite proposta inexistente ou não
aprovada. Esta última é a que importa: ela detecta, **depois do fato**, uma
mudança estrutural aplicada em silêncio.

Uma mudança aprovada preserva a história da estrutura original e é reversível
através de `id_aliases` e `lineage` na coleção — campos opcionais que ficam
**ausentes** enquanto nenhuma mudança aprovada tiver acontecido. Cada entrada
de linhagem cita a proposta que a autorizou e declara `reversible_by`.

---

## 6 · Quando uma obra nova entra

### 6.0 A lista é a entrada, não a pesquisa — decisão do Mathews, 2026-09-06

> O que o Mathews fornece é **entrada inicial**, nunca a pesquisa bibliográfica
> final. Para cada obra nova, o agente **pesquisa e verifica primeiro** tudo o
> que possa ser resolvido externamente — identidade da obra, autoria, natureza,
> edições e publicações, editora, ano, ISBN, idioma, traduções, relações entre
> edições, e os demais dados bibliográficos e curatoriais necessários.
>
> **Só se pergunta** quando resta uma ambiguidade que a pesquisa confiável não
> resolve, ou quando a decisão depende genuinamente dele.

Vale para toda entrada de obra, não só para a coleção em que a regra foi
enunciada.

Por que precisa de estar escrito, já que o passo 2 abaixo sempre esteve antes
do passo 3: a ordem dos passos diz *o que* fazer, e não impede o atalho de
devolver ao Mathews uma pergunta que uma busca teria respondido. Esse atalho
transfere-lhe o trabalho e disfarça-se de prudência — parece o portão de
confiança do passo 8, e não é. **O portão do passo 8 aplica-se depois da
pesquisa, não em vez dela**, e a §E.2 do `bibliographic-rules.md` diz a mesma
coisa em miniatura: uma correspondência, seguir; várias, perguntar — perguntar
é o que sobra quando a resolução falha.

Duas coisas que a regra não muda. A pesquisa continua sujeita ao §7: **nada de
inventar** para preencher um campo que a busca não resolveu — o campo fica
`null` e o que falta é nomeado. E continua sujeita ao §0.3: o que foi
verificado e o que foi apenas relatado permanecem distinguíveis, por
`research_status`, por `confidence` na proveniência e pelo tier da fonte.

---

Uma obra nova dispara o **pipeline completo de curadoria e revalidação de
consistência** — nunca contorna a estrutura existente em silêncio:

1. resolver e deduplicar contra ids, aliases, autoria normalizada e ISBN;
2. pesquisar a obra e as suas publicações físicas segundo os critérios de edição;
3. determinar a que coleções pertence genuinamente, com papel, posição,
   prerequisitos locais e argumento **por coleção** — três coleções, três
   argumentos, não um copiado três vezes;
4. estabelecer relações com o que já existe, incluindo as oposições;
5. reavaliar as coleções afetadas: `scope_map`, cobertura, registros de lacuna,
   relações, prerequisitos e lógica de sequência;
6. **invalidar conclusões que envelheceram** — é para isso que existem os
   `check:`; uma lacuna cuja evidência deixou de valer fica `stale`, com a
   prosa original preservada ao lado do que os dados dizem agora;
7. atribuir `priority_library` e **não tocar** em `priority_personal`;
8. **portão de confiança**: qualquer colocação intelectualmente ambígua vai
   para revisão e é levantada, não decidida;
9. validar e registrar.

Nada disso autoriza expansão. Regiões vazias continuam vazias.

---

## 6.9 Movimentos, e onde uma obra entra — decisão do Mathews, 2026-09-19

Nasceu de um erro meu, e o erro vale mais escrito do que esquecido: Kant,
*Fundamentação da Metafísica dos Costumes*, e Marcuse, *O Homem
Unidimensional*, foram acrescentados ao fim da sequência de Pensamento
Político e caíram dentro do movimento **X. Literatura como crítica política**,
porque um movimento é uma **faixa** — tudo o que vem depois do cabeçalho
pertence a ele até o cabeçalho seguinte. Kant ficou registrado como literatura
distópica. Foi o Mathews quem viu.

Quatro regras, todas dele:

1. **Movimento é território, não etiqueta.** Um movimento nomeia uma região
   ampla do argumento da coleção, e deve continuar verdadeiro depois de
   entrarem mais obras.

2. **Nunca criar movimento para acomodar uma obra.** Se uma obra não cabe em
   nenhum movimento existente, isso é sinal de escopo, e vai à escada do §4 —
   não se resolve com um cabeçalho novo. Um movimento por obra é a
   fragmentação que a §4 existe para evitar, disfarçada de organização.

3. **Acrescentar ao fim NÃO é a opção conservadora.** Numa sequência com
   movimentos, o fim tem dono. Colocar ali é uma afirmação sobre a obra, e a
   afirmação costuma estar errada.

4. **A colocação é conclusão de pesquisa, não de impressão.** Antes de
   colocar uma obra num movimento, o agente estabelece o que ela é — forma,
   gênero, data, tradição — pelo §E, e escreve o porquê da colocação citando
   a fonte. Uma obra com `form` e `work_type` ainda nulos não tem colocação
   defensável; tem palpite.

### A ordem do Mathews, e o que o agente faz com ela

> **Decisão dele, 2026-09-19:** a ordem que ele envia é **sugestão inicial**.
> O agente **valida a ordem, propõe melhorias e diz os porquês**, sempre com
> pesquisa que sustente a colocação — nunca por inferência.

Isto **não** afrouxa o §7 nem o §5: propor não é aplicar. Toda alteração de
ordem continua a exigir aprovação explícita e fica registrada em
`order_changes`, com `from`, `to`, razão e `reversible_by`, obra a obra.

O que muda é o dever positivo: **o silêncio deixou de ser uma opção
defensável**. Ver uma obra em posição errada e não dizer nada passa a ser
falha, do mesmo tipo que alterar a ordem sem perguntar. A primeira aplicação
desta regra está em `collections/political-thought.md`, `order_changes` —
até 2026-09-19 esse campo estava vazio em todo o acervo.

---

## 7 · O que um agente nunca faz

- Alterar a seleção ou a ordem do Mathews sem aprovação explícita.
- Renomear, dividir, fundir ou redefinir uma coleção em silêncio.
- Acrescentar obras para que uma coleção pareça mais completa.
- Tratar uma região `absent` como uma compra devida.
- Produzir uma grande lista de recomendações proativamente.
- Derivar `inclusion_criteria` do conteúdo atual da coleção.
- Deixar o contexto — idioma, preço, disponibilidade, saliência local —
  hierarquizar necessidade.
- Apresentar uma conclusão provisória, não pesquisada ou desatualizada como
  fato estabelecido.
- Sobrescrever o raciocínio do Mathews (`why_here_by: voce`) com o seu.
- Escrever em `state/personal.yaml` — esse arquivo é da interface e dele.
- Escrever em arquivos canônicos a partir da build: a build só escreve em
  `_generated/`.
- Inventar dado bibliográfico não verificado para preencher um campo vazio.
- Criar um movimento para acomodar uma obra que não cabe nos existentes (§6.9).
- Colocar uma obra numa sequência sem ter estabelecido, por pesquisa, o que
  ela é — forma, gênero, data, tradição (§6.9).

---

## 8 · Regra × maquinaria

A diferença entre o que é regra e o que é código, explícita.

### 8.1 Implementado

| Mecanismo | Onde |
|---|---|
| Propostas estruturais como registro próprio: tipos `refine\|rename\|split\|merge`, estados `open\|approved\|rejected`, evidência com `check:` revalidada a cada build como nos registros de lacuna | `config/structural-proposals.yaml`, `review/structural/*.yaml`, `_TEMPLATE.yaml` |
| Portão de aprovação: `approved\|rejected` exige `decision`; `decision.by` tem de ser `voce`; toda entrada de `lineage` tem de citar proposta existente **e aprovada** | validado pela build; violações viram problemas de integridade no índice |
| Validação de forma: campos obrigatórios, ids únicos, tipo e estado válidos, coleções citadas existentes | idem |
| `id_aliases` e `lineage` em coleções, com verificação de colisão de alias | campos **opcionais**; ausência tratada como vazio. **Nenhuma coleção os tem hoje**, e nenhum dado histórico foi inventado |
| A interface distingue os três estados e explica o estado vazio | *Revisão → Propostas estruturais* |
| Capa e fontes de aquisição na publicação, com `match_basis` obrigatório para qualquer link, frescor derivado por data e capas embutidas na interface | `config/acquisition.yaml`, `covers/`, `publications/_TEMPLATE.md`; validado pela build |

### 8.2 Continua sendo julgamento, não código

| Regra | Estado |
|---|---|
| Detectores automáticos de sinal estrutural: membros que falham os critérios da própria coleção; grafo de relações da coleção separado em componentes sem arestas entre si; sobreposição de membros entre duas coleções acima de um limiar; um movimento que cresce até dominar os demais | **Não implementado.** Quem percebe o sinal é o agente; o que existe é o lugar para registrá-lo com disciplina |
| Aplicar uma mudança aprovada — renomear os arquivos, realocar membros num split, fundir sequências — e escrever a linhagem correspondente | **Não implementado.** Feito à mão, sob aprovação. A build verifica o resultado depois, não executa a operação |
| Desfazer uma mudança a partir de `reversible_by` | **Não implementado.** O campo declara como reverter; reverter continua sendo uma operação manual |
| Detectar que uma proposta ficou obsoleta porque a coleção mudou | Parcial: a evidência da proposta é revalidada e pode ficar `stale`, mas nada rebaixa a proposta automaticamente |
| Validar vocabulários — `role`, `demand`, `work_type`, `form`, tipo de lacuna, tipo de relação | **Não implementado.** `config/vocabularies.yaml` documenta o que existe; a build não o lê. Um valor inventado não produz erro de integridade, só um acervo incoerente. A exceção parcial: um tipo de relação fora do mapa de `tools/build.py` passa adiante sem inversão declarada — também sem erro |
| Validar a forma de um registro de lacuna | **Não implementado.** `config/gap-records.yaml` documenta a forma; a build valida apenas o que executa — os predicados de `check` e o resultado da revalidação. Campo obrigatório em falta não é reportado |
| Validar `source_tier` | **Não implementado.** A hierarquia 1–7 está declarada em `config/bibliographic-rules.md` §E.1 desde a recuperação de 2026-09-06, mas a build não verifica se o tier atribuído corresponde ao tipo de fonte — só que uma entrada de aquisição cita um `retailer` conhecido |

---

## 9 · Onde vive cada seção

As seções `§C`, `§E`, `§F` e `§I` são citadas por todo o repositório — pelos 53
registros de obra, pelo modelo de publicação, por `config/acquisition.yaml`,
por este documento e pelas três revisões. Elas viviam **fora** do repositório,
num documento externo que não faz parte da biblioteca. Cada uma tem agora um
lugar canônico, com o mesmo nome, para que todas as referências existentes
resolvam:

| Seção | Assunto | Onde vive |
|---|---|---|
| **§C** | Identificadores | `config/bibliographic-rules.md` §C |
| **§E** | Hierarquia de fontes e pesquisa de edição | `config/bibliographic-rules.md` §E |
| **§F** | Hierarquia de idiomas | `config/bibliographic-rules.md` §F |
| **§I** | Lacunas e recomendações | **este documento** — §0.1, §2.1 a §2.7, §3, §4 e §7 |

Duas partes do §I não estavam neste documento e foram trazidas para cá a partir
das revisões que as citavam: o **teto de três propostas abertas por coleção**
(§2.2) e a regra de que **uma ausência pode ser uma participação em falta e não
uma compra** (§2.7).

### 9.1 A segunda rodada de recuperação — 2026-09-06

O Mathews forneceu o **blueprint original**, arquivado em
`sources/blueprint-2026-09-05.md`. Ele fechou três dos quatro buracos que a
primeira rodada tinha declarado não recuperáveis: a **hierarquia de fontes 1–7**
completa, o **procedimento de seleção de edição** e o **fluxo de pesquisa** do
§E, e vários vocabulários (`form`, `sequence_kind`, `research_status`,
`gap.status`, os tipos de lacuna com os seus sinais).

**Precedência, estabelecida por ele:** decisões diretas dele e regras aprovadas
posteriores › dados canônicos e arquitetura atual › esta documentação › o
blueprint › inferência marcada. **Uma regra atual não é substituída porque o
blueprint diz outra coisa**, e onde os dois divergem o blueprint fica anotado
como superado — tanto no arquivo de origem quanto na regra. Divergências
preservadas dessa forma: a hierarquia de idiomas fixa do §F, o campo `severity`
dos registros de lacuna (hoje `necessity` + `context`), os registros de lacuna
em Markdown (hoje YAML com evidência revalidável), e os valores em inglês do
estado pessoal (hoje portugueses, em `config/writable-fields.yaml`).

**O que continua NÃO RECUPERÁVEL, e o blueprint também não resolve:** quais são
as 4 obras a que a emenda de identificadores se aplica. Ele afirma o número e dá
um exemplo (Tucídides); não nomeia as outras três. Um agente que precise delas
**levanta a questão** (§6.8); não as deduz (§7).

Vocabulários controlados: `config/vocabularies.yaml`.
Forma dos registros de lacuna: `config/gap-records.yaml`.
Fonte histórica arquivada: `sources/blueprint-2026-09-05.md`.

---

*Este documento é regra, não dado. A build não o lê. Alterá-lo muda como o
agente raciocina; não muda nada na biblioteca.*
