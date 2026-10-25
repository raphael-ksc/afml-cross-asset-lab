"""Chapter 3 - Labeling."""
import pandas as pd


def daily_vol(close: pd.Series, span: int = 100):
    """EWM std of daily returns, used as dynamic barrier width (Snippet 3.1)."""
    raise NotImplementedError("TODO: Chapter 3.3")


def triple_barrier_events(close: pd.Series, t_events: pd.DatetimeIndex, pt_sl: tuple[float, float],
                          target: pd.Series, min_ret: float, num_days: int,
                          side: pd.Series | None = None):
    """First-touch time of profit-take / stop-loss / vertical barriers (Snippets 3.2-3.6)."""
    raise NotImplementedError("TODO: Chapter 3.4")


def get_bins(events: pd.DataFrame, close: pd.Series):
    """Label each event; with ``side`` present, produce meta-labels {0,1} (Snippet 3.7)."""
    raise NotImplementedError("TODO: Chapter 3.6")
