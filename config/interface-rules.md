# Regras da interface — o que chega à tela do Mathews

Aprovadas por ele em 2026-09-21, depois de uma auditoria que encontrou, só na
aba *Revisão e lacunas*, cinco classes de jargão — nomes de campo crus,
referências a parágrafo de regra, valores de vocabulário, identificadores
técnicos como título, e cinco blocos de JSON despejados na tela.

Este arquivo cobre um lado que as demais regras não cobriam. O
`curation-rules.md` e o `bibliographic-rules.md` governam **o que é verdadeiro
e o que pode ser gravado**. Nenhum dos dois dizia uma palavra sobre **o que é
legível**, e o `AGENT.md` define `_generated/` em cinco palavras. O resultado
previsível: todo agente escreve pensando no registro e despeja o registro na
tela.

Válido para qualquer agente, não só o Claude.

---

## 1 · A tela é para ele, não para o esquema

**Nenhum identificador de esquema aparece em texto renderizado.** Isso inclui:

- nomes de campo — `scope_map`, `why_here`, `pending_assignment`, `work_type`,
  `order_changes`, `inclusion_criteria`, `research_status`;
- valores de vocabulário controlado — `one-sided-tradition`, `gap-filler`,
  `not_researched`, `absent`, `thin`, `covered`, `unassessed`;
- referências a parágrafo de regra ou a arquivo de configuração —
  `curation-rules.md §4`, `§E.2`, `§6.9`;
- estruturas de dados: nenhum bloco JSON ou YAML vai para a tela. Um objeto
  vira frases.

**O identificador não desaparece — muda de lugar.** O id de um registro
(`religion--g01`) continua visível como nota de rodapé, para rastreabilidade,
nunca como título. O título é o que a coisa é, em português.

**Quem traduz é o template, não o autor do texto.** Valores de campo têm mapa
de tradução em `tools/ui.template.html`; acrescentar um valor novo ao
vocabulário implica acrescentá-lo ao mapa, na mesma tarefa. Um valor sem
tradução aparece cru, e isso é um defeito, não um estado aceitável.

**Texto escrito à mão é escrito para ele desde o início.** O `statement` de uma
lacuna, o de uma proposta estrutural e o corpo de uma revisão são lidos por ele.
Se a frase só faz sentido para quem escreveu o esquema, está errada.

## 2 · Duas audiências, duas camadas — e nesta ordem

Um arquivo de revisão serve a duas audiências ao mesmo tempo: é registro
curatorial (precisa de precisão e de referência à regra) e é tela (precisa de
linguagem corrente). Essa colisão é a causa da maior parte do jargão.

A regra: **a revisão abre pelo que ele precisa decidir, em linguagem corrente, e
o fundamento técnico vem depois.** Concretamente, todo `review/<coleção>.md`
começa por uma seção que responde, sem vocabulário interno:

1. o que foi feito;
2. o que espera decisão dele, em ordem de importância;
3. o que explicitamente **não** espera nada dele.

As seções seguintes podem ser tão técnicas quanto o registro exigir. A
informação é a mesma; o que muda é a ordem, e a ordem é a favor de quem lê.

**Todo `review/*.md` tem cabeçalho de metadados** com `collection`, `kind`,
`by`, `date` e `status`. Sem ele a interface não sabe de que coleção o
documento é e o mostra como linha sem nome — foi o que aconteceu com
`greco-roman.md` e `religion.md` até 2026-09-21. O `status` é uma frase em
português, não um resumo em siglas.

## 3 · Critério de pronto: a tela entra na verificação

`python3 tools/build.py` terminar com **problemas 0** verifica integridade
referencial — se o autor existe, se a obra existe, se a capa está no disco.
**Não verifica se o resultado é compreensível**, e confiar nela para isso produz
confiança falsa. Já aconteceu: uma lacuna foi reescrita, a build fechou limpa, a
aba não foi aberta, e o relatório disse que a aba estava corrigida.

Portanto:

- **Nenhuma tarefa que altere o que aparece na tela se declara concluída sem
  renderizar a tela e olhar o resultado.** A build local produz
  `_generated/bibliotheca.html`; abri-lo num navegador headless e ler o texto
  renderizado é barato e é obrigatório. Isto **não** é ler `_generated/` para se
  orientar, o que o `AGENT.md` proíbe: é verificar a própria saída antes de
  entregá-la.
- **O relato diz o que foi verificado e o que não foi.** "Corrigi o jargão" não
  é relato; "auditei as oito abas, corrigi estas quatro classes, esta permanece
  nas outras seis coleções" é.
- **Correção de classe, não de instância.** Quando ele aponta um sintoma, a
  pergunta é onde mais esse sintoma ocorre. Corrigir só o caso apontado e
  relatar como se a classe estivesse resolvida é a falha que originou estas
  regras.
