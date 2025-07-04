# ETL_python_SQL_PowerBi_Get_Geo_Population_from_Worldmeter

Georgian Population Dashboard and ETL Pipeline
This project contains:

✅ A Power BI dashboard visualizing Georgia's population trends, forecasts, and regional distribution.
✅ A Python ETL script that scrapes Georgian population data from Worldometer and loads it into a SQL Server database.

📊 Dashboard Overview
The Power BI dashboard includes:

Full Population (4M)

Land Area (69.12K sq km)

Global Rank of 2025 (131)

Median Age (40.00)

Population by Region (choropleth map)

Historical Population of Georgia by Year (1955–2025)

Future Population Forecast (2030–2050)

The visual report helps understand past trends, current demographics, and future projections of Georgia’s population.


⚙️ ETL Pipeline
The ETL pipeline is written in Python and does the following:

Extract:

Downloads population tables from Worldometer.

Transform:

Parses HTML tables into pandas DataFrames.

Cleans/structures historical and forecast data.

Load:

Inserts the data into Microsoft SQL Server using SQLAlchemy.
