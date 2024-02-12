import pandas as pd
import numpy as np

def przydzielSygnały(data):

    
    #create an empty df named punkty
    sygnały = pd.DataFrame()


    ###ATR###
    średniaATR = data['ATR'].mean()
    # create a column in sygnały that will tell if atr is triggered. index is timmestamp as in data
    sygnały.index = data.index
    # w tabelce sygnały w kolumnie ATR przypisz 1 jeśli wartość ATR jest większa od średniej, w przeciwnym wypadku przypisz 0
    sygnały['ATR'] = np.where(data['ATR'] > średniaATR, 1, 0)

    ###RSI###
    # w tabelce sygnały w kolumnie RSI przypisz 1 jeśli wartość RSI jest większa od 70, w przeciwnym wypadku przypisz 0
    sygnały['RSI'] = np.where(data['RSI'] > 70, 1, 0)
    # w tabelce sygnały w kolumnie RSI przypisz -1 jeśli wartość RSI jest mniejsza od 30, w przeciwnym wypadku przypisz tą samą wartość
    sygnały['RSI'] = np.where(data['RSI'] < 30, -1, sygnały['RSI'])
    # w tabelce sygnały w kolumnie RSI przypisz 0 jeśli wartość RSI jest pomiędzy 30 a 70, w przeciwnym wypadku przypisz tą samą wartość
    sygnały['RSI'] = np.where((data['RSI'] > 30) & (data['RSI'] < 70), 0, sygnały['RSI'])
    

    ###ADX###
    # create a column in sygnały that will tell if adx is triggered. index is timmestamp as in data
    sygnały['ADX'] = np.where(data['ADX'] > 25, 1, 0)
    sygnały['ADX'] = np.where(data['ADX'] < 20, -1, sygnały['ADX'])
    sygnały['ADX'] = np.where((data['ADX'] > 20) & (data['ADX'] < 25), 0, sygnały['ADX'])


    ###MACD###
    # create a column in sygnały that will tell if macd is triggered. index is timmestamp as in data
    sygnały['MACD'] = np.where(data['MACD'] > data['MACD_signal'], 1, 0)
    sygnały['MACD'] = np.where(data['MACD'] < data['MACD_signal'], -1, sygnały['MACD'])
    sygnały['MACD'] = np.where(data['MACD'] == data['MACD_signal'], 0, sygnały['MACD'])


    ###Bollinger Bands###
    # create a column in sygnały that will tell if bollinger bands is triggered. index is timmestamp as in data
    sygnały['Bollinger Bands'] = np.where(data['Close'] > data['UpperBand'], 1, 0)
    sygnały['Bollinger Bands'] = np.where(data['Close'] < data['LowerBand'], -1, sygnały['Bollinger Bands'])
    sygnały['Bollinger Bands'] = np.where((data['Close'] < data['UpperBand']) & (data['Close'] > data['LowerBand']), 0, sygnały['Bollinger Bands'])
    

    ###SMA - Crossover###
    # create a column in sygnały that will tell if sma is triggered. index is timmestamp as in data
    sygnały['SMAC'] = np.where(data['SMA_short'] > data['SMA_long'], 1, 0)
    sygnały['SMAC'] = np.where(data['SMA_short'] < data['SMA_long'], -1, sygnały['SMAC'])
    sygnały['SMAC'] = np.where(data['SMA_short'] == data['SMA_long'], 0, sygnały['SMAC'])
    
    ###SMA - Aktualna cena###
    # create a column in sygnały that will tell if sma is triggered. index is timmestamp as in data
    sygnały['SMA'] = np.where(data['SMA_short'] > data['Close'], 1, 0)
    sygnały['SMA'] = np.where(data['SMA_short'] < data['Close'], -1, sygnały['SMA'])
    sygnały['SMA'] = np.where(data['SMA_short'] == data['Close'], 0, sygnały['SMA'])

    ###Stochastic###
    # create a column in sygnały that will tell if stochastic is triggered. index is timmestamp as in data
    sygnały['Stochastic'] = np.where(data['Stochastic'] > data['Stochastic_signal'], 1, 0)
    sygnały['Stochastic'] = np.where(data['Stochastic'] < data['Stochastic_signal'], -1, sygnały['Stochastic'])
    sygnały['Stochastic'] = np.where(data['Stochastic'] == data['Stochastic_signal'], 0, sygnały['Stochastic'])
    


    

    return sygnały



# RSI - powyżej 70 przekupienie, poniżej 30 przesprzedanie, pomiędzy 30 a 70 neutralnie, jeśli jest przekupione i spada, to może być sygnał do sprzedaży, jeśli jest przesprzedane i rośnie, to może być sygnał do kupna
# ATR - Im wyżysza wartość, tym większa zmienność, jest to różnica między najwyższą a najniższą ceną
# NATR - Im wyżysza wartość, tym większa zmienność, jest to różnica między najwyższą a najniższą ceną, od ATR różni się tym, że jest to wartość procentowa
# AVGPRICE - Oblicza średnią wartość cenową (dostarcza informacje na temat przeciętnej ceny) 
# ADX - powyżej 25 silny trend, poniżej 20 słaby lub brak trendu
# MACD - prognozowany spadek kiedy linia sygnałowa będzie powyżej linii MACD, prognozowany wzrost kiedy linia sygnałowa będzie poniżej linii MACD
# SMA - 
# Cena powyżej SMA: Może sugerować wzrost cen.
# Cena poniżej SMA: Może sugerować spadek cen.        

'''
if data['SMA_long'][-1]> data['Close'][-1]:
    sma_color.write(":green[SMA - Aktualna cena SMA jest większa od aktualnej ceny akcji co wskazuje na wzrost ceny akcji]")
 #   licznik+=1
if data['SMA_long'][-1]< data['Close'][-1]:
    sma_color.write(":red[SMA - Aktualna cena SMA jest mniejsza od aktualnej ceny akcji co wskazuje na spadek ceny akcji]")
else:
    sma_color.write(":blue[SMA - Aktualna cena SMA jest mniej więcej taka sama jak cena akcji(neutralnie)]")
    

'''