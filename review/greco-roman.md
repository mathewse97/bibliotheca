---
collection: greco-roman
kind: import-report + avaliação curatorial
by: claude
date: 2026-09-12
status: "Importada — 74 obras a partir de uma lista de 57 entradas, porque três
         entradas eram volumes que viraram obras individuais, com a sua
         aprovação. Três lacunas registradas e uma proposta estrutural em
         aberto: dividir ou não a coleção entre Grécia e Roma."
---

# Revisão curatorial — Cultura e História Greco-Romana

Importada em 2026-09-12. Quinta coleção do acervo. É, por larga margem, a
maior: 74 membros contra 40 de Política, 11 de Educação, 11 de Sobrevivência e
4 de Cultura.

Este arquivo é avaliação. O que é fato canônico está em
`collections/greco-roman.md`; as lacunas estão em `review/gaps/greco-roman.yaml`;
a proposta estrutural em `review/structural/greco-roman.yaml`.

---

## 1 · O que a importação teve de corrigir

Quatro correções de transcrição e modelagem. Nenhuma delas é julgamento
curatorial: são fatos verificáveis, e todas foram decididas por você.

**1.1 Numeração.** A lista tinha 57 entradas numeradas até 52. As seções VIII e
IX reiniciavam em 40, repetindo os números 40 a 44. Nenhuma obra se perdeu.

**1.2 Três entradas eram publicações, não obras.** *A Trilogia Tebana* de
Sófocles, *Teatro Completo II–V* de Eurípides e a seleção de *Vidas Paralelas*
de Plutarco. Expandidas em 3, 13 e 7 obras respectivamente, com os volumes
registrados em `publications/`. É a distinção do §1 das regras de curadoria, e
o efeito dela aqui não é formal: sem a expansão, treze tragédias de Eurípides
teriam **uma** posição de leitura e **nenhuma** relação individual com o resto
da coleção. A Poética de Aristóteles não poderia declarar `requires` sobre uma
tragédia específica; a tensão entre Aristófanes e Platão sobre Sócrates não
teria onde ser registrada.

**1.3 Finley é organizador, não autor.** *O Legado da Grécia: uma nova
avaliação* é um volume coletivo de ensaios. O registro da obra declara isso;
os ensaios individuais não foram pesquisados, e essa indefinição está declarada
e não resolvida.

**1.4 "Seleção grega" incluía César.** Plutarco escreveu as Vidas em pares
grego/romano e Alexandre é pareado com César. Por decisão sua, César fica e o
rótulo foi corrigido — o par é o único ponto da coleção em que a passagem
Grécia → Roma acontece dentro de uma fonte antiga.

---

## 2 · A pergunta da coleção, e a ambiguidade que ela carrega

O nome anuncia "Cultura e História", mas cerca de 60% dos membros são
literatura e filosofia, e os movimentos V e VI são um curso de filosofia antiga
completo. A pergunta que propus — *como a cultura grega se formou, se converteu
em pensamento, e foi herdada por Roma e pelo Ocidente* — é a que a sua ordem de
fato executa. Ela é `proposta`, não `estabelecida`.

**A ambiguidade em aberto é a filosofia.** Platão e Aristóteles já estão em
Política por outra razão, e estão agora aqui por uma terceira. Enquanto não
existir uma coleção de Filosofia a questão é teórica — três participações do
mesmo registro canônico são exatamente o que a arquitetura suporta. Quando
existir, a pergunta não será "de quem são estas obras" (de ninguém: o registro
é único), mas "qual coleção argumenta por elas". Registro como questão em
aberto, não como pendência.

**A segunda ambiguidade é o nome.** Não propus renomear. Um nome só precisa
mudar quando deixa de representar a pergunta, e "Cultura e História
Greco-Romana" ainda a representa — *cultura* no sentido largo, que inclui o
pensamento. Se o escopo vier a ser refinado para excluir a filosofia, o nome
precisará ser reavaliado junto.

