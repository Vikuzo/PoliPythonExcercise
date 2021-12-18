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
# Disegnate il diagramma di flusso per l’algoritmo. Verificate se l’algoritmo si
# comporta correttamente con una serie di date di prova

# @param season rappresenta la stagione del mese
season = ''
# @param month rappresenta il mese del quale vogliamo individuare la stagione
month = 7
# @param day rappresenta il giorno del mese del quale vogliamo individuare la stagione
day = 22

# Questo blocco di if viene utilizzato per ricercare la stagione alla quale appartiene il mese; attenzione! Questo
# programma può essere risolto in modi più semplici e immediati con strumenti di cui non siamo ancora a disposizione
if month == 1 or month == 2 or month == 3:
    season = 'Winter'
elif month == 4 or month == 5 or month == 6:
    season = 'Spring'

elif month == 7 or month == 8 or month == 9:
    season = 'Summer'

elif month == 10 or month == 11 or month == 12:
    season = 'Fall'

# In questo blocco invece andremo ad occuparci dei casi in cui la stagione è diversa in funzione dei giorni del mese.
# Esempio: 21 Marzo
if month % 3 == 0 and day >= 21:
    if season == 'Winter':
        season = 'Spring'
    elif season == 'Spring':
        season = 'Summer'
    elif season == 'Summer':
        season = 'Fall'
    else:
        season = 'Winter'

# La funzione str(x) permette di convertire un numero di una stringa, qui viene utilizzate per effettuare una
# concatenazione in modo tale da creare una scritta più leggibile
print('Il', str(month) + '°', 'mese di giorno', day, 'cade nella stagione:', season)
