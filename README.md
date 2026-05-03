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
| SVD (Funk MF) | Model-based CF | Matrix factorization, tuned `n_factors` and `reg_all` via 3-fold CV |
| User-Based KNN | Memory-based CF | Cosine similarity, tuned `k` via 3-fold CV |

All three are evaluated on the **same held-out 20% test set** (`random_state=42`) for fair comparison, using **RMSE** and **MAE**. **Precision@5** and **Recall@5** are also reported.

## Dataset

**CiaoDVD** — crawled from the DVD section of dvd.ciao.co.uk in December 2013.

The `movie-ratings.txt` file has 72,665 ratings across 17,615 unique users and 16,121 unique movies, with the columns: `userId, movieId, movie_categoryId, reviewId, movieRating (1–5), reviewDate`.

- Rating matrix is **99.97% sparse** (only 0.026% of all possible (user, movie) pairs have a rating)
- Ratings are integers from 1 to 5
- Distribution is left-skewed — most ratings are 4 or 5

Download from: https://guoguibing.github.io/librec/datasets.html

After downloading, place `movie-ratings.txt` in `data/raw/`.

## Repository Structure

```
recommendation-system/
├── README.md
├── SETUP.md                            # Step-by-step setup + git commands
├── CODE_MAP.md                         # How the code is organized
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/                            # Place movie-ratings.txt here (not committed)
│   └── processed/
│       └── ratings_clean.csv           # Cleaned data
├── notebooks/
│   └── recommendation_system.ipynb     # Phase 1 + Phase 2 (main notebook)
├── src/
│   ├── data_loader.py                  # Load movie-ratings.txt
│   ├── preprocessing.py                # Clean + drop unused columns
│   ├── cf_model.py                     # User-Based KNN with grid search
│   ├── svd_model.py                    # SVD with grid search
│   └── evaluation.py                   # RMSE, MAE, Precision@K, Recall@K
├── results/
│   ├── figures/
│   │   ├── rating_distribution.png
│   │   ├── long_tail.png
│   │   └── model_comparison.png
│   └── metrics.csv
└── report/
    └── final_report.pdf
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

## Final Results

RMSE / MAE on the 20% held-out test set (same split, `random_state=42`, for all three models):

| Model | RMSE | MAE | Precision@5 | Recall@5 |
|---|---|---|---|---|
| Global Average | 1.0886 | 0.8399 | — | — |
| **SVD (best)** | **0.9506** | **0.7361** | 0.8283 | 0.8549 |
| User-Based KNN | 1.0839 | 0.8200 | 0.8278 | 0.8544 |

Best SVD hyperparameters: `n_factors=50, n_epochs=20, lr_all=0.005, reg_all=0.1`

**Headline finding:** SVD wins. On a 99.97% sparse rating matrix, latent-factor models generalize far better than memory-based KNN, because each rating refines the entire factor space rather than a single user-pair similarity. KNN improves slightly on the baseline but is fundamentally limited by how few users share rated movies in common.

The Precision@5 / Recall@5 numbers are very close between SVD and KNN because they measure top-5 ranking quality rather than per-rating accuracy — and both models do a reasonable job of putting high-rated movies near the top of their recommendations.

See the discussion section at the end of the notebook for the full analysis.

## Tools Used

Python 3 · Jupyter · pandas · NumPy · matplotlib · seaborn · [scikit-surprise](https://surprise.readthedocs.io/) · Git / GitHub · VS Code + Claude (vibe coding)
