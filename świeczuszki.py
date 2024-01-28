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

    st.table(świeczki)
    st.sidebar.subheader("Świeczki które są: ")
    for i in świeczki.columns:
        for y in świeczki[i][-4:]:
            if y == 100 or y == -100:
                lista.append(i)


    na_plus = 0
    na_minus = 0
    na_odwrócenie = 0
    kontynuacja = 0


    if 'Doji' in lista:
        st.sidebar.write(":green[Doji] - odwórcenie ceny")
        na_odwrócenie += 1
    if 'Doji Star' in lista:
        st.sidebar.write(":green[Doji Star] - odwórcenie ceny")
        na_odwrócenie += 1
    if 'Dragonfly Doji' in lista:
        st.sidebar.write(":green[Dragonfly Doji] - odwórcenie ceny")
        na_odwrócenie += 1
    if 'Two Crows' in lista:
        st.sidebar.write(":green[Two Crows] - odwórcenie ceny")
        na_minus += 1

    if 'Three Black Crows' in lista:
        st.sidebar.write(":green[Three Black Crows] - mocny sygnał spadkowy zazwyczaj się nie myli")
        na_minus += 1
    # if 'Three Inside Up/Down' in lista:
    #     st.sidebar.write(":green[Three Inside Up/Down - sugeruje spadek]")
    #     na_minus += 1
    if 'Three Line Strike' in lista:
        st.sidebar.write(":green[Three Line Strike] - sygnał wzrostowy po uprzednich spadkach")
        na_minus += 1
        na_odwrócenie += 1

    # if 'Three Outside Up/Down' in lista:
    #     st.sidebar.write(":green[Three Outside Up/Down - na odwrócenie]")
    #     na_odwrócenie += 1

    if 'Three Stars In The South' in lista:
        st.sidebar.write(":green[Three Stars In The South] - sygnał koniec trendu bessy")
        na_odwrócenie += 1
        na_plus += 1
    if 'Three White Soldiers' in lista:
        st.sidebar.write(":green[Three White Soldiers] - przewiduje odwrócenie się rynku spadkowego w stronę wzrostową")
        na_plus += 1
        na_odwrócenie += 1

    if 'Abandoned Baby' in lista:
        st.sidebar.write(":green[Abandoned Baby] - bardzo krótkoterminowy sygnał odwrócenia trendu w dół")
        na_odwrócenie += 1
        na_minus += 1

    if 'Advance Block' in lista:
        st.sidebar.write(":green[Advance Block] - sygnał odwrócenia trendu, ale tylko w dół w stosunkowo krótkim okresie")
        na_odwrócenie += 1
        na_minus += 1
    if 'Belt Hold' in lista:
        st.sidebar.write(":green[Belt Hold] - odwrócenie trendu")
        na_odwrócenie += 1
    if 'Breakaway' in lista:
        st.sidebar.write(":green[Breakaway] - odwrócenie trendu w piątym dniu po znalezieniu formacji")
        na_odwrócenie += 1
    if 'Closing Marubozu' in lista:
        na_odwrócenie += 1
        st.sidebar.write(":green[Closing Marubozu] - jest silniejszym wzorem świecowym. Powstaje, gdy cena zamknięcia jest równa najwyższej lub najniższej cenie dnia. Kiedy cena zamknięcia jest równa najniższej, wówczas nazywa się to niedźwiedziem, a gdy cena zamknięcia jest równa najwyższej, jest to byczy")
    if 'Concealing Baby Swallow' in lista:
        st.sidebar.write(":green[Concealing Baby Swallow] - zwyżkowy wzór odwrócenia")
        na_odwrócenie += 1
        na_plus += 1
    if 'Engulfing' in lista:
        st.sidebar.write(":green[Engulfing] - odwrócenie trendu")
        na_odwrócenie += 1
    if 'Evening Doji Star' in lista:
        st.sidebar.write(":green[Evening Doji Star] - odwrócenie trendu na spadkowy")
        na_minus += 1
    if 'Evening Star' in lista:
        st.sidebar.write(":green[Evening Star] - odwrócenie trendu na spadkowy")
        na_minus += 1
        na_odwrócenie += 1
    if 'Gaps Side-by-Side White' in lista:
        st.sidebar.write(":green[Gaps Side-by-Side White] - kontynuacja trendu wzrostowego")
        kontynuacja += 1
    if 'Gravestone Doji' in lista:
        st.sidebar.write(":green[Gravestone Doji] - średnia wiarygodność sugeruje odwrócenie trendu na rosnący")
        na_odwrócenie += 1
        na_plus += 1
    if 'Hammer' in lista:
        st.sidebar.write(":green[Hammer] - odwrócenie trendu na wzrostowy")
        na_odwrócenie += 1
        na_plus += 1
    if 'Hanging Man' in lista:
        st.sidebar.write(":green[Hanging Man] - odwrócenie trendu na spadkowy ale nie jest to pewne")
        na_odwrócenie += 1
        na_minus += 1
    if 'Harami' in lista:
        st.sidebar.write(":green[Harami] - Ogólnie wskazuje na niewielki wzrost ceny")
        na_plus += 1

    if 'Harami Cross' in lista:
        st.sidebar.write(":green[Harami Cross] - odwrócenie trendu")
        na_odwrócenie += 1
    # Ta formacja świecowa praktycznie nic nam nie mówi o kierunku rynku.
    # if 'High-Wave' in lista:
    #     st.sidebar.write(":green[High-Wave]")
    if 'Hikkake' in lista:
        st.sidebar.write(":green[Hikkake] - formacja wzrostowa, ale nie jest to pewne")
        na_plus += 1
    if 'Homing Pigeon' in lista:
        st.sidebar.write(":green[Homing Pigeon] - odwrócenie trendu na wzrostowy")
        na_odwrócenie += 1
        na_plus += 1
    if 'Identical Three Crows' in lista:
        st.sidebar.write(":green[Identical Three Crows] - odwrócenie trendu na spadkowy")
        na_odwrócenie += 1
        na_minus += 1
    if 'In-Neck' in lista: 
        st.sidebar.write(":green[In-Neck] - kontynuacja trendu spadkowego")
        na_minus +=1
        kontynuacja += 1  
    if 'Inverted Hammer' in lista: 
        st.sidebar.write(":green[Inverted Hammer] - odwrócenie trendu")  
        na_odwrócenie += 1
    if 'Kicking' in lista: 
        st.sidebar.write(":green[Kicking] - odw®ócenie trendu")  
        na_odwrócenie += 1
    if 'Kicking by Length' in lista: 
        st.sidebar.write(":green[Kicking by Length] - odwrócenie trendu na wzrostowy")
        na_odwrócenie += 1
        na_plus += 1  
    if 'Ladder Bottom' in lista: 
        st.sidebar.write(":green[Ladder Bottom - odwrócenie trendu na wzrostowy]")  
        na_odwrócenie += 1
        na_plus += 1
    if 'Long Legged Doji' in lista: 
        st.sidebar.write(":green[Long Legged Doji] - niepewność na rynku, nie wiadomo czy wzrost czy spadek")
        na_odwrócenie += 1  
    # if 'Long Line' in lista: 
    #     st.sidebar.write(":green[Long Line]")  
    if 'Marubozu' in lista: 
        st.sidebar.write(":green[Marubozu] - brak wahania, stabilnie, git, otwarcie długoterminowej pozycji")  
    if 'Matching Low' in lista: 
        st.sidebar.write(":green[Matching Low] - dno spadku, wymaga potwierdzenia")
        na_odwrócenie += 1
        na_plus += 1  
    if 'Mat Hold' in lista: 
        st.sidebar.write(":green[Mat Hold] - kontynuacja trendu")
        kontynuacja += 1
    if 'Morning Doji Star' in lista: 
        st.sidebar.write(":green[Morning Doji Star] - odwrócenie trendu na wzrostowy")
        na_odwrócenie += 1
        na_plus += 1
    if 'Morning Star' in lista: 
        st.sidebar.write(":green[Morning Star] - odwrócenie, dno spadku")
        na_odwrócenie += 1
        na_plus += 1
    if 'On-Neck' in lista: 
        st.sidebar.write(":green[On-Neck] - kontynuacja trendu spadkowego") 
        na_minus +=1
        kontynuacja += 1 
    if 'Piercing' in lista: 
        st.sidebar.write(":green[Piercing] - odwrócenie na wzrostowy")  
        na_plus += 1
    if 'Rickshaw Man' in lista: 
        st.sidebar.write(":green[Rickshaw Man] - odwrócenie trendu")
        na_odwrócenie += 1
    if 'Rising/Falling Three Methods' in lista: 
        st.sidebar.write(":green[Rising/Falling Three Methods]")  
    # if 'Separating Lines' in lista: 
    #     st.sidebar.write(":green[Separating Lines] ")  
        
    if 'Shooting Star' in lista: 
        st.sidebar.write(":green[Shooting Star] - odwrócenie trendu na spadkowy")  
        na_odwrócenie += 1
        na_minus += 1
    if 'Short Line' in lista: 
        st.sidebar.write(":green[Short Line] - kontynuacja trendu wzrostowego")
        kontynuacja += 1
        
         
    if 'Spinning Top' in lista: 
        st.sidebar.write(":green[Spinning Top] - zmiana trendu")  
        na_odwrócenie += 1

    if 'Stalled Pattern' in lista: 
        st.sidebar.write(":green[Stalled Pattern] - zmiana trendu na spadkowy")  
        na_minus += 1
        na_odwrócenie += 1
    if 'Stick Sandwich' in lista: 
        st.sidebar.write(":green[Stick Sandwich] - krótkoterminowa zmiana trendu")  
        na_odwrócenie += 1
        
    if 'Takuri' in lista: 
        st.sidebar.write(":green[Takuri] - odwrócenie trendu spadkowego i kontynuacja wzrostowego")   
        na_odwrócenie += 1
        na_plus += 1
    if 'Tasuki Gap' in lista: 
        st.sidebar.write(":green[Tasuki Gap] - kontynuacja trendu wzrostowego")  
        na_minus += 1
        na_odwrócenie += 1
    if 'Thrusting' in lista: 
        st.sidebar.write(":green[Thrusting] - kontynuacja lub odwrócenie")  
        na_minus += 1
        na_odwrócenie += 1
    if 'Tristar' in lista: 
        st.sidebar.write(":green[Tristar] - 3 doji pod rząd")  
        na_odwrócenie += 1



    # if 'Unique 3 River' in lista: 
    #     st.sidebar.write(":green[Unique 3 River]")  
        
    if 'Upside Gap Two Crows' in lista: 
        st.sidebar.write(":green[Upside Gap Two Crows] - odwrócenie trendu, ale tylko w dół")  
        na_odwrócenie += 1
        na_minus += 1
    if 'Upside/Downside Gap Three Methods' in lista: 
        st.sidebar.write(":green[Upside/Downside Gap Three Methods] - kontynuacja obecnego trendu")  
        kontynuacja += 1
    return świeczki






# Funkcja CDLMATHOLD jest częścią biblioteki TA-lib i służy do identyfikowania formacji świec japońskich. 
# Parametr penetration określa poziom penetracji ciała świecy poprzedzającej przez ciało świecy aktualnej formacji. 
# Innymi słowy, penetration definiuje minimalną część, o jaką ciało świecy aktualnej formacji musi się różnić od ciała świecy 
# poprzedzającej, aby została uznana za ważną. Domyślnie penetration jest ustawione na 0, co oznacza brak penetracji. 
# Zwiększenie tego parametru może pomóc w uwzględnieniu większej liczby formacji jako ważnych.

