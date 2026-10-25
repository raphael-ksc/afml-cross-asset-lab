"""AFML FX Lab - landing page. Run with: streamlit run app/Home.py"""
import sys
from pathlib import Path

import plotly.graph_objects as go
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from afml_fx.data.loader import ASIA_PAIRS, G10_PAIRS, load_daily  # noqa: E402

st.set_page_config(page_title="AFML FX Lab", page_icon="💱", layout="wide")

st.title("💱 AFML FX Lab")
st.markdown(
    "An FX trader's implementation of **Advances in Financial Machine Learning** "
    "(López de Prado, 2018): from raw ticks to a deflated-Sharpe-validated, HRP-allocated FX strategy."
)

MODULES = [
    ("1 · Data Structures", "Ch 2", "Tick / imbalance bars and CUSUM sampling on EUR/USD ticks"),
    ("2 · Labeling", "Ch 3", "Triple-barrier labels and meta-labeling on a carry / momentum signal"),
    ("3 · Fractional Differentiation", "Ch 5", "Stationary features that keep memory"),
    ("4 · Modeling & Purged CV", "Ch 4, 6-9", "Uniqueness weights, purged k-fold, MDI / MDA / SFI"),
    ("5 · Bet Sizing", "Ch 10", "From predicted probability to position size"),
    ("6 · Backtest Lab", "Ch 11-15", "CPCV paths, PSR / DSR, implied precision"),
    ("7 · HRP Allocation", "Ch 16", "G10 FX basket: HRP vs inverse-variance vs min-variance"),
    ("8 · Regimes & Microstructure", "Ch 17-19", "SADF, entropy, Corwin-Schultz spreads"),
]
st.subheader("Pipeline")
st.dataframe(
    {"Module": [m[0] for m in MODULES], "Book": [m[1] for m in MODULES], "What it shows": [m[2] for m in MODULES]},
    hide_index=True,
    use_container_width=True,
)

st.subheader("Market snapshot")
ticker = st.selectbox("FX pair", G10_PAIRS + ASIA_PAIRS, index=G10_PAIRS.index("EURUSD=X"))


@st.cache_data(ttl=3600)
def _load(t):
    return load_daily(t, start="2018-01-01")


try:
    df = _load(ticker)
    fig = go.Figure(go.Candlestick(x=df.index, open=df["Open"], high=df["High"], low=df["Low"], close=df["Close"]))
    fig.update_layout(height=420, xaxis_rangeslider_visible=False, margin=dict(l=0, r=0, t=10, b=0))
    st.plotly_chart(fig, use_container_width=True)
except Exception as exc:  # network / Yahoo hiccups shouldn't break the landing page
    st.warning(f"Could not load {ticker}: {exc}")
