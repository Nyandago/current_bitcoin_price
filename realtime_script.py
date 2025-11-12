import websocket, json

def on_message(ws, message):
    data = json.loads(message)
    price = float(data['p'])
    print(f"Live BTC/USDT Price: ${price:,.2f}")

socket = "wss://stream.binance.com:9443/ws/btcusdt@trade"
ws = websocket.WebSocketApp(socket, on_message=on_message)
ws.run_forever()