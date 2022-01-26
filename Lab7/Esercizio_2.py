# # TRACCIA DELL'ESERCIZIO
# Scrivete un programma che acquisisca da tastiera una sequenza di numeri interi
# (terminata da una riga vuota), calcoli la somma alternata degli elementi di una lista.
# Ad esempio, se il programma legge i dati 1 4 9 16 9 7 4 9 11, deve calcolare e
# visualizzare 1 – 4 + 9 – 16 + 9 – 7 + 4 – 9 + 11 = –2.

# @param lis la lista che conterrà i valori da sommare
lis = list()

# @param number la variabile che conterrà i nuovi numeri inseriti dall'utente
number = 's'

# @param c il contatore ci permetterà di cambiare i segni ai numeri inseriti dall'utente
c = 0

while number != '':
    number = input('Inserisci un numero intero o premi invio per terminare la sequenza: ')

    if number != '':
        if c % 2 != 0:
            lis.append(int(number) * -1)
        else:
            lis.append(int(number))

    c += 1

# @som la variabile che conterrà il totale dei valori presenti nella lista
som = 0

for item in lis:
    if item > 0 and som != 0:
        print('+' + str(item), end='')
    else:
        print(item, end='')
    som += item

print('=', som)
