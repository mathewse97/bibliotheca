# STATE.md — onde o trabalho está

Estado **operacional**: o que está em andamento, o que espera decisão, o que
ficou por fazer. Não é curadoria — a prosa curatorial vive em `review/`, as
lacunas em `review/gaps/`, as propostas em `review/structural/`. Este arquivo
é o resumo que faz alguém retomar sem reler tudo.

Não é uma segunda base de dados. Quando uma linha daqui divergir de um arquivo
canônico, **o arquivo canônico é o fato**.

**Atualizado em 2026-10-02.** Os números envelhecem; a contagem viva é a que
`python3 tools/build.py` imprime.

---

## Onde a biblioteca está

```
203 obras · 6 coleções · 154 publicações · 157 autores · 0 problemas
12 lacunas abertas · 5 obras sem coleção · 4 propostas estruturais (2 abertas)
```

Coleções: Política, Educação, Cultura, Religião, Cultura
Greco-Romana, Sobrevivência e Autossuficiência.

---

## Esperando decisão sua

A fila completa está em `review/decisions.yaml` e na tela **Decisões** da
interface — 12 itens. Os que têm consequência estrutural:

| o quê | onde | desde |
|---|---|---|
| Se uma regra deve proibir derivar o **propósito de um movimento** das obras que ele hoje contém | cartão `d-reg-proposito-movimento` | 2026-09-27 |
| O crescimento do movimento VII de Política (de 10 para 15 obras) pede subdivisão | registrado em `collections/political-thought.md` | 2026-09-28 |
| Auditoria de Política pela pirâmide de Adler: duas saídas, duas trocas e três grupos com redundância | cartões `d-pol-adler-*`; registro em `review/political-thought.md` §10 | 2026-10-14 |
| Auditoria de Greco-Romana pela pirâmide de Adler: tragédias de Eurípides, quatro introduções repetidas, Campbell e a lacuna de Lucrécio | cartões `d-greco-adler-*`; registro em `review/greco-roman.md` §9 | 2026-10-14 |
| Auditoria das outras cinco coleções: clássicos fundadores em Religião, fontes em Educação e Oriente Próximo, Eliot em Cultura, manuais repetidos em Sobrevivência | cartões `d-rel-adler-*`, `d-edu-adler-*`, `d-cult-adler-eliot`, `d-sob-adler-repetidos`, `d-ane-adler-fontes`; registros nas revisões de cada coleção | 2026-10-14 |

**Regra de edições, combinada em 2026-10-10:** com a edição escolhida, as
alternativas saem do registro. Ficam só: volumes da mesma edição; edição que
ele tem; alternativa enquanto a escolhida não está à venda; e edição de
função diferente (referência de estudo). Exceções vigentes: a Valla do
Pseudo-Apolodoro (referência); as duas edições de Homero (ele quer as duas);
a Odysseus de *As Bacantes* — **remover depois de 26/10/2026**, quando sai o
Teatro completo VI da Editora 34.

---

## Regras novas de 2026-10-14

- **Pirâmide de Adler** (`config/curation-rules.md` §2.9): toda obra precisa de
  um papel que nenhuma outra cumpre, e recebe um nível: grande livro, livro de
  estudo, ou informação ou consulta (nomes trocados a pedido do Mathews em
  2026-10-14; antes "releitura" e "uma leitura séria"). Auditorias: feitas as
  sete coleções.
- **Mesmo critério de edição para todas as obras**
  (`config/bibliographic-rules.md` §F.7): sem exceção por tipo nem por nível
  da pirâmide; a ordem dos lotes de pesquisa não muda o rigor.
- **Como ler** (`config/interface-rules.md` §13): seção nova na página da obra.
  Feito (2026-10-14): todas as 231 obras. Obra nova entra com Como ler
  junto de Sobre a obra.
- **Tipo de cada obra** (`config/vocabularies.yaml`, `work_type`): as 230
  classificadas em 2026-10-14; 13 casos duvidosos listados no próprio
  vocabulário.
- **Por que está aqui** (`config/interface-rules.md` §14): diz também o que
  buscar na obra naquela coleção; 20 textos vazios reescritos.

---

## Pendências de pesquisa

