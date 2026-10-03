# Bibliotheca

Uma biblioteca intelectual pessoal. Arquivos de texto simples são a
biblioteca; tudo o mais — o índice, a interface, Claude — é um serviço a
esses arquivos e pode ser substituído sem os perder.

Estado em 2026-09-06: **53 obras · 3 coleções · 1 publicação · 46 autores**.
Estágio de bootstrap — nenhuma obra teve pesquisa de edição, e a interface
diz isso em vez de o esconder. *(Estes números envelhecem; a contagem viva é a
que `tools/build.py` imprime.)*

---

## 0. Manifesto — o que é fonte, o que é derivado, como sai daqui

Esta tabela é o contrato de portabilidade da biblioteca. Quem chegar sem
contexto nenhum — outra pessoa, outro agente, você daqui a dois anos — lê isto
primeiro e sabe o que precisa levar e o que pode jogar fora e reconstruir.

**Entregar a biblioteca inteira a outro agente é um comando:**

```bash
git clone https://github.com/<usuario>/<repositorio>.git
```

Nada do que importa fica de fora disso, e nada do que fica de fora importa.

| material | o que guarda | fonte ou derivado | como sai daqui | vai na entrega |
|---|---|---|---|---|
| `collections/` | coleções: pergunta, critérios, mapa de escopo, sequência, movimentos, tensões, ordem original e desvios | fonte | clone ou download | sim |
| `works/` | obras — a unidade intelectual | fonte | clone ou download | sim |
| `publications/` | edições físicas: editora, tradutor, ISBN, aparato, aquisição | fonte | clone ou download | sim |
| `covers/` | capas das publicações, uma por arquivo | fonte | clone ou download | sim |
| `images/` | imagens de fundo dos cartões de coleção | fonte | clone ou download | sim |
| `people/authors.yaml` | autores, tradutores, organizadores | fonte | clone ou download | sim |
| `review/`, `review/gaps/`, `review/structural/` | prosa curatorial, lacunas com evidência verificável, propostas estruturais | fonte | clone ou download | sim |
| `config/` | as regras: curadoria, bibliografia, interface, pesquisa, vocabulários, esquemas | fonte | clone ou download | sim |
| `sources/` | proveniência congelada: o blueprint fundador e as listas originais | fonte | clone ou download | sim |
| `state/personal.yaml` | leitura, posse, prioridade pessoal | fonte — e o único arquivo que a interface escreve | clone ou download | sim |
| `tools/` | `build.py`, `check.py`, `pages.py`, `ui.template.html` | fonte | clone ou download | sim |
| `README.md`, `AGENT.md`, `STATE.md` | mecânica, contrato de leitura, estado operacional | fonte | clone ou download | sim |
| `.github/workflows/build.yml` | quando construir, conferir e publicar | fonte — mas só tem efeito dentro do GitHub (§12) | clone ou download | sim |
| `_generated/` | `index.json`, `bibliotheca.html`, `artifact.html` | **derivado** | não sai — reconstrua com `python3 tools/build.py` | não |
| `site/` | a pasta que o Pages serve | **derivado** | não sai — remonte com `python3 tools/pages.py` | não |
| `Claude outputs/` | variante de interface nunca declarada canônica | **não canônico** | fica no disco, fora do repositório — ver §12 | não |
| o site publicado, o artifact no Claude | retratos da biblioteca num instante | **derivado** | não sai — republique a partir da fonte | não |

**Derivado nunca se edita à mão, e nunca é consultado como se fosse fato.** Um
agente que se orienta por `index.json` está raciocinando sobre uma cópia que
pode estar atrasada. A única exceção, declarada e estreita, é `tools/check.py`,
que lê o índice imediatamente depois de gerá-lo, para conferir — e diz isso de
si mesmo no cabeçalho.

**Manter esta tabela verdadeira faz parte do trabalho.** Material canônico novo
ganha uma linha aqui antes do fim da sessão em que nasceu; material que deixou
de ser canônico sai. Uma tabela desatualizada é pior do que nenhuma, porque
alguém vai confiar nela.

---

## 1. Estrutura canônica

