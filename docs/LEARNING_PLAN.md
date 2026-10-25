# Learning Plan: AFML, Crypto Target + Cross-Asset Factors (~16 weeks, ~8–10 h/week)

Each phase ends with **one shipped app page + unit tests + a notebook**. Commit weekly so the GitHub history shows steady progress.

Priority: ★★★ core · ★★ important · ★ skim

## Phase 0: Setup & Chapter 1 (week 1)
- [ ] Ch 1 ★★ Why financial ML projects fail; the "strategy factory" mindset
- [ ] Pull one week of BTCUSDT aggTrades (`load_agg_trades_range`) and the factor series
- **Ship:** Home page ✅

## Phase 1: Data Analysis (weeks 2–5) → Pages 1–3
- [ ] Ch 2 ★★★ Tick / volume / dollar / imbalance bars, CUSUM filter. *Exercise:* compare normality and serial correlation of time vs dollar bars on BTC
- [ ] Ch 3 ★★★ Dynamic thresholds, triple barrier, **meta-labeling**. *Exercise:* primary = momentum or funding-rate signal, secondary = RF bet / no-bet
- [ ] Ch 4 ★★★ Concurrency, average uniqueness, sequential bootstrap, time decay
- [ ] Ch 5 ★★★ FFD; minimum stationary d for BTC, ETH and each factor
- **Ship:** Pages 1, 2, 3

## Phase 2: Factors & Modelling (weeks 6–9) → Pages 4–5
- [ ] Factor pipeline: implement DefiLlama + funding loaders, build the point-in-time factor matrix
- [ ] Ch 6 ★★ Bagging vs boosting; RF with `max_samples = avg uniqueness`
- [ ] Ch 7 ★★★ Purged K-Fold + embargo (key interview topic: leakage)
- [ ] Ch 8 ★★★ MDI / MDA / SFI, substitution effects, orthogonal features. **Core question:** which cross-asset factors matter for crypto?
- [ ] Ch 9 ★★ Randomized search, log-uniform priors, neg-log-loss scoring
- **Ship:** Page 4 (factor explorer + importance), Page 5 (naive vs purged CV)

## Phase 3: Backtesting & Portfolio (weeks 10–14) → Pages 6–8
- [ ] Ch 10 ★★ Bet sizing from probabilities, averaging active bets
- [ ] Ch 11 ★★ The seven sins of backtesting; selection bias
- [ ] Ch 12 ★★★ Walk-forward vs CV vs **CPCV**
- [ ] Ch 13 ★ Optimal trading rules on synthetic O-U data
- [ ] Ch 14 ★★★ Drawdown, TuW, HHI, **PSR & DSR**: does adding factors survive deflation?
- [ ] Ch 15 ★★ Implied precision, probability of strategy failure
- [ ] Ch 16 ★★★ **HRP** across coins and strategies vs IVP vs min-variance
- **Ship:** Pages 6, 7, 8

## Phase 4: Regimes & Microstructure (week 15) → Page 9
- [ ] Ch 17 ★★ CUSUM tests, **SADF** on crypto bubbles
- [ ] Ch 18 ★ Entropy as a market-efficiency gauge
- [ ] Ch 19 ★★ Roll, Corwin-Schultz, Kyle / Amihud lambda, **VPIN** with real signed volume

## Phase 5: HPC & Polish (week 16)
- [ ] Ch 20 ★ Vectorization, multiprocessing (`joblib`) for bars and CV
- [ ] Ch 21–22 ★ Skim
- [ ] Deploy to Streamlit Community Cloud; add screenshots / GIF to README
- [ ] Case study in README: end-to-end BTC meta-labeling strategy, with and without cross-asset factors, compared by DSR

## Interview talking points
1. Why standard K-Fold leaks, and how purging, embargo and point-in-time factor lags fix it
2. Meta-labeling: separating side (view) from size (ML)
3. Which cross-asset factors drive crypto, and how MDA / SFI handle their collinearity
4. Deflated Sharpe: how many trials did you run?
5. HRP vs Markowitz on correlated assets
