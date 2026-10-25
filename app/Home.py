"""AFML Cross-Asset Lab - landing page. Run with: streamlit run app/Home.py"""
import sys
from pathlib import Path

import plotly.graph_objects as go
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from afml_lab.data.sources.yahoo import load_daily  # noqa: E402
from afml_lab.factors.registry import FACTORS  # noqa: E402

st.set_page_config(page_title="AFML Cross-Asset Lab", page_icon="🌐", layout="wide")

st.title("🌐 AFML Cross-Asset Lab")
st.markdown(
    "An implementation of **Advances in Financial Machine Learning** (López de Prado, 2018) "
    "that trades **crypto** and conditions on **cross-asset factors** from equities, rates, FX, "
    "commodities, stablecoins and tokenized real-world assets."
)

MODULES = [
    ("1 · Data Structures", "Ch 2", "Dollar / imbalance bars and CUSUM sampling on BTC tick data"),
    ("2 · Labeling", "Ch 3", "Triple-barrier labels and meta-labeling on a momentum / funding-carry signal"),
    ("3 · Weights & Fracdiff", "Ch 4-5", "Label uniqueness, stationary features that keep memory"),
    ("4 · Cross-Asset Factors", "Ch 5, 8", "Point-in-time factor matrix and which factors actually matter"),
    ("5 · Modeling & Purged CV", "Ch 6-9", "Random forest, purged k-fold vs naive k-fold"),
    ("6 · Bet Sizing", "Ch 10", "From predicted probability to position size"),
    ("7 · Backtest Lab", "Ch 11-15", "CPCV paths, PSR / DSR, implied precision"),
    ("8 · Crypto Portfolio", "Ch 16", "HRP vs inverse-variance vs min-variance across coins / strategies"),
    ("9 · Regimes & Microstructure", "Ch 17-19", "SADF bubbles, entropy, VPIN, Kyle's lambda"),
]
st.subheader("Pipeline")
st.dataframe(
    {"Module": [m[0] for m in MODULES], "Book": [m[1] for m in MODULES], "What it shows": [m[2] for m in MODULES]},
    hide_index=True,
    use_container_width=True,
)

st.subheader("Factor universe")
st.dataframe(
    {"Factor": [f.name for f in FACTORS], "Asset class": [f.asset_class for f in FACTORS],
     "Source": [f.source for f in FACTORS], "Publication lag": [f.lag for f in FACTORS],
     "Why": [f.description for f in FACTORS]},
    hide_index=True,
    use_container_width=True,
)

st.subheader("Market snapshot")
ticker = st.selectbox("Instrument", ["BTC-USD", "ETH-USD", "SOL-USD"])


@st.cache_data(ttl=3600)
def _load(t):
    return load_daily(t, start="2020-01-01")


try:
    df = _load(ticker)
    fig = go.Figure(go.Candlestick(x=df.index, open=df["open"], high=df["high"], low=df["low"], close=df["close"]))
    fig.update_layout(height=420, xaxis_rangeslider_visible=False, margin=dict(l=0, r=0, t=10, b=0))
    st.plotly_chart(fig, use_container_width=True)
except Exception as exc:  # network / Yahoo hiccups shouldn't break the landing page
    st.warning(f"Could not load {ticker}: {exc}")
