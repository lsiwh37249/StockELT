import yfinance as yf
import pandas as pd
import os

def gold_monthly_data():
    # 금 선물
    gold = yf.Ticker("GC=F")
    gold_data = gold.history(period="1mo")

    file_path = "../stockfinance/data/gold_data.csv"

    if os.path.exists(file_path):
        os.remove(file_path)

    gold_data.to_csv(path_or_buf="../stockfinance/data/gold_data.csv")
    return gold_data
