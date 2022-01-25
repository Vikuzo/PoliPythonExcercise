# # TRACCIA DELL'ESERCIZIO
# Scrivere un programma che memorizzi due numeri interi in due costanti definite nel
# codice, e poi ne visualizzi:
# • La somma
# • La differenza
# • Il prodotto
# • Il valore medio
# • La distanza (cioè il valore assoluto della differenza)
# • Il valore massimo (cioè il maggiore tra i due)
# • Il valore minimo (cioè il minore tra i due)
# Suggerimento: utilizzare le funzioni max e min definite in Python. Esse accettano
# una sequenza di valori separati da virgola in input e restituiscono rispettivamente il
# valore massimo e minimo della sequenza. (Es: max(10, 5) restituisce 10).

# IMPORTANTE, è prassi scrivere i nomi delle variabili costanti in maiuscolo!
# @param a il primo dei nostri due numeri interi
A = 3

# @param b il secondo dei nostri due numeri interi
B = 8

# Ora effettuiamo tutte le operazioni che ci sono state richieste
print("La somma dei due valori è:", (A + B))
print("La differenza dei due valori è:", (A - B))
print("Il prodotto dei due valori è:", (A * B))
print("La media dei due valori è:", (A + B) / 2)
print("La distanza dei due valori è:", abs(A - B))
print("Il massimo fra i due valori è:", max(A, B))
print("Il minimo fra i due valori è:", min(A, B))
