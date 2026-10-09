# Procedimento de pesquisa de edição — passo a passo operacional

Este arquivo é **operação**, não regra. Ele transforma o §E e o §F de
`config/bibliographic-rules.md` numa rotina executável, em lotes pequenos,
usando o navegador interno do Claude. Quando este arquivo e as regras
discordarem, **as regras vencem** e a divergência é relatada.

Válido para qualquer agente. Criado em 2026-09-17.

---

## 0 · Princípios que não mudam em nenhum passo

1. **Amazon é tier 7.** Serve para: achar ISBN/ASIN, ver que a edição existe,
   disponibilidade, faixa de preço. **Não serve** para confirmar dado
   bibliográfico nem qualidade. Nada vindo dela toca `verdict`.
2. **Campo não verificado fica `null`.** Nunca preencher por dedução.
3. **Toda afirmação ganha `provenance`** com fonte, tier, data e confiança.
4. **Posse não é escrita pelo agente.** `ownership` vive em
   `state/personal.yaml`, que só a interface escreve. Se os pedidos da Amazon
   mostrarem que você comprou algo, o agente **informa** e você marca na
   interface.
5. **Na conta Amazon, só leitura.** Sem carrinho, compra, lista, avaliação ou
   alteração de conta.
6. **Nada estrutural é alterado** durante a pesquisa (coleções, ordem, papéis,
   lacunas). Achados desse tipo viram nota para decisão.

---

## 1 · Tamanho e ritmo

- **Lote = 3 a 5 obras** por sessão. Obras que compartilham um volume
  (ex.: Eurípides, Oresteia, Plutarco) contam como um lote só.
- Cada lote termina **gravado e relatado**. Não se abre lote novo com o
  anterior pela metade.
- Uma obra pode sair do lote como `partially_researched` com os itens em falta
  nomeados. Isso é um resultado válido, não uma falha.

---

## 2 · Ordem dos lotes

A ordem é de **custo e aproveitamento**, não de importância intelectual
(prioridade não é afetada por esta fila).

| Fase | O quê | Por quê primeiro |
|---|---|---|
| **A · Piloto** | Platão EDUFPA (*República*, *Apologia/Críton*, *Fédon*) + *O Banquete* (Ed. 34) | Já têm ISBN; testam a série bilíngue e a questão §7.7 da revisão |
| **B** | Demais obras da Greco-Romana com publicação registrada (59 publicações) | Metade do trabalho (identificar a edição) já foi feita |
| **C** | Greco-Romana sem edição (*Bacantes*, 4 Vidas de Plutarco, Campbell, Kirk-Raven-Schofield) | Exigem enumeração do zero |
| **D** | Política (40) — edições declaradas por você, `verified: false` | Converter escolha declarada em verificada ou recusada |
| **E** | Educação (11) | Nenhuma editora informada |
| **F** | Sobrevivência e Cultura — só o que falta (Dickson, Werner, Skousen, Bezmenov, *Dark Secrets*, Lobo, confirmações tier 6→1) | Poucos itens, mas dependem de você ter os livros |

Você pode reordenar a qualquer momento.

---

## 3 · O ciclo de uma obra (os dez passos do §E, em forma de checklist)

### Passo 1 — Carregar o que já existe
Ler: registro da obra (`works/`), publicações que a contêm (`publications/`),
participações na coleção e o trecho da revisão que a cita.
**Saída:** lista do que já se sabe e do que já foi decidido (não repetir
decisões em silêncio).

### Passo 2 — Fatos da obra
Estabelecer: título original, língua original, data/circunstância de
composição, forma (`form`), `work_type`, transmissão textual e **edição
crítica de referência** do original (ex.: OCT, Teubner, Loeb).
**Fontes:** tier 4–5 (enciclopédias acadêmicas, Oxford Classical Dictionary,
Stanford Encyclopedia, introduções de edições críticas).
**Grava em:** frontmatter da obra + seção `## Fatos`.

