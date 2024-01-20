import talib
import yfinance
import numpy as np
from talib.abstract import *
from talib import SMA, RSI, ATR, NATR, AVGPRICE
import talib as ta
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import go
import plotly.graph_objects as go



if 'current_ticker' not in st.session_state:
    st.session_state.current_ticker = 'AAPL'

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


@st.cache_data()
def get_stock(stock):
    data = yfinance.download(tickers=ticker, period='30d', interval='1h')
    return data


print("makapaka")
with st.sidebar.form(key='my_form'):
    ticker = st.text_input('Podaj symbol akcji', 'AAPL')
    st.session_state['current_ticker'] = ticker
    doRSI = st.checkbox('RSI - Przekupienie i przesprzedanie')
    doATR = st.checkbox('ATR - Im wyżysza wartość, tym większa zmienność')
    doNATR = st.checkbox('NATR - Im wyżysza wartość, tym większa zmienność')
    doAVGPRICE = st.checkbox('AVGPRICE - Oblicza średnią wartość cenową (dostarcza informacje na temat przeciętnej ceny) ')
    doADX = st.checkbox('ADX - Wartość ADX określa siłę trendu, a nie jego kierunek. Osiąga wartość od 0 do 100.ADX poniżej 20: Słaby lub brak trendu.ADX między 20 a 25: Początek trendu, ale jeszcze słaby.ADX powyżej 25: Silny trend.')
    doMACD = st.checkbox('MACD - Histogram MACD: Różnica między linią MACD a linią sygnałową. Histogram pokazuje siłę i kierunek trendu. Histogram rośnie, gdy różnica między MACD a linią sygnałową rośnie, co może wskazywać na wzrostowy trend. Zmniejszający się histogram może sygnalizować spadek trendu.) ')
    doSMA = st.checkbox('SMA - SMA jest używane do identyfikowania ogólnego trendu cenowego. Kiedy aktualna cena przekracza SMA, może to sugerować wzrost cen, a gdy cena spada poniżej SMA, może to sugerować spadek cen. ')
    doBollingerBands = st.checkbox('Bollinger Bands - Pasmo otaczające cenę aktywa. Standardowo używane do kontrolowania szerokości pasów, a średnia krocząca jako wskaźnik kierunku trendu.')
    submit_button = st.form_submit_button(label='Execute')
    if submit_button:
        st.success('Wykonano!', icon='👏')
        st.balloons()
st.title(f'Analiza techniczna :green[{st.session_state["current_ticker"]}]')
try:
    data = get_stock(ticker)
    st.toast('Wczytano dane!', icon='✅')
except Exception as e:
    st.error(f'Wystąpił błąd')
    st.toast(e)


#st.line_chart(data['Close']) do it in go, use candlestick, show only last 12 entries, remove empty space between stock days
candle_chart = go.Figure(data=[go.Candlestick(x=data.index,
                open=data['Open'][-12:],
                high=data['High'][-12:],
                low=data['Low'][-12:],
                close=data['Close'][-12:])])
st.plotly_chart(candle_chart)

if st.checkbox('Pokaż tabelke 📝', key='show_table'):
    st.table(data)
#cout rows

data['RSI'] = ta.RSI(data['Close'], timeperiod=2)
data['ATR'] = ta.ATR(data['High'], data['Low'], data['Close'], timeperiod=2)
data['NATR'] = ta.NATR(data['High'], data['Low'], data['Close'], timeperiod=2)
data['AVGPRICE'] = ta.AVGPRICE(data['Open'], data['High'], data['Low'], data['Close'])
data['RSI'] = data['RSI'].replace(np.nan, 0)
data['ATR'] = data['ATR'].replace(np.nan, 0)
data['NATR'] = data['NATR'].replace(np.nan, 0)
data['AVGPRICE'] = data['AVGPRICE'].replace(np.nan, 0)
data['ADX'] = ta.ADX(data['High'], data['Low'], data['Close'], timeperiod=14)
data['MACD'], _, _ = ta.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
data['SMA'] = ta.SMA(data['Close'], timeperiod=14)



if doRSI:
    st.header("RSI")
    st.subheader("Przekupienie i przesprzedanie")
    st.line_chart(data['RSI'])
if doATR:
    st.header("ATR")
    st.subheader("Im wyżysza wartość, tym większa zmienność")
    st.line_chart(data['ATR'])
if doNATR:
    st.header("NATR")
    st.subheader("Im wyżysza wartość, tym większa zmienność")
    st.line_chart(data['NATR'])
if doAVGPRICE:
    st.header("AVGPRICE")
    st.subheader("Oblicza średnią wartość cenową (dostarcza informacje na temat przeciętnej ceny) ")
    st.line_chart(data['AVGPRICE'])
if doADX:
    st.header("ADX")
    st.write("Wartość ADX określa siłę trendu, a nie jego kierunek. Osiąga wartość od 0 do 100.ADX poniżej 20: Słaby lub brak trendu.ADX między 20 a 25: Początek trendu, ale jeszcze słaby.ADX powyżej 25: Silny trend.) ", )
    # do the linechart in go, add a line at 25 level color red. Add lines for other as well
    fig = go.Figure(data=go.Scatter(x=data.index, y=data['ADX']))
    fig.add_hline(y=25, line_dash="dash",
              annotation_text="Silny trend", annotation_position="top right", line_color="red")
    fig.add_hline(y=20, line_dash="dot", annotation_text="Początek trendu, ale jeszcze słaby", line_color="green")
    fig.add_hline(y=0, line_dash="dot", annotation_text="Słaby lub brak trendu", line_color="blue")
    st.metric(label="ADX", value=f"{truncate(data['ADX'][-1], 3)}", delta=f"{truncate((data['ADX'][-2] - data['ADX'][-1])*-1, 2)}")
    st.plotly_chart(fig)
if doMACD:
    st.header("MACD")
    st.subheader("Histogram MACD: Różnica między linią MACD a linią sygnałową. Histogram pokazuje siłę i kierunek trendu. Histogram rośnie, gdy różnica między MACD a linią sygnałową rośnie, co może wskazywać na wzrostowy trend. Zmniejszający się histogram może sygnalizować spadek trendu. ")
    st.line_chart(data['MACD'])
if doSMA:
    st.header("SMA")
    st.subheader("SMA jest używane do identyfikowania ogólnego trendu cenowego. Kiedy aktualna cena przekracza SMA, może to sugerować wzrost cen, a gdy cena spada poniżej SMA, może to sugerować spadek cen.) ")
    st.line_chart(data['SMA'])
    