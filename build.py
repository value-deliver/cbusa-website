"""Generate carsbuyusa.com into docs/.

Standard library only -- no dependencies, no build toolchain. Run it, commit docs/, done.

    python build.py

Output goes to docs/ because GitHub Pages branch deploys only support the repository root or
/docs. Keeping the output in docs/ means spec/ stays unpublished, which is deliberate: internal
planning notes on a compliance site would be an unforced error.

Two invariants are enforced here rather than trusted to discipline:

  * Every language supplies exactly the same pages and the same block structure. If a translation
    gains or loses a section, the build fails rather than shipping three sites that describe
    subtly different businesses.
  * A fact that is None is omitted entirely, with a warning. "TBD" must never reach a page whose
    only purpose is verification.
"""

import html
import re
import shutil
from pathlib import Path

from content import DOMAIN, FACTS, LANG_ORDER, LANGS, PAGE_ORDER, SITE_URL

ROOT = Path(__file__).parent
OUT = ROOT / "docs"
YEAR = 2026  # bump at the turn of the year; deliberately not date-derived so builds are reproducible

# Order in which company facts appear, wherever they appear.
FACT_ORDER = ["legal_name", "address", "ein", "state", "dos_id", "incorporated"]
CONTACT_ORDER = ["email", "phone", "address", "hours"]

warnings: list[str] = []


# ---------------------------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------------------------

def esc(text: str) -> str:
    return html.escape(str(text), quote=True)


def url(lang: str, slug: str) -> str:
    """Root-absolute URL for a page. English sits at the root; others under /<lang>/."""
    prefix = "" if lang == "en" else f"/{lang}"
    return f"{prefix}/" if slug == "index" else f"{prefix}/{slug}.html"


def out_path(lang: str, slug: str) -> Path:
    return OUT / f"{slug}.html" if lang == "en" else OUT / lang / f"{slug}.html"


def fact_value(key: str) -> str | None:
    """Rendered HTML for one fact, or None if we don't have it yet."""
    value = FACTS.get(key)
    if value is None:
        return None
    if key == "address":
        return "<br>".join(esc(line) for line in value)
    if key == "email":
        return f'<a href="mailto:{esc(value)}">{esc(value)}</a>'
    if key == "phone":
        return f'<a href="tel:{re.sub(r"[^+0-9]", "", value)}">{esc(value)}</a>'
    return esc(value)


def fact_rows(lang: dict, keys: list[str]) -> str:
    labels = lang["fact_labels"]
    rows = []
    for key in keys:
        value = fact_value(key)
        if value is None:
            continue  # omitted, never "TBD"
        rows.append(
            f'      <div class="fact">\n'
            f'        <dt>{esc(labels[key])}</dt>\n'
            f'        <dd>{value}</dd>\n'
            f'      </div>'
        )
    return "\n".join(rows)


# ---------------------------------------------------------------------------------------------
# Blocks
# ---------------------------------------------------------------------------------------------

def render_block(block: dict, lang: dict) -> str:
    kind = block["type"]
    heading = f'    <h2>{esc(block["h2"])}</h2>\n' if block.get("h2") else ""

    if kind == "prose":
        paras = "\n".join(f"    <p>{esc(p)}</p>" for p in block["paras"])
        return f'  <section class="block prose">\n{heading}{paras}\n  </section>'

    if kind == "steps":
        numbered = block.get("numbered", False)
        items = []
        for i, (title, body) in enumerate(block["items"], start=1):
            items.append(
                f'      <li>\n'
                f'        <span class="step-num" aria-hidden="true">{i}</span>\n'
                f'        <div>\n'
                f'          <h3>{esc(title)}</h3>\n'
                f'          <p>{esc(body)}</p>\n'
                f'        </div>\n'
                f'      </li>'
            )
        css = "steps steps-stacked" if numbered else "steps steps-row"
        return (
            f'  <section class="block">\n{heading}'
            f'    <ol class="{css}">\n' + "\n".join(items) + "\n    </ol>\n  </section>"
        )

    if kind == "cards":
        items = "\n".join(
            f'      <div class="card">\n'
            f'        <h3>{esc(title)}</h3>\n'
            f'        <p>{esc(body)}</p>\n'
            f'      </div>'
            for title, body in block["items"]
        )
        return f'  <section class="block">\n{heading}    <div class="cards">\n{items}\n    </div>\n  </section>'

    if kind == "list":
        intro = f'    <p>{esc(block["intro"])}</p>\n' if block.get("intro") else ""
        items = "\n".join(f"      <li>{esc(item)}</li>" for item in block["items"])
        return (
            f'  <section class="block">\n{heading}{intro}'
            f'    <ul class="ticks">\n{items}\n    </ul>\n  </section>'
        )

    if kind == "facts":
        note = f'    <p class="note">{esc(block["note"])}</p>\n' if block.get("note") else ""
        return (
            f'  <section class="block">\n{heading}'
            f'    <dl class="facts">\n{fact_rows(lang, FACT_ORDER)}\n    </dl>\n{note}  </section>'
        )

    if kind == "contact":
        return (
            f'  <section class="block">\n{heading}'
            f'    <dl class="facts">\n{fact_rows(lang, CONTACT_ORDER)}\n    </dl>\n  </section>'
        )

    raise ValueError(f"unknown block type: {kind!r}")


