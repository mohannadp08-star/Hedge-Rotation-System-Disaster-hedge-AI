import yfinance as yf

def get_btc_signal():
    btc = yf.download("BTC-USD", period="2d", interval="5m")
    price = btc['Close'].iloc[-1]
    return f"BTC Signal → Price: {price}"
