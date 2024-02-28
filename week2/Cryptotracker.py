# Crpyto currencry price tracker
import requests
import json

#Add more cryptocurrencies to the cryptocurrency tracker program and allow the user to
#input the desired cryptocurrencies for real-time price tracking.

def find_coin(name, data):
    for currency in data:
        if currency['symbol'] == name:
            return currency['quotes']['USD']['price']
    return "Cryptocurrency not found"

# Fetch the latest prices for cryptocurrencies from an API

url = "https://api.coinpaprika.com/v1/tickers"
data = requests.get(url).json()

# Allow the user to input the desired cryptocurrencies for real-time price tracking
try:
    cryptocurrency = input(str("Enter the name of the cryptocurrency: ")).upper()
    if cryptocurrency == "":
        raise Exception("No cryptocurrency entered")
    print("The latest price for", cryptocurrency, "is: ", find_coin(cryptocurrency, data))
except Exception as error:
    print(error)

# Print the latest prices for cryptocurrencies

# Bitcoin
print("The latest price for Bitcoin is: ", data[0]['quotes']['USD']['price'])

# Ethereum
print("The latest price for Ethereum is: ", data[1]['quotes']['USD']['price'])

# Ripple (XRP)

# The third element in the list is not ripple, so we need a different approach

for currency in data:
    if currency['name'] == "XRP":
        print("The latest price for Ripple is: ", currency['quotes']['USD']['price'])
        break








