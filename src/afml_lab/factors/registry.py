"""What we trade (crypto targets) and what we condition on (cross-asset factors).

``lag`` is how long after its timestamp a value can actually be known, so a factor
never leaks into a bar that precedes its publication. Daily closes stamped at 00:00
UTC get ``1D`` (conservative: usable from the next UTC midnight).
Swap ``source`` to "lseg" / "spglobal" once institutional feeds are available.
"""
from __future__ import annotations

from dataclasses import dataclass

TARGETS = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]


@dataclass(frozen=True)
class Factor:
    name: str
    asset_class: str
    source: str
    ticker: str
    lag: str
    description: str


FACTORS = [
    # equities: risk appetite, crypto-equity beta
    Factor("spx", "equity", "yahoo", "SPY", "1D", "S&P 500 ETF"),
    Factor("ndx", "equity", "yahoo", "QQQ", "1D", "Nasdaq-100 ETF, highest crypto beta"),
    Factor("coin", "equity", "yahoo", "COIN", "1D", "Coinbase, crypto-equity bridge"),
    Factor("vix", "equity", "yahoo", "^VIX", "1D", "Equity implied vol"),
    # rates: liquidity and discount rate
    Factor("ust10y", "rates", "fred", "DGS10", "2D", "10Y Treasury yield"),
    Factor("ust2y", "rates", "fred", "DGS2", "2D", "2Y Treasury yield, policy expectations"),
    Factor("real10y", "rates", "fred", "DFII10", "2D", "10Y real yield"),
    # FX: dollar liquidity and funding currencies
    Factor("dxy", "fx", "yahoo", "DX-Y.NYB", "1D", "US dollar index"),
    Factor("usdjpy", "fx", "yahoo", "JPY=X", "1D", "Yen carry funding"),
    Factor("usdcnh", "fx", "yahoo", "CNH=X", "1D", "Offshore yuan, Asian flow"),
    # commodities
    Factor("gold", "commodity", "yahoo", "GC=F", "1D", "Gold, alternative store of value"),
    # crypto-native cross-market
    Factor("btc_funding", "crypto_derivs", "binance", "BTCUSDT", "0h", "USD-M perp funding rate, crypto carry"),
    Factor("stablecoin_mcap", "stablecoin", "defillama", "all", "1D", "Total stablecoin supply, on-chain USD liquidity"),
    # tokenized real-world assets
    Factor("rwa_tvl", "rwa", "defillama", "RWA", "1D", "Tokenized RWA TVL (treasuries, credit)"),
]


def by_asset_class(asset_class: str) -> list[Factor]:
    return [f for f in FACTORS if f.asset_class == asset_class]


def get(name: str) -> Factor:
    return next(f for f in FACTORS if f.name == name)
