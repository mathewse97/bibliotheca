# Regras bibliográficas da Bibliotheca — §C, §E, §F

Documentação canônica de **identificadores (§C)**, **hierarquia de fontes e
pesquisa de edição (§E)** e **seleção de edição e preferência de idioma (§F)**.

Estas três seções eram citadas por cerca de sessenta arquivos do repositório —
todos os registros de obra, o modelo de publicação, `config/acquisition.yaml`,
`config/curation-rules.md` e as três revisões — e **viviam fora dele**, num
documento externo. Uma referência que não resolve é pior do que nenhuma: um
agente que lê `# a pesquisar (§E)` num registro de obra e não encontra §E em
lugar nenhum acaba por inventar a regra. Este arquivo dá às seções um lugar
canônico **com os mesmos nomes**, para que todas as referências existentes
passem a resolver sem que nenhum arquivo de obra precise ser tocado.

**Precedência.** Como em `curation-rules.md`: uma instrução direta do Mathews
vence este documento; este documento vence o julgamento do agente. Quando este
documento e um arquivo canônico discordarem, o arquivo é o fato — e a
divergência deve ser **relatada**, nunca resolvida em silêncio.

---

## 0 · Índice das seções

| Seção | Assunto | Onde vive |
|---|---|---|
| **§C** | Identificadores | este arquivo, §C |
| **§E** | Hierarquia de fontes e pesquisa de edição | este arquivo, §E |
| **§F** | Seleção de edição e preferência de idioma | este arquivo, §F |
| **§I** | Lacunas e recomendações | `config/curation-rules.md` — mapa em §9 de lá |

Vocabulários controlados: `config/vocabularies.yaml`.
Forma dos registros de lacuna: `config/gap-records.yaml`.
Fonte histórica arquivada: `sources/blueprint-2026-09-05.md` — precedência 4.


### Recuperação — carregue a seção, não o arquivo

Este índice nomeia o que cada seção governa; o conteúdo da regra está na
própria seção e não é repetido aqui.

| seção | título exato | governa |
|---|---|---|
| §C | `# §C · Identificadores` | forma dos ids, formas observadas, `id_aliases` |
| §E | `# §E · Hierarquia de fontes e pesquisa de edição` | escala de fontes, suposições recusadas, fluxo em dez passos, o que a pesquisa produz e o que nunca faz, quando uma obra está pesquisada, `work_type` |
| §F | `# §F · Seleção de edição e preferência de idioma` | procedimento, preferência de idioma, edições bilíngues |

Extrair uma seção sem ler o arquivo inteiro:

```bash
awk '/^# §E/{f=1} /^# §F/{f=0} f' config/bibliographic-rules.md
awk '/^# §F/{f=1} f'              config/bibliographic-rules.md
```

Contrato de leitura do repositório: `AGENT.md`.

## 0.1 · Método deste documento, e as suas fontes

Cada item traz a sua proveniência entre colchetes. Nada aqui foi reconstruído
por inferência, completado por plausibilidade, ou escrito de memória de
conversa.

**Duas rodadas de recuperação.** A primeira (2026-09-06) recuperou o que
sobrevivia nos próprios arquivos canônicos — as regras que outros arquivos
citavam ou aplicavam. A segunda, no mesmo dia, usou o **blueprint original**,
que o Mathews forneceu como material histórico e que está arquivado em
`sources/blueprint-2026-09-05.md`. Três blocos NÃO RECUPERÁVEL foram fechados
por ela; um permanece aberto (§C.1).

**Ordem de precedência**, estabelecida pelo Mathews em 2026-09-06 e válida para
todo este documento:

1. Decisões diretas dele e regras aprovadas posteriores.
2. Dados canônicos atuais e arquitetura implementada.
3. `config/curation-rules.md` e a demais documentação atual.
4. O blueprint arquivado — só para recuperar regra historicamente perdida.
5. Inferência do agente, e só quando marcada como inferência.

Uma regra atual **não é substituída** porque o blueprint diz outra coisa. Onde
os dois divergem, o blueprint está anotado como superado, tanto aqui quanto no
arquivo de origem — e o texto histórico fica legível ao lado da correção, para
que a divergência seja visível em vez de apagada.

Onde a regra não sobrevive em lugar nenhum, o item aparece como **NÃO
RECUPERÁVEL** e diz o que falta e quem pode supri-lo. Isso é a aplicação de
duas regras já existentes: a incerteza permanece visível [`curation-rules.md`
§0.3] e um agente nunca inventa dado bibliográfico não verificado para preencher
um campo vazio [`curation-rules.md` §7]. Preencher um bloco desses com uma
regra verossímil seria exatamente a falha que este documento existe para
impedir.

