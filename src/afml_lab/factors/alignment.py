"""Point-in-time alignment of slow cross-asset factors onto fast crypto bars.

Crypto trades 24/7 on event-driven bars; factors are daily, business-day only and
published with delay. Every factor value is shifted forward by its publication lag
and then forward-filled, so a bar only sees what was knowable at its timestamp.
"""
from __future__ import annotations

import pandas as pd


def _to_utc(index: pd.DatetimeIndex) -> pd.DatetimeIndex:
    return index.tz_localize("UTC") if index.tz is None else index.tz_convert("UTC")


def align_to_bars(bar_index: pd.DatetimeIndex, factor: pd.Series, lag: str) -> pd.Series:
    """Value of ``factor`` known at each bar time, given its publication ``lag``."""
    known = factor.dropna().copy()
    known.index = _to_utc(pd.DatetimeIndex(known.index)) + pd.Timedelta(lag)
    known = known[~known.index.duplicated(keep="last")].sort_index()
    return known.reindex(_to_utc(bar_index), method="ffill").rename(factor.name)


def build_factor_matrix(bar_index: pd.DatetimeIndex, factors: dict[str, pd.Series],
                        lags: dict[str, str]) -> pd.DataFrame:
    """Align several factors at once; columns follow the order of ``factors``."""
    return pd.concat(
        [align_to_bars(bar_index, s.rename(name), lags[name]) for name, s in factors.items()], axis=1
    )
