"""DefiLlama public API: stablecoin supply and RWA TVL, free, no API key."""
from __future__ import annotations

import pandas as pd


def load_stablecoin_mcap() -> pd.Series:
    """Total stablecoin circulating supply in USD, daily."""
    raise NotImplementedError("TODO: stablecoins.llama.fi stablecoincharts endpoint")


def load_rwa_tvl() -> pd.Series:
    """Total value locked in the RWA protocol category, daily."""
    raise NotImplementedError("TODO: api.llama.fi protocol / category TVL endpoint")
