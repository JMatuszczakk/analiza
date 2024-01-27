import talib as ta
import pandas as pd
import numpy as np
import streamlit as st


def Świeczuszki(świeczuszki, data):
    świeczki = pd.DataFrame(index=data.index)
    świeczki['Doji'] = ta.CDLDOJI(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Doji Star'] = ta.CDLDOJISTAR(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Dragonfly Doji'] = ta.CDLDRAGONFLYDOJI(data['Open'], data['High'], data['Low'], data['Close'])
    print(świeczki)

    

    lista = []

    świeczuszki.write(świeczki)
    # wyświetlanie świeczek które są
    st.sidebar.subheader("Świeczki które są: ")
    # jeśli w ostatnich 4 datapointach jest doji to wyświetl doji w kolorze zielonym i objaśnij co to jest
    for i in świeczki.columns:
        for y in świeczki[i][-4:]:
            if y == 100:
                lista.append(i)


    if 'Doji' in lista:
        st.sidebar.write(":green[Doji]")
    if 'Doji Star' in lista:
        st.sidebar.write(":green[Doji Star]")
    if 'Dragonfly Doji' in lista:
        st.sidebar.write(":green[Dragonfly Doji]")
    return świeczki


