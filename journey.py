"""The "How it works" journey: five inline-SVG scenes, one per step.

Markup only. Motion lives in assets/site.css ("journey" section) as CSS scroll-driven animations,
so the site still ships no JavaScript. Without scroll-driven animation support, or with reduced
motion requested, the same markup shows as a static grid of finished scenes; print hides it.

Every word drawn inside a scene comes from the page's "journey" block in content.py, so it is
translated like the rest of the copy. The caption on each scene is the matching step title.
"""

import html

# Labels every language must supply. build.py checks this.
LABEL_KEYS = [
    "budget", "budget_value", "vehicle", "vehicle_value", "destination", "destination_value",
    "auction", "sold", "title", "export", "cleared",
]


def _e(text: str) -> str:
    return html.escape(str(text), quote=True)


DEFS = """<svg width="0" height="0" class="j-defs" aria-hidden="true" focusable="false">
  <defs>
    <symbol id="j-car" viewBox="0 0 210 64" overflow="visible">
      <path d="M8 46 C8 39 13 35 22 34 L56 31 C70 21 88 14 106 13 L138 13 C153 13 166 20 178 29 L192 31 C199 32 202 37 202 43 L202 47 C202 49 200 50 198 50 L10 50 C9 50 8 49 8 47Z"/>
      <path d="M70 30 C80 22 92 18 106 18 L120 18 L120 30Z M125 18 L137 18 C148 18 158 23 168 30 L125 30Z" style="fill:var(--win,#2a3a52)"/>
      <circle cx="52" cy="50" r="13" style="fill:#0b121b"/><circle cx="164" cy="50" r="13" style="fill:#0b121b"/>
      <circle cx="52" cy="50" r="6" style="fill:var(--rim,#2a3a52)"/><circle cx="164" cy="50" r="6" style="fill:var(--rim,#2a3a52)"/>
    </symbol>
    <symbol id="j-person" viewBox="-14 -8 28 88" overflow="visible">
      <circle cx="0" cy="0" r="6.5"/>
      <path d="M-9 11 Q0 7 9 11 L11 46 L4 46 L3 78 L-1 78 L-1 48 L-3 78 L-7 78 L-5 46 L-11 46Z"/>
    </symbol>
    <linearGradient id="j-sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5a6a82"/><stop offset="1" stop-color="#1e2b3d"/></linearGradient>
    <linearGradient id="j-beam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff3d6" stop-opacity=".55"/><stop offset="1" stop-color="#fff3d6" stop-opacity=".05"/></linearGradient>
    <linearGradient id="j-head" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffe2b0" stop-opacity=".55"/><stop offset="1" stop-color="#ffe2b0" stop-opacity="0"/></linearGradient>
    <linearGradient id="j-spot" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff3d6" stop-opacity=".05"/><stop offset="1" stop-color="#fff3d6" stop-opacity=".5"/></linearGradient>
    <radialGradient id="j-glow"><stop offset="0" stop-color="#ffe9c4" stop-opacity=".9"/><stop offset="1" stop-color="#ffe9c4" stop-opacity="0"/></radialGradient>
  </defs>
</svg>"""


