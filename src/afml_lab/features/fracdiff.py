"""Chapter 5 - Fractionally Differentiated Features."""
import pandas as pd


def get_weights_ffd(d: float, thres: float = 1e-5):
    """Weights of the fixed-width-window fractional difference operator (Snippet 5.3)."""
    raise NotImplementedError("TODO: Chapter 5.5.2")


def frac_diff_ffd(series: pd.Series, d: float, thres: float = 1e-5):
    """Apply FFD to a price series (Snippet 5.3)."""
    raise NotImplementedError("TODO: Chapter 5.5.2")


def min_d_for_stationarity(series: pd.Series, p_value: float = 0.05):
    """Scan d in [0, 1]: ADF stat and correlation with the original series (Snippet 5.4)."""
    raise NotImplementedError("TODO: Chapter 5.6")
