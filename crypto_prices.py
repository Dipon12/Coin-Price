import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('COINGECKO_API_KEY')


base_url = "https://api.coingecko.com/api/v3"

headers = {
    'x-cg-api-key': api_key
}

def get_crypto_price(coin_id):
    endpoint = f"{base_url}/simple/price"
    params = {
        'ids': coin_id,
        'vs_currencies': 'usd',
        'include_24hr_change': 'true'
    }
    
    response = requests.get(endpoint, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

bitcoin_data = get_crypto_price('bitcoin')
ethereum_data = get_crypto_price('ethereum')


if bitcoin_data:
    btc_price = bitcoin_data['bitcoin']['usd']
    btc_change = bitcoin_data['bitcoin']['usd_24h_change']
    print(f"Bitcoin (BTC): ${btc_price:,.2f} (24h change: {btc_change:.2f}%)")

if ethereum_data:
    eth_price = ethereum_data['ethereum']['usd']
    eth_change = ethereum_data['ethereum']['usd_24h_change']
    print(f"Ethereum (ETH): ${eth_price:,.2f} (24h change: {eth_change:.2f}%)")