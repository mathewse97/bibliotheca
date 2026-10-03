---
collection: political-thought
kind: import-report + curation
by: claude
date: 2026-09-05
status: nada aplicado — tudo abaixo aguarda sua decisão
---

# 1 · Relatório de importação

**40 obras, 10 movimentos, 2 ordens suas.** Nada foi movido: `order_changes: []`.

| O que li | Resultado |
|---|---|
| Seções I–X | 10 `movement`, títulos seus, literais |
| "Por quê" | 40 `why_here`, transcritos, marcados `voce` |
| ★ | 27 obras marcadas `core: true` |
| "O esqueleto fundamental" | um `path` chamado `nucleo-duro`, 24 obras, ordem sua |
| Edições | 25 identificam edição concreta · 5 nomeiam preferência parcial · 10 são só intenção |

**Nenhuma edição foi registrada como verificada.** As 40 entram como
*sua escolha declarada* (`by: voce, verified: false`), não como conclusão de
pesquisa. A pesquisa do §E converte-as em registros verificados ou em
`verdict: rejected` com razão — nunca antes disso.

---

# 2 · Decisões — resolvidas em 2026-09-05

Registradas aqui para não voltarem à discussão. Todas aplicadas.

### 2.1 ★ e "núcleo duro" são conceitos separados — RESOLVIDO
★ marca importância **dentro da coleção completa**; o núcleo duro é um
caminho deliberadamente comprimido. Uma obra estrelada ausente de um caminho
é normal, não uma inconsistência, e **o sistema não reconcilia os dois**.

Pode sinalizar distorção; não pode corrigir. Sinalizadas no arquivo da
coleção, em `flagged_omissions`:

| Obra estrelada fora do núcleo | Preocupação |
|---|---|
| **Burke — Reflexões** | Sem ele, Rousseau → Tocqueville perde a objeção conservadora e a Revolução aparece sem contestação |
| **Schmitt — O Conceito do Político** | Sem ele, o caminho critica o liberalismo só a partir do libertarianismo e do marxismo, não da recusa da premissa parlamentar |
| **Berlin — Dois Conceitos** | Baixa. Mill e Rawls cobrem boa parte do terreno |

Ao dispensar qualquer uma destas, ela migra para `accepted_omissions` com a
sua razão e **nunca mais é levantada**.

### 2.2 O núcleo é uma espinha ocidental assumida — RESOLVIDO
Deliberado, e agora declarado no próprio caminho (`declares` +
`excludes_by_design`). Não é uma afirmação de que as seções II e III sejam
dispensáveis: a coleção completa inclui as tradições não ocidentais por
decisão sua. A consequência prática é que a análise de cobertura deixa de
redescobrir essa ausência como lacuna a cada execução.

Um caminho comparativo / não ocidental sobre os mesmos membros pode ser
criado depois: é aditivo, não altera este caminho nem a coleção.

### 2.3 Obras são unidades intelectuais, não livros — RESOLVIDO
Mudança de modelo, não de dados. Obra = unidade intelectual (livro, ensaio,
conferência, discurso, diálogo, tratado). Publicação física = objeto próprio,
que **pode conter várias obras**. Campo `form` no registro da obra, separado
de `work_type`.

| Caso | Obra(s) | Publicação |
|---|---|---|
| Weber | duas conferências, dois registros | um volume, contendo as duas |
| Berlin | *Dois Conceitos de Liberdade*, `form: essay` | *Quatro Ensaios sobre a Liberdade* |
| Orwell | *A Política e a Língua Inglesa*, `form: essay` | coletânea de ensaios |

Nota: `part_of` **não** se aplica a estes casos. Um ensaio numa coletânea de
editor é uma publicação que contém obras, não uma obra dentro de outra obra.
`part_of` fica reservado a volumes de uma obra autoral única.

### 2.3b Weber — destino das duas conferências — RESOLVIDO
*A Política como Vocação* permanece em Pensamento Político. *A Ciência como
Vocação* **sai** — não é membro só porque partilha volume. Casa provável:
Educação e/ou Cultura, a decidir pelos critérios dessas coleções.

