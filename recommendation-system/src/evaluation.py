"""
evaluation.py
-------------
Evaluation metrics used in the comparison.

- ``rmse_mae_constant``: closed-form RMSE/MAE for a constant predictor (the
  Global Average baseline). We don't need Surprise for this.
- ``precision_recall_at_k``: top-K evaluation. For each user, sort their test
  predictions by estimated rating and take the top K. A movie is "relevant" if
  its true rating is >= ``threshold`` (we use 4).
"""

from collections import defaultdict
import numpy as np


def rmse_mae_constant(testset, prediction: float) -> tuple[float, float]:
    """Compute RMSE and MAE for a constant predictor (e.g., the global mean).

    ``testset`` is a Surprise testset: list of (uid, iid, true_rating) tuples.
    """
    true_ratings = np.array([true_r for (_, _, true_r) in testset])
    preds = np.full(len(testset), prediction)
    rmse = float(np.sqrt(np.mean((true_ratings - preds) ** 2)))
    mae = float(np.mean(np.abs(true_ratings - preds)))
    return rmse, mae


def precision_recall_at_k(
    predictions, k: int = 5, threshold: float = 4
) -> tuple[float, float]:
    """Compute average Precision@K and Recall@K across users.

    ``predictions`` is a list of Surprise Prediction objects (e.g., the result
    of ``model.test(testset)``).

    A movie is "relevant" if its true rating is >= ``threshold``.
    Precision@K = (# relevant in top-K) / K
    Recall@K    = (# relevant in top-K) / (# total relevant for that user)
    """
    user_est_true: dict = defaultdict(list)
    for uid, _, true_r, est, _ in predictions:
        user_est_true[uid].append((est, true_r))

    precisions: list[float] = []
    recalls: list[float] = []

    for _, user_ratings in user_est_true.items():
        # Sort by estimated rating, descending
        user_ratings.sort(key=lambda x: x[0], reverse=True)
        top_k = user_ratings[:k]

        n_rel = sum(true_r >= threshold for (_, true_r) in user_ratings)
        n_rec_k = len(top_k)
        n_rel_and_rec_k = sum(true_r >= threshold for (_, true_r) in top_k)

        precision = n_rel_and_rec_k / n_rec_k if n_rec_k else 0.0
        recall = n_rel_and_rec_k / n_rel if n_rel else 0.0
        precisions.append(precision)
        recalls.append(recall)

    return float(np.mean(precisions)), float(np.mean(recalls))
