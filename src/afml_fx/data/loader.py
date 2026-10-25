"""FX data loaders.

Daily OHLC comes from Yahoo Finance (e.g. ``EURUSD=X``, ``TWD=X``).
Tick data for Chapter 2 bars should come from Dukascopy / HistData CSVs placed in ``data/``.
"""
from __future__ import annotations

import pandas as pd

G10_PAIRS = ["EURUSD=X", "GBPUSD=X", "AUDUSD=X", "NZDUSD=X",
             "USDJPY=X", "USDCHF=X", "USDCAD=X", "USDSEK=X", "USDNOK=X"]
ASIA_PAIRS = ["TWD=X", "CNH=X", "KRW=X", "SGD=X"]


def load_daily(ticker: str, start: str = "2010-01-01") -> pd.DataFrame:
    """Download daily OHLC for one FX ticker."""
    import yfinance as yf

    df = yf.download(ticker, start=start, auto_adjust=False, progress=False)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    return df[["Open", "High", "Low", "Close"]].dropna()


def load_ticks_csv(path: str) -> pd.DataFrame:
    """Load a tick CSV with columns: timestamp, bid, ask[, bid_volume, ask_volume].

    Returns a frame indexed by timestamp with a ``mid`` column added.
    """
    df = pd.read_csv(path, parse_dates=["timestamp"], index_col="timestamp")
    df["mid"] = (df["bid"] + df["ask"]) / 2
    return df
