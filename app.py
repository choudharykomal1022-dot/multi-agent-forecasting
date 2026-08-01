import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Multi-Agent Forecasting", layout="wide")
st.title("Multi-Agent Financial Forecasting")

@st.cache_data
def load():
    results = pd.read_csv("backtest_results.csv", index_col=0, parse_dates=True)
    report = pd.read_csv("metrics_report.csv")
    return results, report

results, report = load()
agent_names = [c[:-5] for c in results.columns if c.endswith("_pred") and c != "ensemble_pred"]

tab1, tab2, tab3 = st.tabs(["Forecast vs Actual", "Agent Weights", "Performance"])

with tab1:
    n = st.slider("Days to show", 50, len(results), 250)
    recent = results.tail(n)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=recent.index, y=recent["actual"], name="Actual", line=dict(color="black")))
    fig.add_trace(go.Scatter(x=recent.index, y=recent["ensemble_pred"], name="Ensemble"))
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(report)

with tab2:
    fig = go.Figure()
    for nm in agent_names:
        col = f"{nm}_weight"
        if col in results.columns:
            fig.add_trace(go.Scatter(x=results.index, y=results[col], name=nm, stackgroup="one"))
    fig.add_vline(x="2020-03-01", line_dash="dash")
    fig.add_vline(x="2022-01-01", line_dash="dash")
    fig.update_layout(title="Hedge Agent Weights Over Time")
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.plotly_chart(px.bar(report, x="Label", y="Sharpe Ratio", color="Sharpe Ratio"), use_container_width=True)
    st.plotly_chart(px.bar(report, x="Label", y="Directional Accuracy", color="Directional Accuracy"), use_container_width=True)
    ens_pos = np.sign(results["ensemble_pred"].values)
    ens_curve = 10000 * np.exp(np.cumsum(ens_pos * results["actual"].values))
    bh_curve = 10000 * np.exp(np.cumsum(results["actual"].values))
    eq = go.Figure()
    eq.add_trace(go.Scatter(x=results.index, y=ens_curve, name="Ensemble"))
    eq.add_trace(go.Scatter(x=results.index, y=bh_curve, name="Buy & Hold"))
    eq.update_layout(title="$10,000 invested")
    st.plotly_chart(eq, use_container_width=True)
