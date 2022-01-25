# # TRACCIA DELL'ESERCIZIO
# Scrivete un programma che legga tre numeri e visualizzi il messaggio “increasing” se
# sono in ordine crescente, “decreasing” se sono in ordine decrescente e “neither” se
# non sono né in ordine crescente né in ordine decrescente. In questo esercizio
# crescente significa strettamente crescente, cioè ciascun valore deve essere maggiore
# del precedente (analogo significato ha il termine decrescente): la sequenza 3 4 4,
# quindi, non va considerata crescente.

# @param a primo numero che verrà inserito dall'utente
a = int(input('Inserire il primo numero: '))

# @param b secondo numero che verrà inserito dall'utente
b = int(input('Inserire il secondo numero: '))

# @param c terzo numero che verrà inserito dall'utente
c = int(input('inserire il terzo numero: '))

print('\n\n')

# Controlliamo se crescono
if a < b:
    if b < c:
        print('Risultato: INCREASING')
    else:
        print('Risultato: NEITHER')
# Controlliamo se decrescono
elif c < b:
    print('Risultato: DECREASING')
else:
    print('Risultato: NEITHER')
