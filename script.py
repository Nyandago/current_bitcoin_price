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


get_bitcoin_price()