# ---------------------------------------------------------------------------------------------
# Page
# ---------------------------------------------------------------------------------------------

def render_nav(lang_code: str, current: str) -> str:
    lang = LANGS[lang_code]
    links = []
    for slug in PAGE_ORDER:
        aria = ' aria-current="page"' if slug == current else ""
        links.append(f'<a href="{url(lang_code, slug)}"{aria}>{esc(lang["nav"][slug])}</a>')
    return "\n        ".join(links)


def render_lang_switch(lang_code: str, current: str) -> str:
    links = []
    for code in LANG_ORDER:
        other = LANGS[code]
        if code == lang_code:
            links.append(f'<span aria-current="true">{esc(other["short"])}</span>')
        else:
            links.append(
                f'<a href="{url(code, current)}" lang="{code}" '
                f'hreflang="{code}" title="{esc(other["label"])}">{esc(other["short"])}</a>'
            )
    return "\n        ".join(links)


def render_alternates(current: str) -> str:
    tags = [
        f'  <link rel="alternate" hreflang="{code}" href="{SITE_URL}{url(code, current)}">'
        for code in LANG_ORDER
    ]
    tags.append(f'  <link rel="alternate" hreflang="x-default" href="{SITE_URL}{url("en", current)}">')
    return "\n".join(tags)


def render_footer(lang_code: str) -> str:
    lang = LANGS[lang_code]
    return f"""  <footer>
    <div class="wrap footer-grid">
      <div>
        <h2>{esc(lang["footer_heading"])}</h2>
        <dl class="facts facts-compact">
{fact_rows(lang, FACT_ORDER + ["email", "phone"])}
        </dl>
      </div>
      <div class="footer-notes">
        <p>{esc(lang["footer_trademark"])}</p>
        <p class="copyright">&copy; {YEAR} {esc(FACTS["legal_name"])} {esc(lang["footer_rights"])}</p>
      </div>
    </div>
  </footer>"""


def render_page(lang_code: str, slug: str) -> str:
    lang = LANGS[lang_code]
    page = lang["pages"][slug]
    blocks = "\n\n".join(render_block(b, lang) for b in page["blocks"])
    title = f'{page["h1"]} — {FACTS["legal_name"]}' if slug != "index" else \
            f'{FACTS["legal_name"]} — {lang["tagline"]}'
    css_href = "/assets/site.css"

    return f"""<!doctype html>
<html lang="{lang_code}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(page["desc"])}">
  <link rel="canonical" href="{SITE_URL}{url(lang_code, slug)}">
{render_alternates(slug)}
  <link rel="stylesheet" href="{css_href}">
</head>
<body>
  <a class="skip" href="#main">{esc(lang["skip_link"])}</a>
  <header>
    <div class="wrap header-inner">
      <a class="brand" href="{url(lang_code, "index")}">
        <span class="brand-name">{esc(FACTS["legal_name"])}</span>
        <span class="brand-tag">{esc(lang["tagline"])}</span>
      </a>
      <nav class="nav" aria-label="{esc(lang["nav"]["index"])}">
        {render_nav(lang_code, slug)}
      </nav>
      <nav class="langs" aria-label="{esc(lang["lang_switch_label"])}">
        {render_lang_switch(lang_code, slug)}
      </nav>
    </div>
  </header>

  <main id="main" class="wrap">
  <div class="hero">
    <h1>{esc(page["h1"])}</h1>
    <p class="lead">{esc(page["lead"])}</p>
  </div>

{blocks}
  </main>

{render_footer(lang_code)}
</body>
</html>
"""