- **Edições sem veredito depois da primeira passada (revisto em 2026-10-21): 21 obras.**
  Recomendadas: 214 publicações; alternativas: 9. O que falta em cada uma:
  - *Decisão do Mathews em cartão* (7): Maquiavel (`d-ed-maquiavel`),
    Rousseau (`d-ed-rousseau`), Montesquieu (`d-ed-montesquieu-unesp`),
    Cícero (`d-ed-cicero`), Tomás de Aquino (`d-ed-aquino`), Popper
    (`d-ed-popper`), Berlin (`d-ed-berlin`).
  - *Tradutor conhecido, falta comparar com o original* (4): Rothbard
    (Fernando Fiori Chiocca) e Hoppe (Marcelo Werlang de Assis), ambos do
    Instituto Mises Brasil, cujos PDFs são gratuitos; Aron/Vide (Christian
    Lesage, uma fonte só); João Paulo II (Antônio Angonese e Ephraim
    Ferreira Alves, talvez traduzido do inglês).
  - *Nome do tradutor ainda não achado* (6): Weber (as duas conferências,
    Cultrix: os tradutores são conhecidos, falta a língua de partida), Adler (*Paideia* e *Como
    Ler Livros*, Kírion), Scruton, Mark S. Smith; procurados de novo em
    2026-10-21, sem resultado.
  - *Identificação ou comparação que falta* (3): Seymour (qual obra a
    edição traduz), *Manual do Arquiteto Descalço* (comparar com o original
    espanhol), *A Tábua de Esmeralda* (comparar com traduções acadêmicas).
  - *Fora de coleção, sem escolha* (1): Werner (cartão arquivado).
  - O ambiente não abre sites de editoras, da Travessa nem PDFs do
    Instituto Mises; as comparações de tradução ficam para quando houver
    acesso ou para o Mathews, com o livro na mão.

