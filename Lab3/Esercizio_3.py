# # TRACCIA DELL'ESERCIZIO
# Scrivete un programma che legga una stringa e visualizzi i messaggi appropriati,
# dopo aver verificato se:
# a. contiene soltanto lettere
# b. contiene soltanto lettere maiuscole
# c. contiene soltanto lettere minuscole
# d. contiene soltanto cifre
# e. contiene soltanto lettere e cifre
# f. inizia con una lettera maiuscola
# g. termina con un punto

# @param sentence sarà la variabile in cui allocheremo la stringa inserita dall'utente
sentence = input('Inserire una stringa a piacere: ')

# Sviluppo punto a)
if sentence.isalpha():
    print('La stringa è composta da sole lettere.')

# Sviluppo punto b)
if sentence.isupper():
    print('La stringa è scritta tutta in maiuscolo.')

# Sviluppo punto c)
if sentence.islower():
    print('La stringa è scritta tutta in minuscolo.')

# Svilupppo punto d)
if sentence.isdigit():
    print('La stringa è composta soltanto da cifre.')

# Sviluppo e), abbiamo bisogno della seconda condizioni poiché la funzione "isalnum()" ci darà vero se la stringa e
# composta solo da lettere o numeri o solo da una accoppiata dei due
if sentence.isalnum() and not (sentence.isdigit() or sentence.isalpha()):
    print('La stringa è composta soltanto da cifre e lettere.')

# Sviluppo f)
if sentence[0].isupper():
    print('La stringa ha la prima lettera maiuscola.')

# Sviluppo g)
if sentence.endswith('.'):
    print('La stringa termina con un punto.')
