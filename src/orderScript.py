# README
# usage: python coinRoutes.py
# optional command line arguments:
#   -k : adds Kraken exchange
#   -q <quantity> : set order quantity to a specific amount (default = 10)
# usage w/ optional parameters: python coinRoutes.py -q 3.75 -k
# Developed in python 3.10 environment w/ requests pkg added
# Patrick O'Leary

import requests
import sys
from decimal import *

from requests.models import ContentDecodingError

# for sort algo
def price(order):
  return order['Price']

addKraken = False
orderQty = Decimal(10)
aggregatedBidData = []
aggregatedAskData = []
totalSalePrice = Decimal(0)
totalPurchasePrice = Decimal(0)

# check command line arguments
if len(sys.argv) > 1:
    for index , arg in enumerate(sys.argv):
        if arg == '-q' and index != len(sys.argv) - 1: 
            orderQty = Decimal(sys.argv[index + 1])
        elif arg == '-k':
            addKraken = True

print('\nFetching data to buy/sell', orderQty, 'BTC')
print('Exchanges: Coinbase, Gemini, Kraken\n' if addKraken else 'Exchanges: Coinbase, Gemini\n')

# get coinbase data
response = requests.get('https://api.pro.coinbase.com/products/BTC-USD/book?level=2')
coinBaseData = response.json()
for bid in coinBaseData['bids']:
    aggregatedBidData.append(dict(Price=Decimal(bid[0]), Qty=Decimal(bid[1]), Exchange='CoinBase'))
for ask in coinBaseData['asks']:
    aggregatedAskData.append(dict(Price=Decimal(ask[0]), Qty=Decimal(ask[1]), Exchange='CoinBase'))

# get gemini data
response = requests.get('https://api.gemini.com/v1/book/btcusd')
geminiData = response.json()
for bid in geminiData['bids']:
    aggregatedBidData.append(dict(Price=Decimal(bid['price']), Qty=Decimal(bid['amount']), Exchange='Gemini'))
for ask in geminiData['asks']:
    aggregatedAskData.append(dict(Price=Decimal(ask['price']), Qty=Decimal(ask['amount']), Exchange='Gemini'))

# get kraken data
if addKraken:
    response = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
    krakenData = response.json()['result']['XXBTZUSD']
    aggregatedBidData.append(dict(Price=Decimal(krakenData['b'][0]), Qty=Decimal(krakenData['b'][2]), Exchange='Kraken'))
    aggregatedAskData.append(dict(Price=Decimal(krakenData['a'][0]), Qty=Decimal(krakenData['a'][2]), Exchange='Kraken'))

# sort data, low to high if ask, high to low if bid
aggregatedAskData.sort(key=price)
aggregatedBidData.sort(reverse=True, key=price)

# iterate through sorted ask data until order quantity is satisfied
remainingBuyQty = orderQty
aggregatedBuyOrders = []
for ask in aggregatedAskData:
    aggregatedBuyOrders.append(ask)
    if remainingBuyQty >= ask['Qty']:
        totalPurchasePrice = totalPurchasePrice + ask['Qty'] * ask['Price']
        remainingBuyQty = remainingBuyQty - ask['Qty']
    else:
        totalPurchasePrice = totalPurchasePrice + remainingBuyQty * ask['Price']
        aggregatedBuyOrders[-1]['Qty'] = remainingBuyQty
        remainingBuyQty = 0
        break


# iterate through sorted bid data until order quantity is satisfied
remainingSellQty = orderQty
aggregatedSellOrders = []
for bid in aggregatedBidData:
    aggregatedSellOrders.append(bid)
    if remainingSellQty >= bid['Qty']:
        remainingSellQty = remainingSellQty - bid['Qty']
        totalSalePrice = totalSalePrice + bid['Qty'] * bid['Price']
    else:
        totalSalePrice = totalSalePrice + remainingSellQty * bid['Price']
        aggregatedSellOrders[-1]['Qty'] = remainingSellQty
        remainingSellQty = 0
        break

# Summary
print('Buy Order')
print(orderQty, 'bitcoin can be bought accross', len(aggregatedBuyOrders), 'orders')
print('Total Price (USD): ' , totalPurchasePrice)
print('Avg Price (USD): ' , totalPurchasePrice / orderQty)

print('\nSell Order')
print(orderQty, 'bitcoin can be sold accross', len(aggregatedSellOrders), 'orders')
print('Total Price (USD): ' , totalSalePrice)
print('Avg Price (USD): ' , totalSalePrice / orderQty, '\n')

# coinbaseOrder=dict(Qty=0,Price=0, Avg=0)
# purchaseOrders= dict()
# for order in aggregatedBuyOrders:
#     if order['Exchange'] in purchaseOrders:
#         purchaseOrders[order['Exchange']]['Qty'] += order['Qty']
#         purchaseOrders[order['Exchange']]['Price'] = order['Price']
#     else:
#         purchaseOrders[order['Exchange']] = dict()
#         purchaseOrders[order['Exchange']]['Qty'] = order['Qty']
#         purchaseOrders[order['Exchange']]['Price'] = order['Price']
    
# print(purchaseOrders)