---

## 3 · A proposta estrutural: dividir Grécia e Roma

Registrada em `review/structural/greco-roman.yaml` como `greco-roman--sp01`,
status `open`, com gatilho declarado.

**Por que não dividir agora.** Três razões, e a primeira é a que decide:

1. O argumento da coleção **é** a transmissão. Virgílio é lido contra Homero,
   Cícero e Sêneca contra os gregos que apropriam, Ovídio contra a tradição
   mitológica das seções II e III. Numa coleção "Roma" separada, esse argumento
   deixa de ser uma sequência — que o sistema registra bem — e vira uma relação
   entre coleções, que ele registra mal.
2. Uma coleção "Roma" hoje teria 9 membros e um `scope_map` que reivindicaria
   República, Império, historiografia antiga, direito, religião e teatro —
   território que a sua lista não cobre. Toda análise de cobertura futura
   devolveria uma fila de ausências. Dentro da coleção greco-romana, a mesma
   escassez é um movimento mais fino que os outros: um fato, não uma dívida.
3. A escada do §4 manda responder no degrau mais baixo que resolva. Onze
   movimentos resolvem.

**Por que a proposta fica aberta mesmo assim.** O gatilho não é tamanho, é
evidência. Se Roma ganhar fontes antigas próprias — Lívio, Tácito, Salústio, o
Cícero republicano, teatro latino — a coleção passará a conter duas perguntas
de fato, e aí a exceção do §4 se aplica: não dividir é que corrompe a
maquinaria de escopo, porque a cobertura passa a medir contra a união de dois
territórios. O gatilho está escrito no registro para que não precise ser
redescoberto.

---

## 4 · Participações sobre registros existentes

Três membros não são registros novos: `platao--politeia`,
`aristoteles--politika` e `tucidides--historiai` vieram de Política. Cada um
recebeu uma participação com papel, posição e `scope` próprios — o campo
`scope` diz explicitamente o que a obra faz **aqui** que não faz lá.

Isto é o caso previsto pelo §2.7, e é a primeira vez que ele aparece em escala:
até agora o acervo tinha sobreposição zero entre coleções. É também o primeiro
teste real do princípio "um registro canônico, várias participações" — se
alguma coisa na arquitetura estava errada nesse ponto, é aqui que aparece.

Uma consequência prática: as lacunas de Política podem ter mudado. Nada foi
alterado lá; a revalidação automática de cada build reexecutará os `check:`
existentes. Se alguma lacuna de Política dependia da ausência de fontes
gregas, ela ficará `stale` sozinha.

---

## 5 · As duas reordenações aprovadas, e a que eu retirei

**Finley + Highet → XI (aprovada).** A que eu recomendei sem ressalva. A seção
VII terminava com dois livros sobre o Renascimento e o Ocidente moderno, dentro
de um movimento sobre historiografia e instituições gregas.

**Epicteto → X (aprovada), com perda declarada.** Ganhou-se a única dependência
direta entre dois autores visível na própria ordem da coleção: Marco Aurélio
leu Epicteto. Perdeu-se o par Epicuro–Epicteto do movimento VIII, que tinha um
argumento próprio — as duas escolas helenísticas como respostas à perda do
mundo político da pólis. A compensação está declarada no `purpose` do movimento
VIII; quando a pesquisa das obras existir, a relação deve ser registrada
explicitamente em `relations`.

**Historiografia antes de tragédia (retirada por mim).** Eu a propus e a
retirei depois de ler a sua ordem inteira. A sua sequência não é cronológica —
é genética, e cada movimento explica como o anterior se transformou. Mover
Heródoto e Tucídides para o meio conserta uma dependência factual e destrói o
argumento que estrutura a coleção. O problema real — ler *As Nuvens* e a
*Apologia* antes da guerra que as explica — é exatamente o que um caminho
alternativo resolve a custo zero, e você aprovou o caminho cronológico.