- **Pesquisa de edições em lotes** (`config/research-procedure.md` §2).
  Lote 1 (2026-10-14): Hobbes, Arendt, Dostoiévski, Ibn Khaldun, todos
  recommended. Lote 2 (2026-10-17): Locke (Martins Fontes, edição crítica de
  Peter Laslett) e Tocqueville (Martins Fontes, prefácio de François Furet)
  recommended; Maquiavel, Rousseau e Montesquieu em cartão
  (`d-ed-maquiavel`, `d-ed-rousseau`, `d-ed-montesquieu-unesp`). Falta:
  registrar o Livro II de Tocqueville (só achado usado). Lote 3
  (2026-10-17): Kant (Guido Antônio de Almeida, revista), Burke (Vide), Mill
  *Sobre a Liberdade* (Penguin-Companhia) e *Governo Representativo* (L&PM,
  Denise Bottmann) recommended; Cícero em cartão (`d-ed-cicero`). Aristóteles
  e Platão já estavam recommended. Lote 4 (2026-10-17):
  Tucídides (Madamu, Mário da Gama Kury), Confúcio (Unesp, Giorgio Sinedino),
  Kautilya (Oxford, Patrick Olivelle) e Agostinho (Gulbenkian, J. Dias
  Pereira) recommended; Tomás de Aquino em cartão (`d-ed-aquino`). Rever
  Agostinho quando a Paulus completar a sua edição. Lote 5 (2026-10-17):
  *Ricardo II*, *Júlio César* e *Coriolano* (Nova Fronteira, Barbara
  Heliodora), *A Ideologia Alemã* (Boitempo, integral), o *Manifesto*
  (Penguin-Companhia, Sérgio Tellaroli) e *O 18 de Brumário* (Boitempo, Nélio
  Schneider) recommended. Lote 6 (2026-10-17):
  Lukács (WMF, Rodnei Nascimento), Marcuse (Edipro, introdução de Douglas
  Kellner), Michels (Realpolitik, direto do alemão) e Schmitt (Edições 70,
  Alexandre Franco de Sá) recommended. **Weber ficou sem veredito:** não se
  sabe de que língua a Cultrix traduziu; surgiram duas edições novas (Unesp,
  2026; Vozes de Bolso, 2021) sem tradutor identificado. Falta ver a página
  de créditos de cada uma. Lote 7 (2026-10-18):
  Zamiátin (Editora 34), Huxley (Biblioteca Azul, Fabio Fernandes),
  Koestler (Sétimo Selo, do alemão) e Voegelin (Vide) recommended. Popper
  continua no cartão `d-ed-popper`. **Aron ficou sem veredito:** a Vide
  (2024), sua escolha, não tem tradutor identificado; a da Três Estrelas
  (2016, trad. Jorge Bastos) está esgotada. Lote 8 (2026-10-18):
  Bezmenov (Audax, única), os três Orwell (Penguin-Companhia e Companhia
  das Letras) e Klemperer (Contraponto, trad. Miriam Oelsner) recommended.
  Lote 9 (2026-10-18):
  Habermas (Unesp), Dahl (UnB), Levitsky e Ziblatt (Zahar), Rawls (Martins
  Fontes, edição revista) e Rothbard, *Anatomia do Estado* (Vide)
  recommended. A partir do lote 10, lotes de 10 obras
  (pedido do Mathews, 2026-10-18). Lote 10 (2026-10-18): Rothbard, *A Ética
  da Liberdade*, e Hoppe (Instituto Mises Brasil, únicas) fecham Política,
  onde só restam obras em cartão ou pendentes (Weber, Aron, Berlin, Popper,
  Cícero, Tomás de Aquino, Maquiavel, Montesquieu, Rousseau). Greco-Romana:
  Cline, Hesíodo, Homero (as duas edições), Eurípides, *As Bacantes*, e as
  Vidas de Plutarco e Vegécio recommended. Lote 11 (2026-10-18): os oito
  manuais em inglês da Greco-Romana e do Oriente Próximo (importados na
  Amazon; Cameron com disponibilidade a confirmar), Campbell (Palas Athena)
  e as cinco obras em português do Oriente Próximo recommended. Greco-Romana
  e Oriente Próximo sem pendências de edição. Lote 12 (2026-10-18): as
  15 obras de Cultura recommended (Scruton com tradutor a identificar);
  Cultura sem pendências de edição. Lote 13 (2026-10-18): as
  19 obras de Educação com edição recommended; só resta *A Ciência como
  Vocação*, de Weber, que depende da mesma pendência da Cultrix. **Correção (2026-10-18):** seis
  recomendações "por falta de alternativa" sem tradutor identificado foram
  revertidas para sem veredito, porque o §F.2 pede comparar a tradução com o
  original quando não se sabe se ela é boa: Adler (*A Proposta Paideia* e
  *Como Ler Livros*, Kírion), Rothbard (*A Ética da Liberdade*), Hoppe,
  Scruton e Mark S. Smith. Falta, em cada uma, o nome do tradutor ou a
  comparação com o original em inglês. Lote 14 (2026-10-18):
  Sobrevivência, 12 recommended; quatro pendentes, com a razão registrada:
  Seymour (não se sabe qual obra a edição traduz), *Primeiros Socorros* (só
  identificado em loja), PHTLS (falta confirmar se é a tradução da 10ª
  edição) e *Manual do Arquiteto Descalço* (esgotado, sem tradutor; comparar
  com o original espanhol). Lote 15 (2026-10-19): Religião,
  22 obras recommended; a parada sobre *O Sagrado e o Profano* foi
  resolvida (Eliade escreveu o livro em francês). Pendentes: *Cruzando o
  Limiar da Esperança* (tradutor e edição), *A Tábua de Esmeralda*
  (microeditora sem aparato) e *O Memorial de Deus* (tradutor). Lote 16 (2026-10-19): obras
  fora das coleções, 8 recommended; pendentes Krakauer (comparar com a
  tradução da Companhia das Letras), London (o Mathews decide depois de
  ler) e Werner (saiu de Sobrevivência; cartão arquivado sem edição
  escolhida). Fim da primeira passada da pesquisa de edições. Lote 17 (2026-10-21): pendências.
  *Primeiros Socorros* recommended (a editora é a Martinari, 2023; a DI
  Livros é a livraria); tradutores achados para Rothbard, Hoppe, Aron/Vide e
  João Paulo II. Decisões do Mathews no mesmo dia: Krakauer fica só com o
  exemplar dele; London fica com o exemplar dele e a Oxford World's
  Classics entra como alternativa; PHTLS recommended pela nova regra de
  manuais técnicos traduzidos pela editora do original
  (`config/bibliographic-rules.md` §F.2).
- **Cartão `d-edu-fonte` aplicado (2026-10-27), opção B.** Agostinho, *A
  Doutrina Cristã* (Paulus, Patrística 17), e Hugo de São Vítor,
  *Didascálicon* (Vozes 2001, bilíngue, só usada; alternativa Kírion 2018),
  entram no movimento I de Educação. Posições a confirmar; ver
  `review/education.md` §14.
