'''
web.DataReader()の引数は以下のとおり。

    name : ティッカーシンボル - str
        'GOOG', 'AAPL', 'MSFT'など
    data_source : データソースの名前 - str
        'av-daily', 'av-daily-adjusted'（調整後終値）など
    start : 取得したい期間の開始日時 - datetime.datetime
    end : 取得したい期間の終了日時 - datetime.datetime
    api_key: APIキー - str

    open : 始値
    high : 高値
    low : 安値
    close : 終値
    volume: 出来高
'''
import pandas_datareader.data as web
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
import mplfinance as mpf
from matplotlib.dates import date2num

company_code = input("Enter Stock Symbol:")
start = str(input("Enter Start Date (Year-Month-Day):"))
end = str(input("Enter End Date (Year, Month, Day):"))

# Get stock price
df = web.DataReader(company_code, 'yahoo', start, end)
# Sort Old data --> New data
df = df.sort_index()

# print(df.head(10))
df.to_csv(company_code + '_' +  start + '_' + end + '.csv')

mpf.plot(
        df, 
        type='candle', 
        style='charles', 
        figscale=2.5, 
        title=company_code,
        ylabel='Price ($)', 
        mav=(5,20,50), 
        volume=True, 
        ylabel_lower='Shares\nTraded'
        )