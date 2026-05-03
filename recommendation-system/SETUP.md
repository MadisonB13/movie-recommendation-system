# SETUP — Quick Start

This guide gets you from "I just unzipped the repo" to "I have a public GitHub repo with everything pushed" in about 10 minutes.

---

## Step 1 — Fix the NumPy 2 import error first (one-time)

Your screenshot showed:

```
ImportError: numpy.core.multiarray failed to import
```

This happens because `scikit-surprise` is built against NumPy 1.x but you have NumPy 2.x installed. The fix is to pin NumPy below 2:

```bash
pip install --break-system-packages "numpy<2"
```

Or, cleaner: do a fresh virtual environment using the `requirements.txt` in this repo (see Step 2).

---

## Step 2 — Set up a clean environment in the project folder

Open a terminal and `cd` into the unzipped `recommendation-system/` folder:

```bash
cd ~/Downloads/recommendation-system   # or wherever you put it

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate                # on macOS

# Install the pinned dependencies
pip install -r requirements.txt
```

When the venv is active you'll see `(venv)` at the start of your prompt. Anything you `pip install` from here on is local to this project.

---

## Step 3 — Drop the dataset in

1. Download CiaoDVD from https://guoguibing.github.io/librec/datasets.html
2. Unzip and copy `movie-ratings.txt` to `data/raw/movie-ratings.txt`
3. (Optional, for the trust bonus) also copy `trusts.txt` to `data/raw/trusts.txt`

These files are git-ignored on purpose — datasets don't belong in repos.

---

## Step 4 — Run the notebooks in order

```bash
jupyter notebook
```

In the browser tab that opens, run:
1. `notebooks/01_eda.ipynb` — produces `data/processed/ratings_clean.csv`
2. `notebooks/02_cf_model.ipynb` — KNN
3. `notebooks/03_svd_model.ipynb` — SVD
4. `notebooks/04_evaluation.ipynb` — final comparison + Precision@5/Recall@5

`04_evaluation.ipynb` re-runs all three models for the comparison, so even if you skip 02 and 03, the comparison still works as long as 01 was run.

---

## Step 5 — Create the GitHub repo and push

The assignment requires **5+ meaningful commits**, so don't `git add .` everything in one shot. Make a commit at each milestone.

```bash
# In the recommendation-system/ folder

git init
git branch -M main

# Commit 1: scaffolding
git add README.md requirements.txt .gitignore
git commit -m "Initial commit: README, requirements, gitignore"

# Commit 2: src modules
git add src/
git commit -m "Add src modules: data loading, preprocessing, models, evaluation"

# Commit 3: EDA notebook
git add notebooks/01_eda.ipynb
git commit -m "Add Phase 1 EDA notebook"

# Commit 4: model notebooks
git add notebooks/02_cf_model.ipynb notebooks/03_svd_model.ipynb
git commit -m "Add KNN and SVD model notebooks with hyperparameter tuning"

# Commit 5: evaluation + results
git add notebooks/04_evaluation.ipynb results/
git commit -m "Add evaluation notebook with model comparison and Precision@5/Recall@5"
```

Now create the GitHub repo:

1. Go to https://github.com/new
2. Repository name: `recommendation-system` (or whatever you prefer)
3. **Public** (the assignment requires this so the instructor can see it)
4. Do NOT check "Add a README" — you already have one
5. Click "Create repository"

GitHub will show you the commands. Run the two for an existing repo:

```bash
git remote add origin https://github.com/<your-username>/recommendation-system.git
git push -u origin main
```

After that, every later commit just needs `git push`.

---

## Step 6 — After running the notebooks, push the figures

Once you've actually run all 4 notebooks, your `results/figures/` folder will fill up with PNGs and `results/metrics.csv` will exist:

```bash
git add results/
git commit -m "Add final metrics and figures from notebook runs"
git push
```

---

## Step 7 — Verify before you submit

Open your repo URL in a private browser window. Check:

- [ ] README displays with the project description
- [ ] All 4 notebooks render (GitHub previews `.ipynb` natively)
- [ ] `data/raw/` does NOT contain `movie-ratings.txt` (it should be gitignored)
- [ ] You have **at least 5 commits** in the History tab
- [ ] The repo is set to **Public** (Settings → General)

Then submit the URL on Canvas.

---

## Troubleshooting

**`No module named 'src'` in a notebook.** The notebooks add the project root to `sys.path` in their first code cell. If you moved the notebook, run it from inside the `notebooks/` folder so the bootstrap code finds the parent.

**`FileNotFoundError: data/raw/movie-ratings.txt`.** You forgot Step 3.

**The grid search is taking forever.** It runs 4 SVD configs × 3 folds = 12 model fits. On a laptop this should be 2–5 minutes. KNN is similar. If it's much slower, your machine might be swapping — close other apps.

**`ImportError: numpy.core.multiarray failed to import` is back.** You activated a different environment. Run `which python` to confirm it points at `venv/bin/python`. If not, re-activate: `source venv/bin/activate`.
