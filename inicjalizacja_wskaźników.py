import numpy as np
import talib as ta
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
    data['Stochastic'], data['Stochastic_signal'] = ta.STOCH(data['High'], data['Low'], data['Close'], fastk_period=5, slowk_period=3, slowd_period=3)
    return data