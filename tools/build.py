#!/usr/bin/env python3
"""
build.py — camada gerada da Bibliotheca.

Lê os arquivos canônicos, deriva tudo o que é derivável, e escreve:
  _generated/index.json        o índice completo
  _generated/bibliotheca.html  a interface (arquivo único, abre localmente)
  _generated/artifact.html     a mesma interface no formato de artifact

Nada aqui é escrito à mão. Uma coleção nova aparece na interface por existir
em collections/ — não há nenhuma lista de coleções no código.

  python3 tools/build.py
"""
import os, re, json, glob, io, datetime
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GEN = os.path.join(ROOT, "_generated")


# --------------------------------------------------------------------------
# leitura
# --------------------------------------------------------------------------
def read(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()


# Cabeçalhos que falharam ao ser lidos. A build NÃO pode tratar isso como
# "arquivo sem dados": um arquivo canônico cujo cabeçalho não abre e fecha, ou
# cujo YAML não parseia, entra no índice como casca vazia e passa por todas as
# checagens — foi o que aconteceu em 2026-09-22, quando metade de um registro
# de obra foi destruída por uma expressão regular e a build fechou com
# `problemas 0`. A integridade referencial estava intacta porque não havia
# referência nenhuma a verificar.
FRONTMATTER_FAILURES = []


def frontmatter(path):
    """Devolve (dict, corpo markdown). Registra falha de leitura em vez de
    devolver um dicionário vazio em silêncio."""
    t = read(path)
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", t, re.S)
    if not m:
        FRONTMATTER_FAILURES.append((path, "cabeçalho não abre e fecha com ---"))
        return {}, t
    try:
        data = yaml.safe_load(m.group(1)) or {}
    except Exception as e:                       # YAML inválido não é dado vazio
        FRONTMATTER_FAILURES.append((path, "YAML inválido: %s" % type(e).__name__))
        return {}, m.group(2)
    if not isinstance(data, dict):
        FRONTMATTER_FAILURES.append((path, "cabeçalho não é um mapa YAML"))
        return {}, m.group(2)
    return data, m.group(2)


def load_yaml(path):
    return yaml.safe_load(read(path)) or {}


# --------------------------------------------------------------------------
# markdown mínimo (só o que os arquivos de review usam)
# --------------------------------------------------------------------------
def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def inline(s):
    s = esc(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\*\w])\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    return s


def md(text):
    out, i = [], 0
    lines = text.split("\n")
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        if ln.startswith("---") and set(ln.strip()) == {"-"}:
            out.append("<hr>")
            i += 1
            continue
        h = re.match(r"^(#{1,6})\s+(.*)$", ln)
        if h:
            lv = min(len(h.group(1)) + 1, 6)
            out.append("<h%d>%s</h%d>" % (lv, inline(h.group(2)), lv))
            i += 1
            continue
        if ln.lstrip().startswith("|") and i + 1 < len(lines) and re.match(
                r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            hdr = [c.strip() for c in ln.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            out.append('<div class="tw"><table><thead><tr>' +
                       "".join("<th>%s</th>" % inline(c) for c in hdr) +
                       "</tr></thead><tbody>" +
                       "".join("<tr>" + "".join("<td>%s</td>" % inline(c) for c in r) +
                               "</tr>" for r in rows) + "</tbody></table></div>")
            continue
        if ln.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i].lstrip(">").strip())
                i += 1
            out.append("<blockquote>%s</blockquote>" % inline(" ".join(buf)))
            continue
        if re.match(r"^\s*[-*]\s+", ln):
            buf = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                buf.append(re.sub(r"^\s*[-*]\s+", "", lines[i]))
                i += 1
            out.append("<ul>" + "".join("<li>%s</li>" % inline(b) for b in buf) + "</ul>")
            continue
        if re.match(r"^\s*\d+\.\s+", ln):
            buf = []
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i]):
                buf.append(re.sub(r"^\s*\d+\.\s+", "", lines[i]))
                i += 1
            out.append("<ol>" + "".join("<li>%s</li>" % inline(b) for b in buf) + "</ol>")
            continue
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(
                r"^(#{1,6}\s|\s*[-*]\s|\s*\d+\.\s|>|\|)", lines[i]):
            buf.append(lines[i].strip())
            i += 1
        if buf:
            out.append("<p>%s</p>" % inline(" ".join(buf)))
    return "\n".join(out)


# --------------------------------------------------------------------------
# REVALIDAÇÃO — predicados verificáveis sobre a evidência das lacunas.
#
# Uma conclusão curatorial guardada só em prosa envelhece em silêncio: a frase
# "zero fontes primárias" continua a ser exibida como achado atual muito depois
# de deixar de ser verdade. Cada `check` é reexecutado a cada build; quando
# deixa de valer, a lacuna é marcada `stale` no ÍNDICE — nunca nos arquivos
# canônicos, que a build não escreve. A prosa é sempre preservada.
# --------------------------------------------------------------------------
def _cmp(actual, expect):
    if isinstance(expect, dict):
        for op, v in expect.items():
            if op == "eq" and not actual == v: return False
            if op == "ne" and not actual != v: return False
            if op == "gt" and not actual > v: return False
            if op == "gte" and not actual >= v: return False
            if op == "lt" and not actual < v: return False
            if op == "lte" and not actual <= v: return False
        return True
    return actual == expect