**Jaeger na posição 5 (mantida).** A observação continua válida: *Paideia*
comenta obras que, nesta ordem, ainda não foram lidas. Mas ela é o único item
da lista que declara a **tese** da coleção — que literatura, religião, política
e filosofia gregas são um só projeto formativo —, e os movimentos II a VI são o
teste dessa tese. Lida em quinto lugar ela não é exegese, é programa. O custo
fica registrado na entrada, e o caminho cronológico a coloca depois.

---

## 6 · Cobertura — o que o mapa mostra

Dezoito regiões. Dez `covered`, três `thin`, cinco `absent`. Nenhuma
`not-pursued`: essa decisão é sua e eu não a tomei.

A assimetria é o achado. A **Grécia** está coberta em quase toda a sua largura:
formação histórica, mito, religião praticada, drama, filosofia,
historiografia, instituições. **Roma** entra por dois historiadores modernos,
quatro obras literárias, três filósofos morais e um tratado militar — e **sem
uma única fonte antiga sobre a própria história romana**. A coleção estuda como
os gregos narraram a si mesmos e como os romanos escreveram poesia e moral, mas
não como os romanos narraram a si mesmos.

Três das cinco regiões `absent` são consequências disso ou do recorte declarado:
`arte-arquitetura-cultura-material`, `ciencia-e-medicina-antigas`,
`religiao-romana-e-cristianismo-antigo`. A primeira é a que mais tensiona o
nome da coleção: "Cultura" no título, e nenhuma obra sobre o que a cultura
greco-romana produziu em objetos.

Nada disso é defeito, e nada disso gerou recomendação. Ver
`review/gaps/greco-roman.yaml`: três registros, todos `candidates: []`.

---

## 7 · Edições

Atualizado em 2026-09-12, depois do levantamento que você fez na Amazon: **59
publicações registradas, cobrindo 67 dos 74 membros.** A coleção passou de não
ter praticamente nenhuma edição a ter quase todas — mas o nível de evidência
não mudou: tudo veio de anúncios de varejo, tier 7, e nada foi confirmado em
catálogo de editora. Todas as publicações estão `partially_researched`.

### 7.1 O caso inverso ao de Eurípides: a Oresteia

A Iluminuras publica a Oresteia em três volumes (Torrano). Onde o Teatro
Completo punha muitas obras num volume, aqui uma obra está repartida em três.

Decisão sua de 2026-09-12: **continua uma obra, com três publicações.** O teste
que a distingue da Trilogia Tebana é se cada parte se sustenta sozinha como
argumento. *Antígona* sustenta — foi escrita doze anos antes de *Édipo Rei* e é
encenada isolada rotineiramente. *Coéforas* não: abre sobre o túmulo em que
*Agamêmnon* termina, e sem isso o ato central da peça não tem premissa. A
Oresteia é a única trilogia conexa sobrevivente, composta e encenada como
unidade num único dia de 458 a.C.

Consequência para a interface: o indicativo visual de volume compartilhado
precisa existir nos DOIS sentidos — "este volume contém N obras" e "esta obra
vem em N volumes". Xenofonte (Loeb I e II) é o mesmo formato sem a carga
intelectual: um livro grande partido em dois.

### 7.2 Duas obras com duas publicações, por desenho

Ilíada e Odisseia têm a caixa Penguin (Frederico Lourenço), que você já possui,
e as edições bilíngues da Editora 34 (Trajano Vieira). Não é duplicata: é
exatamente o caso que justifica a separação Obra × Publicação, e é a primeira
vez que ele aparece no acervo por escolha, não por acidente.

### 7.3 A Metafísica é parcial, e a preferência é deliberada

320 páginas não comportam os catorze livros da *Metafísica* em português — a
edição da Vozes é volume de uma tradução em curso. Nenhuma fonte pública
(blog da Vozes, página de autor, ficha da Livraria Vozes) declara o sumário; a
relação exata de livros fica por confirmar com o exemplar em mãos.

