import yfinance as yf

def get_gold_signal():
    gold = yf.download("GC=F", period="2d", interval="5m")
    price = gold['Close'].iloc[-1]
    return f"GOLD Signal → Price: {price}"
