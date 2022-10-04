# some notes
import fire 

# table_data = [
#     ["Ticker", "Open", "Close"],
#     ["AAPL", 363.25, 363.4],
#     ["AMZN", 2756.0, 2757.99],
#     ["GOOG", 1409.1, 1408.2]
# ]
# #print (f' Amazon info: {table_data[2]}')

# for row in table_data :
#     ticker = row [0]
#     Open = row [1]
#     Close = row [2]
#     print (ticker, Open, Close)


# table_data = [
#     {
#         "Ticker": "AAPL",
#         "Open": 363.25,
#         "Close": 363.4
#     },
#     {
#         "Ticker": "AMZN",
#         "Open": 2756.0,
#         "Close": 2757.99
#     },
#     {
#         "Ticker": "GOOG",
#         "Open": 1409.1,
#         "Close": 1408.2
#     }
# ]
# for item in table_data :
#     ticker = item.get ("Ticker")
#     Close = item.get("Close")
#     print(ticker, Close)

# import pathlib
# from pathlib import Path
# my_directory = Path(".")
# print(my_directory )

# trying to create a bitcoin price predictor using machine learning.
# from this link - https://thecleverprogrammer.com/2021/12/27/cryptocurrency-price-prediction-with-machine-learning/ - 
# #seem to be getting error importing pandas and yfinance.    
# import pandas as pd
# import yfinance
# import datetime 
# from datetime import date, timedelta 
# today = date.today()

# d1 = today.strftime("%Y-%m-%d")
# end_date = d1 
# d2 = date.today() - timedelta(days=360)
# d2 = d2.strftime("%Y-%m-%d")
# start_date = d2

# data = yfinance.download('BTC-USD', start= start_date, end= end_date, progress=False)
# data ["Date"] = data.index 
# data = data [["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
# data.reset_index(drop=True, inplace=True)
# print(data.head())

