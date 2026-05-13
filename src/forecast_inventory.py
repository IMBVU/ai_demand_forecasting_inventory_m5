import pandas as pd
import numpy as np
from pathlib import Path

DATA_PATH = Path("../data/processed/m5_inventory_sales_cleaned_sample.csv")
OUTPUT_PATH = Path("../outputs/m5_inventory_forecast_recommendations.csv")

def build_forecast(df: pd.DataFrame) -> pd.DataFrame:
    recent = df.sort_values("date").groupby(["store_id", "item_id"]).tail(90)

    metrics = recent.groupby(["store_id", "item_id", "dept_id", "cat_id", "state_id"]).agg(
        avg_daily_units=("units_sold", "mean"),
        demand_std=("units_sold", "std"),
        avg_price=("sell_price", "mean"),
        revenue_last_90_days=("revenue", "sum"),
        total_units_last_90_days=("units_sold", "sum"),
        last_date=("date", "max"),
    ).reset_index()

    metrics["forecast_28_day_units"] = (metrics["avg_daily_units"] * 28).round(1)
    metrics["safety_stock_units"] = (metrics["demand_std"].fillna(0) * 1.65 * np.sqrt(7)).round(1)
    metrics["reorder_point_units"] = (metrics["avg_daily_units"] * 7 + metrics["safety_stock_units"]).round(1)

    # In a real implementation, current inventory would come from ERP/WMS data.
    # This sample creates a planning inventory assumption for demonstration.
    rng = np.random.default_rng(12)
    metrics["current_inventory_units"] = np.maximum(
        0, (metrics["forecast_28_day_units"] * rng.uniform(.25, 1.35, len(metrics))).round(0)
    )

    metrics["stockout_risk"] = np.where(
        metrics["current_inventory_units"] < metrics["reorder_point_units"],
        "High Risk",
        "Healthy"
    )

    metrics["recommended_order_qty"] = np.maximum(
        0,
        (metrics["forecast_28_day_units"] + metrics["safety_stock_units"] - metrics["current_inventory_units"]).round(0)
    )

    metrics["estimated_reorder_value"] = (metrics["recommended_order_qty"] * metrics["avg_price"]).round(2)

    return metrics

if __name__ == "__main__":
    df = pd.read_csv(DATA_PATH, parse_dates=["date"])
    forecast = build_forecast(df)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    forecast.to_csv(OUTPUT_PATH, index=False)
    print(forecast.head())
