# # TRACCIA DELL'ESERCIZIO
# Realizzate il crivello di Eratostene: una funzione che calcola i numeri primi, nota
# anche nell’Antica Grecia. Scegliete un numero intero, 𝑛: questa funzione calcolerà
# tutti i numeri primi fino a 𝑛. Per prima cosa, create un insieme ed inseritevi tutti i
# numeri interi da 2 a 𝑛, poi eliminate dall’insieme tutti i multipli di 2, tranne 2 (cioè 4,
# 6, 8, 10, 12, …), quindi eliminate tutti i multipli di 3, tranne 3 (cioè 6, 9, 12, 15, …) e
# proseguite così, cancellando ogni volta i multipli del valore minimo presente
# nell’insieme, fino al numero √𝑛. I numeri rimasti nell’insieme sono quelli richiesti.

from math import sqrt, floor


n = int(input("Inserisci un intero positivo: "))
primes = set(range(2, n + 1))

for i in range(2, floor(sqrt(n)) + 1):
    for j in range(i ** 2, n + 1, i):
        primes.discard(j)

print("I numeri primi fino a", n, "sono:")
for p in sorted(primes):
    print(" ", p)
