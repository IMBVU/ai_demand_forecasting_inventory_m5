import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Demand Forecasting", layout="wide")

st.title("AI-Powered Demand Forecasting & Inventory Optimization")
st.caption("Built with M5 Forecasting Accuracy retail demand data")

df = pd.read_csv("../outputs/m5_inventory_forecast_recommendations.csv")

k1, k2, k3, k4 = st.columns(4)
k1.metric("Products Analyzed", len(df))
k2.metric("High Risk Products", int((df["stockout_risk"] == "High Risk").sum()))
k3.metric("28-Day Forecast Units", f"{df['forecast_28_day_units'].sum():,.0f}")
k4.metric("Estimated Reorder Value", f"${df['estimated_reorder_value'].sum():,.0f}")

st.subheader("Inventory Forecast Recommendations")
st.dataframe(df)

st.subheader("Reorder Value by Product")
chart_df = df.sort_values("estimated_reorder_value", ascending=False).head(15)
st.bar_chart(chart_df.set_index("item_id")["estimated_reorder_value"])

st.subheader("AI-Style Recommendation Preview")
sample = df.sort_values("estimated_reorder_value", ascending=False).head(5)
for _, row in sample.iterrows():
    st.write(
        f"**{row['item_id']} | {row['store_id']}**: "
        f"{row['stockout_risk']} risk. Recommended order quantity: {int(row['recommended_order_qty'])} units."
    )