**Contabilidade, porque a distinção importa:** a biblioteca ganha **1 obra**;
Pensamento Político **não ganha um 41º item**. A entrada original valia pelas
duas conferências, e o que ela significava para esta coleção era a política.
A coleção continua com 40 membros. Registrado em `structural_changes` com os
dois efeitos declarados em separado.

A publicação `pub--cultrix--ciencia-e-politica` **não mudou uma linha** com
essa saída — continua a conter as duas conferências. É o teste do modelo
obra/publicação, e ele passa: conter é propriedade do objeto físico,
pertencer a um currículo é outra coisa.

*A Ciência como Vocação* ganhou `pending_assignment`: obra sem coleção por
decisão declarada, isenta da checagem de órfãs até Educação e Cultura serem
importadas — e não depois disso.

### 2.4 Uma emenda à regra de identificadores
A regra do §C (id = título original) sobrevive ao contato com os dados, com
uma exceção: obras cujo título original é instável ou compartilhado.
Tucídides e Heródoto têm ambos *Ἱστορίαι*. Usei `tucidides--historiai`, mas a
regra precisa de uma cláusula: **título original quando estável e convencional,
título curto acadêmico convencional quando não** — sempre com `id_aliases`.
Isso vale para 4 das 40.

### 2.5 Obras que outras coleções vão reivindicar
Não criei nada fora desta coleção. Mas 14 destas obras têm reivindicação óbvia
de coleções que você ainda não me enviou — Greco-Romana (Platão, Aristóteles,
Tucídides, Cícero), Religião (Agostinho, Aquino, e Dostoiévski com bom
argumento), Educação (Platão, Aristóteles VII–VIII, Rousseau, Mill), Cultura
(Confúcio, Sun Tzu, Ibn Khaldun, Zamiátin, Huxley, Orwell). Ficam em espera:
quando as listas chegarem, entram como novas *memberships* do mesmo registro
canônico, com papel e posição próprios — sem nenhum registro duplicado.

---

# 3 · Lacunas

**Status: as três permanecem `open`. Nenhuma aceita.**
`recheck_after: outras-colecoes-importadas` — decisão sua de 2026-09-05.
Serão reavaliadas contra a biblioteca inteira antes de qualquer proposta de
aquisição, porque parte do que parece ausente pode estar noutra coleção, e
uma obra já presente precisa de uma nova *membership*, não de uma compra.

Três propostas abertas — o teto do §I. Cada uma nasce de um sinal na
estrutura da sua própria lista, não de "livros interessantes".

> **Aviso de método:** esta é a primeira coleção importada. Uma análise de
> lacunas com uma só coleção produz falsos positivos, porque parte do que
> parece ausente estará nas listas que faltam. As três abaixo são internas à
> lógica desta coleção e sobrevivem a esse teste; qualquer outra coisa
> espera as demais listas.

---

### G1 · Rawls sem o seu interlocutor direto
**Tipo:** dangling interlocutor · **Severidade:** alta

**Sinal.** A coleção põe Rawls (VIII) e a crítica libertária (IX) em oposição
declarada — é uma das tensões mais fortes da lista. Mas Rothbard e Hoppe **não
respondem a Rawls**: escrevem a partir de uma fundamentação de direitos
naturais que não engaja o argumento rawlsiano. A oposição existe na estrutura
da coleção e não existe nos textos.

**Candidato.** **Robert Nozick — *Anarquia, Estado e Utopia*.** É a resposta
direta e canônica a *Uma Teoria da Justiça*, escrita contra ela, e é o texto
que fez o debate acontecer. Edição brasileira a verificar na pesquisa do §E.

**Por que preferível.** Rothbard rejeita a pergunta de Rawls; Nozick aceita a
pergunta e recusa a resposta — o que é o que torna a tensão legível. Manter
Rothbard e Hoppe e acrescentar Nozick dá à seção IX um texto que dialoga com
VIII em vez de passar ao largo dela.

