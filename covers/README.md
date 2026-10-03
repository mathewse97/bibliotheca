# covers/

Imagens de capa das **publicações**. Uma capa pertence ao objeto físico, não à
obra: *A República* não tem capa; a edição da Gulbenkian tem.

**Convenção de nome:** `<publication-id>.<ext>` — o mesmo id do arquivo em
`publications/`. Extensões aceitas: `.jpg`, `.jpeg`, `.png`, `.webp`.

A imagem vive aqui, no repositório, e não como link remoto. Um link de imagem
de vendedor quebra, troca de edição sem aviso e não funciona offline. Com o
arquivo local, a capa sobrevive ao anúncio que a originou.

Cada capa é declarada no bloco `cover:` da sua publicação, com `source` —
de onde a imagem veio, literal — e `checked`. Ver `config/acquisition.yaml`.

**Sem fonte confiável, não há capa.** Ausência de capa nunca é defeito
bibliográfico, e a build não a reporta como problema. O que a build reporta é
um bloco `cover:` cujo arquivo não existe em disco, ou que não diz de onde a
imagem veio — isto é, um registro que afirma mais do que sabe.

A build embute as imagens na interface gerada quando cabem no limite de
`cover.embed_max_bytes`, para que a interface continue sendo um arquivo único.

*Vazio hoje. Nenhuma publicação foi pesquisada.*
