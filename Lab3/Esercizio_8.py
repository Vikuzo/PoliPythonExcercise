# # TRACCIA DELL'ESERCIZIO
# Scrivete un programma per la conversione di unità di misura che chieda all’utente da
# quale unità (scegliendo tra: ml, l, g, kg, mm, cm, m, km) e verso quale unità
# (scegliendo tra: fl. oz, gal, oz, lb, in, ft, mi) vuole effettuare una
# conversione, rifiutando conversioni incompatibili (come, ad esempio, km → gal).
# Chiedete, poi, il valore da convertire e, infine, visualizzate il risultato:
# Convert from? l
# Convert to? gal
# Value? 2.5
# 2.5 l = 0.6605019815059445 gal

import sys

# @param from_unit conterrà l'unita di misura di partenza
from_unit = input("Inserire l'unita di cui si vuole convertire il valore (ml, l, g, kg, mm, cm, m, km): ")

# @param to_unit conterrà l'unità di misura di arrivo
to_unit = input("Inserire l'unita in cui si vuole convertire il valore (fl. oz, gal, oz, lb, in, ft, mi): ")

# Sviluppo delle unità di volume
if from_unit == "ml" and to_unit == "fl. oz":
    factor = 0.03381406
elif from_unit == "l" and to_unit == "fl. oz":
    factor = 33.81405650
elif from_unit == "ml" and to_unit == "gal":
    factor = 0.00026417
elif from_unit == "l" and to_unit == "gal":
    factor = 0.26417218
# Sviluppo delle unità di massa
elif from_unit == "g" and to_unit == "oz":
    factor = 0.03527399
elif from_unit == "kg" and to_unit == "oz":
    factor = 35.27399072
elif from_unit == "g" and to_unit == "lb":
    factor = 0.00220462
elif from_unit == "kg" and to_unit == "lb":
    factor = 2.20462442
# Sviluppo delle unità di distanza
elif from_unit == "mm" and to_unit == "in":
    factor = 0.03937008
elif from_unit == "cm" and to_unit == "in":
    factor = 0.39370079
elif from_unit == "m" and to_unit == "in":
    factor = 39.37007874
elif from_unit == "km" and to_unit == "in":
    factor = 39370.07874016
elif from_unit == "mm" and to_unit == "ft":
    factor = 0.00328084
elif from_unit == "cm" and to_unit == "ft":
    factor = 0.03280840
elif from_unit == "m" and to_unit == "ft":
    factor = 3.28083990
elif from_unit == "km" and to_unit == "ft":
    factor = 3280.83989501
elif from_unit == "mm" and to_unit == "mi":
    factor = 0.00000062
elif from_unit == "cm" and to_unit == "mi":
    factor = 0.00000621
elif from_unit == "m" and to_unit == "mi":
    factor = 0.00062137
elif from_unit == "km" and to_unit == "mi":
    factor = 0.62137119
# Unità incompatibili
else:
    sys.exit("Le unità non sono compatibili fra loro")

# @param value valore da convertire
value = float(input('Inserire il valore che si vuole convertire: '))

print(value, from_unit, "=", value * factor, to_unit)
