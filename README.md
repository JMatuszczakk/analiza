# 1. short term
- dodać do data bool'a który będzie przechowywał decyzję o tym czy kupować czy nie
- dodać int który będzie sumą decyzji
- dodać skrypt który będzie dodawał decyzję i dodać do niego różne wagi
- liczenie średniej ważonej
- sprawdzanie czy średnia jest większa czy mniejsza od 1
# 2. mid term
- co 30 min sprawdzanie kilkunastu najpopularniejszych akcji 
- jeśli są git do kupienia, to powiadomienie do ntfy
- Ewentualnie podpiąć do tego llm
# 3. long term
- skrypt llm czytający newsy i analizuje je czy jest to dobry news dla danej akcji czy zły
- dodawnie wartości newsom
- dodać skale od -10 do 10 i bard będzie analizował jaką wartość przyznać newsom




# 1 Analiza wskaźnikó
- Rsi - mierzy prędkość i zmiany cen, pomagając inwestorom zidentyfikować, czy aktywo jest przekupione (nadkupione) lub przesprzedane (nadzwyczaj sprzedawane).
- Przekupienie rynku - Stan, w którym cena danego aktywa jest uznawana za wysoką w stosunku do swojej przewidywanej wartości
- Przesprzedarz - Stan, w którym cena danego aktywa jest uznawana za niską w stosunku do swojej przewidywanej wartości.

- ATR - TR pomaga określić zmienność rynku, 

- NATR - jest to znormalizowana wersja ATR, co pozwala porównać zmienność między różnymi aktywami.

- AVGPRICE - oblicza średnią wartość cenową na podstawie  Dostarcza informacje na temat przeciętnej ceny danego okresu.

- ADX -  opis: ADX określa siłę trendu, a nie jego kierunek. Wartości powyżej 25 wskazują na silny trend.
Zastosowanie: Pomaga inwestorom ocenić, czy na rynku występuje trend oraz jego siłę.

- MACD -Opis: MACD to wskaźnik momentum, który porównuje dwie średnie kroczące dla cen.
Zastosowanie: Pomaga inwestorom zidentyfikować potencjalne punkty zwrotne na rynku.

- SMA - Opis: SMA to średnia krocząca prostą, która wygładza cenę, pomagając identyfikować ogólny trend.
Zastosowanie: Pomaga inwestorom zobaczyć ogólny kierunek ruchu cenowego.









RSI   52-88 czeba kupować 
        +1 do sumy bo jest mało ważne
        bool = True

