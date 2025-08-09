from fastapi import FastAPI
import pymongo
import pprint

app = FastAPI()

my_client = pymongo.MongoClient('localhost', 27017)
my_db = my_client['my_database']
my_collection = my_db['tickers']


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/symbols/{symbol}")
async def say_hello(symbol: str):
    if symbol == 'all':
        ticker = list(my_collection.find())
    else:
        ticker = my_collection.find_one({"symbol": symbol})

    for t in ticker:
        if "_id" in t:
            t["_id"] = str(t["_id"])
    return ticker
