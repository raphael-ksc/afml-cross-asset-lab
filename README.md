# 🌐 AFML Cross-Asset Lab

A hands-on implementation of **_Advances in Financial Machine Learning_** (Marcos López de Prado, Wiley 2018), delivered as an interactive Streamlit app.

**Trade crypto, condition on everything else.** The strategy universe is crypto (BTC, ETH, SOL), built from free tick-level trade data. Equities, rates, FX, commodities, stablecoin supply and tokenized real-world assets enter as **point-in-time cross-asset factors**.

> Research question: do cross-asset factors improve a meta-labeled crypto strategy **after** purged cross-validation and the deflated Sharpe ratio?

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the data-flow diagram and design rules, and [docs/LEARNING_PLAN.md](docs/LEARNING_PLAN.md) for the chapter-by-chapter roadmap.

## Why crypto as the target

| AFML idea | Why crypto fits |
|---|---|
| Dollar / imbalance bars (Ch 2) | Free trade-level data with real volume and aggressor side (Binance aggTrades) |
| Meta-labeling (Ch 3) | Primary signal from momentum or perp **funding rate** (crypto's carry); ML decides whether and how big |
| Structural breaks (Ch 17) | Frequent bubbles and crashes: an ideal SADF testbed |
| Microstructure (Ch 19) | Signed volume makes VPIN and Kyle's lambda computable as in the book |
| HRP (Ch 16) | Coins are highly correlated, the case where Markowitz breaks down |

## Cross-asset factors

| Asset class | Examples | Source (free today) |
|---|---|---|
| Equity | SPY, QQQ, COIN, VIX | Yahoo |
| Rates | 2Y / 10Y / 10Y real yield | FRED |
| FX | DXY, USD/JPY, USD/CNH | Yahoo |
| Commodity | Gold | Yahoo |
| Crypto derivatives | Perp funding rate | Binance |
| Stablecoins / RWA | Stablecoin supply, tokenized RWA TVL | DefiLlama |

Each factor declares a publication lag, so it only reaches crypto bars once it was knowable.

## App modules

| # | Page | Book | Status |
|---|---|---|---|
| 1 | Data Structures | Ch 2 | ⬜ |
| 2 | Labeling & Meta-labeling | Ch 3 | ⬜ |
| 3 | Sample Weights & Fractional Differentiation | Ch 4–5 | ⬜ |
| 4 | Cross-Asset Factors | Ch 5, 8 | ⬜ |
| 5 | Modeling & Purged CV | Ch 6–9 | ⬜ |
| 6 | Bet Sizing | Ch 10 | ⬜ |
| 7 | Backtest Lab (CPCV, PSR/DSR) | Ch 11–15 | ⬜ |
| 8 | Crypto Portfolio (HRP) | Ch 16 | ⬜ |
| 9 | Regimes & Microstructure | Ch 17–19 | ⬜ |

## Project structure

```
├── app/                     # Streamlit UI (presentation only)
│   ├── Home.py
│   └── pages/1_…9_*.py
├── src/afml_lab/            # all logic, unit-tested
│   ├── data/
│   │   ├── schema.py        # canonical tick / daily frames
│   │   ├── sources/         # binance, yahoo, fred, defillama (lseg later)
│   │   └── bars.py          # Ch 2
│   ├── factors/
│   │   ├── registry.py      # TARGETS vs FACTORS, publication lags
│   │   └── alignment.py     # point-in-time join onto crypto bars
│   ├── labeling/            # Ch 3
│   ├── weights/             # Ch 4
│   ├── features/            # Ch 5, 17-19
│   ├── cv/                  # Ch 7, 12
│   ├── models/              # Ch 8
│   ├── sizing/              # Ch 10
│   ├── backtest/            # Ch 14-15
│   └── portfolio/           # Ch 16
├── notebooks/
├── tests/
└── docs/
```

## Quick start

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows  (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
pytest
streamlit run app/Home.py
```

```python
from afml_lab.data.sources.binance import load_agg_trades
ticks = load_agg_trades("BTCUSDT", "2025-06-01")   # ~650k trades, cached under data/
```

## References

- López de Prado, M. (2018). *Advances in Financial Machine Learning*. Wiley.
- Papers: [quantresearch.org](https://www.quantresearch.org)

*The code is my own re-implementation for learning. The book is not distributed in this repo. Nothing here is investment advice.*
