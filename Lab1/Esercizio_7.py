# # TRACCIA DELL'ESERCIZIO
# Scrivete un programma che visualizzi il saldo di un conto bancario dopo il primo,
# secondo e terzo anno. Il conto ha un saldo iniziale di 1000 dollari e vi vengono
# accreditati interessi annuali al 5%.

# @param payment rappresenta il saldo iniziale che possediamo sul conto bancario
payment = 1000

# @param payoff rappresenta la percentuale che ci verrà accreditata annualmente
payoff = 5

# Per ottenere il saldo alla fine del primo anno aggiungiamo al saldo il risultato della proporzione
# (payment : 100 = x : payoff), e lo ripetiamo 3 volte.
# La funzione round(x, y) ci permette di limitare le cifre dopo la virgola dei nostri numeri decimali: x rappresenta
# il numero in virgola mobile da approssimare e y il numero di cifre decimali
payment = round((payment + (payment * payoff) / 100), 2)
print("Il saldo del vostro conto bancario dopo un anno:", payment)

# secondo anno
payment = round((payment + (payment * payoff) / 100), 2)
print("Il saldo del vostro conto bancario dopo due anni:", payment)

# terzo anno
payment = round((payment + (payment * payoff) / 100), 2)
print("Il saldo del vostro conto bancario dopo tre anni:", payment)
