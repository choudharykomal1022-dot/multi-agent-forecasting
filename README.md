# 📈 Multi-Agent Financial Forecasting System

[![Live App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://multi-agent-forecasting-vfjklg36dptbikplrehhha.streamlit.app/)

> **Live Interactive Dashboard:** [Launch Multi-Agent Forecasting App](https://multi-agent-forecasting-vfjklg36dptbikplrehhha.streamlit.app/)

An end-to-end financial forecasting system powered by a multi-agent framework. The project creates a complete pipeline: engineering financial features, training four specialized forecasting agents, using a game-theoretic referee to dynamically adjust model weights over time, and hosting an interactive analytics dashboard.

---

## 🌟 Key Features

* **Multi-Agent Pipeline**: Combines predictions from specialized financial models (e.g., Volatility, Trend, Technicals) into an ensemble forecast.
* **Game-Theoretic Refereeing**: Dynamically re-allocates confidence weights to agents based on market regimes and historical performance.
* **Honest Backtesting**: Evaluates out-of-sample log-returns, directional accuracy, Sharpe ratios, and simulated equity growth.
* **Interactive Dashboard**: A multi-tab Streamlit dashboard offering real-time filtering of forecasts, agent weight evolution, and financial metrics.

---

## 📊 Dashboard Visualizations

| **Forecast vs. Actual** | **Agent Weight Allocation** |
| :---: | :---: |
| Compare ensemble log-return predictions against historical market actuals over customizable time windows. | Stacked area visualization tracking how trust shifts between agents during market events (e.g., 2020 crash). |

