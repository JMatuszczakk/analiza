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
from inicjalizacja_wskaźników import inicjalizujWskaźniki
from sajdbar import sidebar
from przydzielaniePunktów import przydzielSygnały
import extra_streamlit_components as stx
from świeczuszki import Świeczuszki
import polygon
#

# funkcja inicjalizująca cookie managera
def get_manager():
    return stx.CookieManager()

#inicjalizacja cookie managera
cookie_manager = get_manager()
#pobranie wszystkich ciasteczek
cookies = cookie_manager.get_all()
#sprawdzenie czy jest ciasteczko o nazwie pomelojekebaba i przypisanie bool'a do zmiennej czyJestKuki
czyJestKuki = 'pomelojekebaba' in cookies

# Jeśli nie ma ciesteczka pomelojekebaba
if czyJestKuki is not True:
    # Wyświetl pole do wpisania hasła w sidebarze
    hasło = st.sidebar.text_input("Podaj hasło", type='password')
else: # jeśli jest ciasteczko pomelojekebaba
    # przypisz do zmiennej hasło wartość pomelojekebaba
    hasło = "pomelojekebaba"
    # wyświetl powiadomienie o zalogowaniu automatycznym
    st.toast("Zalogowano automatycznie", icon="🍪")
    
if 'data' not in st.session_state:
    st.session_state['data'] = None
# Jeśli hasło to nie pomelojekebaba
if hasło != "pomelojekebaba" and czyJestKuki is not True:
    # Jeśli hasło nie jest puste
    if hasło != "": 
        # Wyświetl 50 razy 'nieprawidłowe hasło'
        for i in range(50):
            st.error("Nieprawidłowe hasło", icon="🔑")
            st.sidebar.error("Nieprawidłowe hasło", icon="🔑")
    else: # jeśli hasło jest puste
        # wyświetl 50 razy 'podaj hasło'
        for i in range(50): 
            st.info("Podaj hasło", icon="🧑") 
            st.sidebar.info("Podaj hasło", icon="🧑")
    st.stop() # jeśli hasło jest puste lub nie jest pomelojekebaba, zatrzymaj program
# Jeśli hasło to pomelojekebaba i nie ma ciasteczka pomelojekebaba
if hasło == "pomelojekebaba" and czyJestKuki is not True: 
    # Ustaw ciasteczko pomelojekebaba na pomelojekebaba
    cookie_manager.set('pomelojekebaba', 'pomelojekebaba')
    # Wyświetl powiadomienie o dodaniu ciasteczka
    st.toast("Dodano plik kuki", icon="🍪")

# Sprawdzanie czy akcja jest w obecnej sesji, jeśli nie, przypisywanie AAPL
if 'current_ticker' not in st.session_state:
    st.session_state.current_ticker = 'AAPL'
#Zaokrąglanie
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
#Pobiera dane z biblioteki yfinance i je kejszuje
źródło = st.sidebar.selectbox(label='Źródło danych', options=['yfinance', 'csv'])
miejsce_na_file_uploader2 = st.sidebar.empty()
miejsce_na_file_uploader = st.sidebar.empty()
def get_stock(stock):
    if źródło == 'yfinance':
    # spróbuj
        try:
            # pobierz dane z biblioteki yfinance i przypisuje je do zmiennej data
            data = yfinance.download(tickers=ticker, period='7d', interval='30m', timeout=5)
            # jeśli data jest pusta
            if data.shape[0] == 0:
                # wyświetl error i zatrzymaj program
                st.error("Coś poszło nie tak")
                st.stop()
        except:
            pass
    elif źródło == 'csv':
        plik_csv = miejsce_na_file_uploader.file_uploader("Wybierz plik csv", type=['csv'], ) # wyświetl przycisk do wybrania pliku csv
        if plik_csv is not None:
            data = pd.read_csv(plik_csv)
            data['Datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'])
            data = data.set_index('Datetime')
            data = data.drop(['Date', 'Time'], axis=1)

        else:
            # wyświetl error i zatrzymaj program
            miejsce_na_file_uploader2.success("Wybierz plik csv")
            st.stop()
    st.session_state['data'] = data
    return data # zwróć data jeśli nie było błędu