### Passo 3 — Enumerar candidatos (antes de julgar)
Listar edições em **português, espanhol, italiano, inglês**, e opções em
língua original/bilíngues.
**Onde procurar:**
- Amazon (navegador interno) — rápido para descobrir o que existe;
- catálogos de editoras;
- Biblioteca Nacional (BN), WorldCat, catálogos universitários;
- bibliografias em resenhas acadêmicas.
**Saída:** tabela de candidatos com editora, tradutor, ano, ISBN, fonte da
pista. Nada ordenado ainda.

### Passo 4 — Verificar campo a campo
Para cada candidato sério, confirmar em **tier 1–5**:
editora · tradutor · ano/edição · páginas · formato · ISBN-13 · completude ·
texto-base · tradução direta ou por intermediário · bilíngue (no livro, nunca
pelo título).
**Ordem de consulta:** página bibliográfica da editora (tier 1) → catálogo
universitário (2) → BN / ISBN Brasil (3) → bases e resenhas acadêmicas (4) →
fontes em língua original (5).
**Grava em:** `verified_fields` só o que foi checado.

### Passo 5 — Avaliar qualidade
Credenciais do tradutor, texto-base, aparato (notas, introdução, índice),
recepção acadêmica. Registrar `framing` separado da qualidade.
Checar as quatro suposições recusadas (E.1b): popularidade, prestígio da
editora, novidade, título grego na capa.
**Grava em:** `## Avaliações acadêmicas` na obra, `contains[]` na publicação.

### Passo 6 — Disponibilidade no Brasil (datada)
Aqui entra a Amazon de novo, com a Estante Virtual e a loja da editora.
Para cada anúncio: `match_basis` (ISBN confere? editora+tradutor+ano?).
Sem correspondência confirmada → `unconfirmed`.
**Grava em:** `availability_br`, `availability_checked`, bloco `acquisition`
(só `price_band`, nunca preço exato, nunca avaliações).

### Passo 7 — Aplicar o §F
1. portão textual (completa, texto-base defensável, direta);
2. portão físico;
3. faixas de qualidade;
4. idioma só dentro da faixa;
5. regra do grego/bilíngue (F.3).
**Emite só vereditos que diferem:** melhor acadêmica · melhor em português ·
melhor obtenível no Brasil.
**Grava em:** `contains[].verdict` + `reason`, inclusive `rejected` com razão.

### Passo 8 — Lugar na biblioteca
O que a obra prepara, o que a responde, o que a contesta no acervo.
**Só registrar**; relações novas ficam como proposta para você aprovar.
**Grava em:** `## Lugar na biblioteca` / nota na revisão.

### Passo 9 — Status
Conferir a lista E.4. Tudo cumprido → `researched`. Caso contrário →
`partially_researched` com `missing:` nomeando o que falta.

### Passo 10 — Gravar e relatar
- Editar os arquivos canônicos no Drive.
- Rodar a build (`tools/build.py`) quando houver ambiente para isso.
- Relatório curto ao Mathews (formato na §5).

---

## 4 · Uso do navegador interno

- O navegador já está logado na sua conta Amazon; o agente **não faz login**
  nem digita senha.
- **Busca:** por ISBN quando existir; senão, título + tradutor.
- **Leitura:** preferir texto da página (ficha técnica: editora, idioma, páginas,
  ISBN-10/13, dimensões) a screenshot.
- **Pedidos ("Seus pedidos"):** consultados só quando você pedir, para
  identificar a edição exata que você comprou. O resultado é informado a você,
  não gravado como posse.
- Fontes tier 1–5 são abertas no mesmo navegador, em abas separadas.
- Site bloqueado ou recusado: parar e avisar, sem contornar.

---

## 5 · Relatório de fim de lote

Para cada obra:

| Obra | Status final | Edição recomendada | Vereditos | Falta |
|---|---|---|---|---|

Mais, se houver:
- **Discordâncias** com a edição que você tinha escolhido, com a razão;
- **Decisões para você** (trocar edição, relação proposta, achado estrutural);
- **Dados que só o seu exemplar resolve** (foto da ficha técnica).

---

## 6 · O que interrompe o lote

- Dois candidatos equivalentes em faixa e idioma → pergunta a você.
- Evidência de que a edição que você possui é problemática (cortes, tradução
  indireta existindo direta) → para e relata antes de gravar veredito.
- Conflito entre fontes tier 1–5 → registra ambos, `confidence: reported`,
  e relata.
