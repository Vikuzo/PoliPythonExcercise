# # TRACCIA DELL'ESERCIZIO
# Scrivete un programma che converta un numero romano, come MCMLXXVIII, nella
# sua rappresentazione decimale. Suggerimento: per prima cosa, scrivete una funzione
# che restituisce il valore numerico di ciascuna singola lettera, poi usate l’algoritmo
# seguente:
# totale = 0
# Finché la stringa s contenente il numero romano non è vuota
# Se s ha lunghezza 1 oppure valore(primo carattere di s) è almeno uguale a
# valore(secondo carattere di s)
# Aggiungi valore(primo carattere di s) a totale.
# Elimina il primo carattere di s.
# Altrimenti
# Aggiungi a totale la differenza:
# valore(secondo carattere di s) – valore(primo carattere di s)
# Elimina il primo e il secondo carattere di s.

# @function decimal_value la funzione che ci restituisce il singolo valore di una lettera romana
# @param letter la lettere di cui si vuole conoscere il valore
# @return value il valore decimale della lettera
def decimal_value(letter):
    value = 0

    if letter == 'I':
        value = 1
    if letter == 'V':
        value = 5
    if letter == 'X':
        value = 10
    if letter == 'L':
        value = 50
    if letter == 'C':
        value = 100
    if letter == 'D':
        value = 500
    if letter == 'M':
        value = 1000

    return value


# @function __main__ la funzione che si occupa del lancio del programma
def __main__():
    number = input('Inserisci il numero romano che si vuole convertire: ')
    memorial = number

    total = 0

    while number != '':
        if len(number) == 1:
            total += decimal_value(number)
            number = ''
        # Controllo se entrambi hanno lo stesso valore e quindi non indicano valori diversi da quello assegnato loro
        # naturalmente
        elif decimal_value(number[-1]) == decimal_value(number[-2]):
            total += decimal_value(number[-1])
            number = number[0:len(number) - 1]
        # Se il primo è più grande del secondo il valore reale è la loro differenza
        elif decimal_value(number[-1]) > decimal_value(number[-2]):
            total += (decimal_value(number[-1]) - decimal_value(number[-2]))
            number = number[0:len(number) - 2]
        # ALtrimenti il valore reale è la loro somma
        else:
            total += (decimal_value(number[-2]) + decimal_value(number[-1]))
            number = number[0:len(number) - 2]

        print(total)

    print('Il numero romano %s in decimale è: %s' % (memorial, total))


if __name__ == '__main__':
    __main__()