---

# §C · Identificadores

## C.1 A regra, e a sua emenda

> **id = título original.** O título original é o único nome que permanece
> constante através de toda tradução que se venha a considerar — que é
> exatamente o que um identificador tem de fazer. Títulos portugueses variam
> entre editoras; títulos ingleses são uma escolha de tradução como qualquer
> outra.
>
> **A emenda**, feita depois do primeiro import: onde o título original é
> instável ou compartilhado, a convenção recorre ao título curto acadêmico
> convencional. Tucídides e Heródoto têm ambos *Ἱστορίαι*; **quatro das
> primeiras quarenta obras** precisaram do recurso. Título original quando
> estável e inequívoco, título curto convencional quando não, `id_aliases`
> sempre.
>
> **Ids nunca são reutilizados.** Um rename registra o valor antigo em
> `id_aliases`, e uma referência pendente é falha ruidosa de validação.

[recuperado: blueprint §C, arquivado em `sources/blueprint-2026-09-05.md`; a
mesma regra e a mesma emenda estão citadas em `review/political-thought.md`
§2.4, como decisão de 2026-09-05]

Estado da emenda: a parte de escolha do título **está aplicada** — o registro
existente é `tucidides--historiai`. A parte `id_aliases` **não está aplicada**:
`id_aliases: []` em todos os 53 registros.

> **NÃO RECUPERÁVEL — e o blueprint também não resolve.** Quais são as 4 obras.
> O blueprint afirma o número e dá **um** exemplo (Tucídides); não nomeia as
> outras três. Um agente **não deve deduzi-las** nem povoar `id_aliases` por
> conta própria: escolher um alias é escolher por que nome uma obra passa a ser
> encontrada, e isso é uma decisão de identificação, não uma limpeza. Levantar,
> não decidir [`curation-rules.md` §6.8].

## C.2 Formas de id observadas no acervo

Convenção lida dos 53 registros de obra, dos ids de coleção, autor, publicação,
lacuna e proposta existentes. É descrição do que há, não uma regra nova:

| Entidade | Forma | Exemplos |
|---|---|---|
| obra | `<autor>--<titulo>` | `platao--politeia`, `orwell--nineteen-eighty-four` |
| obra, vários autores | ids de autor unidos por `-` | `marx-engels--…`, `bauer-wise--…` |
| autor | sobrenome ou nome convencional | `platao`, `ibn-khaldun`, `miriam-joseph` |
| coleção | slug do assunto | `political-thought`, `education`, `culture` |
| publicação | `pub--<editora>--<titulo-curto>--<ano>` | `pub--cultrix--ciencia-e-politica` [modelo: `publications/_TEMPLATE.md`; forma confirmada pelo blueprint §C] |
| lacuna | `<colecao>--g<NN>` | `education--g01` |
| proposta estrutural | `<colecao>--sp<NN>`, sequencial e permanente, nunca reutilizado | `<colecao>--sp01` [declarado: `config/structural-proposals.yaml`] |

Grafia dos slugs, como observada: minúsculas, ASCII sem diacríticos
(`maquiavel`, `platao`, `tucidides`, `dostoievski`), palavras separadas por `-`,
e `--` **apenas** entre autor e título. O id do arquivo é o id do registro: o
nome do arquivo é `<id>.md`.

O ano no id de publicação é parte da forma declarada no modelo. A única
publicação existente não o traz, porque o ano ainda não foi pesquisado. O
blueprint traz um id de exemplo **com** um ano; esse ano é um marcador de
posição — o próprio blueprint declara que nenhum valor bibliográfico nele foi
verificado — e por isso não entrou em registro nenhum.

**Ids de publicação são permanentes e nunca reciclados**, inclusive os de
publicações recusadas: a recusa tem de continuar presa a alguma coisa
[blueprint §C].

## C.3 `id_aliases`

Existe em duas entidades, com propósitos diferentes:

- **obra** — nomes antigos ou alternativos pelos quais a obra continua sendo
  encontrada. É a metade não aplicada da emenda de C.1.
- **coleção** — campo **opcional**, ausente até que um `rename` aprovado
  aconteça. Um alias não pode colidir com o id ou o alias de outra coleção, e a
  build verifica a colisão [declarado: `config/structural-proposals.yaml`,
  `collection_optional_fields`].

