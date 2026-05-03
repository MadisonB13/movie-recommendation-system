"""
cf_model.py
-----------
User-Based Collaborative Filtering using Surprise's KNNBasic.

Why user-based? The assignment lists user-based and item-based KNN as two of the
allowed CF algorithms. We pick user-based + cosine similarity here. Item-based
would just flip ``user_based`` to False.

The function ``tune_user_knn`` runs a small 3-fold grid search over k (the number
of neighbors). On a >99.97% sparse dataset like CiaoDVD, KNN is fundamentally
limited because most user pairs share very few movies in common — but tuning k
still gives a meaningful comparison against the baseline and SVD.
"""

from surprise import KNNBasic
from surprise.model_selection import GridSearchCV


def tune_user_knn(data, cv: int = 3) -> dict:
    """Grid-search User-Based KNN over k. Returns ``gs.best_params['rmse']``."""
    param_grid = {
        "k": [20, 40],
        "sim_options": {
            "name": ["cosine"],
            "user_based": [True],
        },
    }

    gs = GridSearchCV(
        KNNBasic,
        param_grid,
        measures=["rmse", "mae"],
        cv=cv,
        n_jobs=-1,
    )
    gs.fit(data)
    return gs.best_params["rmse"]


def fit_user_knn(trainset, best_params: dict) -> KNNBasic:
    """Fit KNNBasic on the trainset using the best params from the grid search."""
    model = KNNBasic(**best_params)
    model.fit(trainset)
    return model
