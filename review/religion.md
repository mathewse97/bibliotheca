---
collection: religion
kind: import-report + avaliação curatorial
by: claude
date: 2026-09-20
updated: 2026-09-21
status: "Importada com as 30 obras. Cinco trocas de ordem e a colocação da
         Bíblia de Jerusalém foram aprovadas por você em 2026-09-20 e estão
         aplicadas. Três lacunas registradas, nenhuma é compra devida."
---

# Revisão curatorial — Religião

Importada em 2026-09-20 a partir de `sources/lists/religiao.md`, 30 entradas.
Fonte complementar: anúncios de varejo (Amazon), consultados em 2026-09-19 —
usados só para identificar edições e ISBNs, nunca como autoridade
bibliográfica (as regras de pesquisa: varejo é tier 7).

A pesquisa foi feita antes de perguntar, como a as regras de curadoria manda. O que restou de
pergunta está na seção 9, e é o que a pesquisa confiável não resolve ou o que depende
genuinamente dele.

---

---

## 0 · Em resumo — o que está feito e o que espera você

Esta seção é o resumo em linguagem direta. O resto do documento é o registro
técnico, com as fontes e as razões.

**O que foi feito.** A coleção Religião foi importada com as suas 30 obras. A
importação corrigiu um erro de autoria e treze confusões entre autor, tradutor e
editora — todas herdadas do catálogo da Amazon, nenhuma sua. Em 2026-09-20 você
aprovou cinco mudanças de ordem e a colocação da Bíblia de Jerusalém; estão
aplicadas e registradas, e qualquer uma pode ser desfeita.

**O que espera você, em ordem de importância:**

1. **Duas obras da coleção fazem a mesma coisa que outras duas.** Não é erro,
   mas vale saber. O *Dicionário das religiões* cobre o mesmo terreno que o
   manual de Noss e Grangaard, em um terço do tamanho. E *O sagrado e o
   profano* é a versão curta de 198 páginas do *Tratado de história das
   religiões*, de 496 — o conteúdo do primeiro está inteiro dentro do segundo.
2. **Três obras cujo exemplar exato eu não consegui identificar**, e que só a
   sua estante resolve: qual edição de *Cruzando o Limiar da Esperança* você
   tem, qual *Epopeia de Gilgámesh*, e o que fazer com o *What the Buddha
   Taught* que você marcou — esse último tem um número de registro que não
   existe em catálogo nenhum do mundo.
3. **Um movimento cujo nome não corresponde ao conteúdo.** O que se chama
   Cristianismo não tem nenhuma obra sobre a história do cristianismo. Pode ser
   de propósito; é você quem diz.
4. **Uma escolha de vocabulário** que eu preciso que você aprove para poder
   preencher campos que hoje estão vazios nos registros. É burocrático e está
   no fim da seção 9.

**O que não espera você:** nada aqui é uma lista de compras. As três lacunas
registradas são constatações sobre o que a coleção contém, não dívidas.

---

## 1 · O que a importação corrigiu

A lista dele carrega, em treze entradas, um defeito que **não é dele**: o campo
*byline* da Amazon Brasil concatena "autor + segundo colaborador" sem tipar o
papel, e ele transcreveu o que o catálogo mostrava. Nos trinta itens isso
produziu **seis tipos distintos de erro**, e todos foram corrigidos contra fonte
tier 1–4 antes de qualquer registro ser escrito.

**Erro de autoria, corrigido — entrada 26.** A lista atribui *Cruzando o Limiar
da Esperança* a **Senel Paz**. A obra é de **João Paulo II**, livro-entrevista
com **Vittorio Messori**, original *Varcare la soglia della speranza*, 1994.

A causa foi encontrada, e é mais específica do que "a Amazon errou". A Agência
Brasileira do ISBN, com registros de origem Biblioteca Nacional (tier 3), mostra:

| ISBN-10 | Obra | Autor | Selo |
|---|---|---|---|
| **8526503146** | O LOBO, O BOSQUE E O HOMEM NOVO | PAZ, SENEL | Francisco Alves |
| **8526503154** | CRUZANDO O LIMIAR DA ESPERANÇA | JOÃO PAULO II, PAPA | Francisco Alves |
| 8533208839 | CRUZANDO O LIMIAR DA ESPERANÇA | JOÃO PAULO II | Círculo do Livro |

Os dois primeiros ISBNs são **adjacentes na mesma sequência da Francisco Alves**,
que publicou as duas obras. O catálogo de varejo cruzou registros vizinhos. Senel
Paz é, portanto, o autor **correto** do ISBN 8526503146 — o que está errado é o
pareamento do título com o número.