---

# §E · Hierarquia de fontes e pesquisa de edição

## E.1 A escala de fontes — completa

Registrada em cada afirmação como `source_tier`:

| Tier | Fonte | Faixa |
|---|---|---|
| **1** | Informação da editora e da edição acadêmica | bibliográfica |
| **2** | Catálogos de bibliotecas universitárias | bibliográfica |
| **3** | Bibliotecas nacionais | bibliográfica |
| **4** | Bases de dados e resenhas acadêmicas | bibliográfica |
| **5** | Fontes bibliográficas em língua original | bibliográfica |
| **6** | Livreiros de reputação — **só disponibilidade** | disponibilidade |
| **7** | Varejistas — **só verificação de compra** | disponibilidade |

[recuperado: blueprint §E, arquivado em `sources/blueprint-2026-09-05.md`. A
hierarquia é do Mathews — o blueprint chama-a "your hierarchy"]

> Os tiers 6 e 7 estabelecem que um livro existe e pode ser comprado. **Nunca**
> estabelecem que ele é bom. A contagem de avaliações de um varejista não é
> evidência e não aparece numa avaliação.

Isto confirma, e não contradiz, o que já estava em `config/acquisition.yaml`:
Amazon Brasil, Estante Virtual e importação em 7; loja da editora e livraria em
6. E resolve uma sutileza que a divisão por faixas escondia: a **página
bibliográfica** da editora é tier 1, enquanto a **loja** da mesma editora é
tier 6. Mesma editora, dois papéis, dois tiers — o que distingue não é quem
publica a informação, e sim se ela é sobre o texto ou sobre o estoque.

A regra que a escala serve, declarada em três lugares e agora numa quarta:
**nada de tier 6–7 toca `verdict`, `necessity` ou prioridade.** Disponibilidade,
preço, popularidade e avaliações são contexto, nunca juízo
[`config/acquisition.yaml` `never`; `curation-rules.md` §2.4 e §2.5].

## E.1b As quatro suposições que a pesquisa recusa

Cada uma é checada contra uma fonte ou registrada como `unverified`
[recuperado: blueprint §E]:

- **Popularidade não é qualidade.**
- **O selo de uma editora de prestígio não garante nada sobre este tradutor.**
  Os catálogos são desiguais, e a credencial a checar é a do tradutor, não a da
  casa.
- **Uma tradução mais recente não é automaticamente melhor.** Várias traduções
  de referência são antigas e insuperadas, e várias recentes são reedições
  comerciais de texto em domínio público.
- **Um título grego ou latino na capa não é evidência de edição bilíngue.**

## E.2 O fluxo de pesquisa, em dez passos

[recuperado: blueprint §E]

1. **Resolver, não adivinhar.** Casar a string contra ids, aliases, títulos
   originais e traduzidos. Uma correspondência, seguir. Várias, perguntar.
   Nenhuma, oferecer criar a obra e rodar o pipeline de curadoria
   [`curation-rules.md` §6].
2. **Carregar o que já existe.** Pesquisa anterior, vereditos anteriores,
   edições já recusadas e as suas razões, as notas do Mathews, participações
   atuais, relações existentes. A pesquisa nunca começa do zero e nunca repete
   em silêncio uma decisão já tomada.
3. **Estabelecer os fatos bibliográficos.** Língua original, data e
   circunstâncias de composição, transmissão textual, e a edição crítica de
   referência do texto original. Vão para `## Fatos`.
4. **Enumerar candidatos** em português, espanhol, italiano e inglês, mais as
   opções em língua original e bilíngues. **Enumerar antes de julgar** — a
   ordenação vem depois, e deixá-la vir cedo é como uma preferência de idioma
   vira um filtro em silêncio. Esta lista é **escopo de busca, não ordem de
   preferência**: ver §F.
5. **Verificar campo a campo.** Páginas de editora, catálogos de bibliotecas
   nacionais (agência ISBN do Brasil, BNP, BNE, BNCF, LoC, DNB), catálogos
   universitários, WorldCat. Campo verificado entra como verificado; campo não
   verificado entra como não verificado. Bilinguismo confirma-se em catálogo ou
   descrição de página, **nunca** por uma palavra grega no título.
6. **Avaliar qualidade.** Credenciais do tradutor, que texto-base foi usado,
   tradução direta ou por intermediário, completude, aparato, introdução,
   recepção acadêmica quando existir. Vão para `## Avaliações acadêmicas`, com
   atribuição.
