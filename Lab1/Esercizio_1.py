# # TRACCIA DELL'ESERCIZIO
# Volete calcolare la percentuale di utilizzo della vostra automobile per uso personale
# e, separatamente, per recarvi al lavoro. Conoscete la distanza tra casa vostra e il
# vostro luogo di lavoro e, dato un periodo di tempo, avete registrato il valore riportato
# dal contachilometri all’inizio ed alla fine del periodo; inoltre è noto il numero di
# giorni in cui vi siete recati al lavoro in tale periodo. Scrivete un algoritmo per
# risolvere questo problema e calcolare la percentuale citata.

# @param distance rappresenta la distanza fra il vostro luogo di lavoro e casa vostra
distance = 150

# @param starting_km rappresenta il valore iniziale del contachilometri
starting_km = 100000

# @param ending_km rappresenta il valore finale del contachilometri
ending_km = 120000

# @param working_days rappresenta i giorni in cui vi siete recati a lavoro
working_days = 7

# @param working_km rappresenta il numero di chilometri percorsi per andare e tornare dal lavoro; attenzione! Non farti
# ingannare dal fatto che il problema ci dica che siamo a conoscenza dell'intero periodo di tempo perché non è
# necessario alla risoluzione dello stesso
working_km = (distance * 2) * 7

# Per ottenere la soluzione della nostra proporzione ((ending_km -  starting_km) : 100 = working_km : x) non è
# necessario infilare tutto all'interno di una variabile possiamo direttamente far eseguire tutto nella print come
# riportato di seguito. L'utilizzo di nuove variabili va intuito in base alla situazione
print('La percentuale di utilizzo del veicolo per motivi lavorativi è:', (working_km * 100)/(ending_km - starting_km),
      '%')
print('La percentuale di utilizzo del veicolo per svago invece è:', 100 - (working_km * 100)/(ending_km - starting_km),
      '%')
