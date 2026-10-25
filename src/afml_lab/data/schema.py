"""Canonical data schemas shared by every asset class.

Every source adapter (Binance today; LSEG / S&P / futures later) converts its raw
format into these frames, so bars, labels and features never care where data came from.

Tick frame:   DatetimeIndex (UTC), columns ``price``, ``volume``, ``side``
              side = +1 buyer-initiated, -1 seller-initiated, NaN unknown
Daily frame:  DatetimeIndex (UTC), columns ``open``, ``high``, ``low``, ``close``, ``volume``
"""
from __future__ import annotations

import numpy as np
import pandas as pd

TICK_COLUMNS = ["price", "volume", "side"]
DAILY_COLUMNS = ["open", "high", "low", "close", "volume"]


def validate_ticks(df: pd.DataFrame) -> pd.DataFrame:
    """Check a tick frame conforms to the schema and is time-sorted."""
    missing = set(TICK_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"tick frame missing columns: {sorted(missing)}")
    if not isinstance(df.index, pd.DatetimeIndex):
        raise TypeError("tick frame must have a DatetimeIndex")
    if not df.index.is_monotonic_increasing:
        df = df.sort_index(kind="stable")
    return df[TICK_COLUMNS]


def tick_rule(price: pd.Series) -> pd.Series:
    """Infer trade side from price changes when the venue doesn't report it (AFML 19.3.1)."""
    sign = np.sign(price.diff())
    return sign.replace(0, np.nan).ffill()
