# AI-Powered Demand Forecasting & Inventory Optimization

## Business Problem
Retail teams need to forecast future demand and decide what inventory to reorder before stockouts happen. This project uses M5 retail sales data to create a business-ready inventory planning workflow.

## Dataset
**M5 Forecasting Accuracy Dataset**  
The original Kaggle dataset contains Walmart-style daily sales data, calendar information, and sell prices.

For GitHub usability, this repo includes a cleaned sample focused on 60 high-volume product-store combinations from the most recent 365 days.

## Key Outputs
- Cleaned long-format M5 demand dataset
- 28-day demand forecast
- Safety stock calculation
- Reorder point calculation
- Stockout risk flag
- Recommended order quantity
- Estimated reorder value
- AI-style executive recommendation framework
- Excel planning workbook
- Dashboard blueprint

## Business Value
This project demonstrates how raw sales data can be transformed into operational decisions. The value is not just the forecast, but the recommendation layer that helps a business user know what action to take.

## Tools
Python, Pandas, SQL, Excel, Streamlit, Power BI/Tableau planning

## Folder Structure
```text
data/processed/
src/
sql/
outputs/
excel/
images/
```

## How to Run
```bash
pip install -r ../../requirements.txt
cd src
python forecast_inventory.py
python ai_recommendation_generator.py
streamlit run app_streamlit.py
```
