---
collection: null
kind: proposta de vocabulário (lugar e tema das obras)
by: claude
date: 2026-11-03
status: "aprovada pelo Mathews em 2026-11-03 (cartão d-reg-lugar-tema, opção A); listas em config/lugar-tema.yaml"
---

# Lugar e tema das obras — proposta de listas

Pedido do Mathews em 2026-11-03: os fios do Guia do ano precisam de critério
que sirva a qualquer obra. A mesma marcação alimenta o mapa histórico, que é
pendência registrada. Nada aqui foi aplicado ainda.

## Princípios

1. **Três tipos de fio, cada um com uma fonte nos dados da obra.**
   - *Lugar*: onde se passa a obra ou de onde ela fala (lista A).
   - *Tema*: de que assunto trata, em dois níveis (lista B).
   - *Diálogo*: relações já registradas entre obras ("responde a",
     "pré-requisito de", "tratamento literário de", "critica").
2. **Um fio só aparece quando liga pelo menos duas obras.** O nome do fio é o
   nome do lugar, do tema ou da relação; a frase explicativa é opcional.
3. **Nível médio de detalhe.** "Grécia", não "Atenas" nem "Mundo antigo";
   "Totalitarismo", não "Política" nem "Stalinismo de 1937".
4. **Lugar e tema são opcionais.** Uma obra de teoria (Rawls, Kant) pode não ter
   lugar; um panorama mundial (Eliade, Frankopan) leva "Mundo" e não forma fio
   de lugar.
5. **Uma obra pode ter mais de um de cada**, mas poucos: até 3 lugares e até 4
   temas específicos. Marcar tudo é o mesmo que não marcar nada.
6. **A época continua separada** (`period_covered`), e é ela que posiciona a
   obra no mapa histórico e na viagem do ano.
7. **As listas são fechadas.** Lugar ou tema novo entra por decisão, como
   qualquer valor de vocabulário.

## Lista A — Lugares (um nível)

**Antiguidade e mundo não europeu**
Mesopotâmia · Egito antigo · Levante e Israel antigo · Anatólia · Pérsia ·
Grécia · Roma · Índia · China · Mundo islâmico · Ásia Central · Mesoamérica

**Europa e Américas, da Idade Média em diante**
Europa medieval · Itália · França · Inglaterra e Reino Unido · Alemanha ·
Rússia e URSS · Espanha e Portugal · Estados Unidos · Brasil

**Sem lugar específico**
Mundo (panoramas; não forma fio de lugar)

## Lista B — Temas (dois níveis: o geral agrupa, o específico vira fio)

**Política e poder**
Democracia · Totalitarismo · Tirania e despotismo · Liberalismo ·
Socialismo e marxismo · Conservadorismo · Libertarianismo e anarquismo ·
Contrato social · Lei natural e direito · Império · Guerra e estratégia ·
Propaganda e ideologia

**Religião**
Mito e criação do mundo · Deuses e heróis · Religião grega e romana ·
Religiões do antigo Oriente · Bíblia e judaísmo · Jesus e cristianismo antigo ·
Igreja e teologia · Reforma · Fim dos tempos · Islã · Hinduísmo · Budismo ·
Mística e esoterismo · Teoria da religião

**Filosofia**
Do mito à razão · Ética: a vida boa · Filosofia como modo de vida ·
Conhecimento e razão · Estética e gosto · Morte e finitude

**História e sociedade**
Ascensão e queda de impérios · Vida cotidiana · Arte e arqueologia ·
Historiografia · Colonização e conquista · Economia e trabalho

**Literatura e cultura**
Épica · Tragédia e comédia · Poesia lírica · Romance · Tradição clássica e
legado · Cultura e decadência

**Educação**
Formação e paideia · Escola e pedagogia · Como se aprende

**Ciência e técnica**
Matemática · Medicina · Astronomia e cosmologia · Técnica e engenharia

**Vida prática e sobrevivência**
Sobrevivência · Socorro e saúde · Plantas e cultivo · Defesa · Construção ·
Autossuficiência e economia doméstica

## Exemplos

**O plano de 2027**

| Mês | Obra | Lugar | Tema específico |
|---|---|---|---|
| jan | Woolf, *Roma* | Roma | Ascensão e queda de impérios |
| fev | Plutarco, *Alexandre e César* | Grécia, Roma | Império; Ética: a vida boa |
| mar | Flusser, *Jesus* | Levante e Israel antigo | Jesus e cristianismo antigo |
| abr | Beard, *Pompeia* | Roma | Vida cotidiana; Arte e arqueologia |
| mai | Hesíodo, *Teogonia* | Grécia | Mito e criação do mundo; Deuses e heróis |
| jun | Hesíodo, *Trabalhos e Dias* | Grécia | Ética: a vida boa; Economia e trabalho |
| jul | Hadot | Grécia, Roma | Filosofia como modo de vida; Ética: a vida boa |
| ago | Almond, *O Anticristo* | — | Fim dos tempos; Igreja e teologia |
| set | *Piratas no Brasil* | Brasil | Colonização e conquista |
| out | Townsend, *O Quinto Sol* | Mesoamérica | Colonização e conquista; Ascensão e queda de impérios |
| nov | Matsumoto, *Os Mitos Maias* | Mesoamérica | Mito e criação do mundo; Deuses e heróis |
| dez | Frankopan | Mundo, Ásia Central | Império; Economia e trabalho |

Fios que sairiam sozinhos: **Grécia** (fev, mai, jun, jul), **Roma** (jan,
fev, abr, jul), **Mesoamérica** (out, nov), **Mito e criação do mundo** (mai,
nov), **Deuses e heróis** (mai, nov), **Ética: a vida boa** (fev, jun, jul),
**Colonização e conquista** (set, out), **Ascensão e queda de impérios** (jan,
out), **Império** (fev, dez), **Economia e trabalho** (jun, dez).
Cristianismo (mar, ago) não sairia como fio de tema, porque os dois livros
caem em temas específicos diferentes; os dois chips apareceriam juntos sob
"Religião". Se ele quiser o fio, o caminho certo é marcar Almond também com
"Jesus e cristianismo antigo", e não inventar um fio à mão.

**O exemplo do Mathews (URSS, democracia, nazismo)**
*Arquipélago Gulag* (Rússia e URSS; Totalitarismo), *A Democracia e seus
Críticos* (—; Democracia), *LTI* (Alemanha; Totalitarismo, Propaganda e
ideologia): o fio **Totalitarismo** liga o Gulag a *LTI*; Dahl aparece ao lado,
sob o mesmo tema geral "Política e poder", sem um fio que finja que os três
tratam da mesma coisa.
