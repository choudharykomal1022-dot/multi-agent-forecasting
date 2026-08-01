#  Multi-Agent Financial Forecasting & Game-Theoretic Referee

[![Live Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://multi-agent-forecasting-vfjklg36dptbikplrehhha.streamlit.app/)
![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)


##  One-Line Pitch

An algorithmic trading framework combining specialized machine learning agents via Hedge ensembling to forecast daily SPY returns.

---

##  Live Interactive Dashboard

Explore live forecasts, interactive backtests, and agent weight evolution:  
👉 **[Launch Live Streamlit Dashboard](https://multi-agent-forecasting-vfjklg36dptbikplrehhha.streamlit.app/)**

---

##  Architecture & Pipeline

This project employs a multi-agent framework where specialized quantitative models generate independent daily log-return predictions. The individual forecasts are dynamically weighted using a game-theoretic **Hedge Aggregator**, fed into a walk-forward backtest, and visualized in real time.

```text
┌─────────────────┐
│   TrendAgent    │──────┐
└─────────────────┘      │
┌─────────────────┐      │
│  MomentumAgent  │──────┤     ┌──────────────────┐     ┌──────────────────────┐     ┌────────────────────┐
└─────────────────┘      ├────►│ Hedge Aggregator │────►│ Walk-Forward Backtest│────►│ Streamlit Dashboard│
┌─────────────────┐      │     └──────────────────┘     └──────────────────────┘     └────────────────────┘
│ VolatilityAgent │──────┤
└─────────────────┘      │
┌─────────────────┐      │
│  SequenceAgent  │──────┘
└─────────────────┘
