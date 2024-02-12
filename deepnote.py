import numpy as np
import talib as ta
import pandas as pd
import yfinance

def pobierzDane(nazwa, okres, interwał):
    data = yfinance.download(tickers=nazwa, period=okres, interval=interwał, timeout=5)
    return data



def inicjalizujWskaźniki(data):
    data['RSI'] = ta.RSI(data['Close'], timeperiod=16)
    data['ATR'] = ta.ATR(data['High'], data['Low'], data['Close'], timeperiod=16)
    data['NATR'] = ta.NATR(data['High'], data['Low'], data['Close'], timeperiod=16)
    data['AVGPRICE'] = ta.AVGPRICE(data['Open'], data['High'], data['Low'], data['Close'])
    data['ADX'] = ta.ADX(data['High'], data['Low'], data['Close'], timeperiod=16)
    data['MACD'], data['MACD_signal'], data['MACD_direction'] = ta.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    data['SMA_short'] = ta.SMA(data['Close'], timeperiod=16)
    data['SMA_long'] = ta.SMA(data['Close'], timeperiod=48)
    upper_band, middle_band, lower_band = ta.BBANDS(data['Close'], timeperiod=16, nbdevup=2, nbdevdn=2)
    data['UpperBand'] = upper_band
    data['MiddleBand'] = middle_band
    data['LowerBand'] = lower_band
    return data



def Świeczuszki(świeczuszki, data, czy_pokazać = False):
    świeczki = pd.DataFrame(index=data.index)
    świeczki['Doji'] = ta.CDLDOJI(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Doji Star'] = ta.CDLDOJISTAR(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Dragonfly Doji'] = ta.CDLDRAGONFLYDOJI(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Two Crows'] = ta.CDL2CROWS(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Three Black Crows'] = ta.CDL3BLACKCROWS(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Three Inside Up/Down'] = ta.CDL3INSIDE(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Three Line Strike'] = ta.CDL3LINESTRIKE(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Three Outside Up/Down'] = ta.CDL3OUTSIDE(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Three Stars In The South'] = ta.CDL3STARSINSOUTH(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Three White Soldiers'] = ta.CDL3WHITESOLDIERS(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Abandoned Baby'] = ta.CDLABANDONEDBABY(data['Open'], data['High'], data['Low'], data['Close'], penetration=0)
    świeczki['Advance Block'] = ta.CDLADVANCEBLOCK(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Belt Hold'] = ta.CDLBELTHOLD(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Breakaway'] = ta.CDLBREAKAWAY(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Closing Marubozu'] = ta.CDLCLOSINGMARUBOZU(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Concealing Baby Swallow'] = ta.CDLCONCEALBABYSWALL(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Engulfing'] = ta.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Evening Doji Star'] = ta.CDLEVENINGDOJISTAR(data['Open'], data['High'], data['Low'], data['Close'], penetration=0)
    świeczki['Evening Star'] = ta.CDLEVENINGSTAR(data['Open'], data['High'], data['Low'], data['Close'], penetration=0)
    świeczki['Gaps Side-by-Side White'] = ta.CDLGAPSIDESIDEWHITE(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Gravestone Doji'] = ta.CDLGRAVESTONEDOJI(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Hammer'] = ta.CDLHAMMER(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Hanging Man'] = ta.CDLHANGINGMAN(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Harami'] = ta.CDLHARAMI(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Harami Cross'] = ta.CDLHARAMICROSS(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['High-Wave'] = ta.CDLHIGHWAVE(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Hikkake'] = ta.CDLHIKKAKE(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Homing Pigeon'] = ta.CDLHOMINGPIGEON(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Identical Three Crows'] = ta.CDLIDENTICAL3CROWS(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['In-Neck'] = ta.CDLINNECK(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Inverted Hammer'] = ta.CDLINVERTEDHAMMER(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Kicking'] = ta.CDLKICKING(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Kicking by Length'] = ta.CDLKICKINGBYLENGTH(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Ladder Bottom'] = ta.CDLLADDERBOTTOM(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Long Legged Doji'] = ta.CDLLONGLEGGEDDOJI(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Long Line'] = ta.CDLLONGLINE(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Marubozu'] = ta.CDLMARUBOZU(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Matching Low'] = ta.CDLMATCHINGLOW(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Mat Hold'] = ta.CDLMATHOLD(data['Open'], data['High'], data['Low'], data['Close'], penetration=0)  
    świeczki['Morning Doji Star'] = ta.CDLMORNINGDOJISTAR(data['Open'], data['High'], data['Low'], data['Close'], penetration=0)  
    świeczki['Morning Star'] = ta.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'], penetration=0)  
    świeczki['On-Neck'] = ta.CDLONNECK(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Piercing'] = ta.CDLPIERCING(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Rickshaw Man'] = ta.CDLRICKSHAWMAN(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Rising/Falling Three Methods'] = ta.CDLRISEFALL3METHODS(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Separating Lines'] = ta.CDLSEPARATINGLINES(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Shooting Star'] = ta.CDLSHOOTINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Short Line'] = ta.CDLSHORTLINE(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Spinning Top'] = ta.CDLSPINNINGTOP(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Stalled Pattern'] = ta.CDLSTALLEDPATTERN(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Stick Sandwich'] = ta.CDLSTICKSANDWICH(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Takuri'] = ta.CDLTAKURI(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Tasuki Gap'] = ta.CDLTASUKIGAP(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Thrusting'] = ta.CDLTHRUSTING(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Tristar'] = ta.CDLTRISTAR(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Unique 3 River'] = ta.CDLUNIQUE3RIVER(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Upside Gap Two Crows'] = ta.CDLUPSIDEGAP2CROWS(data['Open'], data['High'], data['Low'], data['Close'])  
    świeczki['Upside/Downside Gap Three Methods'] = ta.CDLXSIDEGAP3METHODS(data['Open'], data['High'], data['Low'], data['Close'])    
    print(świeczki)

    lista = []
    wykryte2 = []


    for i in świeczki.columns:
        for y in świeczki[i][-4:]:
            if y != 0:
                lista.append(i)
                wykryte2.append((i, y))
                


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



    

    return sygnały