- **Varredura automática de prosa é proibida.** Substituição mecânica de termos
  em texto corrido já foi tentada em 2026-09-20: passou na verificação
  automática e produziu 55 construções agramaticais em 13 arquivos —
  "é a distinção do as regras de curadoria das regras de curadoria". Foi
  revertida. Prosa se corrige lendo cada frase.

## 4 · Ao apresentar uma decisão a ele

O pipeline de entrada de obra termina em "validar e gravar". Falta o passo que
gera o atrito: **apresentar a decisão numa forma decidível**. Uma decisão
apresentada a ele traz, sempre:

- **o que é**, em uma frase, sem pressupor que ele conheça a obra ou o autor —
  nome do autor sozinho não informa; nome da obra e o que ela faz, sim;
- **as opções**, e o que cada uma produz concretamente;
- **a recomendação**, com a razão — ou a declaração explícita de que a decisão é
  dele e por quê;
- **o que a pesquisa já resolveu**, para que ele não decida o que não precisa
  ser decidido.

## 5 · Fundo dos cartões de coleção

Decisão do Mathews, 2026-09-24.

- **Com foto:** a coleção pode ter uma foto ligada ao tema, **fornecida por ele**.
  Fica em `images/collections/<id-da-coleção>.webp` e é registrada no bloco
  `image:` da coleção (`file`, `subject`, `supplied_by`, `added`). O agente
  nunca escolhe nem busca uma foto por conta própria.
- **Sem foto:** o fundo é um mosaico das capas das edições da própria coleção.
- **Sem foto e sem capas:** cartão liso, com o ícone.
- Nos dois fundos a imagem fica esmaecida sob um degradê azul-escuro forte; o
  texto precisa ficar sempre legível. O leque de capas só aparece no cartão liso.
- A foto é apresentação, não curadoria: não muda sequência, papel nem
  estrutura da coleção, e trocá-la não exige proposta estrutural.
- Guardar em WebP, no máximo ~1600 px de largura: a build embute a imagem no
  artefato, que tem limite de 16 MB.

## 6 · Só o que ele consulta — decisão do Mathews, 2026-09-25

A interface mostra o que ele usa para ler, escolher e comprar: obra, autor,
edição, capa, ordem da coleção e seus movimentos, o porquê de cada obra, o
quanto exige, relações entre obras, link de compra, o estado pessoal dele e as
decisões que esperam por ele. **Não mostra o processo interno**:

- origem e data de importação, ordem original da lista, desvios dessa ordem;
- quem escreveu cada texto ("— claude", "— você", "proposta");
- estado de pesquisa ("Parcial", "Não pesquisado"), lista do que falta
  pesquisar, campos verificados, veredito de edição, nível de fonte, base de
  correspondência do link, notas de proveniência;
- identificadores (`id`), campos curatoriais em código (tipo, período,
  tradições em slug), mudanças estruturais, avisos explicativos sobre o
  modelo de dados.

Tudo isso continua nos arquivos — é o registro — e na aba Revisão quando
exige decisão dele. Informação útil mas densa (mapa de escopo, critérios,
justificativa da ordem) aparece organizada e resumida, com o detalhe
recolhido.

**Ordem original.** A coleção como ela está — obras, ordem, movimentos — é o
registro principal. A ordem da lista de partida não é mostrada nem precisa
ser mantida como referência.

## 7 · Tela Decisões — formato aprovado pelo Mathews, 2026-09-25

Tudo o que espera resposta dele vive em `review/decisions.yaml` e aparece na
tela **Decisões** (antiga "Revisão e lacunas"), como cartões no mesmo formato:

- topo em uma linha: tipo (adicionar obra, escolher edição, confirmar posição,
  mudar uma coleção, onde colocar, mudar uma regra) · coleção, e a prioridade à
  direita. O tipo **mudar uma regra** foi acrescentado por decisão dele em
  2026-09-27: mudança de regra do projeto é decisão dele como qualquer outra e
  até ali não tinha lugar nesta tela — ficava só em prosa de revisão, que é
  exatamente o que esta seção existe para impedir;
- a **pergunta** em linguagem corrente e **por que importa**;
- as **opções**, cada uma com o que muda se for escolhida, a recomendada
  marcada e a razão dela; "agora não" é sempre uma saída possível;
- o detalhe recolhido: obras sugeridas em cartões comparáveis (resolve /
  complementa, o que traz, fatos curtos) e a composição da coleção.

Três estados: **para decidir**, **aguardando** (com o que precisa acontecer) e
**decididas** (com a escolha e a data, reversíveis).

