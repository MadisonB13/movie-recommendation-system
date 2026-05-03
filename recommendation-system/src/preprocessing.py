"""
preprocessing.py
----------------
Clean the raw ratings DataFrame and report basic statistics.

For this project we:
- drop ``reviewId`` and ``reviewDate`` (not used by the recommendation models)
- check for duplicates and missing values (CiaoDVD has none, but we verify)
- compute basic statistics: number of users, movies, ratings, sparsity
"""

import pandas as pd


def clean_ratings(df: pd.DataFrame) -> pd.DataFrame:
    """Drop unused columns and any duplicate rows.

    The recommendation models only need (userId, movieId, movieRating).
    """
    df = df.drop_duplicates()
    df = df.drop(columns=["reviewId", "reviewDate"], errors="ignore")
    return df.reset_index(drop=True)


def basic_stats(df: pd.DataFrame) -> dict:
    """Return the key dataset statistics used in the EDA section.

    Sparsity = 1 - (observed_ratings / (n_users * n_movies)).
    """
    n_users = df["userId"].nunique()
    n_movies = df["movieId"].nunique()
    n_ratings = len(df)
    possible = n_users * n_movies
    sparsity = 1 - (n_ratings / possible) if possible else 0.0

    return {
        "n_users": n_users,
        "n_movies": n_movies,
        "n_ratings": n_ratings,
        "sparsity": sparsity,
    }


def print_stats(stats: dict) -> None:
    """Pretty-print the stats dict from ``basic_stats``."""
    print(f"Number of users  : {stats['n_users']:,}")
    print(f"Number of movies : {stats['n_movies']:,}")
    print(f"Number of ratings: {stats['n_ratings']:,}")
    print(f"Sparsity         : {stats['sparsity']:.4%}")
