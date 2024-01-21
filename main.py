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
import plotly.graph_objects as go




# Sprawdzanie czy akcja jest w obecnej sesji, jeśli nie, przypisywanie AAPL
if 'current_ticker' not in st.session_state:
    st.session_state.current_ticker = 'AAPL'
#Zaokrąglanie
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
#Pobiera dane z biblioteki yfinance i je kejszuje
@st.cache_data()
def get_stock(stock):
    data = yfinance.download(tickers=ticker, period='30d', interval='1h')
    return data

#wyświetla makapaka
print("makapaka")
#sidebar po lewej stronie strony
with st.sidebar.form(key='my_form'):
    #utworzenie dwóch kolumn w sidebarze
    col1, col2 = st.columns(2)
    #wyświetla wartości z biblioteki yfinance w dwóch kolumnach w sidebarze
    with col1:
        st.metric(label=f":green[Zamknięcie ] :green[{st.session_state['current_ticker']}]", value=f"{truncate(get_stock(st.session_state['current_ticker'])['Close'][0], 3)}$", delta=f"{truncate((get_stock(st.session_state['current_ticker'])['Close'][1] - get_stock(st.session_state['current_ticker'])['Close'][0])*-1, 2)}$")
    with col2:
        st.metric(label=f":green[Otwarcie ] :green[{st.session_state['current_ticker']}]", value=f"{truncate(get_stock(st.session_state['current_ticker'])['Open'][0], 3)}$", delta=f"{truncate((get_stock(st.session_state['current_ticker'])['Open'][1] - get_stock(st.session_state['current_ticker'])['Open'][0])*-1, 2)}$")
   #make the descriptions short
    ticker = st.text_input('Podaj symbol akcji', 'AAPL')
    st.session_state['current_ticker'] = ticker
    doRSI = st.checkbox('RSI - Przekupienie i przesprzedanie')
    doATR = st.checkbox('ATR - Im wyżysza wartość, tym większa zmienność')
    doNATR = st.checkbox('NATR - Im wyżysza wartość, tym większa zmienność')
    doAVGPRICE = st.checkbox('AVGPRICE - Oblicza średnią wartość cenową (dostarcza informacje na temat przeciętnej ceny) ')
    doADX = st.checkbox('ADX - Podsumowując, ADX pomaga inwestorom określić, czy rynek znajduje się w fazie trendu i oceniać jego siłę')
    doMACD = st.checkbox('MACD - dostarcza informacji o dynamice zmian w trendzie. ')
    doSMA = st.checkbox('SMA - indentyfikuje ogólny kierunek ruchu cenowego ')
    doBollingerBands = st.checkbox('Bollinger Bands - Przekupienie i przesprzedanie, odwracanie ceny')
    submit_button = st.form_submit_button(label='Execute')
    #sprawdza czy przycisk został wciśnięty
    if submit_button:
        st.success('Wykonano!', icon='👏')
        st.balloons()
#Wyświetla tytuł i nazwę akcji na zielono
st.title(f'Analiza techniczna :green[{st.session_state["current_ticker"]}]')
#pobiera dane i mówi czy dane zostały pomyślnie pobrane, jeśli nie wyświetla error i tosta
try:
    data = get_stock(ticker)
    st.toast('Wczytano dane!', icon='✅')
except Exception as e:
    st.error(f'Wystąpił błąd')
    st.toast(e)
data_for_chart = data.copy()
#Pokazuje wykres ze świeczkami
candle_chart = go.Figure(data=[go.Candlestick(x=data_for_chart.index,
                open=data_for_chart['Open'],
                high=data_for_chart['High'],
                low=data_for_chart['Low'],
                close=data_for_chart['Close'])])
miejsce_na_charta = st.empty()

#Po zaznaczeniu checkboxa pokazuje tabelke
col1, col2, col3, col4 = st.columns(4)
with col2: xdd = st.checkbox('Pokaż tabelke 📝', key='show_table')
with col1: jkfjsk = st.checkbox('Pokaż wykres 📈', key='show_chart23j23nj', value=True)
if xdd:
    st.table(data)
if jkfjsk:
    miejsce_na_charta.plotly_chart(candle_chart)
#inicjacja wskaźników z TA-liba i zapisanie ich do df data
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
upper_band, middle_band, lower_band = ta.BBANDS(data['Close'], timeperiod=10, nbdevup=2, nbdevdn=2)
data['UpperBand'] = upper_band
data['MiddleBand'] = middle_band
data['LowerBand'] = lower_band

#Wyświetlanie wskaźników i ich opisów z TA-lib w zaleźniści, które zaznaczono w sidebarze
if doRSI:
    st.header("RSI")
    st.subheader("Przekupienie i przesprzedanie")
    st.line_chart(data['RSI'])
if doATR:
    st.header("ATR")
    st.subheader("Im :green[wyżysza wartość], tym większa :green[zmienność]")
    st.line_chart(data['ATR'])
