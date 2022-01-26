# # TRACCIA DELL'ESERCIZIO
# Scrivete un programma che inizializzi una lista con dieci numeri interi casuali tra 1 e
# 100 e, poi, visualizzi quattro righe di informazioni, contenenti:
# a. Tutti gli elementi di indice pari.
# b. Tutti gli elementi di valore pari.
# c. Tutti gli elementi in ordine inverso.
# d. Il primo e l’ultimo elemento.

from random import randint

# @param lis sarà la lista contente i nostri 10 numeri
lis = list()

for i in range(10):
    lis.append(randint(1, 100))


# # Sviluppo del punto a)
print('I valori di indice pari sono: ')

for i in range(len(lis)):
    if (i + 1) % 2 == 0:
        print(lis[i], end=' ')
print('\n\n')


# # Sviluppo del punto b)
print('Gli elementi di valore pari sono: ')

for item in lis:
    if item % 2 == 0:
        print(item, end=' ')
print('\n\n')


# # Sviluppo del punto c)
print('Gli elementi in ordine inverso sono: ')

for i in range(len(lis) - 1, -1, -1):
    print(lis[i], end=' ')
print('\n\n')


# # Sviluppo del punto d)
print('Il primo degli elementi:', lis[0])
print("L'ultimo degli elementi:", lis[-1])
