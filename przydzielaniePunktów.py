import streamlit as st
import pandas as pd
import numpy as np

def przydzielSygnały(data):
    #create an empty df named punkty
    
    pass



# RSI - powyżej 70 przekupienie, poniżej 30 przesprzedanie, pomiędzy 30 a 70 neutralnie, jeśli jest przekupione i spada, to może być sygnał do sprzedaży, jeśli jest przesprzedane i rośnie, to może być sygnał do kupna
# ATR - Im wyżysza wartość, tym większa zmienność, jest to różnica między najwyższą a najniższą ceną
# NATR - Im wyżysza wartość, tym większa zmienność, jest to różnica między najwyższą a najniższą ceną, od ATR różni się tym, że jest to wartość procentowa
# AVGPRICE - Oblicza średnią wartość cenową (dostarcza informacje na temat przeciętnej ceny) 
# ADX - powyżej 25 silny trend, poniżej 20 słaby lub brak trendu
# MACD - prognozowany spadek kiedy linia sygnałowa będzie powyżej linii MACD, prognozowany wzrost kiedy linia sygnałowa będzie poniżej linii MACD
# SMA - 
# Cena powyżej SMA: Może sugerować wzrost cen.
# Cena poniżej SMA: Może sugerować spadek cen.        

