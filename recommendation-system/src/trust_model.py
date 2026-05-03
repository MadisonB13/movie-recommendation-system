"""
trust_model.py
--------------
OPTIONAL bonus: incorporate the CiaoDVD trust network.

The ``trusts.txt`` file has 40,133 directed trust links between users:
    trustorId, trusteeId, trustRating

A simple "trust-weighted" recommender predicts a user's rating for a movie as
the average of ratings given by users they trust. If the active user has no
trusted neighbors who rated that movie, fall back to the global mean.

This module is only imported if you decide to attempt the +5% trust network
bonus described in section 7 of the assignment.
"""

from pathlib import Path
import pandas as pd
import numpy as np
from collections import defaultdict


TRUST_COLUMNS = ["trustorId", "trusteeId", "trustRating"]


def load_trusts(path: str | Path = "data/raw/trusts.txt") -> pd.DataFrame:
    """Load the CiaoDVD trusts.txt file."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"Could not find {path}. Place trusts.txt in data/raw/ to use this bonus."
        )
    return pd.read_csv(path, names=TRUST_COLUMNS, header=None)


def build_trust_dict(trusts: pd.DataFrame) -> dict[int, set[int]]:
    """Map each user -> set of users they trust."""
    trust_map: dict[int, set[int]] = defaultdict(set)
    for trustor, trustee in zip(trusts["trustorId"], trusts["trusteeId"]):
        trust_map[int(trustor)].add(int(trustee))
    return dict(trust_map)


def predict_trust_weighted(
    user_id: int,
    movie_id: int,
    ratings: pd.DataFrame,
    trust_map: dict[int, set[int]],
    global_mean: float,
) -> float:
    """Predict a rating as the mean of ratings given by trusted users.

    Falls back to ``global_mean`` if the user has no trusted neighbors who
    rated this movie.
    """
    trusted = trust_map.get(int(user_id), set())
    if not trusted:
        return global_mean

    neighbor_ratings = ratings.loc[
        (ratings["userId"].isin(trusted)) & (ratings["movieId"] == movie_id),
        "movieRating",
    ]
    if len(neighbor_ratings) == 0:
        return global_mean
    return float(np.mean(neighbor_ratings))
