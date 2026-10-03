# Migração da Bibliotheca para o GitHub — pela web

Passo a passo completo, do zero ao site no ar, **sem linha de comando e sem
instalar nada**. Tudo pelo navegador.

**Tempo:** 40 a 60 minutos, a maior parte arrastando arquivos.
**Risco de perder dados:** nenhum. A pasta em `G:\Meu Drive\Biblioteca`
continua intacta do começo ao fim — nada é movido, nada é apagado.

**Decisões já tomadas** (2026-10-02): repositório **público**, capas
**embutidas** no site. Registradas em `STATE.md`.

---

## O que você precisa, e o que NÃO precisa

Precisa de uma conta no GitHub. Se não tiver, crie em
<https://github.com/signup>. O plano gratuito cobre tudo isto.

**Não precisa de Git instalado. Não precisa de Python. Não precisa de
terminal.** A build roda dentro do GitHub a cada envio — é para isso que serve
o `build.yml`. Python local só volta a ser necessário se você quiser abrir a
interface no computador para **gravar** o seu estado pessoal de leitura e
posse, que é a única coisa que uma página na web não consegue fazer (README §6).

**E não precisa tirar a pasta do Google Drive.** O guia anterior mandava tirar,
porque um repositório Git dentro do Drive corrompe. Fazendo pela web, nenhum
repositório Git nasce no seu computador — a pasta do Drive continua sendo uma
pasta comum de arquivos, e o risco não existe. Se um dia você passar a usar o
GitHub Desktop (ver o apêndice), aí sim a pasta precisa sair do Drive primeiro.

---

## Os dois limites que moldam este roteiro

| limite | valor | consequência |
|---|---|---|
| arquivos por envio | **100** | `works/`, `publications/` e `covers/` precisam ir em partes |
| tamanho por arquivo | **25 MiB** | nenhum problema: o maior arquivo seu tem 1,5 MB |

Por isso o roteiro tem nove envios em vez de um. Cada envio é um arrastar e
soltar seguido de um clique.

---

## Parte 1 · Separar o que sobe do que não sobe

Abra `G:\Meu Drive\Biblioteca` no Explorador de Arquivos.

**NÃO suba estas duas pastas:**

| pasta | por quê |
|---|---|
| `_generated` | É saída da build — 26 MB reconstruídos a cada vez. Versioná-la somaria isso ao histórico a cada envio, e em cinquenta envios seria mais de um giga que nunca encolhe. O GitHub reconstrói sozinho. |
| `Claude outputs` | Uma variante de interface que nunca foi declarada canônica em lugar nenhum. Fica no disco à espera de decisão; não some. |

**Tudo o resto sobe.** O `.gitignore` que já está na pasta garante que, daqui
em diante, essas duas nunca entrem por acidente — mas nesta primeira vez quem
não as seleciona é você.

### Opcional: dividir as pastas grandes de antemão

Três pastas passam de 100 arquivos e precisam ir em partes. Você pode separá-las
à mão no Explorador (ordenar por nome, clicar no primeiro, rolar, Shift+clicar
no centésimo) — ou deixar o computador fazer isso sem erro.

Para a segunda opção: tecla Windows, digite `powershell`, abra, e cole o bloco
inteiro de uma vez:

```powershell
$raiz = "G:\Meu Drive\Biblioteca"
$saida = "$HOME\Desktop\lotes-bibliotheca"
Remove-Item $saida -Recurse -Force -ErrorAction SilentlyContinue
foreach ($pasta in @("works","publications","covers")) {
  $arquivos = Get-ChildItem "$raiz\$pasta" -File | Sort-Object Name
  $n = 0
  foreach ($grupo in 0..[math]::Floor(($arquivos.Count - 1) / 90)) {
    $n++
    $destino = "$saida\$pasta-parte$n"
    New-Item -ItemType Directory -Path $destino -Force | Out-Null
    $arquivos | Select-Object -Skip ($grupo * 90) -First 90 |
      Copy-Item -Destination $destino
  }
}
Write-Host "Pronto. Os lotes estão em $saida"
explorer $saida
```

Isso cria, na sua Área de Trabalho, uma pasta `lotes-bibliotheca` com
`works-parte1` a `works-parte3`, `publications-parte1` e `parte2`, e
`covers-parte1` e `parte2` — cada uma com no máximo 90 arquivos, folga
confortável abaixo do limite de 100. **São cópias**: a pasta original não é
tocada. No fim de tudo você apaga `lotes-bibliotheca` e acabou.

---

## Parte 2 · Criar o repositório

### Passo 1 · O repositório vazio

Vá a <https://github.com/new> e preencha:

- **Repository name:** `bibliotheca` (ele aparece no endereço do site)
- **Public**
- **NÃO marque** "Add a README file"
- **NÃO escolha** `.gitignore` nem licença

As três últimas importam de verdade: qualquer arquivo criado aqui faz o
repositório nascer com histórico próprio, e isso atrapalha depois. Ele tem de
nascer **vazio**.