ticker='AAPL' # przypisz AAPL do ticker na wszelki wypadek jakby się nie wczytał ticker z sidebaru
#wyświetla makapaka 
print("makapaka")
ticker = 'AAPL'
fromSidebar = sidebar(st.session_state['current_ticker'])
try: # próba przypisania zmiennych lokalnych do zrzutu z sidebaru z pliku sajdbar.py 
    ticker = fromSidebar['ticker']
    st.session_state['ticker'] = fromSidebar['ticker']
    doRSI = fromSidebar['doRSI']
    doATR = fromSidebar['doATR']
    doNATR = fromSidebar['doNATR']
    doAVGPRICE = fromSidebar['doAVGPRICE']
    doADX = fromSidebar['doADX']
    doMACD = fromSidebar['doMACD']
    doSMA = fromSidebar['doSMA']
    doBollingerBands = fromSidebar['doBollingerBands']
    atr_color = fromSidebar['atr_color']
    natr_color = fromSidebar['natr_color']
    rsi_color = fromSidebar['rsi_color']
    avgprice_color = fromSidebar['avgprice_color']
    sma_color = fromSidebar['sma_color']
    sma_color2 = fromSidebar['sma_color2']
    macd_color = fromSidebar['macd_color']
    adx_color = fromSidebar['ADX_color']
    bollinger_bands_color = fromSidebar['bollinger_color']
    podsumowanie = fromSidebar['podsumowanie']
    świeczuszki = fromSidebar['świeczuszki']
    st.balloons()
except:
    # w przypadku błędu - zatrzymaj program
    st.stop()
#Wyświetla tytuł i nazwę akcji na zielono
st.title(f'Analiza techniczna :green[{st.session_state["current_ticker"]}]')
# próbuje 
try:
    # pobrać dane z yfinance i przypisać je do zmiennej data
    data = get_stock(ticker)
    # wyświetla powiadomienie o wczytaniu danych
    st.toast('Wczytano dane!', icon='✅')
except Exception as e: # jeśli jest błąd przypisuje nazwę błędu do zmiennej e
    # wyświetla error, wysyła toasta i zatrzymuje program
    st.error(f'Wystąpił błąd')
    st.toast(e)
    st.rerun()
# jeśli data jest pusta
if data.shape[0] == 0:
    # wyświetl error
    st.error("Coś poszło nie tak")
    # uruchamia ponownie program
    st.rerun()
# kopiuje dane do zmiennej data_for_chart w celu wyświetlenia wykresu
data_for_chart = data.copy()

# pokazuje wykres z indeksem jako x, open jako open, high jako high, low jako low, close jako close
candle_chart = go.Figure(data=[go.Candlestick(x=data_for_chart.index,
                open=data_for_chart['Open'],
                high=data_for_chart['High'],
                low=data_for_chart['Low'],
                close=data_for_chart['Close'])])
# ustawia widok wykresu na 48 ostatnich punktów danych
last_48_points_range = [data_for_chart.index[-48], data_for_chart.index[-1]]
candle_chart.update_xaxes(range=last_48_points_range)
# zapisuje miejsce na wykres do zmiennej miejsce_na_charta na później
miejsce_na_charta = st.empty()

# tworzy kolumny na dwa checkboxy
col1, col2, col3, col4 = st.columns(4)
# checkbox na tabelkę w col2
with col2: xdd = st.checkbox('Pokaż tabelke 📝', key='show_table')
# checkbox na wykres w col1, domyślnie zaznaczony
with col1: jkfjsk = st.checkbox('Pokaż wykres 📈', key='show_chart23j23nj', value=True)
# jeśli checkbox na tabelkę jest zaznaczony
if xdd:
    # wyświetl tabelkę
    st.table(data)
# jeśli checkbox na wykres jest zaznaczony
if jkfjsk:
    # wyświetl wykres
    miejsce_na_charta.plotly_chart(candle_chart)