**Colocação proposta:** `political-thought`, entre `rawls--a-theory-of-justice`
e `rothbard--anatomy-of-the-state` · role `critical-response` · demand
`exigente` · `requires: [rawls--a-theory-of-justice]` · priority `core` ·
tensão nova com Rawls, substituindo a que hoje está mal atribuída a Rothbard.

---

### G2 · O termo médio ausente entre Montesquieu e Tocqueville
**Tipo:** sequence gap · **Severidade:** média-alta

**Sinal.** Vem da sua própria sequência. Montesquieu dá a teoria da separação
de poderes; Tocqueville descreve o que ela virou numa sociedade real. Entre a
teoria e a observação falta o momento em que ela foi **projetada e defendida**
— e é justamente esse momento que Tocqueville pressupõe conhecido.

**Candidato.** **Hamilton, Madison e Jay — *O Federalista*.** Edição brasileira
a verificar. Não é comentário: é fonte primária, e é o único texto da coleção
em que a arquitetura constitucional é argumentada por quem tinha de a fazer
funcionar.

**Por que preferível.** A alternativa seria uma história constitucional, que
seria comentário e violaria o seu critério de precedência das fontes.

**Colocação proposta:** entre `montesquieu--de-lesprit-des-lois` e
`rousseau--du-contrat-social`, ou logo antes de Tocqueville · role
`primary-source` · demand `moderado` · priority `secondary`.

---

### G3 · O marxismo está presente pelos textos que os seus críticos não atacam
**Tipo:** one-sided tradition · **Severidade:** média

**Sinal.** A tradição **não está ausente** — você tem dois Marx. Mas o
*Manifesto* é panfleto e o *18 de Brumário* é análise de conjuntura, e nenhum
dos dois é a exposição sistemática da teoria da história. Já Popper ataca
exatamente o historicismo, e Aron o mito revolucionário. Resultado estrutural:
três críticas de peso (Popper, Aron, e Arendt em parte) apontadas para uma
teoria que a coleção não contém.

**Candidatos, com a escolha explicitada:**

- **Marx & Engels — *A Ideologia Alemã*** (+ o Prefácio de 1859) —
  `gap-filler`. É onde a concepção materialista da história é enunciada de
  forma mais direta, é curto, e é literalmente o alvo de Popper. Melhor
  relação entre o que fecha e o que custa.
- **Marx — *O Capital*, Livro I** — `gap-filler` alternativo. Mais canônico e
  mais completo, e a Boitempo tem edição de referência a verificar. Mas é um
  compromisso de leitura desproporcional ao papel que a obra teria **nesta**
  coleção, que é de teoria política e não de economia política.
- **Gramsci; Lênin, *O Estado e a Revolução*** — `complementary`. Nenhum
  dos dois fecha a lacuna: são desenvolvimentos, não a exposição.

**Recomendação:** *A Ideologia Alemã*. **Colocação proposta:** antes de
`marx-engels--manifest-kommunistischen-partei` · role `foundational` · demand
`exigente` · priority `secondary`.

---

# 4 · Redundância e equilíbrio

### 4.1 Rothbard ×2 — parece redundante, e não é
*Anatomia do Estado* é breve e em boa medida contido em *A Ética da Liberdade*.
Em abstrato eu marcaria `redundant`. **Na sua sequência, não:** você os ordenou
`Anatomia → Ética`, o que faz do primeiro a porta de entrada do segundo. Isso é
exatamente o que o §I quer dizer com julgar contra o currículo e não contra o
catálogo. **Verdict: não redundante.** Registrado para não voltar à discussão.

### 4.2 Peso por posição — uma observação, não uma proposta
Contagem, sem juízo: crítica libertária do Estado, 3 obras; exposição marxista,
2 (ambas breves); crítica ao marxismo e ao totalitarismo, 4; liberalismo
igualitário, 1; teoria institucional da democracia, 1.

Uma biblioteca que reflete os seus interesses é legítima e não precisa de
correção. A observação é feita porque **você** definiu como objetivo a formação
geral com tradições concorrentes representadas pelos seus próprios textos.
G1 e G3 são a forma mínima de atender a isso; qualquer coisa além seria eu a
escolher a composição da sua biblioteca, o que não é o meu papel.

