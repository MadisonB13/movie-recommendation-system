"""
svd_model.py
------------
Matrix Factorization using Surprise's SVD (Funk SVD).

Funk SVD learns two low-dimensional matrices — one for users, one for movies —
whose product approximates the rating matrix. Each user and each movie is
represented by a vector of ``n_factors`` latent features. Predictions are dot
products plus user/movie biases.

We grid-search the two most important hyperparameters:
- ``n_factors``: how many latent dimensions to learn
- ``reg_all``  : L2 regularization, important on a sparse dataset to avoid
  overfitting on users/movies with very few ratings.
"""

from surprise import SVD
from surprise.model_selection import GridSearchCV


def tune_svd(data, cv: int = 3) -> dict:
    """Grid-search SVD. Returns ``gs.best_params['rmse']``."""
    param_grid = {
        "n_factors": [50, 100],
        "n_epochs": [20],
        "lr_all": [0.005],
        "reg_all": [0.02, 0.1],
    }

    gs = GridSearchCV(
        SVD,
        param_grid,
        measures=["rmse", "mae"],
        cv=cv,
        n_jobs=-1,
    )
    gs.fit(data)
    return gs.best_params["rmse"]


def fit_svd(trainset, best_params: dict) -> SVD:
    """Fit SVD on the trainset using the best params from the grid search."""
    model = SVD(**best_params)
    model.fit(trainset)
    return model
