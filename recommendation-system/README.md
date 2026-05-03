# Movie Recommendation System (CiaoDVD)

**CSIT 360 / 557 — Advanced Techniques in Data Science**
**Spring 2026 — Project 2: Vibe Coding**

A movie recommendation system built on the **CiaoDVD** dataset, comparing three classic collaborative-filtering algorithms.

## Team Members

- Madison Berrios — [GitHub username]

## Project Overview

This project implements and compares three recommendation algorithms on a real-world, sparse rating dataset:

| Model | Type | Notes |
|---|---|---|
| Global Average | Baseline | Predicts the mean rating for every (user, movie) pair |
| User-Based KNN | Memory-based CF | Cosine similarity, tuned `k` via 3-fold CV |
| SVD (Funk MF) | Model-based CF | Matrix factorization, tuned `n_factors` and `reg_all` via 3-fold CV |

All three are evaluated on the **same held-out 20% test set** for fair comparison, using **RMSE** and **MAE**. As a bonus, **Precision@5** and **Recall@5** are also reported.

## Dataset

**CiaoDVD** — crawled from the DVD section of dvd.ciao.co.uk in December 2013.

| File | Rows | Columns |
|---|---|---|
| `movie-ratings.txt` | 72,665 | userId, movieId, movie-categoryId, reviewId, movieRating (1–5), reviewDate |
| `trusts.txt` *(optional)* | 40,133 | trustorId, trusteeId, trustRating |

- 17,615 unique users · 16,121 unique movies
- Rating matrix is **>99.97% sparse**
- Ratings are integers from 1 to 5
- Distribution is left-skewed — most ratings are 4 or 5

Download from: https://guoguibing.github.io/librec/datasets.html

After downloading, place `movie-ratings.txt` in `data/raw/`.

## Repository Structure

```
recommendation-system/
├── README.md
├── SETUP.md                # Step-by-step setup + git commands
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/                # Place movie-ratings.txt here (not committed)
│   └── processed/          # (not committed)
├── notebooks/
│   └── recommendation_system.ipynb    # Main notebook (Phase 1 + Phase 2)
├── results/
│   └── figures/            # Plots saved from the notebook
└── report/
    └── final_report.pdf    # Add your project report here
```

## Installation

> **Important:** This project pins `numpy<2` because `scikit-surprise` is not yet compatible with NumPy 2.x. Using NumPy 2 will cause `ImportError: numpy.core.multiarray failed to import`.

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/recommendation-system.git
cd recommendation-system

# 2. (Recommended) create a virtual environment
python3 -m venv venv
source venv/bin/activate          # macOS / Linux
# venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download the dataset and place it in data/raw/
#    https://guoguibing.github.io/librec/datasets.html
```

## How to Run

```bash
jupyter notebook
```

Open `notebooks/recommendation_system.ipynb` and run all cells from top to bottom. The notebook covers:

1. **Phase 1: EDA** — load the data, basic stats, rating distribution, long-tail plots, cleaning
2. **Phase 2: Models** — Global Average baseline, SVD (with hyperparameter tuning), User-Based KNN (with hyperparameter tuning)
3. **Bonus** — Precision@5 and Recall@5
4. **Comparison** — table, bar chart, and discussion

## Summary of Results

Final RMSE / MAE on the 20% held-out test set (same split for all models):

| Model | RMSE | MAE | Precision@5 | Recall@5 |
|---|---|---|---|---|
| Global Average | (filled after running) | | — | — |
| User-Based KNN | (filled after running) | | (filled) | (filled) |
| **SVD (best)** | **(lowest)** | **(lowest)** | (filled) | (filled) |

**Headline finding:** SVD wins. On a >99.97% sparse rating matrix, latent-factor models generalize far better than memory-based KNN, because each rating refines the entire factor space rather than a single user-pair similarity.

See the discussion section at the end of the notebook for the full analysis.

## Tools Used

Python 3 · Jupyter · pandas · NumPy · matplotlib · seaborn · [scikit-surprise](https://surprise.readthedocs.io/) · Git / GitHub · VS Code + Claude (vibe coding)
