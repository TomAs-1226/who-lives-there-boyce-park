# Who Lives There? Boyce Park Pond Water

A class project (CMU Pre-College Computational Biology, Module 2) by **Group A3, the Alphas**: Thomas Yu, Thomas Kellog, Lexi Dai, Sarah Wu.

We looked at the tiny life (bacteria and algae) in the water of a pond at **Boyce Park**, a county park on old coal mining land. The pond looks scenic, but we wanted to know if old mine runoff is quietly shaping what lives in it.

**Short answer: yes.** The pond is run by an iron eating bacterium and a crew of acid loving microbes, which is the classic sign of acid mine drainage. The full story, with charts, is in the notebook.

## The notebook

**[Boyce_Park_Taxonomy.ipynb](Boyce_Park_Taxonomy.ipynb)** has everything: the code, the charts, and a plain language write up in every section. GitHub shows the charts right in the page, so you can read it without running anything.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TomAs-1226/who-lives-there-boyce-park/blob/main/Boyce_Park_Taxonomy.ipynb)

### To run it yourself
1. Click the **Open in Colab** button above.
2. In Colab, run this first so it can reach the data files:
   ```
   !git clone https://github.com/TomAs-1226/who-lives-there-boyce-park.git repo
   %cd repo
   ```
3. Then use **Runtime, Run all**. The notebook finds the data in the `data` folder on its own.

It runs in about a minute because the DNA search results are saved inside the notebook. If you want to redo that search live, set `RUN_BLAST_LIVE = True` in the search step.

## What the notebook covers
1. Identify the most common microbes ourselves with a DNA search (BLAST).
2. Compare our answers to the lab's answers, and check for contamination.
3. Chart what lives in the pond.
4. Two comparison pictures: our pond next to the rivers, and our own sampling spots.
5. The story of what we found.
6. A plain explanation of every tool we used.

## What is in this repo
- `Boyce_Park_Taxonomy.ipynb` the whole project.
- `data/` the data files the notebook reads (our pond, plus a shared set with the rivers and the clean water controls).
