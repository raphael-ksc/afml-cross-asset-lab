"""Chapter 8 - Feature Importance."""
import pandas as pd


def mdi(fitted_forest, feature_names: list[str]):
    """Mean Decrease Impurity across trees (Snippet 8.2)."""
    raise NotImplementedError("TODO: Chapter 8.3.1")


def mda(clf, X: pd.DataFrame, y: pd.Series, cv, sample_weight: pd.Series, t1: pd.Series):
    """Mean Decrease Accuracy with purged CV (Snippet 8.3)."""
    raise NotImplementedError("TODO: Chapter 8.3.2")


def sfi(clf, X: pd.DataFrame, y: pd.Series, cv, sample_weight: pd.Series):
    """Single Feature Importance (Snippet 8.4)."""
    raise NotImplementedError("TODO: Chapter 8.4.1")