def _request(t: dict) -> str:
    return f"""<svg viewBox="0 0 640 300">
            <path d="M0 240 V200 h30 v-14 h26 v20 h40 v-30 h22 v24 h50 v-10 h30 v10 h60 v-22 h28 v22 h90 v-16 h40 v16 h70 v-28 h24 v28 h50 v-12 h50 V240Z" fill="#3a4a63" opacity=".45"/>
            <rect x="0" y="240" width="640" height="60" fill="#141e2b"/>
            <use href="#j-person" x="80" y="108" width="42" height="132" fill="#141e2b"/>
            <path d="M114 140 L128 132" stroke="#141e2b" stroke-width="5" stroke-linecap="round"/>
            <circle cx="132" cy="126" r="22" fill="url(#j-glow)"/>
            <rect x="127" y="118" width="9" height="15" rx="2" fill="#ffe9c4"/>
            <rect x="210" y="56" width="300" height="170" rx="14" fill="#ffffff" fill-opacity=".14" stroke="#ffffff" stroke-opacity=".5"/>
            <g font-size="10.5" fill="#ffffff" fill-opacity=".75" font-weight="700" letter-spacing="1.5">
              <text x="230" y="84">{_e(t["budget"])}</text><text x="230" y="132">{_e(t["vehicle"])}</text><text x="230" y="180">{_e(t["destination"])}</text>
            </g>
            <g fill="#ffffff" fill-opacity=".1" stroke="#ffffff" stroke-opacity=".35"><rect x="230" y="90" width="260" height="26" rx="6"/><rect x="230" y="138" width="260" height="26" rx="6"/><rect x="230" y="186" width="260" height="26" rx="6"/></g>
            <g font-size="14" fill="#ffffff" font-weight="600">
              <text class="j-a j-ty1" x="240" y="108">{_e(t["budget_value"])}</text><text class="j-a j-ty2" x="240" y="156">{_e(t["vehicle_value"])}</text><text class="j-a j-ty3" x="240" y="204">{_e(t["destination_value"])}</text>
            </g>
            <path class="j-a j-plane" d="M505 214 l30 -12 l-11 27 l-5 -11z" fill="#e7b46a"/>
          </svg>"""


def _auction(t: dict) -> str:
    return f"""<svg viewBox="0 0 640 300">
            <path d="M150 240 V140 L230 108 L410 108 L490 140 V240Z" fill="#3a4a63" opacity=".55"/>
            <rect x="256" y="111" width="128" height="24" rx="3" fill="#141e2b"/>
            <text x="320" y="128" font-size="12" font-weight="800" fill="#ffe2b0" text-anchor="middle" letter-spacing="3">{_e(t["auction"])}</text>
            <path class="j-a j-beam" d="M300 150 L340 150 L440 240 L200 240Z" fill="url(#j-beam)"/>
            <rect x="0" y="240" width="640" height="60" fill="#141e2b"/>
            <use href="#j-car" x="20" y="203" width="120" height="37" fill="#1e2b3d"/>
            <use href="#j-car" x="500" y="203" width="120" height="37" fill="#1e2b3d"/>
            <use href="#j-car" x="215" y="177" width="210" height="64" fill="#141e2b" style="--win:#3c5070;--rim:#5a6a82"/>
            <g class="j-a j-padl"><path d="M150 300 L156 190" stroke="#141e2b" stroke-width="7" stroke-linecap="round"/><circle cx="157" cy="172" r="20" fill="#2a3a52"/><text x="157" y="177" font-size="13" font-weight="700" text-anchor="middle" fill="#c9d3de">12</text></g>
            <g class="j-a j-padr"><path d="M490 300 L484 190" stroke="#141e2b" stroke-width="7" stroke-linecap="round"/><circle cx="483" cy="172" r="20" fill="#e7b46a"/><text x="483" y="177" font-size="13" font-weight="800" text-anchor="middle" fill="#141e2b">27</text></g>
            <g class="j-a j-sold">
              <circle cx="320" cy="161" r="60" fill="url(#j-glow)"/>
              <rect x="250" y="144" width="140" height="30" rx="6" fill="#e7b46a"/>
              <text x="320" y="165" font-size="16" font-weight="800" fill="#141e2b" text-anchor="middle" letter-spacing="1">{_e(t["sold"])} ✓</text>
            </g>
          </svg>"""


