


###################co mówisz? wywaliło mi diskorda
#nie wiem, nie mam pojęcia 
#co



# def Świeczuszki(świeczuszki, data):
#     świeczki = pd.DataFrame(index=data.index)
#     świeczki['Doji'] = ta.CDLDOJI(data['Open'], data['High'], data['Low'], data['Close'])
#     świeczki['Engulfing'] = ta.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])
#     świeczki['Evening Doji Star'] = ta.CDLEVENINGDOJISTAR(data['Open'], data['High'], data['Low'], data['Close'], penetration=0)
#     świeczki['Evening Star'] = ta.CDLEVENINGSTAR(data['Open'], data['High'], data['Low'], data['Close'], penetration=0)
#     świeczki['Gaps Side-by-Side White'] = ta.CDLGAPSIDESIDEWHITE(data['Open'], data['High'], data['Low'], data['Close'])
#     świeczki['Gravestone Doji'] = ta.CDLGRAVESTONEDOJI(data['Open'], data['High'], data['Low'], data['Close'])
#     świeczki['Hammer'] = ta.CDLHAMMER(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Hanging Man'] = ta.CDLHANGINGMAN(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Harami'] = ta.CDLHARAMI(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Harami Cross'] = ta.CDLHARAMICROSS(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['High-Wave'] = ta.CDLHIGHWAVE(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Hikkake'] = ta.CDLHIKKAKE(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Homing Pigeon'] = ta.CDLHOMINGPIGEON(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Identical Three Crows'] = ta.CDLIDENTICAL3CROWS(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['In-Neck'] = ta.CDLINNECK(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Inverted Hammer'] = ta.CDLINVERTEDHAMMER(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Kicking'] = ta.CDLKICKING(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Kicking by Length'] = ta.CDLKICKINGBYLENGTH(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Ladder Bottom'] = ta.CDLLADDERBOTTOM(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Long Legged Doji'] = ta.CDLLONGLEGGEDDOJI(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Long Line'] = ta.CDLLONGLINE(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Marubozu'] = ta.CDLMARUBOZU(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Matching Low'] = ta.CDLMATCHINGLOW(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Mat Hold'] = ta.CDLMATHOLD(data['Open'], data['High'], data['Low'], data['Close'], penetration=0)  # Added this line
#     świeczki['Morning Doji Star'] = ta.CDLMORNINGDOJISTAR(data['Open'], data['High'], data['Low'], data['Close'], penetration=0)  # Added this line
#     świeczki['Morning Star'] = ta.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'], penetration=0)  # Added this line
#     świeczki['On-Neck'] = ta.CDLONNECK(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Piercing'] = ta.CDLPIERCING(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Rickshaw Man'] = ta.CDLRICKSHAWMAN(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Rising/Falling Three Methods'] = ta.CDLRISEFALL3METHODS(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Separating Lines'] = ta.CDLSEPARATINGLINES(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Shooting Star'] = ta.CDLSHOOTINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Short Line'] = ta.CDLSHORTLINE(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Spinning Top'] = ta.CDLSPINNINGTOP(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Stalled Pattern'] = ta.CDLSTALLEDPATTERN(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Stick Sandwich'] = ta.CDLSTICKSANDWICH(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Takuri'] = ta.CDLTAKURI(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Tasuki Gap'] = ta.CDLTASUKIGAP(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Thrusting'] = ta.CDLTHRUSTING(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Tristar'] = ta.CDLTRISTAR(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Unique 3 River'] = ta.CDLUNIQUE3RIVER(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Upside Gap Two Crows'] = ta.CDLUPSIDEGAP2CROWS(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line
#     świeczki['Upside/Downside Gap Three Methods'] = ta.CDLXSIDEGAP3METHODS(data['Open'], data['High'], data['Low'], data['Close'])  # Added this line

#     lista = []

#     st.table(świeczki)
#     st.sidebar.subheader("Świeczki które są: ")
#     for i in świeczki.columns:
#         for y in świeczki[i][-4:]:
#             if y == 100:
#                 lista.append(i)

