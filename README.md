# 📈 Multi-Agent Financial Forecasting & Game-Theoretic Referee

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-app-url.streamlit.app/)
![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)
![Plotly](https://img.shields.io/badge/visualization-Plotly-orange.svg)

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

---

## 📁 Repository Structure

```text
├── app.py                   # Streamlit dashboard application
├── backtest_results.csv     # Historical predictions, actuals, and agent weights
├── metrics_report.csv       # Summary performance metrics (Sharpe ratio, Accuracy)
├── notebooks/               # Development notebooks (Pipeline -> Models -> Backtest)
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
