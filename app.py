import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# ------------------------
# Sidebar Inputs
# ------------------------
st.sidebar.title("📈 Financial Dashboard")

ticker = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, MSFT, TSLA)", "AAPL")
period = st.sidebar.selectbox("Select Period", ["1mo", "3mo", "6mo", "1y", "2y", "5y", "10y"])
interval = st.sidebar.selectbox("Select Interval", ["1d", "1wk", "1mo"])

# ------------------------
# Fetch Data
# ------------------------
st.title(f"📊 {ticker} Stock Dashboard")

try:
    data = yf.download(ticker, period=period, interval=interval)
    if data.empty:
        st.warning("No data found for this ticker/period.")
    else:
        # Compute Moving Averages
        data["SMA_20"] = data["Close"].rolling(window=20).mean()
        data["SMA_50"] = data["Close"].rolling(window=50).mean()

        # ------------------------
        # Price Chart
        # ------------------------
        st.subheader("Stock Price with Moving Averages")

        fig = go.Figure()
        fig.add_trace(go.Candlestick(
            x=data.index,
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close'],
            name="Candlestick"
        ))
        fig.add_trace(go.Scatter(x=data.index, y=data["SMA_20"], line=dict(color="blue", width=1.5), name="SMA 20"))
        fig.add_trace(go.Scatter(x=data.index, y=data["SMA_50"], line=dict(color="orange", width=1.5), name="SMA 50"))

        fig.update_layout(xaxis_rangeslider_visible=False, template="plotly_dark", height=600)
        st.plotly_chart(fig, use_container_width=True)

        # ------------------------
        # Volume Chart
        # ------------------------
        st.subheader("Trading Volume")
        fig_vol = go.Figure()
        fig_vol.add_trace(go.Bar(x=data.index, y=data["Volume"], name="Volume"))
        fig_vol.update_layout(template="plotly_dark", height=400)
        st.plotly_chart(fig_vol, use_container_width=True)

        # ------------------------
        # Data Table
        st.subheader("Raw Data")
        st.dataframe(data.tail(20))

        # ------------------------
        # Export Options
        # ------------------------
        st.subheader("Download Data")
        csv = data.to_csv().encode("utf-8")
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name=f"{ticker}_stock_data.csv",
            mime="text/csv"
        )

except Exception as e:
    st.error(f"Error fetching data: {e}")