Nota simétrica, para não haver dúvida sobre o método: o desequilíbrio na
direção oposta seria sinalizado da mesma maneira e pelo mesmo tipo de sinal
estrutural.

---

# 5 · Prerequisitos que proponho (nenhum aplicado)

Você não declarou prerequisitos, e as setas do esqueleto são sequência, não
dependência — por isso `requires:` está vazio em todos os 40. Proponho estes
seis, que me parecem dependências reais e não meras adjacências:

| Obra | requires | Razão |
|---|---|---|
| `aristoteles--politika` | `platao--politeia` | A crítica é ininteligível sem o alvo |
| `hobbes--leviathan` | `maquiavel--il-principe` | A premissa desencantada vem daí |
| `locke--second-treatise` | `hobbes--leviathan` | Aceita o contrato para recusar a conclusão |
| `rousseau--du-contrat-social` | `hobbes--leviathan`, `locke--second-treatise` | Responde aos dois |
| `popper--the-open-society` | `platao--politeia` | O volume I é inteiramente sobre Platão |
| `hoppe--democracy-the-god-that-failed` | `rothbard--the-ethics-of-liberty` | Assume a fundamentação, não a refaz |

O de Popper é o mais útil e o menos óbvio: hoje a coleção lê Popper como
crítico de Marx, e ele é, mas metade do livro responde ao primeiro título
da sua lista.

---

# 6 · Obra acrescentada após a importação — 2026-09-06

**Yuri Bezmenov — *Subversão: Teoria, Aplicação e Confissão de um Método*.**
Decisão sua, fora do fluxo de importação da lista original: incluir em
`political-thought`, movimento VII ("Poder, partidos, massas e ideologia").

**Razão, nas suas palavras:** a obra trata primariamente de guerra política,
subversão ideológica, influência e transformação política das sociedades. Tem
dimensão psicológica, mas você não a considera o campo intelectual primário —
por isso não foi tratada como candidata a nenhuma coleção de psicologia
(inexistente no acervo, em todo caso).

**Colocação.** Última entrada do movimento VII, depois de Aron. Coloquei-a ali
por afinidade temática — Aron examina, de dentro do Ocidente, a atração dos
intelectuais pelo mito revolucionário; Bezmenov descreve, do lado de quem a
operacionalizava, o método soviético para cultivar essa mesma atração. É uma
leitura minha do encaixe, não uma instrução sua sobre a posição exata; a
coleção é `intellectual` (ordem carrega dependência), então a posição não é
neutra como seria em `survival-self-sufficiency` — mas VII já não é uma cadeia
estrita de pré-requisitos entre Michels, Schmitt, Arendt, Popper, Berlin e
Aron, e Bezmenov fecha essa série sem depender de nenhum predecessor
específico.

**`role: primary-source`.** Bezmenov é testemunha e ex-praticante do método
que descreve — não teórico nem crítico de segunda mão. Mesma lógica de
`role` que Tucídides ou Sun Tzu recebem noutras seções: fonte primária sobre
a prática, não comentário sobre ela.

**`original_order` não foi tocado.** Guarda, permanentemente, a lista que
você enviou em 2026-09-05. Esta é a primeira obra que entra em
`political-thought` fora daquela lista, e por isso não há mecanismo de
`order_changes` ou `structural_changes` a acionar — não é um desvio da sua
ordem original, é um membro novo.

**Estado bibliográfico: `partially_researched`.** Identifiquei o título
bilíngue e o ASIN/ISBN-10 (6599245404, convertido para ISBN-13 por cálculo,
não por catálogo), mas não consegui estabelecer com confiança se este livro é
tradução de uma obra inglesa específica de Bezmenov ou uma compilação sob
título próprio — `original_language` fica `null` em vez de suposto. Editora,
ano e tradutor também não identificados. Fica para pesquisa futura, sem
bloquear a inclusão: você decidiu a colocação, não a edição.

