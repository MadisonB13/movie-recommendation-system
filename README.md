# Movie Recommendation System (CiaoDVD)

**CSIT 360 — Advanced Techniques in Data Science**
**Spring 2026 — Project 2: Vibe Coding**

A movie recommendation system built on the **CiaoDVD** dataset, comparing three classic collaborative-filtering algorithms.

## Team Members

- Madison Berrios — [MadisonB13]

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


## Tools Used

Python 3 · Jupyter · pandas · NumPy · matplotlib · seaborn · [scikit-surprise](https://surprise.readthedocs.io/) · Git / GitHub · VS Code + Claude (vibe coding)