```
collections/    uma coleção por arquivo: pergunta, critérios de inclusão,
                scope_map, sequência com movimentos, caminhos, tensões,
                ordem original e desvios
works/          uma obra por arquivo. Obra = unidade intelectual (livro,
                ensaio, conferência, diálogo, tratado) — não necessariamente
                um livro
covers/         imagens de capa das PUBLICAÇÕES, uma por arquivo, nomeadas
                pelo id da publicação. Vazio hoje
publications/   uma publicação física por arquivo. PODE CONTER VÁRIAS OBRAS,
                por isso não vive dentro de nenhuma delas. O veredito de
                recomendação está no par obra–publicação, não na publicação
people/         authors.yaml — normalização de nomes
review/         a prosa curatorial (uma por coleção)
review/gaps/    as mesmas lacunas em forma estruturada: necessidade, contexto,
                estado, candidatos (opcionais) e evidência verificável
review/structural/  propostas de mudança no NÍVEL DA COLEÇÃO — refine, rename,
                split, merge. Vazio hoje, só com o _TEMPLATE.yaml
config/         writable-fields.yaml — a lista branca de escrita
                curation-rules.md — como um agente deve raciocinar sobre esta
                biblioteca e modificá-la, e o §I (lacunas e recomendações).
                Regra, não dado: a build não o lê
                bibliographic-rules.md — §C identificadores, §E hierarquia de
                fontes e pesquisa de edição, §F hierarquia de idiomas. Regra,
                não dado
                vocabularies.yaml — os valores que os campos admitem, com a
                proveniência de cada lista. Não validado pela build
                gap-records.yaml — forma dos registros de lacuna e catálogo
                dos predicados de `check`
                structural-proposals.yaml — esquema das propostas estruturais,
                seus tipos, estados e portão de aprovação
                acquisition.yaml — vendedores, base de correspondência de
                anúncio, frescor e regras de capa
state/          personal.yaml — o SEU estado. O único arquivo que a
                interface escreve
tools/          scaffold.py, build.py, ui.template.html
_generated/     saída da build. Descartável. Nunca editar à mão
```

`sources/` guarda proveniência congelada, e **existe parcialmente**: contém o
blueprint original arquivado (`blueprint-2026-09-05.md`), fonte histórica de
precedência 4, não regra. As cópias congeladas das suas listas originais, para
as quais os arquivos de coleção apontam em `source.archived_at`, ainda não
foram arquivadas. A build ignora a ausência; o campo é proveniência, não uma
dependência.

**As seções `§C`, `§E`, `§F` e `§I`.** Os registros de obra, o modelo de
publicação, as revisões e os arquivos de configuração citam estas quatro
seções. Elas viviam fora do repositório e agora vivem dentro: §C, §E e §F em
`config/bibliographic-rules.md`, §I em `config/curation-rules.md`. O índice
está em `curation-rules.md` §9, e a história das duas rodadas de recuperação em
§9.1. Uma única coisa continua sem se recuperar, e está declarada como tal em
vez de reconstruída: quais são as 4 obras a que a emenda de identificadores se
aplica.

Regras que a estrutura carrega e que convém não quebrar:

- **uma obra = um registro.** Uma obra em três coleções continua sendo um
  arquivo. Quem repete é a participação, não o registro.
- **participação (`sequence` da coleção) carrega atributos** — posição,
  papel, exigência, prerequisitos locais, `why_here`. É por isso que
  pertencer a uma coleção não é uma etiqueta.
- **a ordem no arquivo É a ordem.** Não há campo de posição. Inserir uma
  obra é mover uma linha.
- **`why_here_by`** diz de quem é o raciocínio: `voce` ou `claude`.
- **cobertura e intenção são dimensões separadas.** No `scope_map` de uma
  coleção, `coverage` (covered/thin/absent) é um fato sobre o que a coleção
  contém; `pursuit` (open/not-pursued) é uma decisão sua sobre o que está
  sendo perseguido. Uma coleção pode ser deliberadamente parcial, e uma
  região vazia nunca é uma obra em falta. Descrições de região dizem que
  perguntas caem ali — nomes de obras candidatas ficam em `review/gaps/`.
- **uma lacuna pode não ter candidatos.** `candidates: []` é detecção pura:
  o problema estrutural está registrado e nenhuma obra foi proposta.
  Detecção e revalidação são automáticas; propor obras não é.
- **capa e fonte de compra são da publicação, não da obra.** Uma obra não tem
  capa nem preço. Vendedor é fonte de nível 6–7: estabelece que o livro existe
  e pode ser comprado, e nada mais — não toca veredito nem prioridade. Um link
  só é apresentado como opção de compra desta edição quando `match_basis`
  registra **como** se sabe que o anúncio é dela. Ausência de anúncio ou de
  capa nunca é defeito. Ver `config/acquisition.yaml`.

