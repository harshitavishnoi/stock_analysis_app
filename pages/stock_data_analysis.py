import pandas as pd 
import numpy as np
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import datetime 
import ta
from pages.utils.figure_functions import table

st.set_page_config(
    page_title = 'Stock Analysis',
    page_icon = "page with curls",
    layout = "wide"
)

st.title('Analysis')

col1, col2, col3 = st.columns(3)

today = datetime.date.today()

with col1:
    ticker = st.text_input("Stock Ticker", "TSLA")
with col2:
    start_date = st.date_input("Choose a Start Date", datetime.date(today.year-1, today.month, today.day))
with col3:
    end_date = st.date_input("Choose a End Date", datetime.date(today.year, today.month, today.day))


st.subheader(ticker)

stock = yf.Ticker(ticker)

# st.write(stock.info)

st.write(stock.info['longBusinessSummary'])
st.write("**Sector:**",stock.info['sector'])
st.write("**Full Time Employees:**",stock.info['fullTimeEmployees'])
st.write("**Website:**",stock.info['website'])

col1, col2 = st.columns(2)

with col1:
    df = pd.DataFrame(index = ['Market Cap', 'Beta', 'Eps', 'PE Ratio'])
    df[''] = [stock.info["marketCap"], stock.info['beta'], stock.info['trailingEps'], stock.info['trailingPE']]
    fig_df = table(df)
    st.plotly_chart(fig_df, use_container_width=True)
with col1:
    df = pd.DataFrame(index = ['Quick Ratio','Revenue per share', 'Profit Margins', 'Debt to Equity','Return on Equity'])
    df[''] = [stock.info["quickRatio"], stock.info['revenuePerShare'], stock.info['profitMargins'], stock.info['debtToEquity'], stock.info['returnOnEquity']]
    fig_df = table(df)
    st.plotly_chart(fig_df, use_container_width=True)