if doNATR:
    st.header("NATR")
    st.subheader("Im :green[wyżysza] wartość, tym większa :green[zmienność] (działa podobnie jak :red[ATR])")
    st.line_chart(data['NATR'])
if doAVGPRICE:
    st.header("AVGPRICE")
    st.subheader("Oblicza :green[średnią wartość cenową] (dostarcza informacje na temat :green[przeciętnej ceny]) ")
    st.line_chart(data['AVGPRICE'])
if doADX:
    
    st.header("ADX")
    st.write("Wartość ADX określa siłę trendu   ", )
    st.write(":blue[ADX poniżej 20: Słaby lub brak trendu.]")
    st.write(":green[ADX między 20 a 25: Początek trendu, ale jeszcze słaby.]")
    st.write(":red[ADX powyżej 25: Silny trend.] ")
    tekst = ''
    if data['ADX'][-1] < 20:
        tekst = "Słaby lub brak trendu"
    elif data['ADX'][-1] > 20 and data['ADX'][-1] < 25:
        tekst = "Początek trendu, ale jeszcze słaby"
    elif data['ADX'][-1] > 25:
        tekst = "Silny trend"
    
    col1, col2, col3, col4 = st.columns(4)
    fig = go.Figure(data=go.Scatter(x=data.index, y=data['ADX']))
    fig.add_hline(y=25, line_dash="dash",
              annotation_text="Silny trend", annotation_position="top right", line_color="red")
    fig.add_hline(y=20, line_dash="dot", annotation_text="Początek trendu, ale jeszcze słaby", line_color="green")
    fig.add_hline(y=0, line_dash="dot", annotation_text="Słaby lub brak trendu", line_color="blue")
    with col1: st.metric(label="ADX", value=f"{truncate(data['ADX'][-1], 3)}", delta=f"{truncate((data['ADX'][-2] - data['ADX'][-1])*-1, 2)}")
    with col2: st.subheader(f"- {tekst}")
    st.plotly_chart(fig)
if doMACD:
    st.header("MACD")
    st.subheader("Histogram MACD: Różnica między :green[linią MACD] a :red[linią sygnałową]. Histogram pokazuje :green[siłę i kierunek trendu]. Histogram rośnie, gdy różnica między MACD a linią sygnałową rośnie, co może wskazywać na wzrostowy trend. Zmniejszający się histogram może sygnalizować spadek trendu. ")
    st.line_chart(data['MACD'])
if doSMA:
    st.header("SMA")
    st.subheader("SMA jest używane do identyfikowania :green[ogólnego trendu cenowego]. Kiedy aktualna cena :green[przekracza SMA], może to sugerować :green[wzrost cen], a gdy cena :red[spada poniżej SMA], może to sugerować :red[spadek cen].) ")
    st.line_chart(data['SMA'])
if doBollingerBands:
        st.header("Bollinger Bands")
        if st.checkbox("Rozprawka 🤓"): st.subheader("Pomaga inwestorom ocenić, czy aktywo jest :green[przekupione] czy :red[przesprzedane], a także określić potencjalne poziomy wsparcia i oporu W praktyce, kiedy ceny zbliżają się do górnego pasa, może to sugerować, że aktywo jest przekupione, a kiedy zbliżają się do dolnego pasa, może to sugerować, że jest przesprzedane. Inwestorzy szukają sygnałów odwrócenia trendu lub potencjalnych punktów wejścia lub wyjścia na rynku w oparciu o relację cen do pasm.")
        st.write("Jak :red[upper band] dotyka ceny lub cena wyprzedzi go, oznacza to, że akcja jest nakupiona lub nadceniona. Może to oznaczać potencjalne odwrócenie.")
        st. write("Jak :green[lower band] dotyka, lub cena spada poniżej go, oznacza to, że akcja może być nadsprzedana, lub pod wartościowana. Może to oznaczać potencjalne odwrócenie ceny.")
        #Wybór przez użytkownika ile danych chce
        ile_danych = st.slider('Ile danych pokazać?', 1, 200, 12)
        
        ile_danych+=12
        #Generowanie trzech wykresów jeden odpowiedzialny za close , drugi UpperBand kolorem czerwonym, trzeci MiddleBand kolorem cyjan, czwarty LowerBand kolorem zielonym
        fig = go.Figure(data=[
            go.Scatter(x=data.index, y=data['Close'][10:ile_danych], name='Close'),
            go.Scatter(x=data.index, y=data['UpperBand'][10:ile_danych], line=dict(color='red', width=1), name='Upper Band'),
            go.Scatter(x=data.index, y=data['MiddleBand'][10:ile_danych], line=dict(color='cyan', width=1), name='Middle Band'),
            go.Scatter(x=data.index, y=data['LowerBand'][10:ile_danych], line=dict(color='green', width=1), name='Lower Band')
        ])
        # Dodanie tytułu, osi x, osi y, szablonu
        fig.update_layout(title='Bollinger Bands', xaxis_title='Data', yaxis_title='Cena', template='plotly_dark')
        # Wyświetlenie wykresu
        st.plotly_chart(fig)

    