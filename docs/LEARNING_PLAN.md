# Learning Plan: AFML for an FX Trader (~16 weeks, ~8–10 h/week)

Each phase ends with **one shipped app page + unit tests + a notebook**. Ship weekly commits so the GitHub history itself shows steady progress.

Priority: ★★★ core (must master) · ★★ important · ★ skim

## Phase 0 — Setup & Chapter 1 (week 1)
- [ ] Ch 1 ★★ Why financial ML projects fail; the "strategy factory" mindset
- [ ] Python refresh: pandas time-series indexing, numpy vectorization, sklearn API
- [ ] Get data: yfinance daily G10 + TWD; one month of EUR/USD ticks from Dukascopy
- **Ship:** Home page running locally

## Phase 1 — Data Analysis (weeks 2–5) → Pages 1–3
- [ ] Ch 2 ★★★ Bars (tick / volume / dollar / imbalance), CUSUM filter. *Exercise:* compare return normality & serial correlation of time vs tick bars on EUR/USD
- [ ] Ch 3 ★★★ Dynamic thresholds, triple-barrier, **meta-labeling**. *Exercise:* primary = MA-crossover or carry signal, secondary = RF deciding bet/no-bet
- [ ] Ch 4 ★★★ Concurrency, average uniqueness, sequential bootstrap, time decay
- [ ] Ch 5 ★★★ Fractional differentiation (FFD); find minimum d that passes ADF for each G10 pair
- **Ship:** Pages 1, 2, 3

## Phase 2 — Modelling (weeks 6–8) → Page 4
- [ ] Ch 6 ★★ Bagging vs boosting in finance; why RF with `max_samples = avg uniqueness`
- [ ] Ch 7 ★★★ Purged K-Fold + embargo (key interview topic: leakage)
- [ ] Ch 8 ★★★ MDI / MDA / SFI, substitution effects, PCA-orthogonal features
- [ ] Ch 9 ★★ Randomized search, log-uniform priors, scoring by neg-log-loss
- **Ship:** Page 4 showing naive KFold vs PurgedKFold score inflation

## Phase 3 — Backtesting (weeks 9–13) → Pages 5–7
- [ ] Ch 10 ★★ Bet sizing from probabilities, averaging active bets, discretization
- [ ] Ch 11 ★★ The seven sins of backtesting; selection bias
- [ ] Ch 12 ★★★ Walk-forward vs CV vs **CPCV** (distribution of Sharpe ratios)
- [ ] Ch 13 ★ Optimal trading rules on synthetic O-U data (good for mean-reverting crosses)
- [ ] Ch 14 ★★★ Drawdown, TuW, HHI concentration, **PSR & DSR**
- [ ] Ch 15 ★★ Implied precision / probability of strategy failure, relate to desk stop-loss limits
- [ ] Ch 16 ★★★ **HRP** on a G10 basket vs IVP vs min-variance, out-of-sample Monte Carlo
- **Ship:** Pages 5, 6, 7

## Phase 4 — Useful Features (weeks 14–15) → Page 8
- [ ] Ch 17 ★★ CUSUM tests, **SADF**: flag CB intervention episodes
- [ ] Ch 18 ★ Entropy (plug-in, Lempel-Ziv) as a market-efficiency gauge
- [ ] Ch 19 ★★ Roll, Corwin-Schultz, Kyle/Amihud lambda, VPIN (on futures)
- **Ship:** Page 8

## Phase 5 — HPC & Polish (week 16)
- [ ] Ch 20 ★ Vectorization, `mpPandasObj` idea; use `joblib` for the slow loops
- [ ] Ch 21–22 ★ Skim only
- [ ] Deploy to Streamlit Community Cloud, add screenshots/GIF to README
- [ ] Write a short "Case study" in README: one end-to-end FX meta-labeling strategy with DSR

## Interview talking points to prepare
1. Why standard K-Fold leaks in finance, and how purging and embargo fix it
2. Meta-labeling: separating side (trader's view) from size (ML)
3. Deflated Sharpe: how many trials did you run?
4. Why HRP beats Markowitz on correlated FX baskets
