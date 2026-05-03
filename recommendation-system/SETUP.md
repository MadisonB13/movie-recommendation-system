# SETUP — Quick Start

This guide gets you from "I just unzipped the repo" to "I have a public GitHub repo with everything pushed" in about 10 minutes.

---

## Step 1 — Drop the dataset in

The dataset is `data/raw/movie-ratings.txt`. If you don't have it there yet, download CiaoDVD from https://guoguibing.github.io/librec/datasets.html and copy `movie-ratings.txt` into `data/raw/`.

The `data/raw/` folder is git-ignored on purpose — datasets don't belong in repos.

---

## Step 2 — (Optional) re-run the notebook

The notebook is already executed and all outputs are saved in the `.ipynb`. You only need to re-run it if you've changed something. If you do re-run:

```bash
jupyter notebook
```

Open `notebooks/recommendation_system.ipynb` and run all cells top to bottom.

If you hit `ImportError: numpy.core.multiarray failed to import`, the first cell installs the right versions:

```python
%pip install --upgrade --force-reinstall joblib scikit-surprise "numpy<2"
```

After that, restart the kernel and run from the top.

---

## Step 3 — Create the GitHub repo and push

The assignment requires **5+ meaningful commits**, so don't `git add .` everything in one shot. Make a commit at each milestone.

```bash
# In the recommendation-system/ folder

git init
git branch -M main

# Commit 1: scaffolding (README, requirements, gitignore, etc.)
git add README.md SETUP.md CODE_MAP.md requirements.txt .gitignore
git commit -m "Initial commit: README, requirements, gitignore"

# Commit 2: project folder structure (.gitkeep files)
git add data/ report/
git commit -m "Add project folder structure (data, report)"

# Commit 3: src modules
git add src/
git commit -m "Add src modules: data loading, preprocessing, models, evaluation"

# Commit 4: main notebook
git add notebooks/recommendation_system.ipynb
git commit -m "Add main notebook: Phase 1 EDA + Phase 2 models with hyperparameter tuning"

# Commit 5: results (figures + metrics)
git add results/
git commit -m "Add final results: metrics.csv, EDA figures, model comparison chart"
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

## Step 4 — When the report is ready

Once you finish writing `report/final_report.pdf`, drop it in the `report/` folder and:

```bash
git add report/final_report.pdf
git commit -m "Add final project report"
git push
```

That's commit 6 — exceeds the 5-commit minimum.

---

## Step 5 — Verify before you submit

Open your repo URL in a private browser window. Check:

- [ ] README displays with the project description and final results table
- [ ] The notebook renders (GitHub previews `.ipynb` natively)
- [ ] `data/raw/` does NOT contain `movie-ratings.txt` (it should be gitignored)
- [ ] You have **at least 5 commits** in the History tab
- [ ] The repo is set to **Public** (Settings → General)
- [ ] `results/metrics.csv` shows the final numbers
- [ ] `results/figures/` shows the 3 plots

Then submit the URL on Canvas along with `final_report.pdf`.