A edição foi mantida mesmo assim, e a razão está registrada: é a primeira
tradução integral e direta do grego publicada no Brasil, e as alternativas
completas são inferiores no critério que decide — Edipro (Bini) e Loyola
(Perine, via o italiano de Reale) não são diretas do grego. É uma escolha de
qualidade de tradução sobre completude, declarada e não escondida.

### 7.4 Vegécio: a única troca por razão intelectual

A Oakpast (inglês) é reimpressão comercial sem aparato. A *Compêndio da Arte
Militar* da Imprensa da Universidade de Coimbra (Gouveia Monteiro & Braga) é
edição acadêmica com comentário, em português. Único caso da coleção em que
hierarquia de idiomas e qualidade acadêmica apontam para o mesmo lado. As duas
ficam registradas, com veredito `recommended` para a Coimbra e `alternative`
para a Oakpast.

### 7.5 As sete obras ainda sem edição — e por que isso não é uma pendência

*As Bacantes*; quatro Vidas de Plutarco (Sólon, Temístocles, Péricles,
Alcibíades); Kirk, Raven & Schofield; Campbell.

**Kirk, Raven & Schofield é o único caso com decisão registrada.** A edição da
Fundação Calouste Gulbenkian é a referência em português e está, hoje, a um
preço que a torna inviável. Decisão sua de 2026-09-12: a obra permanece na
coleção com a mesma necessidade, sem edição de registro, à espera de reimpressão
ou de exemplar a preço razoável.

Isto é a regra §2.4 funcionando pela primeira vez sobre um caso real: preço e
disponibilidade são **contexto**, e contexto não hierarquiza. A obra não desceu
de importância por ser cara. O que ficou vazio foi a publicação, não a
participação — e a interface mostra uma coisa e não a outra.

### 7.6 Obras passageiras

Quatro volumes trazem obras que não são membros desta coleção: o Teatro
Completo I (O Ciclope, Alceste), o Aristófanes da Zahar (Só para mulheres, Um
deus chamado dinheiro), as *Tragédias* de Ésquilo pela Iluminuras (Os Persas,
Sete contra Tebas, As Suplicantes, Prometeu Cadeeiro) e o volume 15 de Plutarco
(Vida de Cícero).

Nenhuma foi registrada como obra. Comprar um volume não faz das outras peças
membros da coleção, e criar registros para elas seria expandir o acervo por
efeito colateral de uma decisão de compra. Ficam anotadas no `contains` da
publicação correspondente, onde pertencem.

Duas merecem atenção quando você reavaliar o escopo: o *Prometeu* é a peça de
Ésquilo com mais peso filosófico e está fora da sua seleção; e a *Vida de
Cícero* é a única fonte antiga sobre um romano republicano que estas edições
trazem — ela toca de raspão a lacuna `greco-roman--g01` sem a fechar.

### 7.7 Uma observação de consistência, não uma correção

> **SUPERADA em 2026-09-17 (piloto de pesquisa).** A página da Editora 34 declara *O Banquete* como edição bilíngue português/grego. Não há quebra de série bilíngue. Ver `publications/pub--editora-34--o-banquete.md`.

*O Banquete* é o único Platão fora da série bilíngue da EDUFPA que você
escolheu para *A República*, *Apologia/Críton* e *Fédon*. A tradução de José
Cavalcante de Souza pela Editora 34 é referência, então não é erro — mas é a
única quebra de série dentro do movimento VI, e a série da EDUFPA é bilíngue
grego-português, que é o formato que você declarou preferir para obras gregas.

### 7.8 O que continua sem pesquisa

Os 71 registros de obra novos permanecem `not_researched`. Ter edição não é ter
pesquisa: sabemos agora por qual objeto físico cada obra será lida, e continuamos
sem saber data de composição, gênero, tradição ou relações — que é o que os
campos nulos dizem, e por isso continuam nulos.

