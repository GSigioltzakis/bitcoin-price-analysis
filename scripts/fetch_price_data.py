import requests
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# --------- URLs & Parameters ---------
url_ohlc = "https://api.coingecko.com/api/v3/coins/bitcoin/ohlc"
params_ohlc = {
    "vs_currency": "usd",
    "days": "14"  #1, 7, 14, 30, 90, 180, 365
}

url_chart = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params_chart = {
    "vs_currency": "usd",
    "days": "14",  # Line chart: last 90 days  1, 7, 14, 30, 90, 180, 365
    "interval": "daily"
}

# --------- API Calls ---------
response_ohlc = requests.get(url_ohlc, params=params_ohlc)
data_ohlc = response_ohlc.json()

response_chart = requests.get(url_chart, params=params_chart)
data_chart = response_chart.json()

# --------- OHLC DataFrame for Candlestick ---------
df = pd.DataFrame(data_ohlc, columns=["timestamp", "open", "high", "low", "close"])
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
df.set_index("timestamp", inplace=True)
df.to_csv("data/processed/btc_price_last14days_candle.csv")

# --------- Price DataFrame for Line Chart ---------
prices = data_chart["prices"]
df2 = pd.DataFrame(prices, columns=["timestamp", "price"])
df2["timestamp"] = pd.to_datetime(df2["timestamp"], unit="ms")
df2.set_index("timestamp", inplace=True)
df2.to_csv("data/processed/btc_price_last14days_chart.csv")


# ----------PLOTS-----------------------

# --------- Plot 1: Line Chart ---------
plt.figure(figsize=(10, 5))
plt.plot(df2.index, df2["price"], label="BTC Price (USD)", color="red")
plt.title("Bitcoin Price - Last 90 Days (Line Chart)")
plt.xlabel("Date")
plt.ylabel("Price in USD")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show(block=False)

# --------- Plot 2: Candlestick Chart ---------
mpf.plot(df, type='candle', style='charles',title='Bitcoin OHLC - Last 90 Days (Candlestick Chart)',ylabel='Price (USD)')
