"""Chapter 4 - Sample Weights."""
import pandas as pd


def num_concurrent_events(close_idx: pd.DatetimeIndex, t1: pd.Series):
    """Number of labels alive at each bar (Snippet 4.1)."""
    raise NotImplementedError("TODO: Chapter 4.3")


def average_uniqueness(t1: pd.Series, num_co_events: pd.Series):
    """Average uniqueness of each label over its lifespan (Snippet 4.2)."""
    raise NotImplementedError("TODO: Chapter 4.4")


def sequential_bootstrap(ind_matrix: pd.DataFrame, s_length: int | None = None):
    """Draw samples favouring low-overlap observations (Snippet 4.5)."""
    raise NotImplementedError("TODO: Chapter 4.5")
