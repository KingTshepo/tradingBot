import alpaca_trade_api as tradeapi
import pandas as pd

# Replace these with your own API key and secret key
API_KEY = 'PKT3I438NCXYNMA6LTWY'
SECRET_KEY = 'f0us7MRfXfXU4flqd54oRkHMT8uYFZ4qd8Njb5hC'

# Initialize the Alpaca API
api = tradeapi.REST(API_KEY, SECRET_KEY, base_url='https://paper-api.alpaca.markets')

# Set the symbol and timeframe
symbol = 'AAPL'  # Example: Apple stock
timeframe = '1D'  # Example: 1 day intervals

# Get historical data
historical_data = api.get_bars(symbol, timeframe=timeframe, limit=1000).df

# Print the first few rows of the data
print(historical_data.head())