Consequência registrada: **o ISBN desse anúncio não identifica esta obra**, e
por isso nenhuma publicação foi criada a partir dele. É exatamente o caso que o
campo `match_basis` existe para apanhar (as regras de curadoria: "marketplaces fundem edições
rotineiramente"), com um agravante — aqui a correspondência não é `unconfirmed`,
é **contradita por ISBN**.

**Tradutor apresentado como autor — dez entradas.** Em todas, o segundo nome do
byline é o tradutor, e tradutor vive no par obra–publicação, nunca em `authors`
(as regras de pesquisa.5):

| Entrada | Nome no byline | Papel real |
|---|---|---|
| 7 | Fernando Tomaz | tradutor (e há um segundo, ver abaixo) |
| 8 | Rogério Fernandes | tradutor |
| 10 | José Marcos Mariani de Macedo | tradutor, direto do alemão |
| 11 | Jacyntho Lins Brandão | tradutor, do acádio |
| 12 | Jacyntho Lins Brandão | tradutor (o "Desconhecido" está certo) |
| 13 | Thais Rocha da Silva | tradutora |
| 14 | Marcelo Jacques de Morais | tradutor |
| 19 | Frederico Lourenço | tradutor, do grego |
| 20 | Marcos Marcionilo | tradutor |
| 27 | David Pessoa de Lira | tradutor, do grego |

**Editora apresentada como autor — entrada 23.** "EDIPRO" é a editora; Jair Lot
Vieira é tradutor e organizador. Mas esta entrada tem um problema maior, que não
é de byline — ver as regras de curadoria.

**Introdutor apresentado como coautor — entrada 24.** Harry Rubenstein assina a
introdução da edição Smithsonian, com Barbara Clark Smith; não é coautor.

**Colaboradores omitidos — quatro casos.** O byline apaga gente que existe:

- entrada 7: o *Tratado de história das religiões* tem **dois** tradutores,
  Fernando Tomaz **e Natália Nunes**;
- entrada 6: o *Dicionário das religiões* traz **H. S. Wiesner** como
  colaborador declarado no original francês;
- entrada 1: a *História das religiões mundiais* apaga **John B. Noss**, autor
  fundador da linhagem em 1949 — não por erro, mas porque a edição corrente é
  assinada só pelos continuadores;
- entrada 29: *O Herói de mil faces* tem **dois** tradutores, Camilo Francisco
  Ghorayeb e Heráclito Aragão Pinheiro, e o byline não traz nenhum.

**Atribuição pseudoepígrafa tratada como autoria — entradas 27 e 28.** Hermes
Trismegisto não é figura histórica. Os catálogos usam o nome como cabeçalho
convencional para agrupar o corpus, não como asserção de autoria. Nos dois
registros `authors` ficou vazio, com a explicação nos `## Fatos`.

---

## 2 · Os movimentos: por que eu NÃO escrevi os `purpose`

A instrução que abriu esta importação mandava eu escrever o `purpose` de cada
movimento e marcá-lo `purpose_by: claude`. **Não fiz, e a razão é o arquivo.**

`sources/lists/religiao.md` traz, sob cada um dos sete cabeçalhos, uma frase em
itálico escrita por ele. É a mesma estrutura de `sources/lists/greco-romana.md`,
e ali essas frases entraram como `purpose` com **`purpose_by: voce`**. Escrever
as minhas por cima seria sobrescrever o raciocínio dele com o meu — o penúltimo
marcador da regra que proíbe sobrescrever o raciocínio dele. As sete frases
entraram verbatim.

E elas fazem mais do que descrever: **várias declaram escopo que a coleção ainda
não cobre.** "Budismo, hinduísmo, islamismo, judaísmo etc." sob um movimento que
só tem budismo; "Padres da Igreja, escolástica, Reforma" sob um movimento que não
tem nenhum dos três; "cultos de mistério" sob um movimento que não os trata. É
daí que vêm seis dos dezoito assuntos marcados como ausentes, todos com
com intenção declarada de cobrir — **a intenção é declarada por ele, não inferida por mim.** É a
base das três lacunas registradas na seção 10.

---

## 3 · A entrada 30 está fora da estrutura, e isso é decisão dele

A **Bíblia de Jerusalém não está em nenhuma das sete seções**. Ela aparece depois
do mapa narrativo de fecho e depois do separador `---`, isolada, e é a **única
das trinta sem Perspectiva, sem Temas e sem frase de justificativa** — traz
apenas dois ISBNs.

Três consequências, todas governadas por regra:

1. **Ela não tem movimento.** Pô-la na VII por ser a última é precisamente o que
   a a regra dos movimentos regra 3 proíbe: *"acrescentar ao fim NÃO é a opção conservadora; numa
   sequência com movimentos, o fim tem dono"*. A leitura do conteúdo a puxaria
   para o movimento IV, mas essa é inferência minha sobre estrutura que é dele.
2. `perspective`, `subjects_stated` e a justificativa que você escreveu ficaram **nulos**, não
   inventados (as regras de curadoria).
3. O registro `works/biblia.md` leva **`pendente de colocação`**, que é o
   mecanismo declarado pela regra da incerteza visível para obra sem coleção
   **por decisão** — isenta da
   checagem de órfãs, e visível como pendência em vez de escondida.

**Os ISBNs que ele escreveu à mão conferem.** ISBN-10 `8534919771` e ISBN-13
`978-8534919777` têm dígito verificador válido, são o mesmo número nas duas
formas, e correspondem à Paulus, nova edição revista e ampliada, 2002, 2208 p.

---

## 4 · Os três volumes de Eliade: três obras, e por quê

A instrução mandava registrar as entradas 3, 4 e 5 como **uma obra com três
publicações**. O arquivo dele diz outra coisa, e o arquivo é o fato (`AGENT.md`
as regras de curadoria).

Ele escreveu **Perspectiva, Temas e justificativa separados para cada volume**.
Três argumentos exigem três posições na sequência, e uma participação carrega um
a justificativa que você escreveu — uma obra só poderia ocupar uma posição e carregar um argumento. Os
outros dois seriam perdidos ou fundidos, e fundir texto dele é pior do que
duplicar um registro.

Entraram como **três obras ligadas por `continues`**, tipo atestado no
vocabulário para "continuações e completamentos". A alternativa canônica seria
`part_of` com um registro-pai da obra inteira — que é o que o vocabulário
descreve para "um volume de uma obra em vários volumes". **Não escolhi entre as
duas em silêncio: é decisão de modelagem, está aqui, e é reversível** — trocar
`continues` por `part_of` e criar o registro-pai não destrói nada.

> **Decidido por ele em 2026-09-20:** mantém-se `continues` entre as três obras.
> Nada foi alterado, porque o repositório já estava assim. Registrado como D1
> nesta seção.

Ids: `eliade--histoire-des-croyances-i`, `-ii`, `-iii`. O título original é
**compartilhado pelos três volumes**, que é exatamente a condição em que a emenda
das regras bibliográficas manda recorrer ao título curto convencional.

**Estado da obra, registrado nos três:** Eliade planejou quatro tomos e morreu em
1986 sem concluir o quarto. Há um tomo IV póstumo publicado **apenas em
espanhol**, escrito por vários especialistas segundo as diretrizes dele. Não
existe em francês nem em português, e não foi registrado.

---

## 5 · A ordem dele: o que a pesquisa confirmou e o que ela propõe

A a regra dos movimentos obriga o agente a **validar a ordem, propor melhorias e dizer os porquês,
sempre com pesquisa que sustente a colocação — nunca por inferência**. Esta
seção é o cumprimento dessa obrigação, feito em 2026-09-20 depois de pesquisar
o conteúdo, o nível e as dependências das trinta obras.

**Conclusão geral: a ordem dele é boa e a maior parte dela está certa por
razões que a pesquisa confirma.** o registro de mudanças de ordem continua vazio — nada foi
aplicado. O que segue é proposta.

### 5.1 As trinta obras: o que cada uma é

Tabela de apoio, para que a decisão de ordem possa ser tomada por quem não leu
os livros. "Exige antes" = obras desta mesma coleção cuja leitura prévia muda
materialmente o proveito.

| # | Obra | O que é, em uma linha | Págs | Nível | Exige antes |
|---|---|---|---|---|---|
| 1 | Noss e Grangaard, *História das religiões mundiais* | Manual universitário descritivo: cada tradição exposta em seus próprios termos, com cronologia, textos e doutrinas. Sem tese | 840 | Introdutório, mas volumoso | — |
| 2 | Armstrong, *Uma História de Deus* | História de **uma ideia**, a de Deus único, nas três tradições abraâmicas. Tem tese: Deus é reinventado sempre que deixa de funcionar | ~460 | Intermediário | — |
| 3-5 | Eliade, *História das crenças*, vols. 1-3 | História mundial da religiosidade, da pré-história à Reforma, escrita por um autor só. Notas bibliográficas críticas extensas | ~1.230 | Intermediário-alto | Noss (nomes e cronologia) |
| 6 | Eliade e Culianu, *Dicionário das religiões* | ~33 ensaios enciclopédicos por tradição, em ordem alfabética. Obra de consulta | 348 | Introdutório | — |
| 7 | Eliade, *Tratado de história das religiões* | A morfologia: o sagrado se manifesta em estruturas recorrentes, classificáveis por tema (céu, água, pedra, tempo, espaço) | 496 | **Técnico — o mais difícil da coleção** | *O sagrado e o profano* |
| 8 | Eliade, *O sagrado e o profano* | A versão curta e didática do *Tratado*. Espaço sagrado, tempo sagrado, ritos de passagem | 198 | Introdutório | — |
| 9 | Berger, *O Dossel Sagrado* | A religião como construção social que legitima a ordem do mundo. **O contraponto interno a Eliade** | 200 | Intermediário-técnico | Weber |
| 10 | Weber, *A ética protestante* | Por que o capitalismo racional surgiu no Ocidente protestante. Afinidade entre ascetismo calvinista e disciplina econômica | ~200 + notas | Técnico, mas curto | Reforma (Armstrong ou Noss) |
| 11 | *Epopeia de Gilgámesh* | O poema. Amizade, morte de Enkidu, viagem fracassada atrás da imortalidade, dilúvio | 160 | Introdutório | — |
| 12 | *Enūma Eliš* | Poema de criação babilônico: Marduk vence Tiámat e faz o cosmos do cadáver dela. Texto **político-teológico** | 432 (poema curto, aparato longo) | Intermediário-técnico | Gilgámesh |
| 13 | Shaw, *Os mitos egípcios* | Guia temático da mitologia egípcia: criação, Osíris-Ísis-Hórus, além-morte | 224 | Introdutório | — |
| 14 | Bottéro, *No começo eram os deuses* | Coletânea sobre a civilização mesopotâmica, do cotidiano à religião, traçando a linha "da Suméria a Jerusalém" | 309 | Intermediário-acessível | Os dois poemas |
| 15 | Kaefer, *A Bíblia, a arqueologia…* | Manual breve brasileiro: Israel e Judá são duas entidades distintas, não um reino unido fraturado | 112 | **Introdutório — o mais acessível do bloco bíblico** | — |
| 16 | Smith, *O memorial de Deus* | O monoteísmo emergiu gradualmente, por circunstância política; a Bíblia é memória coletiva reescrita a cada geração | 264 | **Técnico** (ugarítico, teoria da memória) | Kaefer, Finkelstein-Römer |
| 17 | Finkelstein e Römer, *Às origens da Torá* | Diálogo entre arqueólogo e exegeta sobre Abraão, Jacó, Êxodo e o nome divino. Resumo ao fim de cada seção | 184 | Intermediário, bem guiado | Kaefer |
| 18 | Kugel, *How to Read the Bible* | Cada passagem lida duas vezes: como os intérpretes antigos liam e como a crítica moderna lê. Tese: as duas não se sustentam juntas | 848 | Escrita limpa, extensão monumental | Finkelstein-Römer |
| 19 | *Os quatro evangelhos*, trad. Lourenço | Tradução direta do grego por classicista, deliberadamente não confessional, com notas filológicas | — | Introdutório no texto | — |
| 20 | Ehrman, *O que Jesus disse?* | Crítica **textual**: o que os copistas mudaram. Casos concretos (mulher adúltera, final de Marcos) | ~250 | Introdutório | Os evangelhos |
| 21 | Vermes, *O Autêntico Evangelho de Jesus* | Crítica da **tradição**: dito a dito, o que Jesus disse e o que é da comunidade. Jesus como *hasid* galileu | 488 | Intermediário-técnico | Os evangelhos, Ehrman |
| 22 | Rahula, *What the Buddha Taught* | Exposição doutrinal do budismo a partir do cânone páli, por monge com formação acadêmica | ~200 | Introdutório mas conceitualmente denso | — |
| 23 | *Dhammapada* | 423 versos em 26 capítulos temáticos. Máximas, sem argumentação e sem ordem progressiva | ~100 | **Enganoso**: fácil de ler, difícil de ler bem | Rahula |
| 24 | Jefferson, *The Jefferson Bible* | Não é um livro escrito: é um objeto. Jefferson recortou os evangelhos com navalha e removeu milagres, ressurreição e divindade | curto | Trivial de ler, difícil de interpretar | **Os evangelhos** |
| 25 | Xavier, *Cartas e instruções* | 138 cartas de 1535-1552. Administração missionária concreta; as do Japão registram Xavier descobrindo que sua tradução de "Deus" estava errada | 488 | Documental, fragmentário | Contexto cristão |
| 26 | João Paulo II, *Cruzando o Limiar da Esperança* | Livro-entrevista, ~35 respostas. O conteúdo intelectual está nos capítulos sobre outras religiões | ~250 | Introdutório | **Rahula** (para avaliar o capítulo sobre budismo) |
| 27 | *Corpus Hermeticum* | 17-18 tratados gregos do séc. II-III, diálogos de revelação sobre cosmos, queda e ascensão da alma. Edição bilíngue com glossário | — | **Técnico** (vocabulário do platonismo médio) | — |
| 28 | *Tábua de Esmeralda* | Doze sentenças oraculares. "O que está embaixo é como o que está em cima". Origem **árabe medieval**, não egípcia antiga | 3 min | Impenetrável sem comentário | Corpus Hermeticum |
| 29 | Campbell, *O Herói de mil faces* | Todos os mitos heroicos seriam variações de uma estrutura única, o "monomito", em três atos | ~400 | Intermediário | Ao menos uma fonte primária |
| 30 | *Bíblia de Jerusalém* | Bíblia de estudo da École Biblique: introduções por livro, notas histórico-críticas, referências cruzadas | 2208 | Obra de consulta | — |

### 5.2 O que a pesquisa CONFIRMOU na ordem dele

Seis decisões dele estão certas, e agora com razão declarada:

1. **Evangelhos (19) → Ehrman (20) → Vermes (21).** A ordem é exata e por um
   motivo preciso: Ehrman pergunta *"o texto que tenho é o que foi escrito?"* e
   Vermes pergunta *"o que foi escrito corresponde ao que Jesus disse?"* — a
   primeira pergunta precede logicamente a segunda. E ambos discutem perícopes
   concretas: quem não leu os evangelhos lê os dois como listas de asserções
   sobre um objeto que não conhece.
2. **Rahula (22) → Dhammapada (23).** Sem Rahula, os 423 versos não são mal
   compreendidos — são *bem* compreendidos como outra coisa: aforismo perene de
   sabedoria genérica. Rahula é o que dá arestas aos versos.
3. **Corpus Hermeticum (27) → Tábua de Esmeralda (28).** A Tábua lida antes são
   três minutos de fascínio vazio.
4. **Campbell (29) por último.** Esta é a melhor decisão de ordem da lista. A
   tese de Campbell é que as diferenças entre as tradições não importam. Lido
   primeiro, ele instala uma grade que o leitor projeta em tudo; lido depois de
   se ter visto ao menos uma tradição em sua especificidade, vira um caso a
   avaliar. É exatamente o que a justificativa dele para a entrada 29 já dizia.
5. **Gilgámesh (11) → Enūma Eliš (12).** Gilgámesh é narrativo e humano; o Enūma
   é teogônico e nominalista. Gilgámesh também instala as convenções poéticas
   que tornam o segundo legível.
6. **O movimento V entre o IV e o VI — e eu estava errado ao estranhar isso.**
   Em 2026-09-20 eu levantei a dúvida de que o bloco budista interrompia sem
   razão a continuidade entre Bíblia e cristianismo. **A pesquisa mostra que há
   razão, e é forte:** as cartas de Xavier (25) registram o encontro com o
   budismo japonês, e o capítulo mais discutido de João Paulo II (26) é a
   caracterização do nirvana. **Sem Rahula lido antes, o leitor não tem como
   avaliar nenhum dos dois.** O movimento V é pré-requisito do VI.

### 5.3 As cinco trocas propostas

Nenhuma foi aplicada. Todas são reversíveis e ficariam registradas em
o registro de mudanças de ordem com razão, se aprovadas.

| # | Troca | Por quê |
|---|---|---|
| **T1** | Armstrong (2) **antes de** Noss (1) | Noss tem 840 p. sem narrativa e sem tensão: é feito para consulta, e quase ninguém o lê inteiro. Armstrong dá uma razão para continuar. O erro comum é achar que o manual é "mais fácil" — ele é mais fácil por página e quase impossível como leitura corrida. Noss passa a ser consulta permanente a partir daí |
| **T2** | *O sagrado e o profano* (8) **antes do** *Tratado* (7) | O curto é a versão condensada do longo, escrita para divulgação. Na ordem atual, o leitor enfrenta 496 p. de acúmulo etnográfico — o livro mais difícil da coleção — antes de ter os conceitos que o organizam |
| **T3** | Weber (10) **antes de** Berger (9) | Berger é weberiano declarado e sua discussão de racionalização e secularização pressupõe a *Ética protestante* conhecida |
| **T4** | Bottéro (14) **antes dos** mitos egípcios (13) | Mantém o bloco mesopotâmico contíguo: os dois poemas e depois a síntese que os sistematiza e faz a ponte "da Suméria a Jerusalém", entrando direto em Kaefer. O Egito é digressão comparativa e funciona igualmente bem depois |
| **T5** | Finkelstein-Römer (17) **antes de** Smith (16) | Kaefer dá a cronologia, F-R dá o solo arqueológico e a datação dos textos, e só então Smith — que é o mais técnico do bloco e o que efetivamente responde "como surgiu o monoteísmo" — rende o que pode. ⚠️ **Esta é a única que atravessa a fronteira entre movimentos** (Smith está no III, F-R no IV) |

### 5.4 Uma sexta troca, mais ambiciosa, que eu NÃO recomendo sem ele decidir

*O sagrado e o profano* (8) é a porta de entrada em Eliade. Os três volumes da
*História das crenças* (3-5) são o coroamento dele. Na ordem atual, o leitor
percorre 1.230 páginas do autor antes de encontrar o livro de 198 páginas que
lhe dá o vocabulário.

A correção pedagógica seria mover a entrada 8 para **abrir** o bloco Eliade, no
movimento I. **O custo é estrutural:** *O sagrado e o profano* é obra de teoria,
e o movimento I chama-se "História comparada das religiões". Seria pôr uma obra
de teoria dentro do movimento de história — o tipo de coisa que a a regra dos movimentos regra 1
pede para evitar, porque um movimento deve continuar verdadeiro depois de
entrarem mais obras.

Registro a tensão sem resolvê-la. Uma alternativa que a evita: ler a entrada 8
fora da sequência, como preparação, mantendo-a registrada no movimento II.

### 5.5 Duas redundâncias reais, para decisão consciente

Nenhuma é erro. Uma coleção pode conter as duas obras de cada par de propósito.
Mas ele deve saber que são pares:

- **Dicionário das religiões (6) × Noss (1).** Mesma função — referência
  panorâmica — em pouco mais de um terço do tamanho. É a redundância mais clara
  da coleção. A justificativa dele para a entrada 6 já diz que ela é "obra de
  consulta ao longo de toda a formação", que é exatamente o papel de Noss.
- ***O sagrado e o profano* (8) × *Tratado* (7).** O curto está **integralmente
  contido** no longo, em forma simplificada. Ler os dois na íntegra é ler a
  mesma coisa duas vezes. O uso mais econômico é ler o curto inteiro e o
  *Tratado* seletivamente — espaço sagrado, tempo sagrado, estrutura dos
  símbolos —, tratando o resto como referência.

Uma terceira, menor: o **volume 3 de Eliade (5) × Armstrong (2)** cobrem o mesmo
período, de ângulos diferentes.

### 5.6 O interlocutor de Eliade — achado que alimenta a lacuna g01

Eliade sustenta que existe uma estrutura do sagrado comum a todas as culturas,
que o estudioso pode isolar e classificar. A contestação acadêmica dessa tese
tem uma obra decisiva:

> ***To Take Place: Toward Theory in Ritual***, de **Jonathan Z. Smith**
> (University of Chicago Press, 1987, cerca de 180 páginas). **A tese:** o
> sagrado não é algo que se manifesta e o homem reconhece — é efeito do lugar e
> da atenção, isto é, do ritual. Smith demonstra isso voltando aos casos que o
> próprio Eliade usou como prova, sobretudo o poste sagrado dos aborígenes
> Achilpa australianos, e mostrando que as fontes etnográficas não dizem o que
> Eliade diz que dizem. A conclusão: o padrão que Eliade encontra entre culturas
> é obra de quem compara, não coisa que esteja nas culturas. A frase que resume
> o livro é *"o mapa não é o território"*.

É o melhor contraponto possível porque Smith não desqualifica Eliade de fora:
leu-o a vida inteira e o trata como o adversário que vale a pena refutar, no
terreno dele e com os mesmos materiais.

Outras obras que criticam Eliade, para registro, em ordem de proximidade ao
problema: ***Manufacturing Religion*** (1997), de **Russell McCutcheon**, que
argumenta que tratar a religião como categoria irredutível é uma estratégia para
protegê-la do escrutínio social; ***Religion after Religion*** (1999), de
**Steven Wasserstrom**, que lê Eliade e seus pares como teólogos esotéricos
disfarçados de cientistas; e ***Impostures et pseudo-science: l'œuvre de Mircea
Eliade*** (2005), de **Daniel Dubuisson**, que liga o antimodernismo de Eliade
ao seu envolvimento juvenil com a Guarda de Ferro romena — a crítica mais dura e
a mais biográfica das três. Do outro lado há defesa séria: ***Reconstructing
Eliade*** (1996), de **Bryan Rennie**, argumenta que boa parte dessas críticas
ataca uma caricatura.

**Dentro da coleção, o contraponto já existe e é genuíno:** *O Dossel Sagrado*,
de Berger. Onde Eliade diz que o sagrado se manifesta e o homem o reconhece,
Berger mostra como uma sociedade produz um sagrado e depois esquece que o
produziu. Tamanho parecido, ambição parecida, conclusões incompatíveis. É por
isso que a T3 importa: lidos em sequência, com Eliade fresco, os dois formam o
exercício mais formativo possível com o material que já está na coleção.

Isto **não é proposta de compra** (as regras de curadoria, as regras de curadoria). É o candidato registrado contra a
lacuna `religion--g01`, para o caso de ele decidir fechá-la.

## 6 · Edições: o que a pesquisa achou, e as duas paradas formais

**Nenhum `verdict` foi gravado, em nenhuma das 29 publicações.** Todas estão
`unassessed`, e isso é o estado correto, não uma omissão: o as regras bibliográficas é um procedimento
ordenado — portão textual, portão físico, faixas de mérito, idioma só dentro da
faixa — e ele **não foi percorrido**, porque o as regras de pesquisa passo 4 exige enumerar
candidatos **antes** de julgar, e essa enumeração não existe para nenhuma destas
obras. Julgar antes de enumerar é como uma preferência de idioma vira filtro em
silêncio; a avaliação que existe está nos `## Avaliações acadêmicas` das obras,
como matéria-prima do passo 5.

### Duas paradas formais

**1. *O sagrado e o profano* — tradução por língua intermediária (entrada 8).**
A obra foi publicada primeiro **em alemão** (*Das Heilige und das Profane*,
Rowohlt, 1957). A ficha catalográfica da edição brasileira declara como título
original ***Le sacré et le profane***: a tradução de Rogério Fernandes é feita
**do francês**.

O as regras de escolha de edição portão 1 é taxativo: *"uma edição traduzida por língua intermediária é
recusada sempre que exista uma direta, em qualquer idioma"*. Não emiti
`rejected`, porque falta estabelecer se essa direta existe — e o
o procedimento de pesquisa manda **parar e relatar antes de gravar veredito**
exatamente neste caso. Está relatado.

**2. Dhammapada — a escolha declarada dele e o anúncio guardado são edições
diferentes (entrada 23).** Ele escreveu "EDIPRO; Jair Lot Vieira". A edição
registrada é outra: **Mantra, 2021, tradução do páli
por José Carlos Calazans**, bilíngue.

Pelas regras de pesquisa, a indicação dele entra como escolha declarada e a pesquisa a
converte em verificada **ou** em `rejected` com razão. **Falta a pesquisa que
decide**: qual o texto-base da edição EDIPRO, e se a tradução de Jair Lot Vieira
é direta do páli ou por intermediário. Se for indireta e a Mantra direta, o as regras de escolha de edição
portão 1 resolve sozinho e não há pergunta a fazer.

### Observações de edição, que não são vereditos

- ***Epopeia de Gilgámesh* (11).** Uma das edições é a ilustrada de 2021,
  160 p., **sem aparato**. O mesmo tradutor assina, pela mesma Autêntica, *Ele
  que o abismo viu* (2017, 336 p.), que é a edição **acadêmica**, com aparato.
- ***What the Buddha Taught* (22).** O ISBN da edição Motilal —
  9789391024796, prefixo indiano — **não aparece em nenhum catálogo
  bibliográfico consultado**: nem BnF, nem catálogos universitários, nem a
  agência ISBN indiana, que não expõe busca pública. A única ocorrência na web é
  varejo. Não é edição bibliograficamente atestada. Registrei, em vez dela, a
  **Grove Press, 2ª ed. ampliada** como publicação de referência da obra, com
  `source_of_record: claude` e a razão no arquivo.
- ***A Tábua de Esmeralda* (28).** Microeditora de autopublicação, 112 p.,
  conteúdo largamente de domínio público, sem aparato crítico, sem manuscrito-base
  indicado. Registrada porque é a escolha declarada dele, com a ressalva escrita.
- ***Dicionário das religiões* (6).** A edição brasileira **não avisa** que a
  redação dos verbetes é substancialmente de Culianu, nem que Wiesner colaborou.
- ***O Dossel Sagrado* (9).** Berger formulou aqui a tese da secularização e
  **repudiou-a publicamente** a partir dos anos 1990. A edição brasileira não
  traz esse contraponto. É fato sobre a obra, registrado nos `## Fatos`.
- ***Bíblia de Jerusalém* (30).** O **texto bíblico** é traduzido do hebraico,
  aramaico e grego; só o **aparato** vem do francês. O portão da escolha de edição olha o
  texto — esta edição passa, ao contrário da entrada 8.
- **Duas verificações de bilinguismo pendentes.** *Corpus hermeticum græcum* e o
  Dhammapada da Mantra foram registrados como bilíngues a partir de fonte tier 6.
  O as regras de pesquisa passo 5 e a as regras de escolha de edição exigem catálogo ou descrição de página, e o as regras de pesquisa
  adverte que "um título grego na capa não é evidência" — e o título do Corpus
  traz *græcum*. Os dois estão com `bilingual: false` até reverificação.

### Capas

**Nenhuma capa foi gravada.** (Superado em 25/09/2026 — ver §13.) As miniaturas disponíveis nos anúncios eram de
135 px, pequenas demais para uso, e o acesso às imagens em resolução utilizável
foi recusado pelo proxy desta sessão. Ausência de capa **não é defeito
bibliográfico** (as regras de curadoria, `covers/README.md`) e a build não a reporta. Quando houver
acesso, as capas entram em `covers/<publication-id>.jpg` com `source` literal.

---

## 7 · Efeito sobre outras coleções — proposta, não aplicação

`review/gaps/greco-roman.yaml` já previa isto, por escrito: *"uma revisão será
necessária se Religião for importada — a região
`religiao-romana-e-cristianismo-antigo` é a candidata óbvia a ser coberta de lá
por participação, não por compra (a regra da participação em vez de compra)"*.

A previsão se confirma, e nos dois sentidos:

- **De Religião para Greco-Romana.** As entradas 19, 20 e 21 — os evangelhos na
  tradução de Frederico Lourenço, Ehrman e Vermes — tratam do **cristianismo
  primitivo**, anterior a Constantino e portanto dentro do escopo declarado de
  greco-roman, cujo `out_of_scope` exclui apenas "cristianismo posterior a
  Constantino como assunto próprio". A região `religiao-romana-e-cristianismo-antigo`
  está ausente lá.
- **De Greco-Romana para Religião.** Burkert (*Religião grega na época arcaica e
  clássica*) cobre os cultos de mistério que a frase do movimento VII nomeia e
  que a região `cultos-de-misterio` registra como ausente aqui. Vernant (*Mito e
  religião na Grécia antiga*) e Agostinho (*A Cidade de Deus*, vinda de
  Pensamento Político) são os outros dois casos.

**Nada foi aplicado.** Acrescentar participação é mudança estrutural e exige
aprovação (as regras de curadoria), e a instrução desta importação proibia tocar noutras coleções.
Os candidatos estão em `review/gaps/religion.yaml`, bloco o bloco de participações em falta.
A build confirma que o import **não deixou nenhuma conclusão stale**: os três
registros stale que aparecem já estavam stale antes, e são de Educação e Cultura.

---

## 8 · Convenções levantadas, não decididas (as regras de curadoria)

Quatro coisas precisaram de um valor que o vocabulário não tem. Em nenhuma delas
inventei um slug: **escolher um valor novo é decisão de classificação, e vai a
revisão** (`config/vocabularies.yaml`, nota de uso).

1. **o tipo de obra das obras acadêmicas.** O vocabulário só atesta
   `primary-source` e `political-theory`. As dez fontes primárias desta coleção
   receberam `primary-source`; as dezoito obras de história, fenomenologia e
   sociologia da religião ficaram **nulas**. O blueprint nomeia cinco categorias
   em prosa — fonte primária, teoria, sociologia, literatura, comentário — mas
   não dá as formas de slug. Uma coleção inteira de história das religiões torna
   isso urgente.
2. **`form` de obras que não são livro nem tratado.** Ficaram nulas: epopeia
   (Gilgámesh, Enūma Eliš), coletânea canônica (Bíblia, evangelhos, Dhammapada),
   corpus epistolar (Xavier), obra de referência em verbetes (o Dicionário) e
   texto breve (Tábua de Esmeralda).
3. **Id de obra sem autor pessoal.** A forma observada é `<autor>--<titulo>`, e
   sete obras desta coleção não têm autor. Usei o **título curto sozinho**
   (`enuma-elis`, `dhammapada`, `corpus-hermeticum`, `biblia`…) com `authors: []`
   — honesto e reversível, mas é convenção nova. É parente do problema do autor
   corporativo NAEMT (`review/survival-self-sufficiency.md` as regras de curadoria), e não o mesmo:
   lá havia uma instituição; aqui não há ninguém.
4. **Entrevistador em `authors`.** Vittorio Messori entrou em `authors` da
   entrada 26 porque o campo não distingue papéis. É a mesma lacuna estrutural
   que separa tradutor de autor, só que sem o par obra–publicação para acolhê-la.

---

## 9 · Decisões — o que está decidido e o que espera ele

Esta seção é a **folha de decisões** da coleção. Cada item traz o que é, as
opções, o efeito de cada uma e a minha recomendação. Quando ele decidir, a
decisão é registrada aqui com a data, e o que dela decorrer é aplicado nos
arquivos canônicos.

### Já decidido

**D1 · Modelagem dos três volumes de Eliade — DECIDIDO em 2026-09-20.**
Aprovado manter as três obras ligadas por `continues`, em vez de uma obra-pai
com `part_of`. **Nada a aplicar: o repositório já está assim.** A alternativa
continua reversível se ele mudar de ideia.

### Pendente — estrutura da coleção

**P0 · A ordem de leitura. É a decisão principal, e a única que muda o que ele
vai ler primeiro.** A fundamentação completa, com o que cada uma das trinta
obras é, está na seção 5. Em resumo:

| Opção | O que muda |
|---|---|
| A — não mexer | A ordem dele fica como está. É defensável: a as regras de curadoria lista **seis** decisões dele que a pesquisa confirmou, incluindo uma que eu tinha estranhado por engano |
| **B — cinco trocas locais (recomendada)** | Armstrong antes de Noss · *O sagrado e o profano* antes do *Tratado* · Weber antes de Berger · Bottéro antes dos mitos egípcios · Finkelstein-Römer antes de Smith. Quatro são dentro do mesmo movimento; só a última atravessa a fronteira III–IV |
| C — as cinco mais a sexta | Acrescenta mover *O sagrado e o profano* para abrir o bloco Eliade no movimento I. Ganho pedagógico maior, custo estrutural: põe uma obra de teoria no movimento de história (as regras de curadoria) |

**Recomendação: B.** As cinco trocas resolvem os desencontros reais entre
dificuldade e posição sem tocar na estrutura de movimentos, que a pesquisa
mostrou ser mais bem pensada do que eu supunha.

**P1 · Onde entra a Bíblia de Jerusalém (entrada 30).**
Hoje está pendente de colocação: fora de todos os movimentos, visível como
pendência. Precisa decidir porque na lista de origem ela está fora das sete
seções, sem Perspectiva, Temas nem justificativa, e a a regra dos movimentos regra 3 proíbe
colocá-la no último movimento só por ser a última entrada.

| Opção | Como fica |
|---|---|
| **A — movimento IV, primeira posição** | A coleção passa a ter 30 membros; a Bíblia abre "Bíblia e formação das tradições abraâmicas" e é a edição através da qual as entradas 17 a 21 são lidas |
| B — movimento VI | Fica junto do cristianismo, mas separada da formação da Bíblia, que é o que o movimento IV trata |
| C — continuar fora da sequência | Permanece pendente de colocação, tratada como obra de consulta, ao modo do Dicionário das religiões |

**Recomendação: A, e a pesquisa reforçou.** Três razões convergem:

1. O `purpose` que ele escreveu para o movimento IV **começa nomeando "Bíblia
   de Jerusalém"**. Ele já a pensou como pertencente ao IV; a entrada é que foi
   acrescentada depois, no fim do arquivo, com apenas os ISBNs.
2. Ela é **pré-requisito direto da entrada 24**: a Bíblia de Jefferson é um
   objeto feito de recortes dos evangelhos, e o argumento dela está inteiramente
   nas *ausências* — quem não conhece os evangelhos simplesmente não vê o
   argumento. Posicioná-la no IV a coloca antes do VI, onde Jefferson está.
3. **Mas ela não é uma leitura como as outras**, e isto é um matiz importante
   da opção A: 2208 páginas não se leem em sequência. O uso correto é ler as
   introduções gerais e as introduções por bloco — algumas dezenas de páginas
   que já são uma formação em história literária de Israel — e os blocos
   narrativos, deixando o resto como consulta permanente. Isso vale a nota em
   prosa na participação, e é a mesma natureza que ele próprio atribuiu ao
   Dicionário das religiões na entrada 6.

**P2 · Aprovar ou recusar `question`, os critérios do que entra e o mapa de assuntos.**
Os três são meus, estão marcados `by: claude` e `status: proposta`, e a as regras de curadoria
diz que continuam hipótese enquanto não forem estabelecidos. Enquanto forem
proposta, as três lacunas da seção 10 também são provisórias, porque dependem do
mapa de regiões.

| Opção | Como fica |
|---|---|
| **A — aprovar como está** | `status` passa a `estabelecida`; o mapa de regiões vira fato de referência e as lacunas ganham base firme |
| B — aprovar com ajustes | Ele diz o que muda; eu reescrevo e volto para aprovação |
| C — recusar | Volto a propor do zero, e a coleção segue sem critérios declarados |

**Recomendação: B**, com um ajuste que eu mesmo já identifiquei — o
`out_of_scope` que exclui "religião grega e romana como cultura antiga" está
correto, e é por causa dele que eu retirei a proposta de trazer Burkert e
Vernant para cá. Vale ele confirmar que concorda com essa fronteira.

**P3 · Desdobrar o movimento IV em dois.**
O mapa narrativo que ele escreveu no fim da lista tem **oito** etapas para
**sete** seções: ele separa "formação de Israel e da Bíblia" de "Jesus e Novo
Testamento", que na estrutura numerada são um movimento só.

| Opção | Como fica |
|---|---|
| A — desdobrar | O movimento IV vira dois: um com as entradas 17 e 18 (Torá, exegese), outro com 19 a 21 (evangelhos, Jesus histórico). A coleção passa a ter oito movimentos |
| **B — não desdobrar** | Fica um movimento só, como nas seções numeradas |

**Recomendação: B, por ora.** Dividir movimento é mudança estrutural e exige
a escada de escalonamento; e a regra dos movimentos adverte contra
multiplicar movimentos. O
desdobramento faz sentido intelectual, mas o ganho é pequeno com cinco obras.
Se o movimento crescer, a proposta volta com mais força.

**P4 · O que o movimento VI deve ser — REFORMULADO em 2026-09-23, por objeção
dele.**

Eu tinha oposto "ler a religião de fora" a "deixar as tradições falarem por
si", e ele desmontou isso com uma pergunta: *a própria Bíblia não é isso?*
É. E não só ela. A coleção já tem **sete obras sem autor que são a voz de uma
tradição em primeira pessoa** — a Bíblia de Jerusalém, o Dhammapada, o
*Enūma Eliš*, a *Epopeia de Gilgámesh*, o *Corpus Hermeticum*, os evangelhos
canônicos, a *Tábula Esmeraldina*. A porta que eu descrevi como fechada está
aberta desde a importação, em seis tradições. Minha oposição era falsa.

O eixo verdadeiro é outro, e é mais estreito:

- **Escritura** — o texto fundador de uma tradição. Presente, em abundância.
- **Testemunho** — alguém de dentro relatando sua experiência. Presente: as
  cartas de Francisco Xavier, entrada 25.
- **Teologia** — um crente argumentando sobre a própria doutrina, para
  sustentá-la. Presente só numa forma moderna e popular: *Cruzando o Limiar da
  Esperança*, entrada 26, que é um papa respondendo a um jornalista, não
  teologia sistemática.

O que falta, portanto, não é "a voz de dentro": é **argumentação teológica
clássica** — e é exatamente o que o `purpose` que ele escreveu para o movimento
VI nomeia, ao mencionar Padres da Igreja, escolástica e Reforma.

Isso muda a força do argumento, e a favor de admitir. Se seis tradições falam
por si na coleção e só o cristianismo é estudado de fora, isso é uma
**assimetria**, não um princípio. Era este o argumento que eu deveria ter feito
em 2026-09-20, no lugar de "é o único Padre da Igreja do acervo", que era tapar
buraco.

| Opção | Como fica |
|---|---|
| A — manter | O movimento VI continua sendo o cristianismo visto de fora ou tardiamente. A assimetria fica registrada como escolha consciente |
| B — admitir teologia como objeto de estudo | O movimento passa a admitir a argumentação teológica no mesmo pé em que já admite escritura. *A Cidade de Deus*, de Agostinho, entra por participação vinda de Pensamento Político — sem compra, e reversível |

**A melhor formulação do outro lado**, porque ela é real: escritura e teologia
não são a mesma coisa. As escrituras estão aqui como **objeto histórico** — o
*Enūma Eliš* para mostrar uma cosmogonia, a Bíblia como o texto através do qual
as entradas 17 a 21 são lidas. Elas são lidas como fonte. *A Cidade de Deus* é
um argumento que **pede concordância**. Admitir escritura e admitir teologia
são gestos diferentes, e quem quiser manter A tem esse fundamento, não apenas
inércia.

**Recomendação, agora que tenho uma: B**, com a condição de que a teologia
entre como objeto de estudo e não como posição da biblioteca — a mesma
condição sob a qual a escritura já entrou. O custo é zero (a obra já está no
acervo) e o gesto é reversível. Mas continua sendo decisão dele, porque muda o
caráter declarado de um movimento, e isso é mudança estrutural.


### Pendente — edições

**P5 · Edição de *Cruzando o Limiar da Esperança* — DECIDIDO em 2026-09-23.**
Ele não tem nenhuma das duas edições atestadas, o que anulou a pergunta como eu
a fiz — eu presumira posse, mas a lista de origem registra leituras, não a
estante dele. Decidiu a opção A. **Aplicado:** criada
`pub--francisco-alves--cruzando-o-limiar-da-esperanca`, ISBN-10 8526503154,
como **edição de referência**, com `source_of_record: claude`. Ano, tradutor,
paginação e formato ficam vazios, porque não estão confirmados em fonte
nenhuma. A edição do Círculo do Livro (ISBN-10 8533208839) permanece atestada e
não registrada. Nenhuma das duas parece estar em catálogo: uma edição de
referência fora de catálogo não é indicação de compra.


**P6 · *What the Buddha Taught*.** O exemplar apontado tem ISBN de prefixo
indiano que **não existe em catálogo bibliográfico nenhum** — nem BnF, nem
catálogos universitários, nem a agência indiana. Registrei a **Grove Press, 2ª
edição ampliada** como publicação de referência da obra, com
`source_of_record: claude`. **Recomendação: ratificar**, e tratar o exemplar
indiano como aquisição sem valor bibliográfico.

**P7 · Qual *Epopeia de Gilgámesh* — DECIDIDO em 2026-09-23.**
Ele não tem nenhuma das duas. Decidiu registrar a edição **acadêmica** e pediu
o endereço de compra. **Aplicado:** criada
`pub--autentica--ele-que-o-abismo-viu--2017` — *Ele que o abismo viu: Epopeia
de Gilgámesh*, Autêntica, coleção Clássica, 1ª edição, 10/10/2017, 336 p.,
brochura, ISBN 9788551302835, tradução do acádio e notas de Jacyntho Lins
Brandão, R$ 89,80 de capa na editora nessa data. Todos os campos vieram da
página da própria editora. A ilustrada de 2021 continua registrada, com
referência cruzada entre as duas. Nenhum veredito de edição foi emitido, e a
posse não foi registrada em lugar nenhum — isso é estado pessoal dele.

Em 23/09/2026 ele perguntou se valia ter as duas, e decidiu **ficar só com a
acadêmica**. O que fundamentou a escolha foi um fato verificado na editora
nesse dia: a de 2021 não é a mesma tradução sem notas — é uma **segunda versão
do texto**, em que o tradutor preencheu parte das lacunas do poema para obter
leitura fluente. Numa coleção que lê Gilgámesh como fonte religiosa, as lacunas
são dado. A de 2021 permanece registrada como a outra publicação existente da
obra, e não como a escolhida.

Na mesma conversa ficou esclarecido que *Epopeia da criação: Enūma Eliš*, que
também está na coleção, é **outra obra** — já no acervo como
`enuma-elis`, ligada a esta por `complements` — e não uma terceira edição de
Gilgámesh.

**Não são decisão, são pesquisa minha pendente:** a edição do Dhammapada e a de
*O sagrado e o profano* podem ser resolvidas pelo primeiro portão da escolha de
edição sem pergunta
nenhuma. Ver as regras de curadoria.

### Pendente — vocabulário (aprovar ou recusar em bloco)

O problema em uma frase: **alguns campos dos registros ficaram vazios porque o
vocabulário da biblioteca não tem valor para eles**, e inventar um valor é
decisão de classificação, não preenchimento (as regras de curadoria). Enquanto ficarem vazios, a
interface não filtra por esses campos e um dos detectores de lacuna não
funciona. Abaixo está a proposta; basta aprovar, recusar ou corrigir.

**P8 · o tipo de obra — que tipo de obra é, intelectualmente.**
Hoje a biblioteca só usa `primary-source`, `political-theory` e
`political-sociology`. Dezoito obras desta coleção ficaram nulas. Proposta,
seguindo as cinco categorias que o blueprint nomeia em prosa:

`primary-source` (já existe) · `history` · `theory` · `sociology` ·
`literature` · `commentary` · `reference`

*Ressalva honesta:* os dois valores existentes são qualificados por domínio
(`political-`) e os propostos são gerais. Ou se generaliza e depois se migram os
antigos, ou se mantém a mistura. **Recomendo generalizar.**

**P9 · `form` — que forma bibliográfica a obra tem.**
Hoje: `book, essay, lecture, speech, dialogue, treatise, novel, play`. Ficaram
nulos os poemas épicos, as coletâneas canônicas, o corpus epistolar, a obra de
referência em verbetes e o texto breve. Proposta de acréscimo:

`epic` · `scripture` · `letters` · `reference-work` · `poem`

**P10 · Id de obra sem autor pessoal.**
Sete obras desta coleção não têm autor. A forma observada no acervo é
`<autor>--<titulo>`. Usei **o título curto sozinho**, sem o prefixo de autor:
`enuma-elis`, `dhammapada`, `corpus-hermeticum`, `biblia`,
`epopeia-de-gilgamesh`, `evangelhos-canonicos`, `tabula-smaragdina`, com
`authors: []`. **Recomendação: ratificar** — é honesto (não há autor, não há
slot de autor) e reversível.

**P11 · Entrevistador em `authors`.**
Vittorio Messori entrevistou João Paulo II em *Cruzando o Limiar da Esperança*.
Está em `authors` porque o campo não distingue papéis, como também não distingue
tradutor — só que tradutor tem onde morar, no par obra–publicação, e
entrevistador não tem. **Recomendação: manter assim e revisitar** se aparecerem
mais livros-entrevista; criar um campo agora para um caso só é maquinaria
prematura.

### Propostas que eu retirei

Três sugestões minhas da conversa de 2026-09-20 foram retiradas por mim mesmo,
antes de virarem decisão dele:

- **Burkert e Vernant para Religião.** Contradiziam o `out_of_scope` que eu
  próprio propus, e o movimento VII não é sobre culto grego — é sobre mitologia
  comparada e hermetismo. Ficam na Greco-Romana.
- **Evangelhos, Ehrman e Vermes para a Greco-Romana.** O arquivo de lacunas de
  lá previu a possibilidade, mas previsão não é obrigação: Vermes opera em
  moldura judaica e Ehrman em crítica textual cristã; nenhum responde à pergunta
  daquela coleção. A região `religiao-romana-e-cristianismo-antigo` continua
  ausente, honestamente.
- **Agostinho como "o único Padre da Igreja".** Reformulada em P4, onde é
  pergunta sobre o caráter do movimento e não sobre tapar lacuna.


## 10 · Lacunas

Três registros abertos, todos **detecção pura**, com `candidates: []`. Forma
completa em `review/gaps/religion.yaml`.

- **Uma corrente sem quem a conteste** (registro religion--g01). A fenomenologia de Eliade ocupa seis
  das trinta participações e não tem interlocutor. Berger não cumpre esse papel:
  é sociologia, opera noutro registro e não discute o método. Detectar isto é
  automático; propor o crítico não é, e teria de ser a **melhor** exposição do
  outro lado (a regra de propor sempre o melhor do outro lado).
- **Um movimento que promete mais do que entrega** (registro religion--g02). O movimento V declara quatro
  tradições na frase dele e contém duas obras, ambas budistas.
- **Outro movimento que promete mais do que entrega** (registro religion--g03). O movimento chamado "Cristianismo"
  declara Padres, escolástica, Reforma e teologia, e não tem nenhum dos quatro.
  É, hoje, o movimento em que o cristianismo menos aparece como assunto próprio.

**Nenhuma delas é uma compra devida.** Uma coleção pode ser pequena, parcial e
deliberadamente incompleta (as regras de curadoria), e região ausente não é dívida (as regras de curadoria). O que
essas três lacunas registram é a distância entre o escopo que **ele declarou nas
frases das seções** e o que a coleção contém hoje — e a primeira coisa a fazer
com elas é decidir as participações da seção 7, que podem reduzir duas.

---

## 11 · O peso de Eliade

Vale dizer em prosa o que a lacuna g01 registra em dados, porque é o fato mais
saliente da coleção. **Mircea Eliade comparece em seis das trinta entradas** — os
três volumes da *História das crenças e das ideias religiosas*, o *Tratado de
história das religiões*, *O sagrado e o profano* e, com Culianu, o *Dicionário
das religiões*. Um quinto da coleção.

E não é só um autor recorrente: é **uma escola interpretativa** — a fenomenologia
da religião, com a hierofania e o *homo religiosus* — ocupando simultaneamente o
movimento I (a narrativa histórica), o movimento II (a teoria) e a obra de
consulta que acompanha tudo. Quem ler esta coleção na ordem aprenderá a ver
religião pelos olhos de Eliade três vezes antes de encontrar qualquer outra
lente.

A crítica acadêmica a ele é conhecida e substantiva: o caráter a-histórico da
comparação, a postulação de um sagrado universal transcultural, e a leitura das
tradições concretas através de uma estrutura dada de antemão.

**Isto é observação, e só.** A seleção é dele, não se toca, e nada aqui propõe
compra (as regras de curadoria, as regras de curadoria, as regras de curadoria dos princípios). Registro porque a as regras de curadoria manda reavaliar
coerência à medida que a evidência se acumula, e porque um acervo que não sabe
que tem uma voz dominante não pode decidir se quer ter.

---

## 12 · Estado bibliográfico

Das 30 obras: **21 com editora, ano e ISBN verificados** em página oficial de
editora ou catálogo institucional; 7 com ao menos um campo em hipótese; 2
bibliograficamente problemáticas (o Rahula indiano, sem registro em catálogo
nenhum; e *Cruzando o Limiar da Esperança*, cujo anúncio aponta para outro livro).

Todas as 28 obras novas estão `partially_researched`, com o que falta nomeado em
`missing`. O que falta é o mesmo para todas, e é substantivo: **a enumeração de
candidatos exigida pelas regras de pesquisa**, a forma e o tipo de obra, a
transmissão textual e a edição
crítica de referência do original, e disponibilidade datada com faixa de preço.

O que a pesquisa não resolveu, obra a obra:

- **tradutor não encontrado** em *O memorial de Deus* (Paulus) — procurado na
  ficha da editora, em livrarias brasileiras e portuguesas, em catálogos
  universitários e em referências ABNT de teses e periódicos; nenhuma fonte o
  nomeia. Fecha-se pela folha de rosto de um exemplar;
- **tradutores nominais da Bíblia de Jerusalém** — e aqui a resposta é positiva e
  documentada: a tradução **é creditada coletivamente**, e a recensão de Ney
  Brasil Pereira, ele próprio tradutor da edição de 1981, registra que a autoria
  das revisões de 2002 não é discriminada. Direção, coordenação e revisão
  literária estão nomeadas na proveniência da publicação;
- **ano** da edição de *Uma História de Deus* correspondente ao ISBN registrado,
  e a sua paginação;
- **ano** da edição brasileira dos evangelhos de Frederico Lourenço;
- **editora, ano e tradutor** das duas edições de *Cruzando o Limiar da
  Esperança*;
- **editora e ano** do exemplar indiano de *What the Buddha Taught*;
- **texto-base** da edição EDIPRO do Dhammapada — a que decide a as regras de curadoria.

## 13 · Edições, capas e links de compra — 2026-09-25

As edições registradas das 30 obras foram conferidas por ISBN contra os anúncios
de varejo.

- **Capas**: 30 edições ganharam capa (imagem principal do anúncio, convertida
  para WebP q80 nas mesmas dimensões). Os links de compra já existiam desde 19/09.
- **Gilgámesh**: as duas edições da Autêntica têm capa; a exibida passa a ser
  a de 2017 (*Ele que o abismo viu*, a edição acadêmica, com aparato) —
  proposta minha, a confirmar. A de 2021 continua registrada.
- **ISBN corrigido**: *Uma história de Deus* (Companhia das Letras) tinha o
  dígito verificador errado (…235 → …236). O ISBN-10 85-7164-423-3, já
  verificado na Agência Brasileira do ISBN, converte em …236.
- **Ehrman**: registrada `pub--harpercollins-brasil--o-que-jesus-disse--2015`
  (ISBN 978-85-220-3313-3, mesma tradução de Marcos Marcionilo da Prestígio
  2006), agora a exibida, por escolha sua. A Prestígio 2006 continua registrada.
- **Rahula**: registrada a Motilal Banarsidass 2017
  (`pub--motilal-banarsidass--what-the-buddha-taught--2017`), agora a exibida,
  por escolha sua. A Grove Press 1974 continua. As 119 p. do anúncio são poucas
  para a obra; conferir se é integral.
- **Cruzando o Limiar da Esperança — EM ABERTO**: você vai procurar outra
  edição. A Francisco Alves ISBN-10 8526503146 (1994, 210 p.) não foi
  registrada: preço inviável no anúncio (R$ 1.371).
