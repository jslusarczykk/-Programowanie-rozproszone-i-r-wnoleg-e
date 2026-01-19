from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

CACHE = {"price": None, "ts": 0}
CACHE_TTL = 30  # sekund

@app.get("/price/solana")
def solana_price():
    now = time.time()
    if CACHE["price"] is not None and (now - CACHE["ts"]) < CACHE_TTL:
        return jsonify({"source": "cache", "price": CACHE["price"], "ts": CACHE["ts"]})

    url = "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    price = r.json()["solana"]["usd"]

    CACHE["price"] = price
    CACHE["ts"] = now
    return jsonify({"source": "coingecko", "price": price, "ts": now})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)

