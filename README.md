# 💱 AFML FX Lab

An FX trader's hands-on implementation of **_Advances in Financial Machine Learning_** (Marcos López de Prado, Wiley 2018), applied to G10 and Asian currency pairs, delivered as an interactive Streamlit app.

> Goal: show the full research pipeline the book argues for, from **raw ticks → bars → labels → features → purged CV → bet sizing → overfitting-aware backtest → portfolio allocation**, using FX markets I trade every day.

## Why FX is an interesting testbed

| AFML idea | FX-specific twist |
|---|---|
| Volume / dollar bars (Ch 2) | Spot FX has no consolidated volume, so I use tick-count bars on spot, or CME futures (6E, 6J) for real volume |
| Triple-barrier labels (Ch 3) | Barriers scaled by daily vol; vertical barrier aligned with fixing / rollover times |
| Meta-labeling (Ch 3) | Primary model = classic desk signals (carry, momentum, fixing flow); ML only decides *whether* and *how big* |
| Structural breaks (Ch 17) | Detect central-bank intervention / de-pegs (USD/TWD, USD/JPY 2022, CHF 2015) |
| Microstructure (Ch 19) | Corwin-Schultz spreads on daily OHLC as an FX liquidity gauge |
| HRP (Ch 16) | G10 currencies are highly correlated (USD bloc vs EUR bloc), the exact case where Markowitz breaks down |

## App modules

| # | Page | Book | Status |
|---|---|---|---|
| 1 | Data Structures | Ch 2 | ⬜ |
| 2 | Labeling & Meta-labeling | Ch 3 | ⬜ |
| 3 | Fractional Differentiation | Ch 5 | ⬜ |
| 4 | Modeling & Purged CV | Ch 4, 6–9 | ⬜ |
| 5 | Bet Sizing | Ch 10 | ⬜ |
| 6 | Backtest Lab (CPCV, PSR/DSR) | Ch 11–15 | ⬜ |
| 7 | HRP Allocation | Ch 16 | ⬜ |
| 8 | Regimes & Microstructure | Ch 17–19 | ⬜ |

## Project structure

```
afml-fx-lab/
├── app/                    # Streamlit UI (presentation only, no math here)
│   ├── Home.py
│   └── pages/1_…8_*.py     # one page per module
├── src/afml_fx/            # reusable library: all AFML logic lives here
│   ├── data/               # loaders, bars, CUSUM filter          (Ch 2)
│   ├── labeling/           # triple barrier, meta-labels           (Ch 3)
│   ├── weights/            # concurrency, uniqueness, seq. bootstrap (Ch 4)
│   ├── features/           # fracdiff, SADF, entropy, microstructure (Ch 5, 17-19)
│   ├── cv/                 # PurgedKFold, CPCV                     (Ch 7, 12)
│   ├── models/             # feature importance MDI/MDA/SFI        (Ch 8)
│   ├── sizing/             # bet sizing                            (Ch 10)
│   ├── backtest/           # drawdown, PSR, DSR, strategy risk     (Ch 14-15)
│   └── portfolio/          # HRP                                   (Ch 16)
├── notebooks/              # per-chapter research notebooks / exercises
├── tests/                  # pytest unit tests for every library function
└── data/                   # local only (git-ignored)
```

## Quick start

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows  (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
streamlit run app/Home.py
pytest
```

## Data sources

- **Daily OHLC**: Yahoo Finance via `yfinance` (`EURUSD=X`, `TWD=X`, …)
- **Tick data**: [Dukascopy](https://www.dukascopy.com/swiss/english/marketwatch/historical/) or [HistData](https://www.histdata.com/) CSVs → `data/`
- **Rates for carry**: FRED policy-rate / interbank series

## References

- López de Prado, M. (2018). *Advances in Financial Machine Learning*. Wiley.
- Papers: [quantresearch.org](https://www.quantresearch.org)

*Code is my own re-implementation for learning purposes; the book itself is not distributed in this repo.*