Quando surge uma lacuna, proposta, conflito de edição ou posição a confirmar,
o agente registra o dado técnico onde sempre registrou **e** escreve o cartão
em `review/decisions.yaml`. Nenhuma decisão fica só em prosa de revisão.
Quando ele responde (o botão "Responder" copia a resposta para a conversa), o
agente aplica, marca o cartão como `decidida` com data e escolha, e atualiza o
registro de origem.

## 8 · O livro físico aparece inteiro — 2026-09-25

A página de uma edição mostra **todas** as obras do volume. As que estão em
alguma coleção têm link; as que não estão em nenhuma são listadas pelo campo
`also_contains` da publicação, com a marca "fora das coleções". Nunca guardar
esse conteúdo só em comentário do arquivo: comentário não chega à tela.

## 9 · Por que esta edição — 2026-10-10

Pedido do Mathews: o motivo da escolha de edição tem de aparecer na tela, curto
e objetivo.

- **Campo `why`** em cada item de `contains` da publicação: uma ou duas frases,
  escritas para o leitor (ele é "você"), dizendo o que faz desta edição a
  escolha — tradutor, tradução direta, aparato, ser o exemplar dele, ser a
  única. **Não cita outras edições**, salvo quando a escolha aceitou uma
  concessão (língua, importação, só usado) — aí diz a concessão, não a rival.
  Sem jargão interno: nada de ids de cartão, `verdict` ou "ver a seção".
- `reason` continua sendo o registro de trabalho, mais longo; `why` é o que a
  interface mostra.
- **Página da obra**, abaixo das edições: bloco "Por que esta edição". Sem
  `why`, o bloco diz "A escolha ainda não foi comparada com outras edições" e
  mostra os dados da tradução — nunca inventa um motivo. Logo abaixo, recolhida,
  "Outras edições consideradas": o campo `editions_considered` da obra, uma
  linha por edição (`edition` + `note`, por que não foi a escolhida).
- **O texto de pesquisa não vai para a tela** (revisão de 2026-10-10, pedido do
  Mathews): a seção `## Edições…` do corpo da obra e a `## Avaliação` da
  publicação são registro de trabalho — longas, com tabelas, nomes internos e
  ids de cartão. Tudo o que a tela mostra é escrito para o leitor: sem
  "Mathews", sem ids (`d-ed-…`, `pub--…`), sem nomes de campo.
- **Página da edição**: o mesmo `why`.
- **Cartões decididos**: a escolha e, recolhido, "Ver as opções e os motivos"
  com as edições ou opções, prós e contras e a recomendação. A nota interna da
  decisão (`decided.note`) e o contexto de antes da decisão (`why`) não
  aparecem.
- **Editora**: a tela mostra o nome de `config/publishers.yaml`, não o
  identificador do arquivo.
- **Celular** (até 600 px): capa e texto empilhados na página da edição e nas
  edições dos cartões; nenhuma tela pode rolar na horizontal.
- Ao escolher ou trocar uma edição, o agente escreve o `why` na mesma mudança.

## 10 · Sobre a obra — 2026-10-13

Pedido do Mathews, depois de ver na página de *A Arte da Guerra* uma nota de
revisão inteira (tabela de edições, "Portão 1", id de cartão) no painel "Sobre
a obra". A causa: a página juntava as seções Fatos, Avaliações acadêmicas e
Síntese, que são registro de pesquisa, e qualquer subtítulo (`###`) escrito
dentro delas vazava junto. A regra de §9 dizia que esse texto não ia para a
tela; o código não garantia.

- **A página da obra mostra só as seções `## Sobre a obra` e `## Como ler`**
  (esta desde 2026-10-14, §13) do corpo. Fatos,
  Avaliações acadêmicas, Síntese, Lugar na biblioteca, Edições, Revisões e
  notas de modelo continuam no arquivo como registro e nunca vão para a tela.
- **O texto é escrito para o leitor**: duas a quatro frases dizendo o que a
  obra é, do que trata e, quando estabelecido, como é vista. Quando ajuda,
  diz também como a obra se lê (de ponta a ponta, por consulta, aos poucos),
  pedido do Mathews de 2026-10-14. Sem "Mathews",
  sem "registro", "pesquisa", "lista", "veredito", "portão", sem ids, nomes de
  campo, parágrafos de regra ou datas de trabalho. Não fala de edições (isso é
  o `why` da publicação, §9). Nada inventado: o que não se sabe fica de fora.
- **Toda obra nova** entra com `## Sobre a obra` na mesma mudança. Sem ela o
  painel não aparece, e isso é um defeito, não um estado aceitável.
- Qualquer nível de título no corpo abre uma seção nova na interface, de modo
  que um subtítulo de nota interna não pode cair dentro da seção exibida.

