"""
This file performs the requests to get the historical data for an asset

written by: Tshepo Maredi
"""

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

API_KEY = 'api-key'
SECRET_KEY = 'secret-key'

# No keys required for crypto data
historical_data_client = StockHistoricalDataClient(api_key=API_KEY, secret_key=SECRET_KEY)

symbol_name='NDAQ'

def get_historical_data(symbol_name, limit=None):
    request_params = StockBarsRequest(
                            symbol_or_symbols=[symbol_name],
                            timeframe=TimeFrame.Hour,
                            start=datetime(2024, 1, 1),
                            limit=limit
                            )

    stock_bars = historical_data_client.get_stock_bars(request_params)
    return stock_bars

