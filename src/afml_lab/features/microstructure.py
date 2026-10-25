"""Chapters 18-19 - Entropy and Microstructural Features."""
import pandas as pd


def roll_spread(close: pd.Series, window: int):
    """Roll (1984) effective spread estimator (19.3.2)."""
    raise NotImplementedError("TODO: Chapter 19.3.2")


def corwin_schultz_spread(high: pd.Series, low: pd.Series, window: int = 1):
    """Corwin-Schultz high-low spread estimator (19.3.4); works on daily OHLC when ticks are unavailable."""
    raise NotImplementedError("TODO: Chapter 19.3.4")


def lempel_ziv_entropy(message: str):
    """Lempel-Ziv entropy estimate of an encoded return series (18.4)."""
    raise NotImplementedError("TODO: Chapter 18.4")


def kyle_lambda(ticks: pd.DataFrame, window: int) -> pd.Series:
    """Kyle's lambda: price impact per unit of signed volume (19.4.1)."""
    raise NotImplementedError("TODO: Chapter 19.4.1")


def vpin(ticks: pd.DataFrame, bucket_volume: float, n_buckets: int = 50) -> pd.Series:
    """Volume-synchronized probability of informed trading (19.5.2)."""
    raise NotImplementedError("TODO: Chapter 19.5.2")