## 2. O que é `_generated/`

Saída da build, inteiramente reconstruível. Contém:

| arquivo | o que é |
|---|---|
| `index.json` | o índice completo, com tudo o que é derivado: participações por obra, relações inversas, publicações por obra, obras por autor, integridade referencial |
| `bibliotheca.html` | **a interface local.** Arquivo único, dados embutidos |
| `artifact.html` | a mesma interface no formato da versão hospedada |

Nada em `_generated/` deve ser editado à mão: a próxima build sobrescreve.

## 3. Reconstruir

```bash
python3 tools/build.py          # a partir da raiz do repositório
```

Requer Python 3, PyYAML e Pillow, nas versões de `requirements.txt`
(`pip install -r requirements.txt`). Sem o Pillow a build ainda roda, mas embute as
capas em tamanho original, e a interface muda de bytes.

A build é **somente leitura** sobre `collections/`, `works/`,
`publications/`, `people/`, `config/`, `review/` e `state/`. Ela lê tudo e
escreve exclusivamente dentro de `_generated/`. Rodá-la nunca altera a
biblioteca nem o seu estado pessoal.

Não há nenhuma lista de coleções no código. Uma coleção nova aparece na
interface por existir em `collections/` — e o mesmo vale para obras,
publicações, autores e lacunas.

Se a build encontrar uma referência quebrada (uma coleção apontando para uma
obra inexistente, uma relação sem alvo), ela **não falha**: registra em
`index.json` e a interface mostra em *Revisão → Integridade referencial*.

### Revalidação das conclusões

Toda build reexecuta a evidência das lacunas. Cada afirmação estrutural em
`review/gaps/*.yaml` guarda a prosa original em `claim` e um `check` — um
predicado sobre a biblioteca (quantos membros de um certo tipo, o estado de
uma região, se existe uma relação entre duas obras). A build roda todos os
checks contra o estado atual e marca a lacuna:

| resultado | significa |
|---|---|
| `current` | toda a evidência verificável ainda confere |
| `stale` | a biblioteca mudou e parte da evidência deixou de valer |
| `unverifiable` | nenhuma evidência é verificável por máquina |

O terminal imprime as lacunas `stale` com o esperado e o atual, e a interface
mostra o mesmo em *Revisão*, com a prosa preservada ao lado — para que se veja
o que era afirmado e o que mudou.

`check: null` com `checkable: false` é uma admissão deliberada: a afirmação
depende de julgamento e não pode ser revalidada por máquina. Fingir um
predicado ali seria pior do que assumir o limite.

Isto **não escreve nada** nos arquivos canônicos: o resultado da revalidação
vive só em `_generated/index.json`.

## 4. Abrir a interface local

Abra `_generated/bibliotheca.html` no Edge ou no Chrome. Duplo clique basta.

Sem servidor, sem instalação, sem internet — as fontes vêm da web e, se não
carregarem, o texto usa as fontes do sistema. Os dados estão embutidos no
arquivo, então ele funciona mesmo copiado sozinho para outra pasta (mas veja
§6: para gravar, precisa da pasta do repositório).

## 5. Editar o estado pessoal

Os campos editáveis vêm de `config/writable-fields.yaml`. A interface lê
esse arquivo e desenha os controles a partir dele — não há lista de campos
no código, e acrescentar um campo editável é acrescentar linhas ao YAML.

Hoje são:

| onde | campos | por quê ali |
|---|---|---|
| página da **obra** | leitura, início, conclusão, prioridade sua, nota no Obsidian | você lê uma obra, não um volume |
| página da **publicação** | posse, adquirido em, onde | você compra um objeto físico, e ele pode conter várias obras |

`priority_personal` (sua) é distinta de `priority_library` (curatorial). A
interface escreve a primeira e nunca a segunda.

O campo da nota do Obsidian guarda **apenas um caminho**. A interface nunca
lê nem escreve o conteúdo das suas notas.

## 6. Onde as alterações são gravadas

Em `state/personal.yaml`, e em mais lugar nenhum.

Uma alteração entra primeiro em memória. O indicador no topo mostra sempre
um de dois estados, sem ambiguidade:

- **`● N por gravar`** — há alterações que ainda não estão em disco
- **`✓ sem alterações`** / **`✓ gravado HH:MM`** — o que está na tela está
  em disco

