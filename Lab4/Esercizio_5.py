# # TRACCIA DELL'ESERCIZIO
# Numeri primi. Scrivete un programma che chieda all’utente un numero intero e, poi,
# visualizzi tutti i numeri primi minori o uguali a tale numero. Se, ad esempio, l’utente
# fornisce il numero 20, il programma deve visualizzare:

# @param number sarà il numero di cui andremo a controllare tutti i numeri primi minori
number = int(input('Inserire un numero intero: '))

# Ricerca dei numeri primi
print('I numeri primi fino a %d sono: ' % number)
for i in range(1, number + 1, 1):
    # @param prime servirà per controllare se un numero è primo oppure no
    prime = True

    # @param c ci farà da divisore dei numeri fino a number
    c = 1

    while c < i and prime:
        if i % c == 0 and c != 1:
            prime = False
        c += 1

    if prime and i != 1:
        print(i)
