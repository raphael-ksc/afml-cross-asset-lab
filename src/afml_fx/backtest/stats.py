"""Chapters 14-15 - Backtest Statistics and Strategy Risk."""
import pandas as pd


def drawdown_and_time_under_water(pnl: pd.Series):
    """Drawdown and time-under-water series (Snippet 14.4)."""
    raise NotImplementedError("TODO: Chapter 14.5.2")


def probabilistic_sharpe_ratio(sr: float, sr_benchmark: float, n: int, skew: float, kurt: float):
    """PSR: probability the true SR exceeds a benchmark (14.7.2)."""
    raise NotImplementedError("TODO: Chapter 14.7.2")


def deflated_sharpe_ratio(sr: float, sr_trials: list[float], n: int, skew: float, kurt: float):
    """DSR: PSR adjusted for the number of strategies tried (14.7.3)."""
    raise NotImplementedError("TODO: Chapter 14.7.3")


def implied_precision(stop_loss: float, profit_taking: float, freq: float, target_sr: float):
    """Minimum hit rate needed to reach a target SR (Snippet 15.3)."""
    raise NotImplementedError("TODO: Chapter 15.3")