## 8 · Tensões

Quatro registradas, e é a primeira coleção do acervo com tensões reais em
número. Educação tinha uma (Adler × Illich); Cultura e Sobrevivência, nenhuma;
Política tem as suas. Aqui elas são metodológicas e não ideológicas —
Veyne × Burkert sobre o que "acreditar" significa, Vernant × Burkert sobre
estrutura contra história, Campbell × Vernant sobre universalidade — com uma
exceção que é factual e não interpretativa: **Aristófanes × Platão sobre quem
era Sócrates**, duas fontes contemporâneas e incompatíveis, uma das quais
responde nominalmente à outra.

Essa última é o achado mais interessante da coleção, e ela só existe porque a
sua ordem coloca *As Nuvens* antes da *Apologia*.

---

# Capas e links de compra — 2026-09-23

Escopo decidido por você: capas e links; campos em branco e comparação de
edições ficam para depois, obra por obra.

## O que foi feito

- **51** publicações registradas conferidas pelo ISBN. Todas agora têm link
  de compra; 46 ganharam capa (5 já tinham).
  Capas de vendedor, conferidas por exame da imagem contra a editora do
  registro.
- **As Nuvens (Zahar):** o ISBN registrado tinha o dígito final inválido
  (erro de digitação). Corrigido para 978-85-7110-306-1, o do anúncio.
- **Ésquilo, Tragédias (Iluminuras, Torrano, bilíngue)** — incluído por
  decisão sua: quatro obras novas (Os Persas, Os Sete contra Tebas, As
  Suplicantes, Prometeu Cadeeiro), no movimento IV logo depois da Oresteia.
  **Posição a confirmar**: pela cronologia, ao menos Os Persas é anterior à
  Oresteia. Ano do volume em conflito (2009 na resenha × 2000 no anúncio).
  **Posição confirmada por você em 2026-10-05** (cartão `d-pos-esquilo`,
  opção A): as quatro ficam depois da Oresteia; a ordem de data foi recusada.
  O conflito do ano do volume continua aberto.
- Capas de Vidas Paralelas (Coimbra) são de baixa resolução no anúncio.

## Edições alternativas encontradas em anúncio — mantidos os registros (decisão sua)

| Obra | Edição alternativa (anúncio) | No registro |
|---|---|---|
| Hansen, Athenian Democracy | Univ. of Oklahoma Press, 1999 (978-0806131436) | Blackwell (978-0-631-13822-8) |
| Burkert, Religião grega | Publicações Europa-América, 2026 (sem ISBN no anúncio) | Gulbenkian (978-972-31-0596-4) |
| Finley, Os gregos antigos | Publicações Europa-América, 2025 (sem ISBN no anúncio) | Edições 70 (978-972-44-0330-4) |
| Aristóteles, Política | Madamu, 2021, trad. Gama Kury (978-6586224085) | UnB, trad. Gama Kury (978-85-230-0011-0) |
| Vegécio, De Re Militari | Leonaur, 2012 (978-0857068200) | Oakpast (978-0-85706-821-7) |
| Epicuro, Carta sobre a felicidade | Unesp, 2002 (978-8571393974) | Unesp (978-85-393-0279-6) |
| Sófocles, A trilogia tebana | Zahar, 1990 (978-8571100817) | Zahar (978-85-378-0217-5) |
| Xenofonte, Hellenica I | Loeb 88 (978-0674990982) | Loeb 88 (978-0-674-99088-3) |

Nenhum registro foi alterado. Os dois da Europa-América aparecem no anúncio sem
ISBN, e pedem conferência antes de qualquer troca.

## Sem publicação na coleção

`euripides--bakchai` e `kirk-raven-schofield--the-presocratic-philosophers`
continuam sem edição registrada (Kirk: decisão sua de 2026-09-12, por preço).
