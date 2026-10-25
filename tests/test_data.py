import numpy as np
import pandas as pd

from afml_lab.data.schema import tick_rule
from afml_lab.data.sources.binance import parse_agg_trades
from afml_lab.factors.alignment import align_to_bars, build_factor_matrix
from afml_lab.factors.registry import FACTORS

SPOT_CSV = (
    b"1,42000.5,0.10,1,1,1704067200000,True,True\n"
    b"2,42001.0,0.25,2,3,1704067200500,False,True\n"
)
FUTURES_CSV = (
    b"agg_trade_id,price,quantity,first_trade_id,last_trade_id,transact_time,is_buyer_maker\n"
    b"1,42000.5,0.10,1,1,1704067200000,true\n"
)
SPOT_2025_CSV = b"1,94000.0,0.01,1,1,1735689600000000,False,True\n"


def test_parse_spot_agg_trades():
    ticks = parse_agg_trades(SPOT_CSV)
    assert list(ticks.columns) == ["price", "volume", "side"]
    assert ticks["side"].tolist() == [-1, 1]  # buyer-maker = sell aggressor
    assert ticks.index[0] == pd.Timestamp("2024-01-01", tz="UTC")


def test_parse_futures_with_header():
    ticks = parse_agg_trades(FUTURES_CSV)
    assert ticks["price"].iloc[0] == 42000.5
    assert ticks["side"].iloc[0] == -1


def test_parse_microsecond_timestamps():
    assert parse_agg_trades(SPOT_2025_CSV).index[0] == pd.Timestamp("2025-01-01", tz="UTC")


def test_tick_rule_carries_side_through_unchanged_prices():
    side = tick_rule(pd.Series([1.0, 2.0, 2.0, 1.5, 1.5]))
    assert np.isnan(side.iloc[0])
    assert side.iloc[1:].tolist() == [1, 1, -1, -1]


def test_alignment_respects_publication_lag():
    factor = pd.Series([4.0, 4.1], index=pd.to_datetime(["2024-01-01", "2024-01-02"]), name="ust10y")
    bars = pd.DatetimeIndex(["2024-01-01 12:00", "2024-01-02 00:00", "2024-01-02 23:59", "2024-01-03 00:00"],
                            tz="UTC")
    aligned = align_to_bars(bars, factor, lag="1D")
    assert np.isnan(aligned.iloc[0])  # not yet published
    assert aligned.iloc[1:].tolist() == [4.0, 4.0, 4.1]


def test_factor_matrix_columns():
    idx = pd.DatetimeIndex(["2024-01-05"], tz="UTC")
    s = pd.Series([1.0], index=pd.to_datetime(["2024-01-01"]))
    m = build_factor_matrix(idx, {"a": s, "b": s}, {"a": "1D", "b": "2D"})
    assert list(m.columns) == ["a", "b"]


def test_factor_names_unique():
    names = [f.name for f in FACTORS]
    assert len(names) == len(set(names))
