#!/usr/bin/env python
"""Render the notebook to index.html and add a light header/footer so the page
is not bare. Run after the notebook is executed."""
import subprocess, re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
NB = "Boyce_Park_Taxonomy.ipynb"
COLAB = "https://colab.research.google.com/github/TomAs-1226/who-lives-there-boyce-park/blob/main/Boyce_Park_Taxonomy.ipynb"
GH = "https://github.com/TomAs-1226/who-lives-there-boyce-park"

subprocess.run([sys.executable, "-m", "jupyter", "nbconvert", "--to", "html",
                NB, "--output", "index.html"], cwd=HERE, check=True)

path = os.path.join(HERE, "index.html")
html = open(path, encoding="utf-8").read()

STYLE = """
<style>
:root{ --ink:#1f2a27; --teal:#155e52; --iron:#b0592a; --bg:#eef2f0; --card:#ffffff; --line:#e2e8e4; }
html{ background:var(--bg); }
body.jp-Notebook, body{ max-width:62rem !important; margin:0 auto !important;
  padding:0 1rem 3rem !important; background:var(--bg) !important;
  font-family:system-ui,-apple-system,'Segoe UI',Roboto,sans-serif; }
.jp-Cell{ background:var(--card); }
.site-hero{ background:linear-gradient(135deg,#123a34,#1f5f54); color:#fff;
  border-radius:0 0 16px 16px; padding:2.2rem 1.6rem 1.8rem; margin:0 -1rem 1.5rem;
  box-shadow:0 6px 20px rgba(0,0,0,.12); }
.site-hero .kicker{ text-transform:uppercase; letter-spacing:.12em; font-size:.72rem;
  font-weight:700; color:#bfe6db; }
.site-hero h1{ font-family:Georgia,'Times New Roman',serif; font-size:2rem; margin:.3rem 0 .5rem;
  line-height:1.15; color:#fff; }
.site-hero p{ margin:.2rem 0; color:#e6f2ee; max-width:46rem; line-height:1.5; }
.site-hero .answer{ font-size:1.05rem; }
.site-hero .answer b{ color:#ffd9a8; }
.btnrow{ margin-top:1.1rem; display:flex; gap:.6rem; flex-wrap:wrap; }
.btn{ display:inline-block; text-decoration:none; font-weight:650; font-size:.9rem;
  padding:.55rem .95rem; border-radius:9px; }
.btn.run{ background:#ffb454; color:#3a2610; }
.btn.gh{ background:rgba(255,255,255,.15); color:#fff; border:1px solid rgba(255,255,255,.35); }
.btn:hover{ filter:brightness(1.06); }
.site-foot{ margin:2.5rem -1rem 0; padding:1.4rem 1.6rem; background:#123a34; color:#cfe3dd;
  border-radius:16px 16px 0 0; font-size:.9rem; }
.site-foot b{ color:#fff; }
@media (max-width:640px){ .site-hero h1{ font-size:1.6rem; } }
</style>
"""

HERO = f"""
<header class="site-hero">
  <div class="kicker">CMU Pre-College Computational Biology &middot; Group A3 (Alphas)</div>
  <h1>Who Lives There? The Tiny Life in Boyce Park Pond</h1>
  <p>We read the DNA of the bacteria and algae in Boyce Park pond water to find out who lives there, and whether old coal mine runoff is shaping the pond.</p>
  <p class="answer"><b>The short answer:</b> the pretty pond is really acid mine drainage water, and the microbe that gives it away is <b>Ferrovum</b>, an iron eater.</p>
  <div class="btnrow">
    <a class="btn run" href="{COLAB}">Run every cell in Colab</a>
    <a class="btn gh" href="{GH}">View the code on GitHub</a>
  </div>
</header>
"""

FOOTER = """
<footer class="site-foot">
  <b>Group A3, the Alphas:</b> Thomas Yu, Thomas Kellog, Lexi Dai, Sarah Wu.<br>
  This page is a read-only view of our notebook. Click <b>Run every cell in Colab</b> up top to run it yourself.
</footer>
"""

html = html.replace("</head>", STYLE + "</head>", 1)
html = re.sub(r"(<body[^>]*>)", r"\1" + HERO, html, count=1)
html = html.replace("</body>", FOOTER + "</body>", 1)

open(path, "w", encoding="utf-8").write(html)
print("Wrote index.html with header + footer (", len(html)//1024, "KB )")
