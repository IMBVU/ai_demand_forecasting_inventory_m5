CREATE TABLE m5_inventory_sales (
    date DATE,
    d TEXT,
    item_id TEXT,
    dept_id TEXT,
    cat_id TEXT,
    store_id TEXT,
    state_id TEXT,
    units_sold INTEGER,
    sell_price DECIMAL(10,2),
    revenue DECIMAL(12,2),
    weekday TEXT,
    month INTEGER,
    year INTEGER,
    event_name_1 TEXT,
    event_type_1 TEXT
);

CREATE TABLE inventory_forecast_recommendations (
    store_id TEXT,
    item_id TEXT,
    dept_id TEXT,
    cat_id TEXT,
    state_id TEXT,
    avg_daily_units DECIMAL(10,2),
    demand_std DECIMAL(10,2),
    avg_price DECIMAL(10,2),
    revenue_last_90_days DECIMAL(12,2),
    total_units_last_90_days INTEGER,
    forecast_28_day_units DECIMAL(10,2),
    safety_stock_units DECIMAL(10,2),
    reorder_point_units DECIMAL(10,2),
    current_inventory_units INTEGER,
    stockout_risk TEXT,
    recommended_order_qty INTEGER,
    estimated_reorder_value DECIMAL(12,2)
);