def _members(idx, cid, after=None, before=None):
    """Membros de uma coleção, opcionalmente só os que ficam ENTRE duas obras."""
    col = idx["collections"].get(cid) or {}
    ms = [s for s in (col.get("sequence") or []) if s.get("kind") == "work"]
    if after:
        i = next((k for k, s in enumerate(ms) if s["work"] == after), None)
        ms = ms[i + 1:] if i is not None else []
    if before:
        j = next((k for k, s in enumerate(ms) if s["work"] == before), None)
        ms = ms[:j] if j is not None else ms
    return ms


def _match(idx, entry, where):
    """`where` casa campos da PARTICIPAÇÃO (role, demand, core) ou da OBRA."""
    w = idx["works"].get(entry.get("work")) or {}
    for k, v in (where or {}).items():
        val = entry[k] if k in entry else w.get(k)
        if isinstance(val, list):
            if v not in val: return False
        elif val != v:
            return False
    return True


def _regions(idx, cid):
    col = idx["collections"].get(cid) or {}
    return ((col.get("scope_map") or {}).get("regions") or [])


def _region_field(r, f):
    # tolera o esquema antigo, em que `coverage` se chamava `status`
    if f == "coverage" and "coverage" not in r and "status" in r:
        return r["status"]
    return r.get(f)


def _tensions(idx, cid):
    col = idx["collections"].get(cid) or {}
    t = col.get("tensions")
    if isinstance(t, dict): return t.get("pairs") or []
    return t or []


def run_check(chk, idx):
    """-> {ok: bool|None, actual, expect, error?}"""
    try:
        t = chk.get("type")
        if t == "count_members":
            ms = _members(idx, chk["collection"], chk.get("after"), chk.get("before"))
            n = len([m for m in ms if _match(idx, m, chk.get("where"))])
            return {"ok": _cmp(n, chk.get("expect")), "actual": n, "expect": chk.get("expect")}
        if t == "region":
            r = next((x for x in _regions(idx, chk["collection"])
                      if x.get("id") == chk["region"]), None)
            if r is None:
                return {"ok": False, "actual": "região inexistente", "expect": chk.get("expect")}
            got = {k: _region_field(r, k) for k in (chk.get("expect") or {})}
            ok = all(got[k] == v for k, v in (chk.get("expect") or {}).items())
            return {"ok": ok, "actual": got, "expect": chk.get("expect")}
        if t == "region_count":
            rs = _regions(idx, chk["collection"])
            n = len([r for r in rs if all(_region_field(r, k) == v
                                          for k, v in (chk.get("where") or {}).items())])
            return {"ok": _cmp(n, chk.get("expect")), "actual": n, "expect": chk.get("expect")}
        if t == "member_present":
            ids = [m["work"] for m in _members(idx, chk["collection"])]
            got = chk["work"] in ids
            exp = chk.get("expect", True)
            return {"ok": got == exp, "actual": got, "expect": exp}
        if t == "count_tensions":
            n = len(_tensions(idx, chk["collection"]))
            return {"ok": _cmp(n, chk.get("expect")), "actual": n, "expect": chk.get("expect")}
        if t == "tension_present":
            pairs = _tensions(idx, chk["collection"])
            a, b = chk["a"], chk["b"]
            got = any((p.get("a"), p.get("b")) in ((a, b), (b, a)) for p in pairs)
            exp = chk.get("expect", True)
            return {"ok": got == exp, "actual": got, "expect": exp}
        if t == "relation_count":
            w = idx["works"].get(chk["from"]) or {}
            types = chk.get("types")
            n = len([r for r in (w.get("relations") or [])
                     if isinstance(r, dict) and r.get("target") == chk["to"]
                     and (not types or r.get("type") in types)])
            return {"ok": _cmp(n, chk.get("expect")), "actual": n, "expect": chk.get("expect")}
        return {"ok": None, "error": "tipo de check desconhecido: %s" % t}
    except Exception as e:                                   # nunca derruba a build
        return {"ok": None, "error": "%s: %s" % (type(e).__name__, e)}


def revalidate(gap, idx, today):
    """Anota a lacuna com o resultado. Não escreve em nenhum arquivo canônico."""
    out, any_checked, any_failed = [], False, False
    for ev in (gap.get("evidence") or []):
        if isinstance(ev, str):                              # esquema antigo: só prosa
            out.append({"claim": ev, "checkable": False,
                        "reason": "evidência em prosa, sem predicado"})
            continue
        chk = ev.get("check")
        if chk is None:
            out.append({"claim": ev.get("claim"), "checkable": False,
                        "reason": ev.get("reason") or "sem predicado declarado"})
            continue
        checks = chk if isinstance(chk, list) else [chk]
        res = [dict(c, **run_check(c, idx)) for c in checks]
        holds = all(r.get("ok") is True for r in res)
        any_checked = True
        any_failed = any_failed or not holds
        out.append({"claim": ev.get("claim"), "checkable": True,
                    "holds": holds, "checks": res})
    gap["revalidation"] = {
        "checked": today,
        "status": ("stale" if any_failed else "current") if any_checked else "unverifiable",
        "evidence": out,
    }
    return gap


# --------------------------------------------------------------------------
# CAPA E AQUISIÇÃO — propriedades da PUBLICAÇÃO, nunca da obra.
#
# Aquisição não é evidência bibliográfica: vendedores são tier 6–7 e
# estabelecem apenas que o livro existe e pode ser comprado. Nada aqui toca
# `verdict`, prioridade ou qualquer juízo curatorial.
#
# O campo que impede a fabricação é `match_basis`: um anúncio só significa
# algo se soubermos COMO se sabe que é desta edição. `unconfirmed` guarda a
# pista e marca a entrada como não acionável.
# --------------------------------------------------------------------------
import base64, mimetypes


