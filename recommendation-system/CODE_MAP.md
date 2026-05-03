# Code Map — Where Each Piece of My Original Notebook Lives

This document maps every piece of my original `Phase_2.ipynb` to the corresponding file in this repo. The suggested project structure splits the work across multiple files, but **the underlying code is from my notebook** — I wrote and understand all of it.

## Notebooks

| Repo file | Came from this section of `Phase_2.ipynb` |
|---|---|
| `notebooks/01_eda.ipynb` | "Phase 1: Data Loading & Exploratory Data Analysis" — load CSV, basic statistics, rating distribution, ratings-per-user / per-movie long-tail plots, data-quality checks, drop unused columns |
| `notebooks/02_cf_model.ipynb` | "Model 3: User-Based KNN" — build Surprise dataset, 80/20 split, grid search over `k` with cosine similarity, fit best model, evaluate RMSE/MAE |
| `notebooks/03_svd_model.ipynb` | "Model 2: SVD (Matrix Factorization)" — Surprise dataset, same split, grid search over `n_factors` and `reg_all`, fit best model, evaluate RMSE/MAE |
| `notebooks/04_evaluation.ipynb` | "Model 1: Global Average (Baseline)", "Bonus: Top-K Recommendation Evaluation", "Model Comparison Table", "Comparison Bar Chart", and "Discussion: Which Model Performs Best and Why?" |

All four notebooks use `random_state=42` for the train/test split, which is the same value I used in my original notebook. This means every model is evaluated on the exact same held-out test set, so RMSE/MAE values are directly comparable.

## Source modules (`src/`)

The `src/` files just wrap code from my notebook in named functions so the notebooks are shorter and the structure matches the suggested layout. Nothing new — same logic, just organized.

| Repo file | Came from |
|---|---|
| `src/data_loader.py` | The `pd.read_csv(...)` call I used to load `movie-ratings.txt` with the 6 column names from the dataset spec |
| `src/preprocessing.py` | The "Data Cleaning" section: `drop_duplicates()`, `drop(columns=["reviewId", "reviewDate"])`, plus the basic-stats calculation (n_users, n_movies, sparsity) |
| `src/cf_model.py` | The KNN grid-search code (`KNNBasic` + `GridSearchCV` over `k` with cosine similarity) and the final `fit()` call |
| `src/svd_model.py` | The SVD grid-search code (`SVD` + `GridSearchCV` over `n_factors` and `reg_all`) and the final `fit()` call |
| `src/evaluation.py` | The `precision_recall_at_k` function (which I wrote in the bonus section), plus a small helper for computing RMSE/MAE for the Global Average baseline (which I had inline) |
| `src/trust_model.py` | **Not used in my submission.** The suggested structure includes this file for the optional +5% trust-network bonus. I left it in to match the structure exactly, but I am not attempting that bonus, so this file is not imported anywhere. |

## My Three Models

The assignment requires at least 2 models (CSIT 360) or 3 models including SVD (CSIT 557). I implemented three:

1. **Global Average** (baseline) — predict the mean training rating for every (user, movie) pair
2. **SVD** (matrix factorization, with hyperparameter tuning)
3. **User-Based KNN** (collaborative filtering, cosine similarity, with `k` tuning)

All three are compared in `notebooks/04_evaluation.ipynb` using RMSE, MAE, Precision@5, and Recall@5.

## What I'm responsible for explaining

If asked to explain anything in this repo, I can point at the corresponding cell in my original `Phase_2.ipynb`. The split into multiple files is purely organizational — the algorithms, hyperparameters, evaluation logic, and discussion are all from my original work.

The only section that was **not** generated with AI help is the **Vibe Coding Reflection** in `report/final_report.pdf`, per the assignment rules.