# ---------------------------------------------------------------------------------------------
# Structural checks
# ---------------------------------------------------------------------------------------------

def check_parity() -> None:
    """All three languages must describe the same business with the same structure."""
    reference = LANGS["en"]
    for code in LANG_ORDER:
        lang = LANGS[code]
        if set(lang["pages"]) != set(PAGE_ORDER):
            raise SystemExit(f"[{code}] pages {sorted(lang['pages'])} != {sorted(PAGE_ORDER)}")
        if set(lang["nav"]) != set(PAGE_ORDER):
            raise SystemExit(f"[{code}] nav labels do not cover every page")
        if set(lang["fact_labels"]) != set(reference["fact_labels"]):
            raise SystemExit(f"[{code}] fact labels differ from English")
        for slug in PAGE_ORDER:
            ours = lang["pages"][slug]["blocks"]
            theirs = reference["pages"][slug]["blocks"]
            if [b["type"] for b in ours] != [b["type"] for b in theirs]:
                raise SystemExit(f"[{code}] {slug}: block types differ from English")
            for a, b in zip(ours, theirs):
                if a["type"] in ("steps", "cards", "list") and len(a["items"]) != len(b["items"]):
                    raise SystemExit(
                        f"[{code}] {slug}: '{a['type']}' has {len(a['items'])} items, "
                        f"English has {len(b['items'])}"
                    )


def check_facts() -> None:
    for key in FACT_ORDER + CONTACT_ORDER:
        if FACTS.get(key) is None:
            warnings.append(f"fact '{key}' is not set — omitted from all pages")


# ---------------------------------------------------------------------------------------------
# Extras
# ---------------------------------------------------------------------------------------------

def write_sitemap() -> None:
    urls = "\n".join(
        f"  <url><loc>{SITE_URL}{url(code, slug)}</loc></url>"
        for code in LANG_ORDER
        for slug in PAGE_ORDER
    )
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n</urlset>\n",
        encoding="utf-8",
    )