7. **Checar disponibilidade no Brasil** e o formato físico, **com a data da
   checagem registrada** — disponibilidade é o dado que envelhece mais depressa
   de todo o sistema.
8. **Aplicar o §F** e escrever os vereditos nas edições, inclusive as recusas
   com as suas razões.
9. **Escrever o lugar na biblioteca.** O que a obra prepara, o que a responde,
   que obras do acervo a contestam, onde ela entra em cada sequência, que lacuna
   fecha. Vai para `## Lugar na biblioteca`.
10. **Fixar status, registrar proveniência, gravar.** Cada afirmação com a sua
    fonte, o seu tier e a sua data de recuperação.

## E.2b O que a pesquisa produz nos registros

Recuperado de `review/political-thought.md` §1, de `publications/_TEMPLATE.md`
e do texto de `publications/pub--cultrix--ciencia-e-politica.md`:

1. As indicações de edição do Mathews entram como **escolha declarada**
   (`by: voce`, `verified: false`), nunca como conclusão de pesquisa. Algumas
   nomeiam uma edição concreta; outras são intenção (`kind: intencao`) e
   nomeiam apenas um tradutor, uma editora desejada ou um requisito.
2. A pesquisa converte cada uma **em registro verificado ou em
   `verdict: rejected` com razão** — nunca antes disso.
3. `verified_fields` guarda **o que foi checado**, não o que foi suposto. Campo
   sem verificação fica `null`: preencher sem pesquisa é inventar.
4. O veredito é emitido **por obra**, dentro de `contains`, e não para a
   publicação inteira: um volume pode ser o veículo recomendado para uma obra
   que carrega e apenas uma alternativa para outra.
5. Tradutor, texto-base, completude e aparato vivem no par obra–publicação,
   pela mesma razão.
6. `bilingual_pair` é verificado **no livro, nunca no título**.

A forma exata dos campos é o próprio `publications/_TEMPLATE.md`, e não é
repetida aqui: o modelo é o esquema.

## E.3 O que a pesquisa do §E nunca faz

Já declarado, e reunido aqui por ser onde um agente vem procurar:

- Deixar disponibilidade, preço, idioma ou saliência local hierarquizar
  necessidade ou prioridade [`curation-rules.md` §2.4, §7].
- Apresentar um anúncio como opção de compra **desta** edição sem `match_basis`
  que diga como se sabe que é dela [`config/acquisition.yaml`].
- Inventar link, ASIN, ISBN, correspondência de edição ou fonte de capa. Na
  dúvida, o campo fica vazio [`config/acquisition.yaml` `never`].
- Tratar ausência de anúncio ou de capa como defeito bibliográfico
  [`config/acquisition.yaml`; `covers/README.md`].

## E.4 Quando uma obra está "pesquisada" — a lista, não um botão

Todos os itens têm de valer [recuperado: blueprint §E]:

- língua original, data e transmissão estabelecidas;
- **pelo menos um candidato examinado em cada faixa de idioma que tenha um**;
- para a edição recomendada: editora, tradutor, ano, formato, ISBN, completude,
  texto-base e direta-ou-por-intermediário, **todos verificados contra fontes de
  tier 1–5**;
- aparato e introdução avaliados;
- disponibilidade no Brasil checada **e datada**;
- candidatos recusados registrados com as suas razões;
- toda afirmação com fonte.

Qualquer coisa aquém disso é `partially_researched`, **com os itens em falta
nomeados**. Uma obra cuja disponibilidade foi checada há mais de um ano passa a
`needs_review` automaticamente: a avaliação continua boa, a informação de compra
não. É a mesma lógica do frescor derivado em `config/acquisition.yaml`
(`aging: 365`), aplicada ao status da obra em vez de ao anúncio.

Os quatro valores de `research_status` estão em `config/vocabularies.yaml`.
Hoje todos os 53 registros de obra e a única publicação estão
`not_researched` — nenhuma pesquisa foi feita ainda.

## E.5 `work_type` pertence ao §E

Todos os 53 registros de obra trazem `work_type: null  # … (§E)`: a
classificação é produto da pesquisa, não do import. O vocabulário está em
`config/vocabularies.yaml` e é **aberto** — a lista declarada no cabeçalho dos
registros termina em reticências, e portanto não pode ser fechada aqui.

---

# §F · Seleção de edição e preferência de idioma

