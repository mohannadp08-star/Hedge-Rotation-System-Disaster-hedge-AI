import yfinance as yf
import pandas as pd

def detect_market_regime():
    gold = yf.download("GC=F", period="5d", interval="15m")

    if gold.empty or len(gold) < 60:
        return "GOLD"  # fallback safety

    gold['ema20'] = gold['Close'].ewm(span=20).mean()
    gold['ema50'] = gold['Close'].ewm(span=50).mean()
    gold['returns'] = gold['Close'].pct_change()

    # خذ آخر صف كقيم رقمية
    last_close = float(gold['Close'].iloc[-1])
    last_ema20 = float(gold['ema20'].iloc[-1])
    last_ema50 = float(gold['ema50'].iloc[-1])

    momentum = gold['returns'].tail(10).mean()

    crash = (
        last_close < last_ema50 and
        last_ema20 < last_ema50 and
        momentum < -0.002
    )

    return "BITCOIN" if crash else "GOLD"
