# # TRACCIA DELL'ESERCIZIO
# Usando la formula seguente (in cui a, b, r, ed m sono numeri interi):
# rnew = (a ⋅ rold + b) % m
# e, poi, ripetendo il calcolo assegnando rnew a rold, si ottiene un semplice generatore
# casuale.
# Scrivete un programma che chieda all’utente di fornire un valore iniziale per rold
# (valore che viene chiamato “seme”, seed), poi visualizzi i primi 100 numeri interi
# generati dalla formula, usando a = 32310901, b = 1729 e m = 2^24.

# Dichiarazione delle costanti
A = 32310901
B = 1729
M = 2 ** 24

# @param seed sarà il parametro che ci permetterà di generare numeri casuali
seed = int(input('Inserire un numero intero a proprio piacere: '))

# @param c ci farà da contatore
c = 0

print('I cento numeri generati casualmente sono: ')

while c < 100:
    r_new = ((A * seed) + B) % M
    seed = r_new
    print(r_new)

    c += 1
