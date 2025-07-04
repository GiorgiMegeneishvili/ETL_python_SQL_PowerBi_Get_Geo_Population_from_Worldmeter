import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import StringIO
from sqlalchemy import create_engine


def get_data_Georgian_population_data(url):

    response = requests.get(url)

    # Wrap response.text in StringIO
    html_data = StringIO(response.text)
    return html_data
def transfrom_data(html_data):

    # Now read the table safely
    tables = pd.read_html(html_data)

    # Get the first table (Population of Georgia (2025 and historical))
    georgia_historical_df = tables[0]
    # Get the second table (Georgia Population Forecast)
    georgia_population_df = tables[1]
    # print(georgia_historical_df.head())

    return  georgia_historical_df, georgia_population_df

    # print(georgia_population_df.head())

def connect_to_sql_server_and_load(georgia_historical_df, georgia_population_df , DB_SERVER, DB_NAME,table_historical_df, table_population_df ):
    # SQLAlchemy engine-ით კავშირი
    engine = create_engine(f"mssql+pyodbc://{DB_SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server", fast_executemany=True)

    try:
        # pandas DataFrame-ის გადატანა SQL-ში
        georgia_historical_df.to_sql(table_historical_df, engine, if_exists='replace', index=False)
        georgia_population_df.to_sql(table_population_df, engine, if_exists='replace', index=False)
        print("Data has been loaded successfully.")
    except Exception as e:
        print(f"Error: {e}")




if __name__ == '__main__':
    DB_SERVER = 'YOUR_SERVER'
    DB_NAME = 'YOUR_DATABASE'
    countries = ['georgia']
    for country in countries:
        url = f'https://www.worldometers.info/world-population/{country}-population/'
        html_data = get_data_Georgian_population_data(url)
        georgia_historical_df, georgia_population_df = transfrom_data(html_data)
        table_historical_df = f'{country}_historical_df'
        table_population_df = f'{country}_population_df'
        connect_to_sql_server_and_load(georgia_historical_df,georgia_population_df, DB_SERVER,DB_NAME,table_historical_df, table_population_df )
        print(georgia_population_df)
    # print(georgia_historical_df)
    # def load_it_into_SQL_server(georgia_historical_df, georgia_population_df,):