Em **Estado pessoal** há três caminhos, e a interface usa o melhor
disponível:

1. **Pasta conectada** — escolhe a raiz do repositório uma vez por sessão e
   a partir daí grava direto em `state/personal.yaml`, sem diálogo e sem
   risco de gravar no lugar errado. A interface confere se a pasta é mesmo
   a raiz (procura `collections/` e `state/`) antes de aceitar.
2. **Salvar como** — reserva, se o primeiro não existir. Diálogo comum;
   você navega até `state/`.
3. **Copiar YAML** — sempre disponível. Único caminho na versão hospedada.

O contador **só volta a zero depois de uma gravação bem-sucedida**. Um
diálogo cancelado ou um erro deixam o indicador vermelho, porque nada foi
para o disco.

Nada é guardado no navegador: sem `localStorage`, sem `IndexedDB`, sem cópia
paralela da biblioteca. A permissão da pasta dura enquanto a aba estiver
aberta.

## 7. Versão hospedada × versão local

| | hospedada (artifact) | local (`_generated/bibliotheca.html`) |
|---|---|---|
| navegar, buscar, comparar | sim | sim |
| ver lacunas e revisão | sim | sim |
| editar estado pessoal | sim, na tela | sim |
| **gravar em disco** | **não** — uma página na web não alcança o seu PC | **sim** |
| onde usar | consultar de qualquer lugar, inclusive numa livraria | trabalhar de verdade |

Se editar algo na versão hospedada, copie o YAML e traga-o para o arquivo
local — ou peça a Claude que o aplique.

Desde 2026-10-02 há uma **terceira** superfície, com o mesmo estatuto de
retrato que o artifact: o site publicado no GitHub Pages. Ver §11.

A versão hospedada é um **retrato**: reflete a biblioteca no momento em que
foi publicada. Depois de novas importações, é republicada.

### 7.1 O artifact publicado — identidade e fluxo

O artifact chama-se **Bibliotheca** e vive em:

```
https://claude.ai/code/artifact/7590455a-7972-409c-a8ca-0fc8b88649dc
```

**Este endereço é o identificador do artifact, e é a razão de estar escrito
aqui.** Republicar de uma sessão futura exige-o: sem ele, uma nova publicação
cria um artifact *separado* em vez de atualizar este. Guardado só numa conversa,
ele perde-se — que é exatamente a falha que as seções §C–§F já custaram a
corrigir.

O que é publicado é **`_generated/artifact.html`**, e não `bibliotheca.html`.
Os dois saem da mesma build e dos mesmos dados; `artifact.html` é o mesmo
arquivo sem o invólucro `<!doctype>/<html>/<head>/<body>`, que é o formato que
a plataforma exige. Nenhum dos dois é fonte: ambos são saída.

O fluxo, e nada mais curto funciona:

```
G:\Meu Drive\Biblioteca   (fonte da verdade)
        ↓  python3 tools/build.py
_generated/artifact.html  (saída canônica)
        ↓  publicação explícita, pedida a Claude
artifact «Bibliotheca»    (retrato hospedado, somente leitura)
```

**A publicação NÃO é automática.** Nada observa o disco: reconstruir não
republica, e editar o estado pessoal na versão hospedada não escreve em
`state/personal.yaml`. Depois de qualquer mudança que deva aparecer no
telemóvel, peça a republicação — é um passo, e é deliberado.

**O artifact nunca é fonte.** É somente leitura por construção: os dois
caminhos de gravação (`showDirectoryPicker`, `showSaveFilePicker`) não existem
no navegador hospedado, e a interface degrada sozinha para *Copiar YAML*, como
o §6 já descrevia. Não há `localStorage`, não há segunda base de dados, e uma
alteração feita lá só entra na biblioteca quando o YAML copiado for aplicado a
`state/personal.yaml`.

### 7.2 Regra de conclusão — decisão do Mathews, 2026-09-06

> Sempre que uma operação modificar arquivos que possam afetar a interface, o
> fluxo de conclusão **tem de incluir** o rebuild de
> `_generated/bibliotheca.html` e `_generated/artifact.html` e a republicação do
> artifact **Bibliotheca** — salvo quando se **verificar** que a alteração não
> tem qualquer efeito sobre a interface.

