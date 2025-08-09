import pymongo
import yfinance as yf
import pprint
import numpy as np

tickers = ['600028.SS', '600030.SS', '600031.SS', '600036.SS', '600048.SS', '600050.SS', '600276.SS',
           '600309.SS', '600406.SS']

my_client = pymongo.MongoClient('localhost', 27017)
my_db = my_client['my_database']
my_collection = my_db['tickers']

data = yf.download(tickers, period='5y')

for ticker in tickers:
    document = {
        "symbol": ticker,
        "date": list(data.index),
        "open": list(data['Open'][ticker]),
        "close": list(data['Close'][ticker]),
        "high": list(data['High'][ticker]),
        "low": list(data['Low'][ticker]),
        "volume": list(data['Volume'][ticker]),
    }
    my_collection.insert_one(document)