#inicjacja wskaźników z TA-liba i zapisanie ich do df data
data = inicjalizujWskaźniki(data)



#Wyświetlanie wskaźników i ich opisów z TA-lib w zaleźniści, które zaznaczono w sidebarze
if doRSI:
    st.header("RSI")
    st.subheader("Mierzy prędkość i zmiany cen, pomagając inwestorom zidentyfikować, czy aktywo jest :blue[przekupione (nadkupione) lub przesprzedane (nadzwyczaj sprzedawane] :red[Przekupienie rynku] - Stan, w którym cena danego aktywa jest uznawana za :red[wysoką]w stosunku do swojej red:[przewidywanej wartości]  :green[Przesprzedarz] - Stan, w którym cena danego aktywa jest uznawana za :green[niską] w stosunku do swojej :green[przewidywanej wartości])")
    st.write(" RSI - powyżej 70 przekupienie, poniżej 30 przesprzedanie, pomiędzy 30 a 70 neutralnie, jeśli jest przekupione i spada, to może być sygnał do sprzedaży, jeśli jest przesprzedane i rośnie, to może być sygnał do kupna")

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
    mfig = go.Figure(data=[go.Scatter(x=data.index, y=data['MACD'], name='MACD'),])
    mfig.add_trace(go.Scatter(x=data.index, y=data['MACD_signal'], name='MACD signal'))
    mfig.add_trace(go.Scatter(x=data.index, y=data['MACD_direction'], name='MACD direction'))
    mfig.update_layout(title='MACD', xaxis_title='Data', yaxis_title='Cena', template='plotly_dark')
    st.plotly_chart(mfig)
if doSMA:
    st.header("SMA")
    st.subheader("SMA jest używane do identyfikowania :green[ogólnego trendu cenowego]. Kiedy aktualna cena :green[przekracza SMA], może to sugerować :green[wzrost cen], a gdy cena :red[spada poniżej SMA], może to sugerować :red[spadek cen].) ")
    #linechart in go for sma short and long

    # sort data by date
    data = data.sort_index(ascending=True, axis=0)

    

    # slider for how many data to show
    ile_danych = st.slider('Ile danych pokazać?', 1, 200, 12, key='dhjajdjakjd2')
    ile_danych = abs(ile_danych - 200)
    # add line for sma long to linechart above
    smas = go.Figure(data=[go.Scatter(x=data.index[ile_danych:], y=data['SMA_short'][ile_danych:], name='SMA_short'),])
    smas.add_trace(go.Scatter(x=data.index[ile_danych:], y=data['SMA_long'][ile_danych:], name='SMA_long'))
    smas.add_trace(go.Scatter(x=data.index[ile_danych:], y=data['Close'][ile_danych:], name='Close'))
    smas.update_layout(title='SMA', xaxis_title='Data', yaxis_title='Cena', template='plotly_dark')
    st.plotly_chart(smas)
    #linechart in st for sma short and long
    
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



################################################-----KOLORKI-----################################################
#Sprawdzanie czy kolorowaćazwy wskaźników
#ATR
#oblicznie średniej atr

średniaATR = data['ATR'].mean()
if data['ATR'][-1] > średniaATR: 
    atr_color.write(":green[ATR - duża zmienność ceny]")
else:
    atr_color.write(":red[ATR - mała zmienność ceny]")

średniaNATR = data['NATR'].mean()
if data['NATR'][-1] > średniaNATR:
    natr_color.write(":green[NATR - duża zmienność ceny]")
else:
    natr_color.write(":red[NATR - mała zmienność ceny]")


# RSI - powyżej 70 przekupienie, poniżej 30 przesprzedanie, pomiędzy 30 a 70 neutralnie, jeśli jest przekupione i spada, to może być sygnał do sprzedaży, jeśli jest przesprzedane i rośnie, to może być sygnał do kupna

if data['RSI'][-1] > 70:
    rsi_color.write(":green[RSI - opłaca się kupić wartość jest powyżej 70]")