def _documents(t: dict) -> str:
    return f"""<svg viewBox="0 0 640 300">
            <path d="M400 240 V150 L500 116 L600 150 V240Z M412 160 h176 v6 h-176Z" fill="#3a4a63" opacity=".5"/>
            <g fill="#3a4a63" opacity=".5"><rect x="420" y="170" width="10" height="70"/><rect x="450" y="170" width="10" height="70"/><rect x="480" y="170" width="10" height="70"/><rect x="510" y="170" width="10" height="70"/><rect x="540" y="170" width="10" height="70"/><rect x="570" y="170" width="10" height="70"/></g>
            <rect x="0" y="240" width="640" height="60" fill="#141e2b"/>
            <use href="#j-car" x="24" y="191" width="160" height="49" fill="#141e2b" style="--win:#3c5070;--rim:#5a6a82"/>
            <rect x="206" y="56" width="150" height="176" rx="5" fill="#141e2b" opacity=".25"/>
            <rect x="200" y="50" width="150" height="176" rx="5" fill="#fbf5ea"/>
            <text x="275" y="78" font-size="9.5" font-weight="800" fill="#1b3a5c" text-anchor="middle" letter-spacing=".5">{_e(t["title"])}</text>
            <g fill="#e6dccb"><rect x="216" y="92" width="118" height="7" rx="3"/><rect x="216" y="107" width="90" height="7" rx="3"/><rect x="216" y="122" width="106" height="7" rx="3"/></g>
            <g class="j-a j-doc2">
              <rect x="306" y="78" width="160" height="164" rx="5" fill="#141e2b" opacity=".25"/>
              <rect x="300" y="72" width="160" height="164" rx="5" fill="#fffaf2"/>
              <text x="380" y="98" font-size="9.5" font-weight="800" fill="#1b3a5c" text-anchor="middle" letter-spacing=".5">{_e(t["export"])}</text>
              <g fill="#e6dccb"><rect x="316" y="112" width="128" height="7" rx="3"/><rect x="316" y="127" width="94" height="7" rx="3"/><rect x="316" y="142" width="112" height="7" rx="3"/></g>
              <g class="j-a j-stamp"><rect x="322" y="168" width="116" height="38" rx="5" fill="none" stroke="#1b3a5c" stroke-width="4"/><text x="380" y="193" font-size="14" font-weight="800" fill="#1b3a5c" text-anchor="middle">{_e(t["cleared"])}</text></g>
            </g>
            <circle cx="530" cy="78" r="30" fill="url(#j-glow)"/>
            <path class="j-a j-tick" d="M515 78 l11 11 l21 -22" fill="none" stroke="#e7b46a" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>"""


def _truck(t: dict) -> str:
    return """<svg viewBox="0 0 640 300">
            <path d="M0 240 V214 h40 v-8 h60 v8 h80 v-12 h50 v12 h120 V240Z" fill="#3a4a63" opacity=".45"/>
            <g fill="#1f2c3e">
              <rect x="470" y="96" width="9" height="144"/><rect x="530" y="96" width="9" height="144"/><rect x="440" y="88" width="200" height="11"/><rect x="474" y="118" width="62" height="6"/>
              <rect x="590" y="70" width="8" height="170"/><rect x="560" y="64" width="80" height="9"/>
              <rect x="560" y="200" width="80" height="40"/><rect x="574" y="170" width="66" height="30" opacity=".85"/>
            </g>
            <rect x="0" y="240" width="640" height="60" fill="#141e2b"/>
            <line class="j-a j-road" x1="0" y1="268" x2="640" y2="268" stroke="#f3c98f" stroke-opacity=".55" stroke-width="3"/>
            <g class="j-a j-truck">
              <path d="M342 204 L440 190 L440 236 L342 228Z" fill="url(#j-head)"/>
              <rect x="120" y="214" width="172" height="9" fill="#0f1722"/>
              <path d="M292 232 V186 q0 -6 6 -6 h30 q8 0 12 8 l6 14 v30Z" fill="#0f1722"/>
              <rect x="306" y="188" width="22" height="13" rx="2" fill="#ffd9a0" opacity=".75"/>
              <g fill="#0b121b"><circle cx="142" cy="234" r="11"/><circle cx="272" cy="234" r="11"/><circle cx="324" cy="234" r="11"/></g>
              <use href="#j-car" x="130" y="168" width="150" height="46" fill="#22324a" style="--win:#3c5070;--rim:#5a6a82"/>
            </g>
          </svg>"""