def write_preview() -> None:
    """A single self-contained file stacking all three languages, for review before DNS.

    Not part of the deployed site -- docs/ never links to it, and it is excluded from the
    sitemap. It exists so the whole site, translations included, can be read and checked in one
    place before it goes live. It carries the site's own stylesheet rather than a second look,
    so what is reviewed here is what ships.
    """
    css = (ROOT / "assets" / "site.css").read_text(encoding="utf-8")

    missing = [k for k in FACT_ORDER + CONTACT_ORDER if FACTS.get(k) is None]
    missing_note = ""
    if missing:
        labels = ", ".join(LANGS["en"]["fact_labels"][k].lower() for k in missing)
        missing_note = (
            f'<p class="proof-missing"><strong>Not yet supplied:</strong> {esc(labels)}. '
            f"These are omitted from every page rather than shown as placeholders. "
            f"Send them over and they appear everywhere at once.</p>"
        )

    jump = " ".join(
        f'<a href="#lang-{code}">{esc(LANGS[code]["label"])}</a>' for code in LANG_ORDER
    )

    parts = []
    for code in LANG_ORDER:
        lang = LANGS[code]
        parts.append(
            f'<div class="proof-lang" id="lang-{code}"><span>{esc(lang["label"])}</span></div>'
        )
        for slug in PAGE_ORDER:
            page = lang["pages"][slug]
            blocks = "\n".join(render_block(b, lang) for b in page["blocks"])
            parts.append(
                f'<article class="proof-page" lang="{code}">\n'
                f'  <div class="proof-crumb">{esc(lang["nav"][slug])}</div>\n'
                f'  <div class="hero"><h1>{esc(page["h1"])}</h1>'
                f'<p class="lead">{esc(page["lead"])}</p></div>\n{blocks}\n</article>'
            )
        parts.append(
            f'<article class="proof-page proof-footer" lang="{code}">\n'
            f'  <div class="proof-crumb">{esc(lang["footer_heading"])}</div>\n'
            f'  <dl class="facts">\n{fact_rows(lang, FACT_ORDER + ["email", "phone"])}\n  </dl>\n'
            f'  <p class="note">{esc(lang["footer_trademark"])}</p>\n</article>'
        )

    (ROOT / "preview.html").write_text(
        f"""<title>Cars Buy USA Site Proof</title>
<style>
{css}
body {{ background: var(--bg-soft); }}
.proof {{ max-width: 62rem; margin: 0 auto; padding: 2.5rem 1.25rem 5rem; }}
.proof-intro {{
  background: var(--bg); border: 1px solid var(--line); border-radius: 10px;
  padding: 1.5rem 1.75rem; margin-bottom: 1rem;
}}
.proof-intro h1 {{ font-size: 1.35rem; letter-spacing: -.015em; margin-bottom: .75rem; }}
.proof-intro p {{ font-size: .92rem; color: var(--ink-soft); max-width: 46rem; }}
.proof-missing {{
  border-left: 3px solid var(--accent); background: var(--accent-soft);
  padding: .8rem 1rem; border-radius: 0 6px 6px 0; margin-top: 1rem !important;
}}
.proof-missing strong {{ color: var(--accent); }}
.proof-jump {{ display: flex; flex-wrap: wrap; gap: .5rem; margin-top: 1.25rem; }}
.proof-jump a {{
  font-size: .8rem; font-weight: 600; text-decoration: none; color: var(--accent);
  border: 1px solid var(--line); border-radius: 999px; padding: .3rem .85rem; background: var(--bg);
}}
.proof-jump a:hover {{ background: var(--accent-soft); }}
.proof-lang {{ margin: 3.5rem 0 0; border-top: 2px solid var(--accent); padding-top: .75rem; }}
.proof-lang span {{
  font: 700 .75rem/1 var(--sans); letter-spacing: .12em; text-transform: uppercase;
  color: var(--accent);
}}
.proof-page {{
  border: 1px solid var(--line); border-radius: 10px; padding: 1.5rem 1.75rem 2rem;
  margin: 1.25rem 0; background: var(--bg);
}}
.proof-crumb {{
  font: 700 .7rem/1 var(--sans); letter-spacing: .1em; text-transform: uppercase;
  color: var(--ink-soft); margin-bottom: 1rem;
}}
.proof-page .hero {{ padding: 0 0 .25rem; max-width: none; }}
.proof-page h1 {{ font-size: 1.5rem; }}
.proof-page .lead {{ font-size: 1rem; }}
.proof-page .block:first-of-type {{ border-top: 0; }}
.proof-footer {{ background: var(--bg-soft); }}
</style>
<div class="proof">
  <div class="proof-intro">
    <h1>Site proof — every page, all three languages</h1>
    <p>This is a review copy, not the live site. On <strong>carsbuyusa.com</strong> each of these
    is a separate page, with a shared header, navigation, language switcher, and a company-details
    footer repeated on all fifteen pages. The styling here is the site's own.</p>
    <p>Worth checking closely: the Ukrainian and Russian wording, and that the company details
    match your invoices exactly.</p>
    {missing_note}
    <div class="proof-jump">{jump}</div>
  </div>
{chr(10).join(parts)}
</div>
""",
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------------------------

def main() -> None:
    check_parity()
    check_facts()

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    (OUT / "assets").mkdir()

    for code in LANG_ORDER:
        if code != "en":
            (OUT / code).mkdir()
        for slug in PAGE_ORDER:
            path = out_path(code, slug)
            path.write_text(render_page(code, slug), encoding="utf-8")

    shutil.copy(ROOT / "assets" / "site.css", OUT / "assets" / "site.css")

    # GitHub Pages plumbing.
    (OUT / "CNAME").write_text(f"{DOMAIN}\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8"
    )
    write_sitemap()
    write_preview()

    count = len(LANG_ORDER) * len(PAGE_ORDER)
    print(f"built {count} pages into {OUT}")
    print(f"preview: {ROOT / 'preview.html'}")
    if warnings:
        print("\nnot yet supplied (omitted from the site, not shown as placeholders):")
        for w in warnings:
            print(f"  ! {w}")


if __name__ == "__main__":
    main()
