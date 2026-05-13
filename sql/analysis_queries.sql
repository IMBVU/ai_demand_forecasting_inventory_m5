-- Top products by forecasted reorder value
SELECT
    store_id,
    item_id,
    stockout_risk,
    recommended_order_qty,
    estimated_reorder_value
FROM inventory_forecast_recommendations
ORDER BY estimated_reorder_value DESC
LIMIT 20;

-- Demand and revenue by category
SELECT
    cat_id,
    SUM(units_sold) AS total_units,
    SUM(revenue) AS total_revenue
FROM m5_inventory_sales
GROUP BY cat_id
ORDER BY total_revenue DESC;

-- High-risk inventory count by store
SELECT
    store_id,
    COUNT(*) AS high_risk_products
FROM inventory_forecast_recommendations
WHERE stockout_risk = 'High Risk'
GROUP BY store_id
ORDER BY high_risk_products DESC;
