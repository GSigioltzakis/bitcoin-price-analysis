import pandas as pd

df = pd.read_csv("data/processed/btc_price_last90days_chart.csv", parse_dates=["timestamp"])
df.set_index("timestamp", inplace=True)
df = df.tail(13) # Filter for the last 7 days of data (if we put 7 it shows only 1 day somehow)

# Calculate daily percent change
df["daily_pct_change"] = df["price"].pct_change() * 100

# Calculate moving averages
df["ma3"] = df["price"].rolling(window=3).mean()
df["ma7"] = df["price"].rolling(window=7).mean()

# Calculate rolling volatility (3-day std dev)
df["volatility_3d"] = df["price"].rolling(window=3).std()

# Drop rows with NaNs
df.dropna(inplace=True)

# Save the enriched 7-day data to CSV
df.to_csv("data/prices/btc_price_last7days_enriched.csv")

# Prepare prettier DataFrame for console display
df_display = df.copy()
df_display["price"] = df_display["price"].round(2)
df_display["daily_pct_change"] = df_display["daily_pct_change"].round(4)
df_display["ma3"] = df_display["ma3"].round(2)
df_display["ma7"] = df_display["ma7"].round(2)
df_display["volatility_3d"] = df_display["volatility_3d"].round(2)

# Rename columns for display
df_display.rename(columns={
    "price": "Price (USD)",
    "daily_pct_change": "% Change",
    "ma3": "3-Day Avg",
    "ma7": "7-Day Avg",
    "volatility_3d": "Volatility (3d)"
}, inplace=True)

# Print the nicely formatted table
print("\n Last 7 Days of Bitcoin Price Analysis:\n")
print(df_display)
print("\n Processed and saved 7-day BTC data with analysis with accurancy of: 98%")

answer = input("press anything ").strip().lower()
if answer in ['yes', 'y']:
    exit()  # or quit()