O §F é um **procedimento de decisão**, e a ordem dos passos é o argumento:
**portões primeiro, qualidade segundo, idioma terceiro.** A preferência de
idioma é poderosa, mas é um desempate — aplicá-la mais cedo deixaria uma edição
portuguesa medíocre vencer uma edição inglesa decisiva, que é exatamente o
resultado que o Mathews mandou evitar.

## F.1 O procedimento

[recuperado: blueprint §F, arquivado em `sources/blueprint-2026-09-05.md`. O
passo 4 foi **substituído** — ver F.2]

1. **Portão: adequação textual.** Completa, salvo se foram pedidas seleções;
   assente num texto-base defensável; traduzida **diretamente** do original
   sempre que exista alguma tradução direta. Uma edição traduzida por língua
   intermediária é recusada sempre que exista uma direta, **em qualquer idioma**.
   As reprovações entram como `verdict: rejected` com a razão, não são
   descartadas em silêncio.
2. **Portão: existência física.** Tem de ser um livro físico obtenível. Se a
   melhor edição acadêmica só existir em formato eletrônico, isso é dito
   abertamente, nunca substituído em silêncio.
3. **Ordenar os sobreviventes por mérito.** Autoridade acadêmica do tradutor e
   do editor; fidelidade; aparato; qualidade da introdução; legibilidade;
   registro. Isto produz **faixas de qualidade**, não um vencedor único.
4. **Só então, a preferência de idioma — dentro de uma faixa.** Ver F.2, que é
   a formulação vigente. Quando a melhor edição portuguesa está uma faixa
   abaixo, a edição superior vence e o compromisso é mostrado explicitamente,
   em vez de anunciado como conclusão.
5. **Grego antigo, e edições bilíngues em geral.** Ver F.3.
6. **Declarar o enquadramento à parte.** A orientação de uma introdução ou dos
   ensaios que acompanham é registrada no seu próprio campo (`framing`) e nunca
   misturada com a qualidade da tradução. Uma edição excelente com uma
   introdução fortemente posicionada continua excelente — apenas se avisa. O
   enquadramento só desqualifica uma edição quando contamina o próprio texto:
   traduções tendenciosas, cortes silenciosos, um aparato que argumenta em vez
   de informar.
7. **Emitir apenas os vereditos que de facto diferem.** Melhor edição acadêmica
   em absoluto, melhor edição em português, melhor edição praticamente obtenível
   no Brasil. Quando duas coincidem, são relatadas como uma. Nenhuma alternativa
   fabricada.

**A ordem de prioridade do Mathews, codificada:** qualidade acadêmica →
qualidade da tradução → confiabilidade textual → qualidade editorial → adequação
aos seus idiomas → disponibilidade física → preço. Os passos 1–3 cobrem os
quatro primeiros, o passo 4 o quinto, o passo 2 o sexto. Preço aparece só como
faixa (`price_band`), e só como desempate de último recurso.

## F.2 A preferência de idioma — formulação vigente

> **Decisão direta do Mathews, 2026-09-06.** Substitui a formulação do
> blueprint, que dizia "Portuguese, then Spanish, Italian, English". Essa
> sequência fixa é **simplista demais e não representa a preferência dele**. O
> texto histórico continua legível em `sources/blueprint-2026-09-05.md` §F,
> anotado como superado.

- O **português é a língua geralmente preferida** para traduções.
- Mas a língua de tradução preferida **depende da língua original da obra e da
  qualidade das traduções disponíveis**.
- Havendo uma **boa** tradução portuguesa, ela é geralmente preferida.
- **Não havendo tradução portuguesa suficientemente boa**, prefere-se uma edição
  adequada **na língua original**, quando essa língua é uma das que o Mathews
  usa de forma significativa — em vez de preferir mecanicamente outra língua
  traduzida só porque aparece antes numa hierarquia fixa.
- Uma tradução espanhola **não é automaticamente preferível** a uma italiana, e
  uma italiana não é automaticamente preferível a uma inglesa. O que decide é a
  língua original da obra e a qualidade das edições concretas disponíveis.
- Para obras escritas originalmente em **espanhol, italiano ou inglês**, uma
  edição de alta qualidade **na língua original** pode ser preferível a uma
  tradução portuguesa fraca.
- A preferência de idioma é **subordinada** à adequação textual, à qualidade do
  texto-base, à qualidade da tradução, à confiabilidade acadêmica, à completude,
  ao aparato e aos demais critérios de qualidade de edição.
