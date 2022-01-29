# # TRACCIA DELL'ESERCIZIO
# Il responsabile amministrativo di un albergo registra le vendite in un file di testo.
# Ogni riga contiene le seguenti 4 informazioni, separate da caratteri “punto e virgola”:
# il nome del cliente, il servizio venduto (ad esempio, cena, conferenza, alloggio, e
# così via), l’importo pagato e la data dell’evento. Scrivete un programma che legga un
# tale file di testo e visualizzi l’importo totale relativo a ciascun tipo di servizio,
# segnalando un errore se il file non esiste oppure se il suo formato non è corretto
# (verificando cioè che ci siano 4 campi per riga e che il prezzo sia float).

import sys


def __main__():
    file = input('Inserire il nome del file da leggere: ')

    try:
        with open(file, 'r') as f:
            lines = f.readlines()
    except IOError:
        sys.exit('Il file inserito non esiste.')

    category = []
    total = []

    for line in lines:
        lis = line.strip().split(';')
        if len(lis) != 4:
            sys.exit('Errore! Numero di campi nel file errato')

        try:
            amount = float(lis[2])
        except ValueError:
            sys.exit('Erroe! Un prezzo non è scritto in un formato adeguato')

        if lis[1] in category:
            total[category.index(lis[1])] += amount
        else:
            category.append(lis[1])
            total.append(amount)

    for item in category:
        print("Durante l'evento %s gli introiti sono stati pari: %s" % (item, total[category.index(item)]))


if __name__ == "__main__":
    __main__()
