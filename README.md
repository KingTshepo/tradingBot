Trading bot in Python

This trading Bot uses python and the Alpaca API to pefrom trades on a trade account.

The bot requires an alpaca account.

This bot is currenty performs  a simple moving average crossover strategy. This strategy involves using two moving averages of different time periods and generating buy/sell signals based on their crossover.

Here's a simplified version of the moving average crossover strategy:

    Setup:
        Choose two moving average periods (e.g., short-term and long-term).
        Calculate the moving averages for each period using historical price data.
  
    Buy Signal:
        Generate a buy signal when the short-term moving average crosses above the long-term moving average. This indicates a potential bullish trend reversal.
  
    Sell Signal:
        Generate a sell signal when the short-term moving average crosses below the long-term moving average. This indicates a potential bearish trend reversal.
  
    Implementation:
        Monitor the price data in real-time.
        When a buy signal is generated, execute a buy order.
        When a sell signal is generated, execute a sell order.

You can enter your Alpaca API and secret key in the main file to perform a trade