def _freshness(checked, cfg, today):
    if not checked:
        return "unchecked", None
    try:
        d = checked if isinstance(checked, datetime.date) else \
            datetime.date.fromisoformat(str(checked)[:10])
    except Exception:
        return "unchecked", None
    days = (datetime.date.fromisoformat(today) - d).days
    th = (cfg or {}).get("freshness_days") or {}
    if days <= (th.get("fresh") or 90):
        return "fresh", days
    if days <= (th.get("aging") or 365):
        return "aging", days
    return "stale", days


def process_acquisition(pub, pid, idx, issues):
    cfg = idx.get("config_acquisition") or {}
    today = idx["built"]
    retailers = cfg.get("retailers") or {}
    bases = cfg.get("match_basis") or {}
    ccfg = cfg.get("cover") or {}

    # ---- aquisição ----
    out = []
    for a in (pub.get("acquisition") or []):
        if not isinstance(a, dict):
            continue
        r = a.get("retailer")
        if r not in retailers:
            issues.append({"kind": "aquisicao-vendedor-desconhecido", "where": pid, "ref": r})
        mb = a.get("match_basis")
        if a.get("url") and not mb:
            issues.append({"kind": "aquisicao-sem-base-de-correspondencia",
                           "where": pid, "ref": a.get("url")})
        if mb and mb not in bases:
            issues.append({"kind": "aquisicao-base-invalida", "where": pid, "ref": mb})
        if a.get("url") and not a.get("checked"):
            issues.append({"kind": "aquisicao-sem-data-de-verificacao",
                           "where": pid, "ref": a.get("url")})
        a["actionable"] = bool((bases.get(mb) or {}).get("actionable"))
        a["retailer_name"] = (retailers.get(r) or {}).get("name") or r
        a["source_tier"] = (retailers.get(r) or {}).get("source_tier")
        a["freshness"], a["days_since_check"] = _freshness(a.get("checked"), cfg, today)
        out.append(a)
    pub["acquisition"] = out

    # ---- capa ----
    cov = pub.get("cover")
    if not cov:
        return                      # ausência de capa NÃO é problema
    for k in (ccfg.get("required_fields") or ["file", "source", "source_type", "checked"]):
        if not cov.get(k):
            issues.append({"kind": "capa-campo-obrigatorio-ausente", "where": pid, "ref": k})
    if cov.get("represents") not in (None, ccfg.get("represents") or "publication"):
        issues.append({"kind": "capa-representa-valor-invalido",
                       "where": pid, "ref": cov.get("represents")})
    cov.setdefault("represents", "publication")
    path = os.path.join(ROOT, str(cov.get("file") or ""))
    if not cov.get("file") or not os.path.exists(path):
        issues.append({"kind": "capa-arquivo-inexistente", "where": pid, "ref": cov.get("file")})
        return
    size = os.path.getsize(path)
    cov["bytes"] = size
    cov["freshness"], cov["days_since_check"] = _freshness(cov.get("checked"), cfg, today)
    cap = ccfg.get("embed_max_bytes") or 400000
    disp = _display_copy(path, ccfg.get("display_max_height"))
    if disp:                        # cópia leve só para a tela; o arquivo em covers/ não muda
        cov["data_uri"] = "data:image/webp;base64,%s" % base64.b64encode(disp).decode()
        cov["embedded"] = True
        cov["display_copy"] = True
    elif size <= cap:
        mime = mimetypes.guess_type(path)[0] or "image/jpeg"
        with open(path, "rb") as fh:
            cov["data_uri"] = "data:%s;base64,%s" % (mime, base64.b64encode(fh.read()).decode())
        cov["embedded"] = True
    else:
        cov["embedded"] = False
        cov["relative_path"] = "../" + str(cov.get("file"))
        issues.append({"kind": "capa-grande-demais-para-embutir", "where": pid,
                       "ref": "%d bytes > %d" % (size, cap)})


def _display_copy(path, max_h):
    """Cópia leve da capa para embutir na interface (config/acquisition.yaml,
    cover.display_max_height — decisão do Mathews, 2026-09-25). O original em
    covers/ fica intacto. Sem Pillow instalado, devolve None e a build embute o
    original, como antes."""
    if not max_h:
        return None
    try:
        from PIL import Image
        import io
    except ImportError:
        return None
    im = Image.open(path)
    im = im.convert("RGB")
    if im.height > max_h:
        im = im.resize((max(1, round(im.width * max_h / im.height)), max_h), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=80, method=4)
    return buf.getvalue()


def _pillow_available():
    try:
        import PIL  # noqa: F401
        return True
    except ImportError:
        return False


def _collection_image(d, cid, issues):
    """Foto de fundo do cartão da coleção (config/interface-rules.md §5).
    Fornecida pelo Mathews; sem foto, a interface usa o mosaico das capas."""
    img = d.get("image")
    if not img:
        return
    if not isinstance(img, dict) or not img.get("file"):
        issues.append({"kind": "imagem-colecao-campo-obrigatorio-ausente", "where": cid, "ref": "file"})
        d.pop("image", None)
        return
    path = os.path.join(ROOT, str(img["file"]))
    if not os.path.exists(path):
        issues.append({"kind": "imagem-colecao-arquivo-inexistente", "where": cid, "ref": img["file"]})
        d.pop("image", None)
        return
    mime = mimetypes.guess_type(path)[0] or "image/webp"
    with open(path, "rb") as fh:
        img["data_uri"] = "data:%s;base64,%s" % (mime, base64.b64encode(fh.read()).decode())


