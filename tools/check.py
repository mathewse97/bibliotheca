#!/usr/bin/env python3
# ---------------------------------------------------------------------------
# PORTÃO DE INTEGRIDADE — o que decide se uma mudança pode entrar no main.
#
# `build.py` imprime os problemas e segue em frente, de propósito: ele é uma
# ferramenta de trabalho, e uma referência quebrada no meio de uma sessão é
# informação, não motivo para parar. O portão é outra coisa. Ele roda depois
# da build, lê o índice e devolve código de saída diferente de zero quando a
# biblioteca está em um estado que não deve virar main.
#
# POR QUE ELE LÊ `_generated/index.json`. O AGENT.md proíbe um AGENTE de se
# orientar pelo derivado, e a proibição continua inteira. Isto aqui não é um
# agente se orientando: é uma máquina conferindo o resultado da build que ela
# mesma acabou de rodar, no mesmo segundo, sem risco de estar lendo uma cópia
# atrasada. É a única leitura de `_generated/` que o projeto autoriza.
#
# A LÓGICA VIVE AQUI, e não dentro do arquivo de workflow do GitHub. Se o
# projeto sair do GitHub amanhã, este arquivo continua funcionando com um
# `python3 tools/check.py`; um portão escrito em YAML de workflow iria embora
# junto com a plataforma.
#
#   python3 tools/build.py && python3 tools/check.py
#
# Saída 0 = pode entrar. Saída 1 = não pode, e o motivo está impresso.
# ---------------------------------------------------------------------------
import io, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "_generated", "index.json")

# As condições que reprovam. Cada uma é um defeito que o próprio projeto já
# define como defeito em algum arquivo canônico — nenhuma regra nova nasce aqui.
BLOQUEIAM = [
    ("unreadable",
     "arquivo canônico que a build não conseguiu ler — o índice está incompleto"),
    ("issues",
     "problema de integridade: referência quebrada, cartão de decisão malformado "
     "ou mudança estrutural aplicada sem decisão registrada"),
]


def main():
    if not os.path.exists(INDEX):
        print("✖ índice ausente. Rode `python3 tools/build.py` antes.")
        return 1

    with io.open(INDEX, encoding="utf-8") as f:
        idx = json.load(f)

    c = idx.get("counts") or {}
    falhou = False

    for chave, descricao in BLOQUEIAM:
        n = c.get(chave) or 0
        if n:
            falhou = True
            print("✖ %s: %d — %s" % (chave, n, descricao))

    if falhou:
        print("")
        print("Detalhe dos problemas (até 20):")
        for it in (idx.get("issues") or [])[:20]:
            print("   !", it.get("kind"), it.get("where"), it.get("ref") or "")
        print("")
        print("O portão reprovou. Nada aqui é opinião de curadoria: são")
        print("defeitos estruturais. Corrija o arquivo canônico e rode a build")
        print("de novo.")
        return 1

    print("✓ integridade: %d obras · %d coleções · %d publicações · 0 problemas"
          % (c.get("works", 0), c.get("collections", 0), c.get("publications", 0)))

    # Sinais que NÃO reprovam, e é importante que não reprovem. Uma lacuna
    # stale significa que a biblioteca mudou e uma conclusão antiga precisa de
    # revisão humana — é exatamente o que o sistema existe para tornar visível,
    # e tratar isso como erro de build ensinaria a apagar o sinal para o verde
    # voltar.
    stale = c.get("gaps_stale") or 0
    abertas = c.get("proposals_open") or 0
    if stale or abertas:
        print("  aviso (não reprova): %d conclusão(ões) stale · %d proposta(s) "
              "estrutural(is) aberta(s)" % (stale, abertas))
    return 0


if __name__ == "__main__":
    sys.exit(main())
