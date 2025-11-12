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




# returns the last trade price on Binance’
# get_binance_btcusd_price()

#returns current Global average Bitcoin Price
get_bitcoin_price()