# --------------------------------------------------------------------------
# índice
# --------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# SANIDADE DOS CARTÕES DE DECISÃO — acrescentado em 2026-09-27.
#
# Nasceu de um defeito real: o botão "Responder" copiava para a conversa a
# frase "opção X" mesmo quando o que havia sido escolhido era uma EDIÇÃO, e
# nos cartões de edição não existe opção nenhuma com aquela letra. A resposta
# colada apontava para algo que não existia no arquivo. O template foi
# corrigido; estas checagens existem para que a classe não volte por outro
# caminho — um cartão sem nada para clicar, sem recomendação, ou decidido sem
# registro do que foi decidido.
# ---------------------------------------------------------------------------
def _check_decision_card(x, issues):
    cid = x.get("id"); st = x.get("state")
    ops = x.get("options") or []; eds = x.get("editions") or []
    chaves = [o.get("key") for o in ops if o.get("key")]
    if st == "decidir":
        if not ops and not eds:
            issues.append({"kind": "cartao-sem-escolha", "where": cid,
                           "ref": "nada para clicar: nem opções nem edições"})
        if ops and not any(o.get("recommended") for o in ops) and not x.get("recommendation"):
            issues.append({"kind": "cartao-sem-recomendacao", "where": cid,
                           "ref": "nem opção recomendada, nem declaração de que a decisão é dele"})
        esperado = [chr(ord("A") + i) for i in range(len(chaves))]
        if chaves and chaves != esperado:
            issues.append({"kind": "cartao-letras-fora-de-ordem", "where": cid,
                           "ref": "opções %s; esperado %s" % (chaves, esperado)})
    if st == "decidida" and not x.get("decided"):
        issues.append({"kind": "cartao-decidido-sem-registro", "where": cid,
                       "ref": "state decidida sem bloco decided"})
    if st == "aguardando" and not x.get("waiting_for"):
        issues.append({"kind": "cartao-aguardando-sem-motivo", "where": cid,
                       "ref": "state aguardando sem waiting_for"})