A isenção é uma verificação, não um palpite. O teste é mecânico e barato:
reconstruir e **comparar byte a byte** os três arquivos de `_generated/` com as
versões anteriores. Idênticos ⇒ a alteração não toca a interface e a
republicação é dispensada; diferentes ⇒ reconstruir, gravar e republicar. A
build é determinística — do mesmo estado canônico sai sempre o mesmo byte — e é
isso que torna a comparação uma prova em vez de uma impressão.

**O que a build lê, e portanto pode afetar a interface:**

```
works/*.md · collections/*.md · publications/*.md   (exceto _TEMPLATE)
people/authors.yaml
config/writable-fields.yaml · config/structural-proposals.yaml
config/acquisition.yaml
state/personal.yaml
review/*.md · review/gaps/*.yaml · review/structural/*.yaml  (exceto _*)
covers/*                       (embutidas na interface)
tools/build.py · tools/ui.template.html   (geram a interface)
```

**O que a build NÃO lê, e por isso nunca exige republicação:**

```
README.md
config/curation-rules.md · config/bibliographic-rules.md
config/vocabularies.yaml · config/gap-records.yaml
sources/*
qualquer arquivo com prefixo _ nas pastas varridas
```

A assimetria não é arbitrária: `config/` guarda duas coisas diferentes. Os três
arquivos que a build lê são **dados de configuração**; os quatro que ela ignora
são **regra**, e regra muda como um agente raciocina, não o que a interface
mostra. `curation-rules.md` diz isso de si mesmo na última linha.

Ordem segura, quando a republicação é devida: gravar o estado pessoal pendente
(§8) → `python3 tools/build.py` → gravar os três arquivos de `_generated/` →
republicar o artifact pelo URL do §7.1 → recarregar a aba local.

## 8. Antes de reconstruir ou fechar o navegador

**Grave.** As alterações pendentes vivem só na aba. A build lê
`state/personal.yaml` do disco — não tem como saber o que está pendente numa
aba aberta.

Ordem segura:

1. gravar (indicador em `✓`)
2. `python3 tools/build.py`
3. recarregar a aba (`F5`)

O que está gravado sobrevive a qualquer número de reconstruções: a build
relê `state/personal.yaml` e reembute o conteúdo. Ao sair com alterações
pendentes, o navegador avisa.

## 9. Requisitos e limitações do navegador

- **Gravar em disco exige Chrome ou Edge no computador**, com a página
  aberta como arquivo local. A File System Access API está disponível em
  `file://` (`showDirectoryPicker` e `showSaveFilePicker` existem, e `file://`
  conta como contexto seguro).
- **Firefox e Safari não suportam** a API. Neles a interface funciona
  inteira para leitura, e a gravação passa por *Copiar YAML*.
- **Na versão hospedada**, a gravação em disco não existe por desenho. O
  botão de copiar pode ser bloqueado pelo sandbox; nesse caso o YAML fica
  selecionado para copiar à mão.
- **A permissão da pasta não persiste** entre sessões — é uma escolha, não
  uma limitação: guardá-la exigiria armazenamento no navegador, e a
  arquitetura recusa qualquer segunda cópia de estado.
- **Um diálogo cancelado não é um erro.** O indicador continua vermelho,
  que é o comportamento correto: nada foi gravado.

## 10. Fluxo com Claude

Claude escreve `collections/`, `works/`, `publications/`, `review/` e
`review/gaps/` — o lado bibliográfico e curatorial. Você escreve
`state/personal.yaml` pela interface. **Nenhum arquivo é escrito pelos
dois**, e é isso que torna o conjunto seguro sem nenhuma trava.

Quando Claude alterar algo, reconstrua e recarregue. Quando você quiser
mudar edição recomendada, papel, posição, classificação ou fechar uma
lacuna, peça — isso passa pelo fluxo de pesquisa e curadoria, não pela
interface.

---

## 11. O repositório e o site

A biblioteca passou a morar num repositório Git em 2026-10-02. O que mudou e o
que não mudou:

**Não mudou nada da biblioteca.** Mesmos arquivos, mesmas pastas, mesmas
regras, mesma build. Git é um registro por cima dos arquivos, não um formato
novo para eles.

**Mudou o registro de quem alterou o quê.** Metade do esquema deste projeto
existe porque o disco não guarda história: `order_changes` com `reversible_by`,
`lineage`, `structural_changes`, o portão que detecta mudança estrutural
aplicada em silêncio. Nada disso deixa de valer — continua sendo registro
**intelectual**, que é outra coisa de registro técnico: `git log` diz que uma
linha mudou, não *por que a obra se moveu de movimento*. O que o Git acrescenta
por baixo é autoria, data e um desfazer que funciona.

