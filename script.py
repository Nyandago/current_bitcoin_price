import requests


def get_bitcoin_price():
    # Using CoinGecko API (free and no authentication needed)
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    data = response.json()
    price = data["bitcoin"]["usd"]
    print(f"Current Bitcoin Price: ${price:,}")

def get_binance_btcusd_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(url).json()
    print(f"Binance BTC Price: ${float(data['price']):,.2f}")




#Binance Price
get_binance_btcusd_price()

#Aggregated Price
get_bitcoin_price()

