import talib as ta
import pandas as pd
import numpy as np
import streamlit as st


def Świeczuszki(świeczuszki, data):
    świeczki = pd.DataFrame(index=data.index)
    świeczki['Doji'] = ta.CDLDOJI(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Doji Star'] = ta.CDLDOJISTAR(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Dragonfly Doji'] = ta.CDLDRAGONFLYDOJI(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Two Crows'] = ta.CDL2CROWS(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Three Black Crows'] = ta.CDL3BLACKCROWS(data['Open'], data['High'], data['Low'], data['Close'])
    świeczki['Three Inside Up/Down'] = ta.CDL3INSIDE(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
    print(świeczki)

    lista = []

    st.table(świeczki)
    st.sidebar.subheader("Świeczki które są: ")
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
    if 'Two Crows' in lista:
        st.sidebar.write(":green[Two Crows]")
    if 'Three Black Crows' in lista:
        st.sidebar.write(":green[Three Black Crows]")
    if 'Three Inside Up/Down' in lista:  # Added this condition
        st.sidebar.write(":green[Three Inside Up/Down]")  # Added this line
    return świeczki

