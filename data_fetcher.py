import requests
import pandas as pd
import logging

DATA_API_URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false"

def fetch_market_data():
    """🌐 Communicates with the web server to pull raw JSON data."""
    logging.info("Initializing connection to CoinGecko server network...")
    print("🌐 [Fetcher] Initializing connection to data API server...")
    
    try:
        response = requests.get(DATA_API_URL, timeout=15)
        if response.status_code == 200:
            raw_json = response.json()
            logging.info(f"Successfully ingested {len(raw_json)} market objects.")
            return pd.DataFrame(raw_json)
        else:
            logging.error(f"Server rejection. HTTP Status: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as error:
        logging.critical(f"Network pipe leakage intercepted safely: {error}")
        print(f"❌ Network Error: Server dropped out connection. Check your Wi-Fi.")
        return None