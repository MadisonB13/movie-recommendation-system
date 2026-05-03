"""
data_loader.py
--------------
Load the CiaoDVD movie-ratings.txt file into a pandas DataFrame.

The file has 6 comma-separated columns and NO header row, per the dataset spec:
    userId, movieId, movie_categoryId, reviewId, movieRating (1-5), reviewDate
"""

from pathlib import Path
import pandas as pd


COLUMNS = [
    "userId",
    "movieId",
    "movie_categoryId",
    "reviewId",
    "movieRating",
    "reviewDate",
]


def load_ratings(path: str | Path = "data/raw/movie-ratings.txt") -> pd.DataFrame:
    """Load the raw movie-ratings.txt file into a DataFrame.

    Parameters
    ----------
    path : str or Path
        Path to movie-ratings.txt. Defaults to ``data/raw/movie-ratings.txt``
        (the suggested project layout).

    Returns
    -------
    pandas.DataFrame
        DataFrame with the 6 CiaoDVD columns.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"Could not find {path}. "
            "Download CiaoDVD from https://guoguibing.github.io/librec/datasets.html "
            "and place movie-ratings.txt in data/raw/."
        )

    return pd.read_csv(path, names=COLUMNS, header=None)


if __name__ == "__main__":
    # Quick sanity check when running this module directly.
    df = load_ratings()
    print(f"Loaded {len(df):,} ratings")
    print(df.head())
