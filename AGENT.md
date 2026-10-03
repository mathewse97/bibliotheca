# AGENT.md — contrato de leitura da Bibliotheca

Este arquivo é **navegação e operação**, não regra substantiva. Ele diz onde
as coisas estão e o que ler; **não** diz como curar, como pesquisar, nem como
escolher uma edição. Essas regras são canônicas nos arquivos citados abaixo e
não são repetidas aqui. Quando este arquivo e um arquivo canônico
discordarem, o arquivo canônico é o fato.

Válido para qualquer agente, não só o Claude.

---

## 1 · Regra dura: `_generated/` nunca é lido

`_generated/` é **saída da build para a interface**. Contém `index.json`,
`bibliotheca.html` e `artifact.html`.

**Um agente nunca lê nenhum arquivo de `_generated/`.** Não para se orientar,
não para consultar, não parcialmente. `index.json` tem ~250 KB e é maior do
que toda a biblioteca canônica somada; lê-lo custa mais do que ler o
repositório inteiro, e tudo o que ele contém é derivado de arquivos que são
individualmente mais baratos de consultar.

Isto não é uma preferência de desempenho. Um agente que se orienta pelo
derivado passa a raciocinar sobre uma cópia que pode estar atrasada em
relação ao canônico. **O canônico é a fonte; o derivado é a tela.**

A build continua a produzir os três arquivos exatamente como antes. Nada em
`_generated/` muda de nome, de tamanho ou de papel. Ver `_generated/README.md`.

---

## 2 · O que é canônico

| pasta | o que guarda | quem escreve |
|---|---|---|
| `works/` | obras — a unidade intelectual | agente |
| `publications/` | edições físicas — editora, tradutor, ISBN | agente |
| `collections/` | coleções, sequência, participações, movimentos, caminhos | agente |
| `people/` | autores | agente |
| `review/`, `review/gaps/`, `review/structural/` | revisão curatorial, lacunas, propostas estruturais | agente |
| `config/` | regras, vocabulários, forma dos registros | agente |
| `state/personal.yaml` | leitura, posse, prioridade sua | **só a interface** |
| `sources/` | documentos de projeto arquivados | agente |
| `covers/` | capas | agente |
| `tools/` | `build.py` (constrói), `check.py` (portão de integridade), `pages.py` (monta o site), `scaffold.py`, o template da interface e as fontes | agente |

**Nenhum arquivo é escrito pelos dois.** `state/personal.yaml` é o único
arquivo que a interface escreve, e o agente não escreve nele. A lista branca
de campos editáveis pela interface está em `config/writable-fields.yaml`.

A Bibliotheca é um sistema de curadoria bibliográfica e intelectual **sobre**
livros. Não é um repositório de livros, PDFs, digitalizações ou textos
integrais. Uma fonte externa consultada durante a pesquisa deixa no
repositório apenas uma entrada em `provenance` — nunca o seu conteúdo.

---

## 3 · Padrão de trabalho: espelhar uma vez, consultar localmente, ler pouco

Transferir arquivos custa tempo; **colocá-los no contexto custa tokens**. São
custos diferentes. O repositório canônico inteiro cabe numa única
transferência. O padrão eficiente é:

1. espelhar o repositório de uma vez (sem `_generated/`);
2. localizar com `grep`/`awk` — de graça;
3. ler no contexto **só** o trecho localizado.

Ler um arquivo inteiro só porque ele foi transferido é o erro que este
contrato existe para evitar.

### 3.1 · Antes de começar: obter o repositório — revisto em 2026-10-02

A Bibliotheca mora num repositório Git. Isso tornou obsoleta a regra anterior
desta seção, que mandava o agente conferir se conseguia rodar comandos dentro
da pasta do Google Drive do Mathews e, não conseguindo, avisar antes de copiar
a biblioteca inteira. A regra existia porque copiar ~300 arquivos era caro e
tinha sido feito uma vez sem avisar. O problema desapareceu com a causa: hoje
o repositório inteiro vem numa operação só, barata e padrão.

```bash
git clone <url-do-repositorio>    # primeira vez
git pull                          # nas seguintes
```

O que a regra antiga protegia continua valendo, e é o parágrafo acima desta
subseção: **transferir é barato, colocar no contexto é caro.** Clonar o
repositório não autoriza ler o repositório. Localize com `grep`, leia só o
trecho localizado.

Duas coisas que não mudaram:

