import streamlit as st
import yfinance
import pytz
from datetime import datetime


def sidebar(ticker):
    try:    
        


        def truncate(n, decimals=0):
            multiplier = 10 ** decimals
            return int(n * multiplier) / multiplier
        #Pobiera dane z biblioteki yfinance i je kejszuje
        def get_stock(stock):
            try:
                data = yfinance.download(tickers=ticker, period='1d', interval='1m')
                if data.shape[0] == 0:
                    st.error("Coś poszło nie tak")
                    st.stop()
            except:
                st.toast("Gówno ")
            return data

        with st.sidebar:
            with st.form(key='my_form'):
                #Poniżej znajduje się kod który wyświetl godzinę z strefy czasowej GMT-5
                tz = pytz.timezone('US/Eastern')
                st.title(f"Godzina w GTM -5 to :green[{datetime.now(tz).strftime('%H:%M')}]")
                st.subheader("Godzina otwarcia giełdy to :green[15:30] czasu polskiego")
                st.subheader("Godzina zamknięcia giełdy to :red[22:00] czasu polskiego")

                #interval = st.selectbox('Wybierz interwał', ['1m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'])
                #utworzenie dwóch kolumn w sidebarze
                col1, col2 = st.columns(2)
                #wyświetla wartości z biblioteki yfinance w dwóch kolumnach w sidebarze
                with col1:
                    st.metric(label=f":green[Zamknięcie ] :green[{ticker}]", value=f"{truncate(get_stock(st.session_state['current_ticker'])['Close'][-2], 3)}$", delta=f"{truncate((get_stock(st.session_state['current_ticker'])['Close'][-2] - get_stock(st.session_state['current_ticker'])['Close'][-1])*-1, 2)}$")
                with col2:
                    st.metric(label=f":green[Otwarcie (Aktualne) ] :green[{ticker}]", value=f"{truncate(get_stock(st.session_state['current_ticker'])['Open'][-1], 3)}$", delta=f"{truncate((get_stock(st.session_state['current_ticker'])['Open'][-2] - get_stock(st.session_state['current_ticker'])['Open'][-1])*-1, 2)}$")
                #make the descriptions short
                ticker = 'AAPL'
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
                st.form_submit_button(label='Zatwierdź')
            #Definiowanie st.empty dla kolorowych wskaźników
            
            
            if ticker == None:
                st.rerun()
           
            return {
                'ticker': ticker,
                'doRSI': doRSI,
                'doATR': doATR,
                'doNATR': doNATR,
                'doAVGPRICE': doAVGPRICE,
                'doADX': doADX,
                'doMACD': doMACD,
                'doSMA': doSMA,
                'doBollingerBands': doBollingerBands,
                'rsi_color': st.empty(),
                'atr_color': st.empty(),
                'natr_color': st.empty(),
                'avgprice_color': st.empty(),
                'ADX_color' : st.empty(),
                'macd_color' : st.empty(),
                'sma_color': st.empty(),
                'sma_color2': st.empty(),
                'bollinger_color' : st.empty(),
            }
    except Exception as e:
        st.error("Coś poszło nie tak")
        st.toast(e)