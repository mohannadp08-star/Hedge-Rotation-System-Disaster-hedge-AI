import yfinance as yf
import pandas as pd

def detect_market_regime():
    gold = yf.download("GC=F", period="5d", interval="15m")
    
    gold['ema20'] = gold['Close'].ewm(span=20).mean()
    gold['ema50'] = gold['Close'].ewm(span=50).mean()

    last = gold.iloc[-1]

    # Crash conditions
    crash = (
        last['Close'] < last['ema50'] and
        last['ema20'] < last['ema50'] and
        gold['Close'].pct_change().tail(10).mean() < -0.002
    )

    if crash:
        return "BITCOIN"
    else:
        return "GOLD"
