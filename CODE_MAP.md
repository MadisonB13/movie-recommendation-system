# Code Map — How This Repo Is Organized

This document explains where each piece of the project lives. The main work is in a single executed notebook; the `src/` folder contains the same logic refactored as reusable functions to match the suggested project structure.

## Main notebook

**`notebooks/recommendation_system.ipynb`** — this is the primary deliverable. It contains all of Phase 1 (data loading, EDA, cleaning) and all of Phase 2 (Global Average baseline, SVD with grid search, User-Based KNN with grid search, Precision@5 / Recall@5, comparison table, bar chart, discussion). Every cell has been executed and the outputs are saved in the `.ipynb` file.

## Source modules (`src/`)

The `src/` files contain the same algorithms from the notebook, refactored into named functions. They mirror the suggested project structure (one module per algorithm) and keep the logic available for reuse:

| File | What it does |
|---|---|
| `src/data_loader.py` | Loads `movie-ratings.txt` with the 6 CiaoDVD columns into a pandas DataFrame |
| `src/preprocessing.py` | Drops duplicates, drops unused columns (`reviewId`, `reviewDate`), computes basic statistics (n_users, n_movies, sparsity) |
| `src/cf_model.py` | User-Based KNN with cosine similarity and grid search over `k` (3-fold CV) |
| `src/svd_model.py` | Funk SVD with grid search over `n_factors` and `reg_all` (3-fold CV) |
| `src/evaluation.py` | `precision_recall_at_k` function and a helper for computing RMSE/MAE for a constant predictor (the Global Average baseline) |

## My Three Models

The assignment requires at least 2 models (CSIT 360) or 3 models including SVD (CSIT 557). I implemented three:

1. **Global Average** (baseline) — predict the mean training rating for every (user, movie) pair
2. **SVD** (matrix factorization, `n_factors=50, reg_all=0.1` via 3-fold CV grid search)
3. **User-Based KNN** (cosine similarity, `k` tuned via 3-fold CV grid search)

All three use the same 80/20 train/test split (`random_state=42`) so RMSE/MAE values are directly comparable.

## What I'm responsible for explaining

The notebook is my own work. Every cell, every algorithm choice, every hyperparameter, and the final discussion are mine. The `src/` modules contain refactored versions of the same code — same logic, same hyperparameters, same library calls.

Per the assignment rules, the **Vibe Coding Reflection** section in `report/final_report.pdf` is written entirely in my own words without AI assistance.