#    licznik +=1
elif data['RSI'][-1]< 30:
    rsi_color.write(":red[RSI- nie opłaca się kupić wartość jest mniejsza niż 30]")
else:
    rsi_color.write(":blue[RSI - jest w przedziale od 30 do 70 (neutralne)]")
    
avgprice_color.write(f":blue[AVGPRICE - przeciętna cena =   {truncate(data['AVGPRICE'][-1], 3)} $] ") 

if data['SMA_long'][-1]> data['Close'][-1]:
    sma_color.write(":green[SMA - Aktualna cena SMA jest większa od aktualnej ceny akcji co wskazuje na wzrost ceny akcji]")
 #   licznik+=1
elif data['SMA_long'][-1]< data['Close'][-1]:
    sma_color.write(":red[SMA - Aktualna cena SMA jest mniejsza od aktualnej ceny akcji co wskazuje na spadek ceny akcji]")
else:
    sma_color.write(":blue[SMA - Aktualna cena SMA jest mniej więcej taka sama jak cena akcji(neutralnie)]")


if data['SMA_short'][-1] > data['SMA_long'][-1]:
    sma_color2.write(":green[SMA crossover - SMA short jest większa od sma long co wskazuje na wzrost ceny akcji]")
if data['SMA_short'][-1] < data['SMA_long'][-1]:
    sma_color2.write(":red[SMA crossover - SMA short jest mniejsza od sma long co wskazuje na spadek ceny akcji]")


# MACD - prognozowany spadek kiedy linia sygnałowa będzie powyżej linii MACD, prognozowany wzrost kiedy linia sygnałowa będzie poniżej linii MACD
# if data['MACD'][-1] > data['MACD_signal'][-1]:
#     macd_color.write(":green[MACD- inia MACD przekracza w górę linii sygnałowej. Oznacza to, że tempo wzrostu jest szybsze niż tempo spadku, co może być interpretowane jako sygnał wzrostowy. ]")
# else:
#     macd_color.write(":red[MACD - linia MACD przekracza w dół linii sygnałowej. Sugeruje to, że tempo spadku jest szybsze niż tempo wzrostu, co może być interpretowane jako sygnał spadkowy.]")
# sprawdzanie czy w ciągu ostatnich 10 wierszy jest sygnał kupna lub sprzedaży
macdkupno = False
for i in range(-5, -1):
    if data['MACD'][i] > data['MACD_signal'][i]: 
        macdkupno = True
        break
if macdkupno == True:
     macd_color.write(":green[MACD- inia MACD przekracza w górę linii sygnałowej. Oznacza to, że tempo wzrostu jest szybsze niż tempo spadku, co może być interpretowane jako sygnał wzrostowy. ]")
else:
     macd_color.write(":red[MACD - linia MACD przekracza w dół linii sygnałowej. Sugeruje to, że tempo spadku jest szybsze niż tempo wzrostu, co może być interpretowane jako sygnał spadkowy.]")

  
#ADX
tekst222 = ''
if data['ADX'][-1] < 20:
    tekst222 = ":blue[ADX - Słaby lub brak trendu]"
elif data['ADX'][-1] > 20 and data['ADX'][-1] < 25:
    tekst222 = ":blue[ADX - Początek trendu, ale jeszcze słaby]"
elif data['ADX'][-1] > 25:
    tekst222 = ":green[ADX - Silny trend]"

adx_color.write(f"{tekst222}")

buldozer = 1
for i in range(-3, -1):
    if data['Close'][i] >= data['UpperBand'][i]:
        buldozer = 1
        break
    elif data['Close'][i] <= data['LowerBand'][i]:
        buldozer = 0
    else:
        buldozer = 2
#        licznik+=1
#bollinger_bands_color
if buldozer == 1:
    bollinger_bands_color.write(":red[Bollinger Bands - upper band dotyka ceny lub cena wyprzedzi go, oznacza to, że akcja jest nakupiona lub nadceniona. Może to oznaczać potencjalne odwrócenie.(chyba to sugeruje spadek)]")
