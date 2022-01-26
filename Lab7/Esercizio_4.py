# # TRACCIA DELL'ESERCIZIO
# Scrivete un programma che generi una sequenza di 20 valori casuali compresi tra 0 e
# 99, poi visualizzi la sequenza generata, la ordini e la visualizzi di nuovo, ordinata.

from random import randint

# @param lis la lista che conterrà i valori da ordinare
lis = list()

for i in range(20):
    lis.append(randint(0, 99))

print('La lista generata è:')

for item in lis:
    print(item, end=' ')

# sort() è il metodo che ordina le liste in python
lis.sort()

print('\nLa lista ordinata è:')

for item in lis:
    print(item, end=' ')
