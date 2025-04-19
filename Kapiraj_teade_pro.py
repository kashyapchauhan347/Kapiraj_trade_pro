import streamlit as st
from datetime import datetime

st.markdown("<h1 style='color:gold; text-align:center;'>Kapiraj Trade Pro</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid gold;'>", unsafe_allow_html=True)

st.subheader("Select Timeframe:")
timeframe = st.radio("Choose timeframe", ["1 MIN", "5 MIN", "15 MIN"], horizontal=True)
st.success(f"Selected Timeframe: {timeframe}")

st.subheader("Live Market Chart:")
tradingview_html = """
<iframe src="https://s.tradingview.com/widgetembed/?symbol=NSE:BANKNIFTY&interval=1&hidesidetoolbar=1&theme=dark"
width="100%" height="400" frameborder="0" allowtransparency="true" scrolling="no"></iframe>
"""
st.components.v1.html(tradingview_html, height=400)

st.subheader("Trade Signals:")
col1, col2 = st.columns(2)

if 'log' not in st.session_state:
    st.session_state.log = []

def log_signal(signal_type):
    timestamp = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    st.session_state.log.append(f"{timestamp} - {signal_type} Signal Triggered")

with col1:
    if st.button("BUY SIGNAL"):
        confirm = st.radio("Confirm Buy?", ["YES", "NO"], key="buy")
        if confirm == "YES":
            st.success("Prepare to BUY!")
            log_signal("BUY")

with col2:
    if st.button("SELL SIGNAL"):
        confirm = st.radio("Confirm Sell?", ["YES", "NO"], key="sell")
        if confirm == "YES":
            st.success("Prepare to SELL!")
            log_signal("SELL")

st.markdown("---")
st.markdown("<h3 style='color:white;'>Scalping Mode:</h3>", unsafe_allow_html=True)
st.markdown("**Target:** 50 Points  \n**Stoploss:** 15–20 Points", unsafe_allow_html=True)

st.markdown("---")
st.subheader("Trade History:")
if st.session_state.log:
    for entry in reversed(st.session_state.log):
        st.write(entry)
else:
    st.info("No trades yet.")

st.markdown("<hr style='border: 1px solid gold;'>", unsafe_allow_html=True)
st.caption("Kapiraj Trade Pro - Built for Focused Scalping.")
