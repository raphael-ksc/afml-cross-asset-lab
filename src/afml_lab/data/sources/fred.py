"""FRED (St. Louis Fed) series via the public CSV endpoint, no API key required."""
from __future__ import annotations

import pandas as pd

CSV_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"


def load_series(series_id: str) -> pd.Series:
    """Download one FRED series (e.g. ``DGS10``) as a float Series indexed by date."""
    df = pd.read_csv(CSV_URL.format(series_id=series_id), index_col=0, parse_dates=True, na_values=".")
    return df.iloc[:, 0].astype(float).rename(series_id).dropna()