**Relação proposta, não confirmada por você:** `complements` com
`aron--lopium-des-intellectuels` (ver `works/bezmenov--subversao-teoria-aplicacao-e-confissao-de-um-metodo.md`).
Fica registrada como leitura de Claude; você pode dispensá-la.

---

# 7 · Lacunas aceitas — 2026-09-19

Você aprovou os candidatos de duas lacunas, e elas passaram a `accepted`:

- **`political-thought--g05`** — Kant, *Fundamentação da Metafísica dos
  Costumes* (1785), como `foundational`. É o termo moral que faltava entre
  Rousseau, *Do Contrato Social*, e Burke, *Reflexões sobre a Revolução em
  França*, e de que Rawls, *Uma Teoria da Justiça*, depende declaradamente —
  a dependência está registrada como `prerequisite_for` no registro da obra.
  *À Paz Perpétua* continua no registro da lacuna como complementar, e **não**
  entrou.
- **`political-thought--g04`** — Marcuse, *O Homem Unidimensional* (1964),
  como `critical-response`. Habermas, *Mudança Estrutural da Esfera Pública*,
  continua registrado como alternativa não aplicada: a lacuna fecha com
  Marcuse, e ele permanece disponível como candidato de outra natureza, mais
  voltado à esfera pública do que à integração da contestação.

A coleção passou de 41 para 43 membros. **A sua ordem não foi tocada** — as
duas entraram no fim da sequência, e `original_order` continua a guardar as 40
entradas da sua lista.

**A `g03` continua aberta**, e não foi absorvida por nenhuma destas. Ela é
sobre a exposição sistemática da teoria da história — *A Ideologia Alemã* — e
nem Kant nem Marcuse a fecham. Marcuse pressupõe essa teoria; não a expõe.

Nenhuma das duas obras tem edição: nada foi enumerado, verificado ou escolhido.

## 7.1 Correção de 2026-09-19 — movimento errado

As duas obras acrescentadas entraram no fim da sequência **sem movimento
próprio**, e um movimento é uma faixa: tudo o que vem depois do cabeçalho
pertence a ele até o cabeçalho seguinte. O resultado foi que Kant,
*Fundamentação da Metafísica dos Costumes*, e Marcuse, *O Homem
Unidimensional*, ficaram dentro do movimento **X. Literatura como crítica
política**, ao lado de Dostoiévski, *Os Demônios*, e Orwell, *1984*.

Erro meu, apanhado por você. Corrigido: cada uma ganhou o seu movimento —
**XI. A fundamentação moral que a disputa pressupõe** e **XII. A releitura
crítica do século XX** —, pelo mesmo procedimento usado em Educação quando
Illich, *Sociedade sem Escolas*, entrou. Os seus dez movimentos e a sua ordem
continuam intactos.

**Lição de método, que vale para os próximos acréscimos:** acrescentar ao fim
de uma sequência com movimentos NÃO é a opção conservadora. É uma afirmação
sobre a obra, e uma afirmação errada quando o último movimento tem tema
próprio.

## 7.2 Auditoria do movimento X, já que a pergunta foi feita

Você perguntou se tudo o que está ali é mesmo literatura. Conferi as sete
entradas: seis são ficção — Dostoiévski, *Os Demônios*; Zamiátin, *Nós*;
Huxley, *Admirável Mundo Novo*; Koestler, *O Zero e o Infinito*; Orwell, *A
Revolução dos Bichos* e *1984* — todas com `role: literary-treatment`.

A sétima **não é**: Orwell, *A Política e a Língua Inglesa*, é ensaio, e já
está registrada com `role: supplementary`, diferente das outras seis. Ela é sua
e está no movimento que você criou, então não mexo — mas registro a
observação: o título do movimento fala de literatura, e o conteúdo é de seis
obras de ficção mais um ensaio sobre linguagem política. Se quiser, o ensaio
pode ir para um movimento próprio, ou o título do movimento pode passar a algo
como "Literatura e linguagem como crítica política", que descreveria as sete.
Qualquer das duas é decisão sua.