## 11 · Como escrever o porquê de uma edição — 2026-10-13

Pedido do Mathews: os textos de §9 estavam curtos mas não explicavam. "Com
numeração de Bekker" supõe que ele saiba o que é isso; "anotada", "em
catálogo", "helenista", "direta" sem mais nada não dizem por que importa.

- **Curto, mas explicando.** Uma a três frases (cerca de 45 palavras) no
  `why`; uma frase (cerca de 25) em cada nota de `editions_considered`.
- **Dizer o que o leitor ganha**, não só listar o que a edição tem: quem
  traduziu e de que língua ("direto do grego, e não de outra tradução"); o
  que acompanha o texto e para que serve ("o grego ao lado, para conferir as
  palavras que importam"; "notas que explicam nomes e alusões"); por que o
  tradutor ou a edição merece confiança, quando há fonte; e a concessão, se
  houver (Portugal, importada, só usada, em inglês, parcial).
- **Nenhum termo técnico sem explicação na mesma frase.** Exemplos: numeração
  de Bekker → "a numeração padrão das obras de Aristóteles, que permite achar
  qualquer passagem citada em outros livros"; aparato → dizer qual (notas,
  introdução, índice); helenista → "especialista em grego antigo"; em
  catálogo → "à venda nova"; texto-base, recepção, língua de partida →
  reescrever em palavras simples.
- **Nada inventado e nada de "a melhor" sem comparação.** Se a edição nunca
  foi comparada com outras, o texto diz o que ela tem e, se for o caso, que
  ainda não foi comparada.
- As notas de `editions_considered` dizem, em palavras simples, por que
  aquela edição não foi a escolhida.
- **Cada texto se entende sozinho** (acréscimo de 2026-10-13, pedido do
  Mathews). Nada de "a mesma tradução", "como a escolhida", "desta edição" ou
  tradutor só pelo sobrenome: o leitor pode ler uma linha sem ter lido as
  outras. Nome completo do tradutor e, quando ajuda e há fonte, quem ele é
  ("tradutor brasileiro de muitos clássicos gregos").

## 12 · Posse não substitui a edição escolhida de uma alternativa — 2026-10-14

Pedido do Mathews, ao escolher para *As Nuvens* um volume que traz também
*Prometeu*, *Édipo Rei* e *Medeia*, peças que ele lê por outras edições.

- Uma edição que ele tem continua sendo a edição mostrada das obras que ela
  contém, **exceto** das obras em que o volume está marcado como
  `verdict: alternative`. Para essas, vale a escolha normal (preferência da
  coleção, edição recomendada).
- O volume continua aparecendo na página da obra como outra edição, e a
  página da edição continua mostrando o livro inteiro (§8).

## 13 · Como ler — 2026-10-14

Decisão do Mathews, a partir de *Como Ler Livros*, de Mortimer Adler: cada
tipo de texto pede uma postura diferente, e cada obra tem uma pergunta própria
que deve guiar a leitura. A página da obra ganha uma seção `## Como ler`, logo
depois de "Sobre a obra".

- **Específica da obra, nunca genérica.** "Leia com atenção aos argumentos"
  serve para qualquer livro e por isso não serve para nenhum. O texto diz o
  que só vale para esta obra.
- **Três itens, nesta ordem, cada um com o rótulo em negrito:**
  - **A pergunta:** a pergunta central que a obra responde, e que deve guiar
    a leitura;
  - **Onde está o centro:** as partes que importam mais e, quando a obra é
    grande, o que dá para ler em parte ou pular sem perder o argumento;
  - **Postura:** como ler (argumento a avaliar, narrativa a viver,
    manual a aplicar, consulta), o que costuma confundir e, quando houver,
    o que ler antes e por quê.
- **Curta:** cerca de 80 a 120 palavras no total. Mesmas proibições de §10:
  sem termos internos, sem ids, sem edições. Termo técnico só com explicação
  na mesma frase (§11). Autor sempre com nome completo e a obra citada pelo
  título.
- **Nada inventado.** A pergunta central e as partes centrais são afirmações
  sobre a obra e saem da pesquisa ou de conhecimento estabelecido sobre ela.
  Sem base, a seção não é escrita.
- **Opcional, ao contrário de "Sobre a obra".** Sem a seção, a página
  simplesmente não a mostra; a falta não é defeito. Entra aos poucos, a
  começar pelas obras de nível A da pirâmide (`curation-rules.md` §2.9).
- **As relações continuam na lista de relações.** "Como ler" pode citar a
  relação principal ("leia depois de…"); o resto fica na lista, que é
  clicável e mostra a relação inversa na outra obra.

Piloto: *A República* de Platão, *Política* de Aristóteles e *Leviatã* de
Thomas Hobbes.
