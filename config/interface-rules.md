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