#     if 'Doji' in lista:
#         st.sidebar.write(":green[Doji]")
#     if 'Engulfing' in lista:
#         st.sidebar.write(":green[Engulfing]")
#     if 'Evening Doji Star' in lista:
#         st.sidebar.write(":green[Evening Doji Star]")
#     if 'Evening Star' in lista:
#         st.sidebar.write(":green[Evening Star]")
#     if 'Gaps Side-by-Side White' in lista:
#         st.sidebar.write(":green[Gaps Side-by-Side White]")
#     if 'Gravestone Doji' in lista:
#         st.sidebar.write(":green[Gravestone Doji]")
#     if 'Hammer' in lista:  # Added this condition
#         st.sidebar.write(":green[Hammer]")  # Added this line
#     if 'Hanging Man' in lista:  # Added this condition
#         st.sidebar.write(":green[Hanging Man]")  # Added this line
#     if 'Harami' in lista:  # Added this condition
#         st.sidebar.write(":green[Harami]")  # Added this line
#     if 'Harami Cross' in lista:  # Added this condition
#         st.sidebar.write(":green[Harami Cross]")  # Added this line
#     if 'High-Wave' in lista:  # Added this condition
#         st.sidebar.write(":green[High-Wave]")  # Added this line
#     if 'Hikkake' in lista:  # Added this condition
#         st.sidebar.write(":green[Hikkake]")  # Added this line
#     if 'Homing Pigeon' in lista:  # Added this condition
#         st.sidebar.write(":green[Homing Pigeon]")  # Added this line
#     if 'Identical Three Crows' in lista:  # Added this condition
#         st.sidebar.write(":green[Identical Three Crows]")  # Added this line
#     if 'In-Neck' in lista:  # Added this condition
#         st.sidebar.write(":green[In-Neck]")  # Added this line
#     if 'Inverted Hammer' in lista:  # Added this condition
#         st.sidebar.write(":green[Inverted Hammer]")  # Added this line
#     if 'Kicking' in lista:  # Added this condition
#         st.sidebar.write(":green[Kicking]")  # Added this line  
#     if 'Kicking by Length' in lista:  # Added this condition
#         st.sidebar.write(":green[Kicking by Length]")  # Added this line
#     if 'Ladder Bottom' in lista:  # Added this condition
#         st.sidebar.write(":green[Ladder Bottom]")  # Added this line
#     if 'Long Legged Doji' in lista:  # Added this condition
#         st.sidebar.write(":green[Long Legged Doji]")  # Added this line
#     if 'Long Line' in lista:  # Added this condition
#         st.sidebar.write(":green[Long Line]")  # Added this line
#     if 'Marubozu' in lista:  # Added this condition
#         st.sidebar.write(":green[Marubozu]")  # Added this line
#     if 'Matching Low' in lista:  # Added this condition
#         st.sidebar.write(":green[Matching Low]")  # Added this line
#     if 'Mat Hold' in lista:  # Added this condition
#         st.sidebar.write(":green[Mat Hold]")  # Added this line
#     if 'Morning Doji Star' in lista:  # Added this condition
#         st.sidebar.write(":green[Morning Doji Star]")  # Added this line
#     if 'Morning Star' in lista:  # Added this condition
#         st.sidebar.write(":green[Morning Star]")  # Added this line
#     if 'On-Neck' in lista:  # Added this condition
#         st.sidebar.write(":green[On-Neck]")  # Added this line
#     if 'Piercing' in lista:  # Added this condition
#         st.sidebar.write(":green[Piercing]")  # Added this line
#     if 'Rickshaw Man' in lista:  # Added this condition
#         st.sidebar.write(":green[Rickshaw Man]")  # Added this line
#     if 'Rising/Falling Three Methods' in lista:  # Added this condition
#         st.sidebar.write(":green[Rising/Falling Three Methods]")  # Added this line
#     if 'Separating Lines' in lista:  # Added this condition
#         st.sidebar.write(":green[Separating Lines]")  # Added this line
#     if 'Shooting Star' in lista:  # Added this condition
#         st.sidebar.write(":green[Shooting Star]")  # Added this line
#     if 'Short Line' in lista:  # Added this condition
#         st.sidebar.write(":green[Short Line]")  # Added this line
#     if 'Spinning Top' in lista:  # Added this condition
#         st.sidebar.write(":green[Spinning Top]")  # Added this line
#     if 'Stalled Pattern' in lista:  # Added this condition
#         st.sidebar.write(":green[Stalled Pattern]")  # Added this line
#     if 'Stick Sandwich' in lista:  # Added this condition
#         st.sidebar.write(":green[Stick Sandwich]")  # Added this line
#     if 'Takuri' in lista:  # Added this condition
#         st.sidebar.write(":green[Takuri]")  # Added this line
#     if 'Tasuki Gap' in lista:  # Added this condition
#         st.sidebar.write(":green[Tasuki Gap]")  # Added this line
#     if 'Thrusting' in lista:  # Added this condition
#         st.sidebar.write(":green[Thrusting]")  # Added this line
#     if 'Tristar' in lista:  # Added this condition
#         st.sidebar.write(":green[Tristar]")  # Added this line
#     if 'Unique 3 River' in lista:  # Added this condition
#         st.sidebar.write(":green[Unique 3 River]")  # Added this line
#     if 'Upside Gap Two Crows' in lista:  # Added this condition
#         st.sidebar.write(":green[Upside Gap Two Crows]")  # Added this line
#     if 'Upside/Downside Gap Three Methods' in lista:  # Added this condition
#         st.sidebar.write(":green[Upside/Downside Gap Three Methods]")  # Added this line