def _arrival(t: dict) -> str:
    # The car finishes in the middle of the picture (x 268-373 of 640), under the spotlight.
    return """<svg viewBox="0 0 640 300">
            <rect x="0" y="232" width="272" height="68" fill="url(#j-sea)"/>
            <g fill="#ffe2b0"><rect x="70" y="272" width="120" height="2" opacity=".5"/><rect x="90" y="280" width="80" height="2" opacity=".38"/><rect x="105" y="288" width="50" height="2" opacity=".28"/></g>
            <rect x="262" y="212" width="378" height="88" fill="#141e2b"/>
            <g class="j-a j-ship">
              <path d="M8 212 L264 212 L244 262 L28 262Z" fill="#141e2b"/>
              <rect x="22" y="160" width="36" height="52" fill="#141e2b"/>
              <g fill="#ffd9a0" opacity=".7"><rect x="28" y="168" width="6" height="5"/><rect x="40" y="168" width="6" height="5"/><rect x="28" y="180" width="6" height="5"/></g>
              <g fill="#1e2b3d"><rect x="66" y="180" width="36" height="32"/><rect x="104" y="180" width="36" height="32"/><rect x="85" y="146" width="36" height="32"/></g>
              <use class="j-a j-ondeck" href="#j-car" x="143" y="181" width="105" height="32" fill="#2a3a52" style="--win:#4a5e7e;--rim:#5a6a82"/>
            </g>
            <g class="j-a j-spot">
              <path d="M306 0 L334 0 L392 213 L248 213Z" fill="url(#j-spot)"/>
              <ellipse cx="320" cy="213" rx="80" ry="8" fill="url(#j-glow)"/>
            </g>
            <use class="j-a j-rolloff" href="#j-car" x="268" y="181" width="105" height="32" fill="#2a3a52" style="--win:#4a5e7e;--rim:#5a6a82"/>
            <use href="#j-person" x="404" y="108" width="34" height="106" fill="#141e2b"/>
            <path class="j-a j-arms" d="M410 134 L401 108 M432 134 L441 108" stroke="#141e2b" stroke-width="4.5" stroke-linecap="round"/>
            <g class="j-a j-spark" fill="#e7b46a"><circle cx="391" cy="100" r="3.5"/><circle cx="453" cy="96" r="3.5"/><circle cx="385" cy="126" r="2.5"/><circle cx="423" cy="84" r="2.5"/></g>
          </svg>"""


SCENES = [_request, _auction, _documents, _truck, _arrival]


def render_journey(labels: dict, titles: list[str]) -> str:
    """The pinned, scroll-driven strip. `titles` are the step titles, one per scene."""
    if len(titles) != len(SCENES):
        raise ValueError(f"journey has {len(SCENES)} scenes but {len(titles)} step titles")
    panels = "\n".join(
        f'        <div class="j-panel">\n'
        f'          {scene(labels)}\n'
        f'          <div class="j-cap"><b>{i}</b> {_e(title)}</div>\n'
        f'        </div>'
        for i, (scene, title) in enumerate(zip(SCENES, titles), start=1)
    )
    dots = "".join(f'<i class="j-a j-d{i}"></i>' for i in range(1, len(SCENES) + 1))
    return f"""  <section class="journey" aria-hidden="true">
  {DEFS}
  <div class="j-sticky">
    <div class="j-stage">
      <div class="j-sky j-sky1"></div><div class="j-sky j-sky2 j-a"></div><div class="j-sky j-sky3 j-a"></div><div class="j-sky j-sky4 j-a"></div><div class="j-sky j-sky5 j-a"></div>
      <div class="j-sun j-a"></div>
      <div class="j-track j-a">
{panels}
      </div>
      <div class="j-dots">{dots}</div>
    </div>
  </div>
  </section>"""
