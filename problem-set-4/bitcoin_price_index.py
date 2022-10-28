"""CS50P -- Problem Set 4: Bitcoin Price Index
Source: https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

Bitcoin is a form of digitial currency, otherwise known as cryptocurrency.
Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network,
otherwise known as a blockchain, to record transactions.

Because there's demand for Bitcoin (i.e., users want it), users are willing to buy it, as by
exchanging one currency (e.g., USD) for Bitcoin.

In a file called bitcoin.py, implement a program that:

Expects the user to specify as a command-line argument the number of Bitcoins, , that they would like to buy.

If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object,
among whose nested keys is the current price of Bitcoin as a float.

Be sure to catch any exceptions, as with code like:
import requests

try:
    ...
except requests.RequestException:
    ...
Outputs the current cost of (`num_bitcoin_to_buy`) Bitcoins in USD to four decimal places, using , as a thousands separator.
"""

import requests
import sys


# Parse command-line argument for number of Bitcoin to buy
try:
    num_bitcoin_to_buy = float(sys.argv[1])
except:
    sys.exit()

# Get Bitcoin price data
try:
    bitcoin_data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    current_bitcoin_price = bitcoin_data.json()['bpi']['USD']['rate_float']
    current_date = bitcoin_data.json()['time']['updatedISO'][:11]
except requests.RequestException:
    print('Whoops! Something went wrong with requests.')

# Calc cost and print
total_cost = num_bitcoin_to_buy * current_bitcoin_price
print(f"The current cost of {int(num_bitcoin_to_buy)} bitcoins on {current_date} \
at a price of {current_bitcoin_price} per bitcoin is ${total_cost:,.4f}")