## 7.3 Colocações corrigidas por aprovação — 2026-09-19

Os movimentos XI e XII, que eu criei para acomodar as duas obras novas, foram
**removidos**. A coleção volta aos seus dez movimentos. As três obras foram
colocadas dentro da estrutura que já existia:

| Obra | Movimento | Por quê |
|---|---|---|
| Kant, *Fundamentação da Metafísica dos Costumes* (1785) | IV. Formação da política moderna, depois de Rousseau, *Do Contrato Social* (1762) | O movimento pergunta de onde vem o poder e o que o limita; Kant dá o fundamento moral do limite. A posição é também cronológica: entre Rousseau e Burke, *Reflexões sobre a Revolução em França* (1790). |
| Marcuse, *O Homem Unidimensional* (1964) | VI. Socialismo, marxismo e revolução, depois de Marx, *O 18 de Brumário* | É o movimento que nomeia a tradição. Marcuse é a releitura dela depois de a previsão falhar — e é dentro do movimento que a assimetria da `g04` de fato se corrige. |
| Orwell, *A Política e a Língua Inglesa* (1946) | VII. Poder, partidos, massas e ideologia | **Não é literatura.** É ensaio, publicado na revista *Horizon* em 1946. Já estava registrado com `role: supplementary`, ao contrário das seis ficções do movimento X, todas `literary-treatment`. O movimento VII trata do que a política moderna produziu quando aplicada: propaganda, eufemismo, ideologia. |

`order_changes` deixou de estar vazio — é a primeira vez em todo o acervo. As
três entradas são reversíveis e dizem de onde cada obra veio. Sua ordem
relativa das seis ficções do movimento X não mudou, e `original_order`
continua a guardar a sua lista verbatim.

A regra que nasceu disto está em `config/curation-rules.md` §6.9, incluindo a
sua decisão de que a ordem enviada é sugestão inicial e que cabe ao agente
validá-la e propor melhorias — com pesquisa, nunca por inferência.

---

# 8 · Os três elos da cadeia — 2026-09-19

Entraram por aprovação sua, e nenhuma cria movimento novo:

| Obra | Movimento | Posição e razão |
|---|---|---|
| Marx e Engels, *A Ideologia Alemã* (1845–46, publicada em 1932) | VI | Antes do *Manifesto*, exatamente como a lacuna `g03` propunha desde 2026-09-05. É a exposição que o panfleto pressupõe e que Popper, *A Sociedade Aberta e Seus Inimigos*, ataca. **`g03` passa a `accepted`.** |
| Lukács, *História e Consciência de Classe* (1923) | VI | Entre *O 18 de Brumário* e Marcuse, *O Homem Unidimensional*. Ordem cronológica e lógica dentro do movimento: 1846, 1848, 1852, 1923, 1964. Sem ele, o salto de Marx a Marcuse é de quase oitenta anos. |
| Habermas, *Mudança Estrutural da Esfera Pública* (1962) | VIII | Abre o movimento das reconstruções, antes de Dahl, *Sobre a Democracia*, e Rawls, *Uma Teoria da Justiça*, que são posteriores. **Não** foi para o movimento VI: a SEP adverte que tratá-lo como membro da Escola de Frankfurt é enganoso, e o que ele faz é responder à tradição, não continuá-la. |

Todas as três com fonte citada no registro da obra, conforme a §6.9. As
inserções estão em `order_changes`, reversíveis uma a uma.

A coleção passou de 43 para 46 membros, e o movimento VI deixou de ser o mais
magro da sequência: tinha dois Marx, tem agora cinco obras cobrindo 1846 a 1964.

**Nenhuma tem edição.** Nada foi enumerado, verificado ou escolhido.

---

# 9 · A pergunta sobre a família — avaliada em 2026-09-19

Você perguntou se a destruição dos valores da família tradicional seria uma
das consequências desse panorama, e depois esclareceu que não queria obras
dedicadas ao tema: achava que a questão já estaria coberta pelas obras sobre a
Escola de Frankfurt e a crítica ao Ocidente. **Não estava**, e a pesquisa feita
para avaliar isso trouxe um achado que vale mais do que a resposta.

