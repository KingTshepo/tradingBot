"""
Trading bot using Alpaca API.
Implements a simple moving average crossover strategy
written by: Tshepo Maredi

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
"""

import alpaca_trade_api as tradeapi
from alpaca.trading.client import TradingClient
from orders import execute_buy_order, execute_sell_order


# Replace these with your own API key and secret key
API_KEY = 'PKT3I438NCXYNMA6LTWY'
SECRET_KEY = 'f0us7MRfXfXU4flqd54oRkHMT8uYFZ4qd8Njb5hC'

trading_client = TradingClient(API_KEY, SECRET_KEY)

api = tradeapi.REST(API_KEY, SECRET_KEY, base_url='https://paper-api.alpaca.markets')

def print_account_details():
    # Get our account information.
    account = trading_client.get_account()

    # Check if our account is restricted from trading.
    if account.trading_blocked:
        print('Account is currently restricted from trading.')

    # Check how much money we can use to open new positions.
    print('${} is available as buying power.'.format(account.buying_power))

    # Get a list of all of our positions.
    portfolio = trading_client.get_all_positions()

    # Print the quantity of shares for each position.
    for position in portfolio:
        print("{} shares of {}".format(position.qty, position.symbol))


    # Check our current balance vs. our balance at the last market close
    balance_change = float(account.equity) - float(account.last_equity)
    print(f'Today\'s portfolio balance change: ${balance_change}')


def generate_moving_avg_crossover_signal(symbol):
    short_term_window = 20
    long_term_window = 50

    from historical_data import get_historical_data
    # Get historical price data
    bars = get_historical_data(symbol, limit=long_term_window)

    # Extract closing prices from historical data
    closing_prices = [bar.close for bar in bars[symbol]]

    # Calculate short-term and long-term moving averages
    short_term_ma = sum(closing_prices[-short_term_window:]) / short_term_window
    long_term_ma = sum(closing_prices[-long_term_window:]) / long_term_window

    # Generate buy/sell signals based on moving average crossover
    if short_term_ma > long_term_ma:
        print('Buy Signal: Short-term MA crossed above Long-term MA')
        return 1

    elif short_term_ma < long_term_ma:
        print('Sell Signal: Short-term MA crossed below Long-term MA')
        return 2
    else:
        print('No Signal')
        return 0


def main():
    # choose an asset to trade and calculate required sl and tp
    asset_symbol = 'NDAQ'
    asset_price = api.get_latest_quote(asset_symbol)
    print('asset bid price:')
    print(asset_price.bp)
    take_profit = asset_price.bp + (0.03 * asset_price.bp)
    print('take-profit calculated at 3% above bid price:')
    print(take_profit)
    stop_loss = asset_price.bp - (0.03 * asset_price.bp)
    print('stop-loss calculated at 3% below bid price:')
    print(stop_loss)

    # generate a signal and execute a trade
    signal = generate_moving_avg_crossover_signal(asset_symbol)
    if signal == 1:     # buy
        # execute a buy order with sl and tp
        execute_buy_order(trading_client=trading_client, symbol=asset_symbol, tp_price=take_profit, sl_price=stop_loss)
        print("Buy order executed")
    elif signal == 2:     # sell
        # execute a buy order with sl and tp
        execute_sell_order(trading_client=trading_client, symbol=asset_symbol, tp_price=take_profit, sl_price=stop_loss)
        print("Sell order executed")
    else:
        print('No order performed')


print_account_details()
main()