import streamlit as st
from regime_detector import detect_market_regime
from gold_analyzer import get_gold_signal
from btc_analyzer import get_btc_signal

st.set_page_config(layout="wide")
st.title("🧠 AI Hedge Rotation System")

mode = detect_market_regime()

st.subheader(f"Current Mode: {mode}")

if mode == "GOLD":
    signal = get_gold_signal()
else:
    signal = get_btc_signal()

st.success(signal)
