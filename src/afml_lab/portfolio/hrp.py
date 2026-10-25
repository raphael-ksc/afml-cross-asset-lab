"""Chapter 16 - Hierarchical Risk Parity, e.g. allocating across a basket of crypto assets."""
import pandas as pd


def hrp_weights(returns: pd.DataFrame):
    """Tree clustering -> quasi-diagonalization -> recursive bisection (Snippets 16.1-16.4)."""
    raise NotImplementedError("TODO: Chapter 16.4")


def inverse_variance_weights(cov: pd.DataFrame):
    """Inverse-variance portfolio, the HRP benchmark (16.A.2)."""
    raise NotImplementedError("TODO: Chapter 16.A.2")
