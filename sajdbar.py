import streamlit as st
import yfinance


def sidebar(ticker):
    def truncate(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier
    #Pobiera dane z biblioteki yfinance i je kejszuje
    @st.cache_data()
    def get_stock(stock):
        data = yfinance.download(tickers=ticker, period='30d', interval='1h')
        return data

    with st.sidebar:
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
        #Definiowanie st.empty dla kolorowych wskaźników
        atr_color = st.empty()
        natr_color = st.empty()
        return {
            'doRSI': doRSI,
            'doATR': doATR,
            'doNATR': doNATR,
            'doAVGPRICE': doAVGPRICE,
            'doADX': doADX,
            'doMACD': doMACD,
            'doSMA': doSMA,
            'doBollingerBands': doBollingerBands,
            'atr_color': st.empty(),
            'natr_color': st.empty()
        }