## 9.1 O que a biblioteca podia responder, e o que não podia

Com o que entrou nesta rodada, você consegue seguir boa parte da cadeia: a
razão instrumental e a indústria cultural em Adorno e Horkheimer, *Dialética
do Esclarecimento*; a absorção da contestação em Marcuse, *O Homem
Unidimensional*; a repressão exigida pela civilização em Freud, *O Mal-Estar
na Civilização*; a formação da disciplina em Weber, *A Ética Protestante e o
Espírito do Capitalismo*; e a crítica pelo outro lado em Scruton, *Culture
Counts*.

O que **não** está no acervo é a peça em que a tese sobre família e autoridade
é formulada pelos próprios autores. Ela existe, e tem endereço: *Estudos sobre
Autoridade e Família* (1936), organizado por Horkheimer e publicado em Paris
pelo Instituto no exílio, com a parte sociopsicológica de Erich Fromm; e *A
Personalidade Autoritária* (1950), de Adorno com Frenkel-Brunswik, Levinson e
Sanford, que constrói a escala F e liga traços de personalidade a experiências
da infância.

Registrado como `political-thought--g06`, aberta, com candidatos e sem nada
aplicado.

## 9.2 O achado, que contraria a versão corrente

A Stanford Encyclopedia of Philosophy descreve que a escola analisou a mudança
na família moderna e sustentou que **o declínio das figuras de autoridade na
família** contribuiu para o declínio das capacidades críticas — do indivíduo e
da sociedade.

Isso é quase o oposto do que a versão popular lhes atribui. Eles não celebram
a dissolução da família: temem que, sem a instância em que a consciência e a
autonomia se formavam, o indivíduo fique exposto **diretamente** à cultura de
massa e à autoridade externa, sem nada no meio.

A tese deles sobre a família patriarcal é, portanto, **ambivalente**: a mesma
instituição que produz obediência produz também a interioridade capaz de
resistir. Quem lê apenas os críticos recebe metade disso; quem lê apenas a
versão conspiratória não recebe nenhuma.

Isso não anula a disputa legítima. Continua de pé a acusação de que a escola
tratou a família tradicional como problema a superar, e a discordância real
sobre se ideias mudam instituições ou apenas as acompanham. O que a pesquisa
mostra é que a resposta honesta exige ler o que eles escreveram, e não o que se
diz que escreveram — dos dois lados.

## 9.3 Ressalva que ficou escrita no registro

*A Personalidade Autoritária* é alvo de crítica metodológica séria e antiga:
viés de amostra, construção da escala F, direcionamento político do
instrumento. Se ela entrar, entra com isso registrado, e não como conclusão
estabelecida — pela mesma regra que vale para qualquer obra: o que é disputado
aparece como disputado.


---

# Edições, capas e links de compra — 2026-09-23

18 publicações novas, todas com capa e link de compra; a `publication_pref`
de cada obra aponta para a edição escolhida por você.

- **Trocas de edição, por decisão sua:** Rousseau (Martin Claret, trad. Ana
  Resende), Rothbard, *Anatomia do Estado* (Vide, trad. Matheus Pacini), Aron
  (Vide, 2024). As indicações antigas continuam no `edition_pref`, como registro.
- **Obras novas, posição a confirmar:** Klemperer, *LTI* (movimento VII, depois
  de Orwell); Levitsky & Ziblatt, *Como as democracias morrem* (VIII, depois
  de Dahl).
- **Tocqueville:** registrado só o Livro I (Martins Fontes). O Livro II é outro
  volume, não registrado.
- **Agostinho:** os três volumes da Gulbenkian registrados; a coleção mostra o I.
- **Pendentes, sem decisão tomada:** *A República* — duas candidatas: a EDUFPA
  (bilíngue, já registrada) e a Gulbenkian (Rocha Pereira), que é a indicação
  da coleção. *Política* — duas candidatas: Madamu e UnB (mesmo tradutor, Gama
  Kury); a indicação e o registro são UnB.
