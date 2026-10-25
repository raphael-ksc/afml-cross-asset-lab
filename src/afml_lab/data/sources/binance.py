"""Binance public bulk data (https://data.binance.vision), free, no API key.

aggTrades carry real volume and the aggressor side (``is_buyer_maker``), which lets
Chapter 2 imbalance bars and Chapter 19 VPIN / Kyle's lambda be built as in the book.
"""
from __future__ import annotations

import io
import urllib.request
import zipfile
from pathlib import Path

import pandas as pd

from afml_lab.data.schema import validate_ticks

BASE_URL = "https://data.binance.vision/data"
MARKETS = {"spot": "spot", "usdm": "futures/um"}
AGG_TRADE_COLUMNS = ["agg_trade_id", "price", "quantity", "first_trade_id",
                     "last_trade_id", "transact_time", "is_buyer_maker", "is_best_match"]


def agg_trades_url(symbol: str, day: str, market: str = "spot") -> str:
    """URL of one daily aggTrades zip, e.g. ``agg_trades_url("BTCUSDT", "2024-01-01")``."""
    return f"{BASE_URL}/{MARKETS[market]}/daily/aggTrades/{symbol}/{symbol}-aggTrades-{day}.zip"


def parse_agg_trades(csv_bytes: bytes) -> pd.DataFrame:
    """Convert a raw aggTrades CSV into the canonical tick schema."""
    first_line = csv_bytes.split(b"\n", 1)[0]
    has_header = not first_line[:1].isdigit()  # futures files ship a header, spot files don't
    raw = pd.read_csv(io.BytesIO(csv_bytes), header=0 if has_header else None,
                      names=None if has_header else AGG_TRADE_COLUMNS)
    raw.columns = AGG_TRADE_COLUMNS[: len(raw.columns)]
    ts = raw["transact_time"].astype("int64")
    # spot timestamps switched from milliseconds to microseconds on 2025-01-01
    unit = "us" if ts.iloc[0] > 10**14 else "ms"
    buyer_maker = raw["is_buyer_maker"].astype(str).str.lower() == "true"
    ticks = pd.DataFrame(
        {
            "price": raw["price"].astype(float).to_numpy(),
            "volume": raw["quantity"].astype(float).to_numpy(),
            # buyer is maker -> the seller crossed the spread -> sell-initiated
            "side": (~buyer_maker).astype(int).mul(2).sub(1).to_numpy(),
        },
        index=pd.to_datetime(ts, unit=unit, utc=True).rename("timestamp"),
    )
    return validate_ticks(ticks)


def load_agg_trades(symbol: str, day: str, market: str = "spot",
                    cache_dir: str | Path = "data/binance") -> pd.DataFrame:
    """Download (or read cached) one day of aggTrades as a canonical tick frame."""
    cache = Path(cache_dir) / market / symbol / f"{symbol}-aggTrades-{day}.zip"
    if not cache.exists():
        cache.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(agg_trades_url(symbol, day, market), cache)
    with zipfile.ZipFile(cache) as zf:
        return parse_agg_trades(zf.read(zf.namelist()[0]))


def load_agg_trades_range(symbol: str, start: str, end: str, market: str = "spot",
                          cache_dir: str | Path = "data/binance") -> pd.DataFrame:
    """Concatenate daily aggTrades for every day in [start, end]."""
    days = pd.date_range(start, end, freq="D").strftime("%Y-%m-%d")
    return pd.concat([load_agg_trades(symbol, d, market, cache_dir) for d in days])


def load_funding_rate(symbol: str, month: str, cache_dir: str | Path = "data/binance") -> pd.Series:
    """USD-M perpetual funding rate for one month (``YYYY-MM``), the crypto analogue of carry."""
    raise NotImplementedError("TODO: futures/um/monthly/fundingRate bulk files")