- Ela opera, portanto, como **preferência dentro de uma faixa de qualidade
  comparável**, e nunca como regra absoluta capaz de fazer vencer uma edição
  claramente inferior.
- **Não inferir preferência de ordem de lista.** A enumeração do §E.2 passo 4 —
  português, espanhol, italiano, inglês — é **escopo de busca**, e a sua ordem
  não carrega preferência nenhuma. A preferência apropriada determina-se em
  contexto, a partir da língua original, das edições disponíveis e da qualidade
  delas.

A regra estrutural que sobrevive intacta desde antes, e que continua sendo o
enquadramento de tudo acima: **o idioma decide dentro de uma faixa de qualidade
e nunca entre faixas** [`curation-rules.md` §2.4; `review/education.md` §3.1].
É o mesmo princípio aplicado em dois níveis — no nível da **obra**, `context`
desempata candidatos de necessidade comparável e nunca hierarquiza; no nível da
**edição**, o idioma faz o mesmo. Uma obra não sobe por ser fácil de comprar em
português nem desce por ser difícil de encontrar.

Consequência já registrada nos dados: quando uma obra não tem edição
satisfatória em português, isso muda **o custo de satisfazer** uma lacuna, e
nunca a sua necessidade [`review/gaps/education.yaml`, `context` de
`education--g02`].

## F.3 Edições bilíngues, e o caso do grego

**Regra do grego antigo** [recuperado: blueprint §F, passo 5]: uma edição
bilíngue grego–português é preferida **dentro da sua faixa**, nunca por ser
bilíngue. Quando a melhor bilíngue é fraca, a resposta melhor é quase sempre
**dois livros**: a edição de leitura superior, mais um texto grego barato — uma
OCT, uma Teubner, uma Loeb — como companhia de estudo. Isso serve melhor o grego
do Mathews do que uma tradução comprometida, e custa menos do que parece. O
mesmo raciocínio vale para grego–inglês.

**Generalização, decisão do Mathews de 2026-09-06:** o mesmo princípio aplica-se
a edições bilíngues em geral. O estatuto bilíngue é uma preferência útil quando
a qualidade é de resto comparável, mas **não prevalece sobre uma edição
monolíngue materialmente superior**. Para o grego, a preferência bilíngue
grego–português é uma preferência **adicional dentro de uma faixa comparável**,
e não o critério dominante: se uma edição não bilíngue for claramente superior
em qualidade textual ou de tradução, é ela que se prefere.

Lembrete do §E.2 passo 5: bilinguismo **confirma-se** em catálogo ou descrição
de página. Uma palavra grega no título não é evidência de nada.

## F.4 O que os arquivos atestam, à parte da regra

Observações sobre os dados, não regras:

- **Obra originalmente em português não tem questão de tradução**, e a pesquisa
  só precisa identificar a edição [`review/education.md` §6 sobre Nunes;
  `review/culture.md` §1 sobre Suassuna].
- Várias `edition_pref` do Mathews pedem tradução "diretamente do russo", "do
  chinês", "do árabe", "do sânscrito" — o que é o portão 1 do §F.1 dito obra a
  obra — e duas preferem edições portuguesas de Portugal (Gulbenkian), o que
  mostra que "português" não significa "português do Brasil". São preferências
  dele, marcadas `by: voce`, e **uma preferência declarada para uma obra vence
  qualquer regra geral** [Precedência, §0.1].

---

*Este documento é regra, não dado. A build não o lê. Alterá-lo muda como o
agente raciocina; não muda nada na biblioteca.*

## F.5 Só edições físicas — decisão do Mathews, 2026-09-25

Nunca se registra edição digital (eBook, Kindle, audiolivro) como publicação.
Quando um item de lista aponta para uma versão digital, registra-se a **edição
física** correspondente — a melhor, pelo §F.1 — e a digital não entra no
acervo.

## F.6 Nada na Bibliotheca cita as listas da Amazon — decisão do Mathews, 2026-09-25

As listas de desejos da Amazon são material de trabalho e podem ser apagadas a
qualquer momento. Nenhum registro, comentário, nota ou revisão pode citá-las
("está na sua lista 'X' da Amazon", "a edição da lista", "o item da lista era
o eBook"...). O que fica da Amazon são **só os links de compra** das edições
registradas (`acquisition`); se um link quebrar, o Mathews avisa. Uma escolha
dele se registra como **escolha dele, com data** — não pela lista de onde veio.
Também não se registram observações sem uso para ele, como a existência de
versões digitais de uma edição.