- **`_generated/` não se clona nem se lê.** Está no `.gitignore`; não vem no
  clone, e é assim que deve ser. Para ter a interface, construa.
- **Trabalhe num branch e abra um pull request.** O portão
  (`tools/check.py`) roda ali e é o que impede que uma referência quebrada ou
  uma mudança estrutural sem decisão registrada entre no `main`.

## 4 · Qual arquivo responde a qual pergunta

| pergunta | onde | como |
|---|---|---|
| em que coleções está a obra X, com que papel e posição | `collections/*.md` | `grep -n "X" collections/*.md`, depois extrair só a entrada |
| o mapa completo de participações | `collections/*.md` | `grep -Hn '  - work: ' collections/*.md` |
| tudo sobre uma obra | `works/<id>.md` | ler o arquivo — ~1 KB |
| editora, tradutor, ISBN, veredito de edição | `publications/<id>.md` | ler o arquivo |
| estado de pesquisa de todas as obras | `works/*.md` | `grep -h '^research_status:' works/*.md \| sort \| uniq -c` |
| lacunas de uma coleção | `review/gaps/<coleção>.yaml` | ler o arquivo |
| propostas estruturais em aberto | `review/structural/*.yaml` | ler o arquivo. CORRIGIDO em 2026-10-02: esta linha apontava para `config/structural-proposals.yaml`, que é o ESQUEMA e não contém proposta nenhuma |
| valores válidos de um campo | `config/vocabularies.yaml` | extrair a chave |
| leitura, posse, prioridade pessoal | `state/personal.yaml` | ler — nunca escrever |
| mecânica: pastas, build, interface, gravação | `README.md` | por seção |

---

## 5 · Onde estão as regras substantivas

Não estão aqui. Carregue **a seção**, não o arquivo — cada um dos dois
arquivos abaixo abre com um índice de recuperação que diz qual seção
responde a quê e como extraí-la.

| assunto | arquivo | seção |
|---|---|---|
| identificadores | `config/bibliographic-rules.md` | §C |
| hierarquia de fontes, pesquisa de edição | `config/bibliographic-rules.md` | §E |
| seleção de edição, preferência de idioma | `config/bibliographic-rules.md` | §F |
| postura, hipóteses, incerteza visível | `config/curation-rules.md` | §0 |
| distinções do modelo | `config/curation-rules.md` | §1 |
| escopo, cobertura, as quatro operações | `config/curation-rules.md` | §2 |
| preservação da estrutura original | `config/curation-rules.md` | §3 |
| escalonamento, aprovação, reversibilidade | `config/curation-rules.md` | §4, §5 |
| **fluxo ao entrar uma obra nova** | `config/curation-rules.md` | §6 |
| o que um agente nunca faz | `config/curation-rules.md` | §7 |
| **o que chega à tela dele** | `config/interface-rules.md` | inteiro — são 4 seções curtas |
| critério de pronto: renderizar e olhar | `config/interface-rules.md` | §3 |

Precedência, nos dois arquivos: uma instrução direta do Mathews vence o
documento; o documento vence o julgamento do agente; um arquivo canônico que
discorde do documento é o fato, e a divergência é **relatada**, nunca
resolvida em silêncio.

---

## 6 · Reconstruir

```bash
python3 tools/build.py
```

Somente leitura sobre o canônico; escreve apenas dentro de `_generated/`.
Detalhes em `README.md` §3. Rodar a build não é ler `_generated/`.

---

## 7 · Fechar o trabalho

```bash
python3 tools/build.py        # reconstrói
python3 tools/check.py        # aprova ou reprova — saída 1 significa não entra
git add -A && git commit -m "..."
git push
```

O portão reprova por referência quebrada, arquivo canônico ilegível, cartão de
decisão malformado e mudança estrutural aplicada sem decisão registrada.
Lacuna `stale` e proposta aberta **não** reprovam: são pedidos de julgamento
humano, e transformá-los em erro de build ensinaria a apagá-los.

O critério de pronto continua sendo o de `config/interface-rules.md` §3 —
renderizar e olhar a tela. O portão confere estrutura, não se a tela ficou
legível.

E uma obrigação que não é mecânica: **manter verdadeira a tabela do §0 do
README.** Material canônico novo ganha uma linha antes do fim da sessão em que
nasceu. É o único lugar que diz a quem chegar depois o que levar e o que
descartar.

---

*Este arquivo é um contrato de leitura. Se ele começar a conter critério
curatorial ou regra bibliográfica, está errado: essa regra pertence a
`config/`.*
