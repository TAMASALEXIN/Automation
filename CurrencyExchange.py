# Create a Python program that fetches the latest exchange rates for
# USD from an API and allows the user to convert a specified amount to EUR, GBP, JPY, and AUD.

import requests
import json

# Fetch the latest exchange rates for USD from an API
url = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd.json"

response = requests.get(url)
data = response.json()

# Allow the user to convert a specified amount to EUR, GBP, JPY, and AUD
amount = float(input("Enter the amount in USD: "))
print("The amount in EUR is: ", amount * data['usd']['eur'])
print("The amount in GBP is: ", amount * data['usd']['gbp'])
print("The amount in JPY is: ", amount * data['usd']['jpy'])
print("The amount in AUD is: ", amount * data['usd']['aud'])

# Output:
# Enter the amount in USD: 100
# The amount in EUR is:  


