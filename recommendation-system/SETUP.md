# SETUP — Quick Start

This guide gets you from "I just unzipped the repo" to "I have a public GitHub repo with everything pushed" in about 10 minutes.

---

## Step 1 — Fix the NumPy 2 import error first

If you're hitting `ImportError: numpy.core.multiarray failed to import`, run this **inside your notebook** at the very top:

```python
%pip install "numpy<2"
```

Then **restart the kernel** (Kernel menu → Restart, or click "Select Kernel" → Restart). The error should be gone.

The `%pip` magic with a percent sign is important — it installs into the same Python that your notebook kernel is using. Plain `!pip` or running `pip` in Terminal can install into the wrong environment.

---

## Step 2 — Drop the dataset in

1. Download CiaoDVD from https://guoguibing.github.io/librec/datasets.html
2. Unzip and copy `movie-ratings.txt` to `data/raw/movie-ratings.txt`

The notebook expects the data at `../data/raw/movie-ratings.txt` (because the notebook lives in `notebooks/`).

The `data/raw/` folder is git-ignored on purpose — datasets don't belong in repos.

---

## Step 3 — Run the notebook

```bash
jupyter notebook
```

Open `notebooks/recommendation_system.ipynb` and run all cells top to bottom.

---

## Step 4 — Create the GitHub repo and push

The assignment requires **5+ meaningful commits**, so don't `git add .` everything in one shot. Make a commit at each milestone.

```bash
# In the recommendation-system/ folder

git init
git branch -M main

# Commit 1: scaffolding
git add README.md SETUP.md requirements.txt .gitignore
git commit -m "Initial commit: README, requirements, gitignore"

# Commit 2: empty folders (the .gitkeep files)
git add data/ results/ report/
git commit -m "Add project folder structure"

# Commit 3: the main notebook
git add notebooks/recommendation_system.ipynb
git commit -m "Add Phase 1 EDA: data loading, stats, rating distribution, long-tail"

# Commit 4: (after running the notebook) push the figures and metrics
git add results/
git commit -m "Add Phase 2 results: model comparison, RMSE/MAE, Precision@5/Recall@5"

# Commit 5: (after writing the report) add it
git add report/final_report.pdf
git commit -m "Add final project report"
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

## Step 5 — Verify before you submit

Open your repo URL in a private browser window. Check:

- [ ] README displays with the project description
- [ ] The notebook renders (GitHub previews `.ipynb` natively)
- [ ] `data/raw/` does NOT contain `movie-ratings.txt` (it should be gitignored)
- [ ] You have **at least 5 commits** in the History tab
- [ ] The repo is set to **Public** (Settings → General)

Then submit the URL on Canvas.

---

## Troubleshooting

**`FileNotFoundError: ../data/raw/movie-ratings.txt`.** You forgot Step 2, or you're running the notebook from the wrong folder. Make sure Jupyter was launched from the `recommendation-system/` folder, not from `notebooks/`.

**`ImportError: numpy.core.multiarray failed to import` is back.** Make sure you actually restarted the kernel after `%pip install "numpy<2"`. The old NumPy stays in memory until restart.

**Grid search taking forever.** The SVD grid search runs 4 configs × 3 folds = 12 model fits. On a laptop this should be 2–5 minutes. If it's much slower, close other apps.
