# crypto_step.py
import requests
import pandas as pd
from sqlalchemy import create_engine

def fetch_and_store():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()

    prices = {
        'Bitcoin price (USD)': data['bitcoin']['usd'],
        'Ethereum price (USD)': data['ethereum']['usd']
    }

    df = pd.DataFrame([prices])

    engine = create_engine("postgresql://kenya:0000@207.180.217.209:5432/kenya_economy")
    df.to_sql('prices', engine, if_exists='replace', index=False, schema='nairobi')

if __name__ == "__main__":
    fetch_and_store() 