elif buldozer == 0:
    bollinger_bands_color.write(":green[Bollinger Bands - lower band dotyka, lub cena spada poniżej go, oznacza to, że akcja może być nadsprzedana, lub pod wartościowana. Może to oznaczać potencjalne odwrócenie ceny.]")
else:
    bollinger_bands_color.write(":blue[Bollinger Bands - Cena jest w przedziale pomiędzy upper band a lower band, zatem nie można nic powiedzieć na temat przekupienia lub przesprzedania.]")
# Dotychczas opisane wskaźniki to: RSI, ATR, NATR, AVGPRICE, ADX, MACD, SMA, Bollinger Bands
# Relative Strength Index (RSI):
# Overbought: Typically above 70
# Oversold: Typically below 30
# Average True Range (ATR):
# No specific rise or fall thresholds. ATR measures volatility, so larger values indicate higher volatility, and smaller values indicate lower volatility.
# Normalized Average True Range (NATR):
# NATR is a normalized version of ATR, so there isn't a standard threshold for rise or fall. It reflects the volatility as a percentage.
# Average Price (AVGPRICE):
# AVGPRICE is the average of the high, low, and close prices. No specific rise or fall thresholds are commonly used.
# Average Directional Index (ADX):
# Generally, an ADX value above 25 may indicate a trending market. A rising ADX suggests a strengthening trend, while a falling ADX suggests a weakening trend.
# Moving Average Convergence Divergence (MACD):
# Signal Line Crossovers: Bullish signal when MACD crosses above the signal line. Bearish signal when MACD crosses below the signal line.
# Histogram: Bullish when histogram bars rise above the zero line. Bearish when bars fall below the zero line.
# Simple Moving Average (SMA):
# SMA crossovers: Bullish when a shorter-term SMA crosses above a longer-term SMA. Bearish when a shorter-term SMA crosses below a longer-term SMA.
# Bollinger Bands:
# Overbought: When the price touches or exceeds the upper band.
# Oversold: When the price touches or falls below the lower band.




sygnały = przydzielSygnały(data)
st.write(sygnały.tail())

metric_label = "Liczba sygnałów kupna"
print(sygnały.columns)
print(sygnały['SMA'][-1])
current_value = sygnały.iloc[-1]['RSI'] + sygnały.iloc[-1]['MACD'] + sygnały.iloc[-1]['Bollinger Bands'] + sygnały.iloc[-1]['SMAC'] + sygnały.iloc[-1]['SMA']
previous_value = sygnały.iloc[-2]['RSI'] + sygnały.iloc[-2]['MACD'] + sygnały.iloc[-2]['Bollinger Bands'] + sygnały.iloc[-2]['SMAC'] + sygnały.iloc[-2]['SMA']

delta = current_value - previous_value
print(sygnały.columns)
podsumowanie.metric(label=metric_label, value=str(current_value), delta=str(delta))


świeczki = Świeczuszki(świeczuszki, data)


# RSI - powyżej 70 przekupienie, poniżej 30 przesprzedanie, pomiędzy 30 a 70 neutralnie, jeśli jest przekupione i spada, to może być sygnał do sprzedaży, jeśli jest przesprzedane i rośnie, to może być sygnał do kupna
# ATR - Im wyżysza wartość, tym większa zmienność, jest to różnica między najwyższą a najniższą ceną
# NATR - Im wyżysza wartość, tym większa zmienność, jest to różnica między najwyższą a najniższą ceną, od ATR różni się tym, że jest to wartość procentowa
# AVGPRICE - Oblicza średnią wartość cenową (dostarcza informacje na temat przeciętnej ceny) 
# ADX - powyżej 25 silny trend, poniżej 20 słaby lub brak trendu
# MACD - prognozowany spadek kiedy linia sygnałowa będzie powyżej linii MACD, prognozowany wzrost kiedy linia sygnałowa będzie poniżej linii MACD
# SMA - 
# Cena powyżej SMA: Może sugerować wzrost cen.
# Cena poniżej SMA: Może sugerować spadek cen.        