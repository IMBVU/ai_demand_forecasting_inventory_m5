import pandas as pd
from pathlib import Path

FORECAST_PATH = Path("../outputs/m5_inventory_forecast_recommendations.csv")

def build_recommendation(row):
    if row["stockout_risk"] == "High Risk":
        return (
            f"{row['item_id']} at {row['store_id']} is currently below its reorder threshold. "
            f"Recommended action: order {int(row['recommended_order_qty'])} units, with an estimated reorder value of "
            f"${row['estimated_reorder_value']:,.2f}. This item should be prioritized to reduce stockout risk."
        )

    return (
        f"{row['item_id']} at {row['store_id']} appears healthy based on the current planning assumptions. "
        f"Continue monitoring demand velocity and price movement before increasing purchase volume."
    )

if __name__ == "__main__":
    df = pd.read_csv(FORECAST_PATH)
    df["ai_style_recommendation"] = df.apply(build_recommendation, axis=1)
    print(df[["store_id", "item_id", "stockout_risk", "ai_style_recommendation"]].head(10).to_string(index=False))
