import yfinance as yf

# 금 선물
gold = yf.Ticker("GC=F")
gold_data = gold.history(period="1mo")

# 원유 선물 (WTI)
oil = yf.Ticker("CL=F")
oil_data = oil.history(period="1mo")

print("금 선물 데이터:")
gold_data.tail()
print("\n원유 선물 데이터:")
print(oil_data.tail())