Clique em **Create repository**. A página que abre mostra instruções de
terminal — ignore todas. Procure o link **"uploading an existing file"**, no
meio do texto, e clique nele. É por ali que tudo acontece.

> Depois do primeiro envio essa página some. Para voltar a enviar arquivos:
> botão **Add file** → **Upload files**, no alto da lista de arquivos.

---

### Passo 2 · Os arquivos da raiz

Na tela de upload, arraste estes seis arquivos de dentro de
`G:\Meu Drive\Biblioteca`:

```
README.md    AGENT.md    STATE.md    MIGRACAO-GITHUB.md
.gitignore   .gitattributes
```

Os dois últimos começam com ponto e aparecem normalmente no Explorador do
Windows — não são ocultos aqui, ao contrário do que acontece no Linux e no Mac.

Embaixo, em **Commit changes**, escreva uma mensagem (`documentos de raiz`
serve) e clique em **Commit changes**.

---

### Passo 3 · O workflow, pelo editor

Este arquivo é digitado, não arrastado — e precisa estar num caminho exato.

Clique em **Add file** → **Create new file**. No campo do nome, digite
exatamente isto, **com as barras**:

```
.github/workflows/build.yml
```

Conforme você digita cada barra, o GitHub transforma o trecho anterior numa
pasta. Ao terminar, o campo mostra `.github / workflows /` e o nome do arquivo
ao lado.

Agora abra o `build.yml` que mandei junto da conversa, copie o conteúdo inteiro
e cole na área de texto grande. Clique em **Commit changes**.

**Confira o caminho antes de seguir.** O GitHub só procura workflows em
`.github/workflows/`. Um arquivo num lugar parecido é ignorado em silêncio, sem
nenhum erro — e você passaria o resto do roteiro sem entender por que nada
publica.

---

### Passo 4 · As pastas pequenas

Estas cabem num envio só cada uma, e você pode arrastar a **pasta inteira** —
o navegador preserva a estrutura de subpastas:

| envio | o que arrastar | arquivos |
|---|---|---|
| 1 | `collections` | 6 |
| 2 | `config` | 9 |
| 3 | `people` | 1 |
| 4 | `review` (com `gaps` e `structural` dentro) | 18 |
| 5 | `images` (com `collections` dentro) | 7 |
| 6 | `sources` (com `lists` dentro) | 3 |
| 7 | `state` | 1 |
| 8 | `tools` (com `fonts` dentro) | 6 |

Você pode juntar várias dessas pastas num envio só, desde que a soma fique
abaixo de 100 — todas juntas dão 51, então **cabem num envio único**. Arraste as
oito de uma vez se preferir.

Mensagem de commit sugerida: `estrutura canônica`.

---

### Passo 5 · As três pastas grandes

Aqui vão as partes. Se você rodou o script opcional, elas já estão prontas na
Área de Trabalho; se não, selecione à mão no Explorador.

**Atenção a um detalhe que custa tempo se passar despercebido:** ao arrastar o
conteúdo de uma pasta `works-parte1`, os arquivos vão para a **raiz** do
repositório, não para `works/`. Antes de confirmar, olhe o campo de caminho que
aparece no alto da tela de upload. Se ele não mostrar a pasta certa, digite o
nome da pasta seguido de barra no campo **"Name your file..."** que aparece ali
— ou, mais simples, **arraste a pasta `works` inteira em vez dos arquivos
soltos**, três vezes, com conteúdos diferentes a cada vez.

A forma que menos erra: renomeie cada lote para o nome final antes de arrastar.
No Explorador, dentro de `lotes-bibliotheca`, renomeie `works-parte1` para
`works`, arraste, confirme; volte, renomeie `works-parte2` para `works`,
arraste, confirme. O GitHub junta as partes na mesma pasta — ele não substitui,
acrescenta.

| envio | pasta | arquivos |
|---|---|---|
| 9 | `works` parte 1 | 90 |
| 10 | `works` parte 2 | 90 |
| 11 | `works` parte 3 | 23 |
| 12 | `publications` parte 1 | 90 |
| 13 | `publications` parte 2 | 65 |
| 14 | `covers` parte 1 | 90 |
| 15 | `covers` parte 2 | 28 |

As capas somam 17 MB e são a parte mais lenta.

Ao terminar, a página inicial do repositório deve listar: `.github`,
`collections`, `config`, `covers`, `images`, `people`, `publications`,
`review`, `sources`, `state`, `tools`, `works`, mais os quatro `.md` e os dois
arquivos com ponto. **Não** devem aparecer `_generated` nem `Claude outputs`.

---

## Parte 3 · Pôr o site no ar

### Passo 6 · Ligar o Pages

No repositório: **Settings** (aba no alto) → **Pages** (menu da esquerda).

Em **Build and deployment**, no campo **Source**, troque
`Deploy from a branch` por **`GitHub Actions`**.

Só isso. Não escolha branch, não escolha pasta, não salve mais nada. É a única
configuração do Pages que você faz na vida deste repositório.

### Passo 7 · Rodar a primeira publicação

Aba **Actions** → **build**, na lista da esquerda → botão **Run workflow**, à
direita → **Run workflow**.