- **★ agora é definida pelo agente (decisão do Mathews, 2026-10-27).**
  Critério em `config/curation-rules.md` §2.9 e no vocabulário. Educação
  tem 8 de 22 estrelas, Oriente Próximo 4 de 9, Cultura 5 de 16, Religião
  11 de 31, Sobrevivência 6 de 18 e Greco-Romana 25 de 87, cada uma com a
  razão escrita na revisão da coleção (seção "Estrelas"). Política mantém as
  27 estrelas da lista do Mathews (27 de 54, metade da coleção). A revisão
  está no cartão `d-pol-estrelas` (2026-10-28): proposta de 21 estrelas,
  em `review/political-thought.md` §11.
- **Bacantes:** em 2026-10-27 o Teatro completo VI (Editora 34) ainda estava
  só em pré-venda, embora com data de 26/10. A Odysseus continua registrada
  até ele estar à venda.
- **Romances do movimento X: edições registradas em 2026-10-09** (Etapa 1).
  O caso difícil, Koestler, foi resolvido: a Sétimo Selo publicou em 2022
  *Escuridão ao meio-dia*, traduzida do manuscrito alemão redescoberto — não
  da versão inglesa de Daphne Hardy. Zamiátin e Huxley ficaram em cartão
  (`d-ed-zamiatin`, `d-ed-huxley`).
- **Lista original de Política ausente do repositório.** A coleção declara
  `archived_at: sources/lists/politica-formacao-geral.md`, mas o arquivo não
  foi enviado na migração (só as listas de Greco-Romana e Religião estão em
  `sources/lists/`). As `edition_pref` marcadas `by: voce` em Política não
  podem, por isso, ser conferidas contra o texto original. Se o Mathews tiver
  a lista, ela deve ser arquivada nesse caminho.
- **Relações ainda não escritas** para `dostoievski--besy`, `zamiatin--my` e
  `orwell--animal-farm`: nenhuma parceira defensável encontrada. Ausência
  honesta, não esquecimento.
- **Decidido em 2026-10-05:** Educação admite a ciência da aprendizagem
  (opção A de `d-edu-ciencia-aprendizagem`). Dehaene e Brown, Roediger e
  McDaniel entraram no movimento VIII novo. Ver `review/education.md` §11.
- **Classificação `work_type`: resolvida em 2026-10-14.** As 230 obras foram
  classificadas nos seis tipos de Adler (`config/vocabularies.yaml`).
- **Cinco conclusões `stale`** de revalidação (três em Educação, uma em
  Cultura, uma em Greco-Romana): a biblioteca mudou e parte da evidência
  deixou de valer. Nenhuma foi reexaminada.
- **ISBN do Dehaene não resolvido**: existem dois números válidos para a edição
  brasileira, `978-65-5541-165-2` e `978-65-5541-166-9`. O registro adotou o
  primeiro, que é o do objeto em papel nas livrarias, e guardou o outro.

---

## Decisões da migração para o Git — 2026-10-02

| decisão | quem | o quê |
|---|---|---|
| Repositório **público** | Mathews | Sabendo que o site do Pages é público na internet em qualquer plano fora do Enterprise Cloud, e que isso torna públicas também as fichas, a prosa de revisão e o estado pessoal |
| Capas **embutidas** no site | Mathews | As 118 capas continuam na interface publicada, como identificação bibliográfica |
| `_generated/` **fora** do repositório | claude, proposto | Derivado; versioná-lo somaria ~26 MB ao histórico por build |
| `Claude outputs/` fora, **sem apagar** | claude, proposto | Variante de interface nunca declarada canônica. Fica no disco à espera de decisão |
| Sem arquivo de licença | claude, proposto | Repositório público sem licença significa todos os direitos reservados, que é a postura certa enquanto houver 118 capas de terceiros embutidas |

---

## Frase de direitos das capas — corrigida em 2026-10-09

Os 118 registros que diziam "uso em acervo pessoal privado" em
`cover.rights_note`, mais o modelo `_TEMPLATE.md`, passaram a dizer
"Imagem de capa usada como identificação bibliográfica da edição." As capas
novas já entram com essa frase.

---

## O próximo passo

A migração para o GitHub está feita e o site publica pelo Actions. O cartão
`d-edu-ciencia-aprendizagem` foi decidido em 2026-10-05. Na fila de curadoria,
o próximo item estrutural é o cartão `d-reg-proposito-movimento`; a
classificação `work_type` de Hirsch, Dehaene e Brown, Roediger e McDaniel
continua devida.
