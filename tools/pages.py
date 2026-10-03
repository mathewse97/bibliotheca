#!/usr/bin/env python3
# ---------------------------------------------------------------------------
# EMPACOTADOR DO SITE — monta `site/` a partir do que a build produziu.
#
# O GitHub Pages serve uma PASTA e procura `index.html` nela. A build produz
# `_generated/bibliotheca.html`, que é a interface completa num arquivo só,
# com os dados e as capas embutidos. Este script é a ponte entre as duas
# coisas, e não faz mais nada: não gera conteúdo, não transforma dado, não
# toma decisão. Se gerasse, seria uma segunda build, e haveria duas verdades.
#
# POR QUE `bibliotheca.html` E NÃO `artifact.html`. São o mesmo conteúdo, com
# embrulhos diferentes: `artifact.html` sai sem <head>, porque quem o publica
# acrescenta o seu próprio; `bibliotheca.html` é um documento HTML completo,
# com doctype, charset e viewport. Um navegador abrindo a URL direto precisa
# do documento completo — sem o charset declarado, todo acento vira ruído.
#
# O script não sabe que existe GitHub. Rodá-lo na sua máquina produz a mesma
# pasta, e `python3 -m http.server -d site` serve o site localmente, idêntico
# ao publicado. É isso que faz o Pages ser uma publicação do projeto, e não
# um lugar onde parte dele mora.
#
#   python3 tools/build.py && python3 tools/pages.py
# ---------------------------------------------------------------------------
import os, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GEN = os.path.join(ROOT, "_generated")
SITE = os.path.join(ROOT, "site")
FONTE = os.path.join(GEN, "bibliotheca.html")


def main():
    if not os.path.exists(FONTE):
        print("✖ _generated/bibliotheca.html não existe. Rode `python3 tools/build.py`.")
        return 1

    if os.path.isdir(SITE):
        shutil.rmtree(SITE)
    os.makedirs(SITE)

    destino = os.path.join(SITE, "index.html")
    shutil.copyfile(FONTE, destino)

    # Sem isto, o Pages passa a pasta pelo Jekyll, que ignora silenciosamente
    # arquivos e pastas começando por underscore. Hoje não há nenhum aqui, mas
    # o dia em que houver, a falha seria invisível: o arquivo simplesmente não
    # apareceria no site, sem erro nenhum.
    open(os.path.join(SITE, ".nojekyll"), "w").close()

    # Mantém a biblioteca fora dos resultados de busca. O site é público porque
    # o Pages não oferece outra coisa fora do plano Enterprise — não porque a
    # intenção seja divulgá-lo. Quem tem o endereço entra; buscadores não
    # indexam. É uma convenção respeitada, não uma trava.
    with open(os.path.join(SITE, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nDisallow: /\n")

    mb = os.path.getsize(destino) / (1024 * 1024)
    print("✓ site/ montado · index.html %.1f MB" % mb)
    if mb > 95:
        print("  AVISO: acima de 95 MB. O limite por arquivo do GitHub é 100 MiB")
        print("  e o site publicado não pode passar de 1 GB. As capas embutidas")
        print("  são o que mais pesa — ver README §11.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