def build():
    issues = []
    idx = {
        "built": datetime.date.today().isoformat(),
        "authors": {}, "works": {}, "collections": {}, "publications": {},
        "gaps": [], "proposals": [], "reviews": [],
        "state": {"works": {}, "publications": {}},
        "config": {}, "issues": issues,
    }

    p = os.path.join(ROOT, "config/writable-fields.yaml")
    if os.path.exists(p):
        idx["config"] = load_yaml(p)

    p = os.path.join(ROOT, "config/structural-proposals.yaml")
    if os.path.exists(p):
        idx["config_structural"] = load_yaml(p)

    p = os.path.join(ROOT, "config/acquisition.yaml")
    if os.path.exists(p):
        idx["config_acquisition"] = load_yaml(p)

    p = os.path.join(ROOT, "state/personal.yaml")
    if os.path.exists(p):
        st = load_yaml(p) or {}
        idx["state"] = {"works": st.get("works") or {},
                        "publications": st.get("publications") or {}}

    p = os.path.join(ROOT, "people/authors.yaml")
    if os.path.exists(p):
        for aid, a in (load_yaml(p) or {}).items():
            a = a or {}
            a.update({"id": aid, "works": []})
            idx["authors"][aid] = a

    # ---- obras -----------------------------------------------------------
    for f in sorted(glob.glob(os.path.join(ROOT, "works/*.md"))):
        d, body = frontmatter(f)
        wid = d.get("id") or os.path.basename(f)[:-3]
        d["id"] = wid
        d["body_html"] = md(body)
        d["memberships"] = []
        d["publications"] = []
        d["relations_in"] = []
        d.setdefault("authors", [])
        if not d["authors"] and d.get("author"):
            d["authors"] = [d["author"]]
        d.setdefault("relations", [])
        # CASCA VAZIA: registro que não tem autor, nem título original, nem
        # proveniência, nem procedência. Sete obras do acervo são legitimamente
        # anônimas (Bíblia, Gilgámesh, Corpus Hermeticum…) e TODAS trazem título
        # original e procedência — por isso a checagem exige a ausência de tudo,
        # e não só a de autor. Sinalizar as anônimas seria ruído, e uma lista de
        # problemas com ruído deixa de ser lida.
        if (not d["authors"] and not d.get("title_original")
                and not (d.get("provenance") or []) and not d.get("derived_from")):
            issues.append({"kind": "registro-vazio", "where": wid,
                           "ref": "sem autor, título original, proveniência ou procedência"})
        idx["works"][wid] = d
        for aid in d["authors"]:
            if aid in idx["authors"]:
                idx["authors"][aid]["works"].append(wid)
            else:
                issues.append({"kind": "autor-desconhecido", "where": wid, "ref": aid})

    # ---- coleções --------------------------------------------------------
    for f in sorted(glob.glob(os.path.join(ROOT, "collections/*.md"))):
        d, body = frontmatter(f)
        cid = d.get("id") or os.path.basename(f)[:-3]
        d["id"] = cid
        d["body_html"] = md(body)
        seq, movement, n = [], None, 0
        for e in (d.get("sequence") or []):
            if not isinstance(e, dict):
                continue
            if "movement" in e:
                movement = e["movement"]
                seq.append({"kind": "movement", **e})
            elif "work" in e:
                n += 1
                wid = e["work"]
                entry = {"kind": "work", "n": n, "movement": movement, **e}
                seq.append(entry)
                w = idx["works"].get(wid)
                if not w:
                    issues.append({"kind": "obra-inexistente", "where": cid, "ref": wid})
                    continue
                w["memberships"].append({
                    "collection": cid, "collection_title": d.get("title_pt", cid),
                    "n": n, "movement": movement,
                    "role": e.get("role"), "demand": e.get("demand"),
                    "core": bool(e.get("core")), "scope": e.get("scope"),
                    "why_here": e.get("why_here"), "why_here_by": e.get("why_here_by"),
                    "requires": e.get("requires") or [],
                    "publication_pref": e.get("publication_pref"),
                    "edition_pref": e.get("edition_pref"),
                    "perspective": e.get("perspective"),
                })
        d["sequence"] = seq
        d["member_count"] = n
        for pth in (d.get("paths") or []):
            for wid in (pth.get("works") or []):
                if wid not in idx["works"]:
                    issues.append({"kind": "obra-inexistente-em-caminho",
                                   "where": "%s/%s" % (cid, pth.get("id")), "ref": wid})
        _collection_image(d, cid, issues)
        idx["collections"][cid] = d

    # ---- publicações -----------------------------------------------------
    for f in sorted(glob.glob(os.path.join(ROOT, "publications/*.md"))):
        if os.path.basename(f).startswith("_"):
            continue
        d, body = frontmatter(f)
        pid = d.get("id") or os.path.basename(f)[:-3]
        process_acquisition(d, pid, idx, issues)
        d["id"] = pid
        d["body_html"] = md(body)
        for c in (d.get("contains") or []):
            wid = c.get("work")
            w = idx["works"].get(wid)
            if not w:
                issues.append({"kind": "obra-inexistente-em-publicacao",
                               "where": pid, "ref": wid})
                continue
            w["publications"].append({"publication": pid,
                                      "title_as_published": d.get("title_as_published"),
                                      "publisher": d.get("publisher"),
                                      "year": d.get("year"), **c})
        idx["publications"][pid] = d

    # ---- edição de exibição (DERIVADA — nunca um campo digitado) ---------
    # Regra aprovada pelo Mathews em 2026-09-18 ("versão marcada"):
    #   1. `publication_pref` da participação → escolha DAQUELA coleção;
    #   2. publicação cujo veredito para esta obra é `recommended`;
    #   3. publicação única registrada → mostrada ATENUADA, `unassessed`;
    #   4. nada, ou ambiguidade entre várias sem veredito → sem capa.
    # A obra continua sem capa e sem edição: isto é exibição, não dado.
    # PRECEDÊNCIA (decisão do Mathews, 2026-09-22): posse → preferência da
    # coleção → veredito → publicação única.
    # AJUSTE (pedido do Mathews, 2026-10-10): no nível da OBRA (catálogo,
    # autor, busca) a ordem é posse → veredito → edição escolhida para uma
    # coleção (`publication_pref`, a da primeira participação que tiver) →
    # publicação única → a de acesso mais fácil (língua na ordem pt, es, it,
    # en; em catálogo; com anúncio). Antes, uma escolha feita por cartão de
    # decisão só aparecia dentro da coleção e a obra ficava sem capa no resto
    # da interface. As duas últimas saem ATENUADAS: não são escolha dele.
    # A razão: uma edição que ele TEM é por onde ele lê a obra, independentemente
    # de qual é a melhor. Posse é fato sobre a estante; veredito é juízo sobre a
    # edição. O juízo não desloca o fato.
    # `tenho` é o único valor que conta como posse — `encomendado` ainda não
    # chegou, `quero-comprar` é intenção (config/writable-fields.yaml).
    pstate = (idx.get("state") or {}).get("publications") or {}

    def _owned(pubs):
        """Publicações desta obra que ele possui, em ordem estável."""
        return sorted([p["publication"] for p in pubs
                       if (pstate.get(p["publication"]) or {}).get("ownership") == "tenho"])

    def _pref_de(wid, w):
        """Edição escolhida para a obra numa coleção, se houver uma válida."""
        for m in w["memberships"]:
            pref = m.get("publication_pref")
            pub = idx["publications"].get(pref) if pref else None
            if not pub:
                continue
            c = next((c for c in (pub.get("contains") or []) if c.get("work") == wid), None)
            if c is not None:
                return {"publication": pref,
                        "state": "chosen" if c.get("verdict") == "recommended" else "unassessed",
                        "by_collection": True}
        return None

    LANG_ORDER = ["pt", "es", "it", "en"]

    def _acesso(pid):
        """Chave de ordenação: mais acessível primeiro (língua, catálogo, anúncio)."""
        pub = idx["publications"].get(pid) or {}
        lang = (pub.get("language") or "").split("-")[0]
        li = LANG_ORDER.index(lang) if lang in LANG_ORDER else len(LANG_ORDER)
        return (li, pub.get("language") != "pt-BR",
                pub.get("availability_br") != "em-catalogo",
                not pub.get("acquisition"), pid)

    for wid, w in idx["works"].items():
        own = _owned(w["publications"])
        rec = [p for p in w["publications"] if p.get("verdict") == "recommended"]
        if own:
            # Mais de uma possuída: a recomendada entre elas desempata; senão a
            # primeira em ordem estável, para que a build seja reproduzível.
            recset = {p["publication"] for p in rec}
            pick = next((o for o in own if o in recset), own[0])
            w["display_edition"] = {"publication": pick, "state": "chosen",
                                    "by_ownership": True}
        elif rec:
            w["display_edition"] = {"publication": rec[0]["publication"], "state": "chosen"}
        elif _pref_de(wid, w):
            w["display_edition"] = _pref_de(wid, w)
        elif len(w["publications"]) == 1:
            w["display_edition"] = {"publication": w["publications"][0]["publication"],
                                    "state": "unassessed"}
        elif w["publications"]:
            pick = min((p["publication"] for p in w["publications"]), key=_acesso)
            w["display_edition"] = {"publication": pick, "state": "unassessed",
                                    "by_access": True}
        else:
            w["display_edition"] = None
        for m in w["memberships"]:
            # Posse vence também a preferência da coleção: a preferência diz por
            # onde esta coleção lê a obra, a posse diz por onde ele a lê de fato.
            if own:
                m["display_edition"] = w["display_edition"]
                continue
            pref = m.get("publication_pref")
            if not pref:
                m["display_edition"] = w["display_edition"]
                continue
            pub = idx["publications"].get(pref)
            if not pub or not any(c.get("work") == wid for c in (pub.get("contains") or [])):
                issues.append({"kind": "publication-pref-nao-contem-a-obra",
                               "where": "%s/%s" % (m["collection"], wid), "ref": pref})
                m["display_edition"] = w["display_edition"]
                continue
            verd = next((c.get("verdict") for c in pub["contains"] if c.get("work") == wid), None)
            m["display_edition"] = {"publication": pref,
                                    "state": "chosen" if verd == "recommended" else "unassessed",
                                    "by_collection": True}

    # ---- relações inversas ----------------------------------------------
    INV = {"prerequisite_for": "requires", "responds_to": "answered_by",
           "criticizes": "criticized_by", "continues": "continued_by",
           "influenced_by": "influenced", "same_tradition_as": "same_tradition_as",
           "opposing_tradition_to": "opposing_tradition_to",
           "complements": "complements", "literary_treatment_of": "treated_literarily_by",
           "primary_source_for": "interprets", "commentary_on": "has_commentary",
           "part_of": "has_part"}
    for wid, w in idx["works"].items():
        for r in w["relations"]:
            if not isinstance(r, dict):
                continue
            t = idx["works"].get(r.get("target"))
            if not t:
                issues.append({"kind": "relacao-pendente", "where": wid,
                               "ref": r.get("target")})
                continue
            t["relations_in"].append({"type": INV.get(r.get("type"), r.get("type")),
                                      "original_type": r.get("type"),
                                      "target": wid, "note": r.get("note")})

    # ---- lacunas ---------------------------------------------------------
    for f in sorted(glob.glob(os.path.join(ROOT, "review/gaps/*.yaml"))):
        d = load_yaml(f)
        for g in (d.get("gaps") or []):
            g["collection"] = d.get("collection")
            idx["gaps"].append(g)
        if d.get("coverage"):
            c = idx["collections"].get(d.get("collection"))
            if c:
                c["coverage_note"] = d["coverage"]
        if d.get("memberships_not_gaps"):
            c = idx["collections"].get(d.get("collection"))
            if c:
                c["memberships_not_gaps"] = d["memberships_not_gaps"]
        if d.get("settled"):
            c = idx["collections"].get(d.get("collection"))
            if c:
                c["settled"] = d["settled"]

    # ---- propostas estruturais -------------------------------------------
    # Nível da COLEÇÃO: pergunta, escopo, nome, ou a suposição de que aquele
    # conjunto é uma coleção só. Ver config/structural-proposals.yaml.
    # A build não aplica nada; garante que nada foi aplicado sem decisão.
    spc = idx.get("config_structural") or {}
    TYPES = list((spc.get("types") or {}).keys()) or ["refine", "rename", "split", "merge"]
    STATUSES = list((spc.get("statuses") or {}).keys()) or ["open", "approved", "rejected"]
    REQ = spc.get("required_fields") or ["id", "type", "affects", "statement", "status"]
    APPROVER = ((spc.get("approval") or {}).get("approver")) or "voce"
    seen_ids = set()

    # ---- decisões (tela "Decisões", interface-rules §7) --------------------
    dpath = os.path.join(ROOT, "review/decisions.yaml")
    if os.path.exists(dpath):
        dd = yaml.safe_load(read(dpath)) or {}
        idx["decisions"] = [x for x in (dd.get("items") or []) if isinstance(x, dict)]
        for x in idx["decisions"]:
            for k in ("work",):
                if x.get(k) and x[k] not in idx["works"]:
                    issues.append({"kind": "decisao-obra-inexistente", "where": x.get("id"), "ref": x[k]})
            for e in (x.get("editions") or []):
                if e.get("pub") and e["pub"] not in idx["publications"]:
                    issues.append({"kind": "decisao-publicacao-inexistente", "where": x.get("id"), "ref": e["pub"]})
            if isinstance((x.get("decided") or {}).get("date"), (datetime.date,)):
                x["decided"]["date"] = x["decided"]["date"].isoformat()
            _check_decision_card(x, issues)
    else:
        idx["decisions"] = []

    for f in sorted(glob.glob(os.path.join(ROOT, "review/structural/*.yaml"))):
        if os.path.basename(f).startswith(spc.get("ignored_prefix") or "_"):
            continue
        d = load_yaml(f) or {}
        for pr in (d.get(spc.get("record_key") or "proposals") or []):
            pr["source_file"] = os.path.relpath(f, ROOT)
            pid = pr.get("id") or "(sem id)"
            for k in REQ:
                if pr.get(k) in (None, "", []):
                    issues.append({"kind": "proposta-campo-obrigatorio-ausente",
                                   "where": pid, "ref": k})
            if pid in seen_ids:
                issues.append({"kind": "proposta-id-duplicado", "where": pid, "ref": None})
            seen_ids.add(pid)
            if pr.get("type") not in TYPES:
                issues.append({"kind": "proposta-tipo-invalido", "where": pid,
                               "ref": pr.get("type")})
            st = pr.get("status") or (spc.get("default_status") or "open")
            pr["status"] = st
            if st not in STATUSES:
                issues.append({"kind": "proposta-status-invalido", "where": pid, "ref": st})
            for cid in (pr.get("affects") or []):
                if cid not in idx["collections"]:
                    issues.append({"kind": "proposta-colecao-inexistente",
                                   "where": pid, "ref": cid})
            # o portão: nada decidido sem decisão registrada, e só ele decide
            if st in ("approved", "rejected"):
                dec = pr.get("decision") or {}
                if not dec:
                    issues.append({"kind": "proposta-sem-decisao", "where": pid, "ref": st})
                else:
                    for k in (spc.get("decision_fields") or ["by", "date", "rationale"]):
                        if not dec.get(k):
                            issues.append({"kind": "proposta-decisao-incompleta",
                                           "where": pid, "ref": k})
                    if dec.get("by") and dec.get("by") != APPROVER:
                        issues.append({"kind": "proposta-aprovada-por-nao-usuario",
                                       "where": pid, "ref": dec.get("by")})
            idx["proposals"].append(pr)

    approved_ids = {p["id"] for p in idx["proposals"]
                    if p.get("status") == "approved" and p.get("id")}

    # ---- linhagem e aliases de coleção -----------------------------------
    # Campos OPCIONAIS. Ausentes = vazios; nenhuma coleção os tem hoje e
    # nenhum dado histórico foi inventado.
    alias_owner = {}
    for cid, col in idx["collections"].items():
        col.setdefault("id_aliases", [])
        col.setdefault("lineage", [])
        for al in col["id_aliases"]:
            if al in idx["collections"] or al in alias_owner:
                issues.append({"kind": "alias-de-colecao-em-conflito",
                               "where": cid, "ref": al})
            alias_owner[al] = cid
        for ln in col["lineage"]:
            ref = (ln or {}).get("proposal")
            if not ref:
                issues.append({"kind": "linhagem-sem-proposta", "where": cid, "ref": None})
            elif ref not in approved_ids:
                # mudança estrutural aplicada sem proposta aprovada que a autorize
                issues.append({"kind": "linhagem-sem-proposta-aprovada",
                               "where": cid, "ref": ref})

    # ---- revalidação das conclusões --------------------------------------
    # Depois de tudo indexado: reexecuta a evidência de cada lacuna contra o
    # estado ATUAL da biblioteca. Detectar é automático; propor obras não é.
    for g in idx["gaps"]:
        revalidate(g, idx, idx["built"])
    for pr in idx["proposals"]:
        revalidate(pr, idx, idx["built"])

    # ---- prosa de revisão ------------------------------------------------
    for f in sorted(glob.glob(os.path.join(ROOT, "review/*.md"))):
        d, body = frontmatter(f)
        idx["reviews"].append({"collection": d.get("collection"),
                               "kind": d.get("kind"), "date": str(d.get("date")),
                               "status": d.get("status"),
                               "path": os.path.relpath(f, ROOT),
                               "body_html": md(body)})

    # ---- obras sem coleção ----------------------------------------------
    for wid, w in idx["works"].items():
        if not w["memberships"]:
            w["orphan"] = not bool(w.get("pending_assignment"))
            if w["orphan"]:
                issues.append({"kind": "obra-sem-colecao", "where": wid, "ref": None})

    idx["counts"] = {
        "works": len(idx["works"]), "collections": len(idx["collections"]),
        "publications": len(idx["publications"]),
        # `authors` conta quem ASSINA obra. Tradutores e estabelecedores de
        # texto vivem no mesmo arquivo por não haver outro lugar para pessoas
        # que não são autores, e são contados à parte — somá-los a autores fazia
        # a interface anunciar mais autores do que obras. Corrigido 2026-09-12.
        "authors": len([a for a in idx["authors"].values()
                        if (a.get("role") or "author") == "author" and a.get("works")]),
        "people": len(idx["authors"]),
        "translators": len([a for a in idx["authors"].values()
                            if (a.get("role") or "author") != "author"]),
        # Pesquisa da OBRA (data, gênero, tradição, relações) e existência de
        # EDIÇÃO são coisas diferentes. O painel antigo fundia as duas e por
        # isso negava trabalho que estava feito.
        "works_researched_any": len([w for w in idx["works"].values()
                                     if w.get("research_status") in
                                     ("partially_researched", "fully_researched")]),
        "works_with_publication": len({c["work"] for pb in idx["publications"].values()
                                       for c in (pb.get("contains") or [])
                                       if c.get("work") in idx["works"]}),
        "gaps_open": len([g for g in idx["gaps"] if g.get("status") == "open"]),
        "gaps_stale": len([g for g in idx["gaps"] + idx["proposals"]
                           if (g.get("revalidation") or {}).get("status") == "stale"]),
        "gaps_unverifiable": len([g for g in idx["gaps"] + idx["proposals"]
                                  if (g.get("revalidation") or {}).get("status") == "unverifiable"]),
        "covers": len([p for p in idx["publications"].values() if (p.get("cover") or {}).get("embedded")]),
        "acquisition_sources": sum(len(p.get("acquisition") or [])
                                   for p in idx["publications"].values()),
        "acquisition_stale": sum(1 for p in idx["publications"].values()
                                 for a in (p.get("acquisition") or [])
                                 if a.get("freshness") == "stale"),
        "proposals": len(idx["proposals"]),
        "proposals_open": len([p for p in idx["proposals"] if p.get("status") == "open"]),
        "proposals_approved": len([p for p in idx["proposals"] if p.get("status") == "approved"]),
        "proposals_rejected": len([p for p in idx["proposals"] if p.get("status") == "rejected"]),
        "checks_run": sum(len(e.get("checks") or [])
                          for g in idx["gaps"]
                          for e in (g.get("revalidation") or {}).get("evidence") or [])
                     + sum(len(e.get("checks") or [])
                           for p in idx["proposals"]
                           for e in (p.get("revalidation") or {}).get("evidence") or []),
        "researched": len([w for w in idx["works"].values()
                           if w.get("research_status") == "fully_researched"]),
        "pending_assignment": len([w for w in idx["works"].values()
                                   if w.get("pending_assignment")]),
        "issues": len(issues),
    }
    # Falhas de LEITURA entram como problema, e entram por último para que
    # nenhuma etapa anterior possa engoli-las. Um arquivo que não foi lido não
    # tem referências pendentes — é por isso que a checagem referencial sozinha
    # dá `problemas 0` sobre um registro destruído.
    for path, motivo in FRONTMATTER_FAILURES:
        issues.append({"kind": "cabecalho-ilegivel",
                       "where": os.path.relpath(path, ROOT), "ref": motivo})
    idx["counts"]["issues"] = len(issues)
    idx["counts"]["unreadable"] = len(FRONTMATTER_FAILURES)
    return idx


