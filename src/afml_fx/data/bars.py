"""Chapter 2 - Financial Data Structures.

FX note: spot FX has no centralized volume, so use tick count as the activity
proxy, or CME FX futures (6E, 6J) when real volume is needed.
"""
import pandas as pd


def tick_bars(ticks: pd.DataFrame, threshold: int):
    """Sample an OHLC bar every ``threshold`` ticks (AFML 2.3.1)."""
    raise NotImplementedError("TODO: Chapter 2.3.1")


def volume_bars(ticks: pd.DataFrame, threshold: float):
    """Sample a bar every ``threshold`` units of traded volume (AFML 2.3.1)."""
    raise NotImplementedError("TODO: Chapter 2.3.1")


def tick_imbalance_bars(ticks: pd.DataFrame, ewma_span: int = 100):
    """Information-driven bars sampled on tick-rule imbalance (AFML 2.3.2)."""
    raise NotImplementedError("TODO: Chapter 2.3.2")


def cusum_filter(close: pd.Series, h: float):
    """Symmetric CUSUM filter for event-based sampling (AFML 2.5.2.1, Snippet 2.4)."""
    raise NotImplementedError("TODO: Chapter 2.5.2")