### 11.1 O ciclo de trabalho

```bash
git pull                      # antes de qualquer coisa
# ... alterações nos arquivos canônicos ...
python3 tools/build.py        # reconstrói o índice e a interface
python3 tools/check.py        # aprova ou reprova
git add -A && git commit -m "o que mudou, e por quê"
git push
```

A build e o portão rodam de novo no GitHub a cada push. Rodá-los antes é o que
evita descobrir um problema depois de publicado.

### 11.2 O site

```
https://<usuario>.github.io/<repositorio>/
```

É `_generated/bibliotheca.html` servido como `index.html`, reconstruído e
republicado automaticamente a cada push no `main`. Um retrato, como o artifact:
reflete a biblioteca no momento do último push.

**O site não grava.** Pelos mesmos motivos do §7.1 — uma página na web não
alcança o seu disco. A gravação de `state/personal.yaml` continua a exigir a
versão local em Chrome ou Edge. Na web, o caminho é *Copiar YAML*.

**O site é público.** O GitHub só oferece controle de acesso a sites do Pages no
plano Enterprise Cloud; em qualquer outro, publicar é publicar para a internet,
e a visibilidade do repositório não altera isso. O repositório é público por
decisão sua de 2026-10-02, tomada sabendo disso. `tools/pages.py` escreve um
`robots.txt` que pede aos buscadores que não indexem — é uma convenção
respeitada pelos buscadores sérios, não uma trava.

**O que isso significa para as capas.** As 118 capas de editora são embutidas na
interface e, portanto, servidas no site. Elas estão ali como identificação
bibliográfica de um acervo pessoal, que é o uso corrente em catálogos e
bibliotecas, e nenhuma é redistribuída como arquivo avulso. Os registros de
publicação que diziam "acervo pessoal privado" foram corrigidos para não
afirmarem uma coisa que deixou de ser verdade.

### 11.3 O portão

`tools/check.py` reprova quando há referência quebrada, arquivo canônico
ilegível, cartão de decisão malformado ou mudança estrutural aplicada sem
decisão registrada. Com a proteção de branch ligada, um pull request nessas
condições não entra no `main`.

Lacuna `stale` e proposta estrutural aberta **não** reprovam, e isso é
deliberado: são sinais pedindo julgamento humano, e tratá-los como erro de build
ensinaria a apagar o sinal para o verde voltar.

---

## 12. Limitações declaradas

Escritas aqui para não serem descobertas no pior momento.

**O que morre se o projeto sair do GitHub.** O agendamento e a publicação
automática — mais nada. `tools/build.py`, `tools/check.py` e `tools/pages.py`
não sabem que o GitHub existe e continuam a funcionar em qualquer máquina com
Python 3 e as dependências de `requirements.txt`. Depois de uma mudança de casa, a interface volta a ser
construída à mão com os três comandos e servida de onde você quiser; o
`.github/workflows/build.yml` fica inerte e pode ser apagado ou traduzido para o
agendador da nova casa.

**A interface não escreve no repositório.** Uma página estática não tem como
fazer um commit. `state/personal.yaml` é gravado em disco pela versão local e
entra no repositório por um commit seu. Na prática isso significa que o seu
estado pessoal de leitura e posse só chega ao repositório quando você o levar.

**O manifesto do §0 não é verificado por máquina.** Nenhum script confere se a
tabela descreve a realidade. Material canônico novo que não ganhe uma linha ali
fica invisível para quem chegar depois, e nada avisa.

**A build não falha sozinha.** `build.py` imprime os problemas e segue adiante,
de propósito. Quem reprova é `check.py`, e ele só roda se alguém o chamar — no
GitHub isso está garantido pelo workflow; fora dele, é disciplina.

**`sources/` continua parcial.** O blueprint fundador está arquivado; as cópias
congeladas de parte das listas originais, para as quais os arquivos de coleção
apontam em `source.archived_at`, não. É proveniência em falta, não dependência
quebrada: a build ignora a ausência.

**Uma pasta ficou fora.** `Claude outputs/` — uma variante de interface, com
template, duas fontes e um HTML construído — nunca foi declarada canônica em
lugar nenhum e está no `.gitignore` à espera de decisão. Ela continua no disco;
não foi apagada. Se a variante é para manter, o lugar dela é `tools/`.