Acompanhe. São dois blocos, *Construir e conferir* e *Publicar no Pages*, e
levam um ou dois minutos. Quando os dois ficarem verdes, o endereço aparece no
segundo bloco e também em **Settings → Pages**:

```
https://SEU-USUARIO.github.io/bibliotheca/
```

Abra. A interface carrega inteira, com as capas. A primeira abertura demora
alguns segundos — são 8,6 MB num arquivo só.

**Se *Construir e conferir* ficar vermelho**, abra o log e procure a linha que
começa com `✖`. Quase sempre significa que algum arquivo não subiu: o portão
detecta uma coleção apontando para uma obra que não existe no repositório.
Suba o que faltou e rode de novo.

### Passo 8 · Trancar o `main` (opcional, recomendado)

Faz o portão ter poder de veto em vez de ser só um aviso.

**Settings → Rules → Rulesets → New ruleset → New branch ruleset**:

- **Name:** `main protegido`
- **Enforcement status:** `Active`
- **Target branches** → **Add target** → **Include default branch**
- Marque **Require status checks to pass** e adicione o check
  **`Construir e conferir`**

Deixe **Require a pull request** desmarcado se você trabalha sozinho e edita
pela web — com ele marcado, cada edição vira um pull request, o que é correto
mas pesado para corrigir um acento.

---

## Como trabalhar daqui em diante

É aqui que a escolha pela web tem consequência, e vale saber antes.

**Editar texto pela web funciona bem.** Abra qualquer `.md` ou `.yaml` no
GitHub, clique no lápis, edite, confirme. O Actions reconstrói e republica o
site em um ou dois minutos. Para corrigir uma frase de revisão ou mudar um
campo, é o caminho mais curto que existe.

**Duas coisas a web não resolve**, e ambas têm saída:

*O seu estado pessoal de leitura e posse.* Continua precisando da interface
local em Chrome ou Edge, com a pasta no computador, como no §6 do README. Na
web o caminho é *Copiar YAML* e trazer para o arquivo.

*As minhas alterações.* Hoje eu escrevo direto na pasta do seu computador. Com
o canônico no GitHub, essa pasta vira uma cópia — e duas cópias que ambas
parecem oficiais é exatamente o problema que esta migração existe para evitar.
**A saída limpa:** depois que o repositório existir, me passe o endereço dele.
Eu provavelmente consigo gravar direto no repositório, e aí a pasta do Drive
deixa de ter papel nenhum e pode ser aposentada. Se não der, o apêndice resolve.

---

## Quando der errado

| o que aparece | o que é | o que fazer |
|---|---|---|
| "Yowza, that's a big file" | arquivo acima de 25 MiB | você está tentando subir algo de `_generated` — não suba |
| Só 100 arquivos entraram de 150 | o limite por envio | suba o resto num segundo envio |
| Os arquivos foram para a raiz, não para a pasta | arrastou o conteúdo em vez da pasta | apague-os pelo GitHub e repita arrastando a pasta |
| Actions não tem nenhum workflow | o `build.yml` está no caminho errado | confira que é exatamente `.github/workflows/build.yml` |
| Actions vermelho em *Publicar no Pages* | Pages não está em modo GitHub Actions | refaça o Passo 6 |
| Actions vermelho em *Conferir a integridade* | o portão reprovou | leia a linha com `✖`; quase sempre é arquivo que faltou subir |
| O site abre em branco | normal nos primeiros segundos | são 8,6 MB; se persistir, F12 e me mande o erro |
| O site mostra a versão antiga | cache do navegador | `Ctrl + Shift + R` |

---

## Apêndice · O caminho com o GitHub Desktop

Se a quinze envios manuais você preferir instalar um programa, o **GitHub
Desktop** faz tudo em três cliques, sem terminal: <https://desktop.github.com>.

Nesse caminho, **a pasta precisa sair do Google Drive primeiro** — o Desktop cria
um repositório Git de verdade no disco, com milhares de arquivos pequenos de
controle, e o Drive sincroniza e trava esses arquivos no meio das operações,
corrompendo o repositório de um jeito que só aparece dias depois.

1. Copie `G:\Meu Drive\Biblioteca` para `C:\Users\<voce>\Projetos\Biblioteca`.
   Copie, não mova — a original fica como rede de segurança.
2. No GitHub Desktop: **File → Add local repository**, aponte para a pasta
   nova. Ele avisa que não é um repositório e oferece **create a repository**;
   aceite.
3. Ele mostra todos os arquivos. O `.gitignore` já exclui `_generated` e
   `Claude outputs` sozinho — confirme que eles não aparecem na lista.
4. Escreva a mensagem, **Commit to main**, depois **Publish repository**.
   Desmarque *"Keep this code private"*, porque a decisão foi repositório
   público.
5. Siga a partir do Passo 3 deste guia (o workflow pode ser criado pela web
   mesmo) e depois o Passo 6.

Daí em diante o ciclo é: **Fetch origin** antes de começar, e **Commit** +
**Push origin** ao terminar. Dois botões.