# --------------------------------------------------------------------------
def jdefault(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    return str(o)


def main():
    idx = build()
    os.makedirs(GEN, exist_ok=True)
    with io.open(os.path.join(GEN, "index.json"), "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False, indent=1, default=jdefault)

    tpl = read(os.path.join(ROOT, "tools/ui.template.html"))
    data = json.dumps(idx, ensure_ascii=False, default=jdefault).replace("</", "<\\/")
    page = tpl.replace("/*__DATA__*/null", data)

    # Favicon embutido, como as fontes e as capas: o documento continua sendo
    # um arquivo só. artifact.html não leva, porque quem o publica põe o head.
    fav = ""
    fav_path = os.path.join(ROOT, "images/favicon.svg")
    if os.path.exists(fav_path):
        with open(fav_path, "rb") as fh:
            fav = ("<link rel=\"icon\" type=\"image/svg+xml\" href=\"data:image/svg+xml;base64,%s\">\n"
                   % base64.b64encode(fh.read()).decode())
    with io.open(os.path.join(GEN, "bibliotheca.html"), "w", encoding="utf-8") as f:
        f.write("<!doctype html>\n<html lang=\"pt-BR\">\n<head>\n"
                "<meta charset=\"utf-8\">\n"
                "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
                + fav +
                "</head>\n<body>\n" + page + "\n</body>\n</html>\n")
    with io.open(os.path.join(GEN, "artifact.html"), "w", encoding="utf-8") as f:
        f.write(page)

    c = idx["counts"]
    print("obras %(works)d · coleções %(collections)d · publicações %(publications)d "
          "· autores %(authors)d · lacunas abertas %(gaps_open)d "
          "· pendentes %(pending_assignment)d · problemas %(issues)d" % c)
    print("aquisição: %(acquisition_sources)d fonte(s) · %(acquisition_stale)d desatualizada(s) "
          "· %(covers)d capa(s) embutida(s)" % c)
    print("propostas estruturais: %(proposals)d "
          "(abertas %(proposals_open)d · aprovadas %(proposals_approved)d "
          "· recusadas %(proposals_rejected)d)" % c)
    if not _pillow_available():
        print("   ⚠ Pillow ausente: as capas vão em tamanho original e a interface sai"
              " bem mais pesada (pip install -r requirements.txt)")
    print("revalidação: %(checks_run)d checks · %(gaps_stale)d lacuna(s) stale "
          "· %(gaps_unverifiable)d sem evidência verificável" % c)
    for g in idx["gaps"] + idx["proposals"]:
        rv = g.get("revalidation") or {}
        if rv.get("status") == "stale":
            print("   ~ STALE", g["id"])
            for e in rv.get("evidence") or []:
                if e.get("checkable") and not e.get("holds"):
                    for ch in e.get("checks") or []:
                        if ch.get("ok") is not True:
                            print("       %s: esperado %r, atual %r %s" % (
                                ch.get("type"), ch.get("expect"), ch.get("actual"),
                                ch.get("error") or ""))
    if idx["counts"].get("unreadable"):
        print("   ARQUIVO CANÔNICO NÃO LIDO — o índice está incompleto:")
        for path, motivo in FRONTMATTER_FAILURES:
            print("   ✖", os.path.relpath(path, ROOT), "—", motivo)
    for it in idx["issues"][:20]:
        print("   !", it["kind"], it["where"], it.get("ref") or "")


if __name__ == "__main__":
    main()
