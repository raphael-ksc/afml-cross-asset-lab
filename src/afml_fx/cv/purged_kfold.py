"""Chapters 7 & 12 - Purged K-Fold and Combinatorial Purged CV."""
import pandas as pd
from sklearn.model_selection import KFold


class PurgedKFold(KFold):
    """K-Fold that purges overlapping labels and applies an embargo (Snippet 7.3)."""

    def __init__(self, n_splits: int = 5, t1: pd.Series | None = None, pct_embargo: float = 0.0):
        super().__init__(n_splits=n_splits, shuffle=False)
        self.t1 = t1
        self.pct_embargo = pct_embargo

    def split(self, X, y=None, groups=None):
        raise NotImplementedError("TODO: Chapter 7.4")


class CombinatorialPurgedKFold:
    """CPCV: N groups, k test groups -> multiple backtest paths (Chapter 12.4)."""

    def __init__(self, n_groups: int = 6, k_test: int = 2, t1: pd.Series | None = None,
                 pct_embargo: float = 0.0):
        self.n_groups, self.k_test, self.t1, self.pct_embargo = n_groups, k_test, t1, pct_embargo

    def split(self, X, y=None, groups=None):
        raise NotImplementedError("TODO: Chapter 12.4")
