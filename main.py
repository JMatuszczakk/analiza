import talib
import yfinance
import numpy as np
from talib.abstract import *
from talib import SMA, RSI, ATR, NATR, AVGPRICE
import streamlit as st

@st.cache_data()
def get_stock(stock):
    data = yfinance.download(tickers=ticker, period='1d', interval='1h')
    return data


print("makapaka")
with st.sidebar.form(key='my_form'):
    ticker = st.text_input('Podaj symbol akcji', 'AAPL')
    doRSI = st.checkbox('RSI - Przekupienie i przesprzedanie')
    doATR = st.checkbox('ATR - Im wyżysza wartość, tym większa zmienność')
    doNATR = st.checkbox('NATR - Im wyżysza wartość, tym większa zmienność')
    doAVGPRICE = st.checkbox('AVGPRICE - Oblicza średnią wartość cenową (dostarcza informacje na temat przeciętnej ceny) ')
    submit_button = st.form_submit_button(label='Execute')
    if submit_button:
        st.success('Wykonano!', icon='👏')
        st.balloons()
st.title(f'Analiza techniczna {ticker}')
try:
    data = get_stock(ticker)
    st.success('Wczytano dane!', icon='✅') 
except Exception as e:
    st.error(f'Wystąpił błąd')
    st.toast(e)


st.line_chart(data['Close'])
st.table(data)
#cout rows

data['RSI'] = RSI(data['Close'], timeperiod=2)
data['ATR'] = ATR(data['High'], data['Low'], data['Close'], timeperiod=2)
data['NATR'] = NATR(data['High'], data['Low'], data['Close'], timeperiod=2)
data['AVGPRICE'] = AVGPRICE(data['Open'], data['High'], data['Low'], data['Close'])
data['RSI'] = data['RSI'].replace(np.nan, 0)
data['ATR'] = data['ATR'].replace(np.nan, 0)
data['NATR'] = data['NATR'].replace(np.nan, 0)
data['AVGPRICE'] = data['AVGPRICE'].replace(np.nan, 0)

if doRSI:
    st.header("RSI")
    st.subheader("Przekupienie i przesprzedanie")
    st.line_chart(data['RSI'])
if doATR:
    st.header("ATR")
    st.subheader("Im wyżysza wartość, tym większa zmienność")
    st.table (data['ATR'])
if doNATR:
    st.header("NATR")
    st.subheader("Im wyżysza wartość, tym większa zmienność")
    st.line_chart(data['NATR'])
if doAVGPRICE:
    st.header("AVGPRICE")
    st.subheader("Oblicza średnią wartość cenową (dostarcza informacje na temat przeciętnej ceny) ")
    st.line_chart(data['AVGPRICE'])