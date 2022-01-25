# # TRACCIA DELL'ESERCIZIO
# L’algoritmo seguente individua la stagione (Spring, Summer, Fall o Winter, cioè,
# rispettivamente, primavera, estate, autunno o inverno) a cui appartiene una data,
# fornita come mese e giorno.
# Se mese è 1, 2 o 3, stagione = “Winter”
# Altrimenti se mese è 4, 5 o 6, stagione = “Spring”
# Altrimenti se mese è 7, 8 o 9, stagione = “Summer”
# Altrimenti se mese è 10, 11 o 12, stagione = “Fall”
# Se mese è divisibile per 3 e giorno >= 21
# Se stagione è “Winter”, stagione = “Spring”
# Altrimenti se stagione è “Spring”, stagione = “Summer”
# Altrimenti se stagione è “Summer”, stagione = “Fall”
# Altrimenti stagione = “Winter”
# Analizzare l’algoritmo e cercare di comprendere se esso è corretto.
# Scrivete poi un programma che, implementando l’algoritmo, chieda all’utente un
# mese e un giorno e, poi, visualizzi la stagione determinata da questo algoritmo.

import sys

# @param month che prenderà il mese dell'anno
month = int(input('Inserire il mese (a numero): '))

# @param day che prenderà il giorno del mese
day = int(input('Inserire il giorno del mese: '))

# @param season variabile che conterrà il nome della stagione
season = 0

if month == 1 or month == 2 or month == 3:
    season = 'Winter'
elif month == 4 or month == 5 or month == 6:
    season = 'Spring'
elif month == 7 or month == 8 or month == 9:
    season = 'Summer'
elif month == 10 or month == 11 or month == 12:
    season = 'Fall'
elif season == 0:
    sys.exit('Valori inseriti non accettabili.')

# Controllo sui giorni
if day >= 21 and (month % 3) == 0:
    if season == 'Winter':
        season = 'Spring'
    elif season == 'Spring':
        season = 'Summer'
    elif season == 'Summer':
        season = 'Fall'
    else:
        season = 'Winter'

print('La stagione corrente è:', season)
