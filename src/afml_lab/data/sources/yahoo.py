"""Daily bars from Yahoo Finance: crypto snapshots and equity / FX / commodity factor proxies.

Yahoo is reachable from Streamlit Community Cloud (US servers), whereas api.binance.com is geo-blocked there.
"""
from __future__ import annotations

import pandas as pd

from afml_lab.data.schema import DAILY_COLUMNS


def load_daily(ticker: str, start: str = "2018-01-01") -> pd.DataFrame:
    """Download daily OHLCV for one ticker in the canonical daily schema."""
    import yfinance as yf

    df = yf.download(ticker, start=start, auto_adjust=False, progress=False)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df.columns = df.columns.str.lower()
    df.index = df.index.tz_localize("UTC")
    return df[DAILY_COLUMNS].dropna(subset=["close"])
