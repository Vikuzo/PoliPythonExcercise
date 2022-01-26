# # TRACCIA DELL'ESERCIZIO
# Scrivete programmi che leggano una sequenza di numeri interi (la sequenza termina
# quando viene inserita la stringa vuota) che visualizzino quanto segue:
# a. il valore minimo e il valore massimo tra quelli acquisiti
# b. il numero di valori pari e il numero di valori dispari tra quelli acquisiti;
# c. le somme parziali di tutti i numeri acquisiti, calcolate e visualizzate dopo ogni
# nuova acquisizione (se, ad esempio, i valori in ingresso sono 1 7 2 9, il
# programma visualizzerà 1 8 10 19);
# d. i valori adiacenti duplicati (se, ad esempio, i valori acquisiti sono 1 3 3 4 5 5 6
# 6 6 3, il programma visualizzerà 3 5 6).

# # Sviluppo punto a)
# @param number la variabile che conterrà i numeri inseriti dall'utente
number = input('A) Inserire un numero intero oppure premere invio per terminare la sequenza: ')
print()

# @param minimum conterrà il valore minimo inserito
minimum = number

# @param maximum conterrà il valore massimo inserito
maximum = number

while number != '':
    minimum = min(int(minimum), int(number))
    maximum = max(int(maximum), int(number))

    print('Il valore minimo acquisito finora è:', minimum)
    print('Il valore massimo acquisito finora è:', maximum)

    print()
    number = input('A) Inserire un numero intero oppure premere invio per terminare la sequenza: ')
    print()


# # Sviluppo punto b)
number = input('B) Inserire un numero intero oppure premere invio per terminare la sequenza: ')
print()

# @param even conterà i numeri pari
even = 0

# @param odd conterà i numeri dispari
odd = 0

while number != '':
    if int(number) % 2 != 0:
        odd += 1
    else:
        even += 1

    print('I numeri pari inseriti sono:', even)
    print('I numeri dispari inseriti sono:', odd)

    print()
    number = input('B) Inserire un numero intero oppure premere invio per terminare la sequenza: ')
    print()


# # Sviluppo del punto c)
number = input('C) Inserire un numero intero oppure premere invio per terminare la sequenza: ')
print()

# @param som conterrà le somme parziali
som = 0

while number != '':
    som += int(number)

    print('La somma dei numeri acquisiti finora è:', som)

    print()
    number = input('C) Inserire un numero intero oppure premere invio per terminare la sequenza: ')
    print()


# # Sviluppo del punto d)
number = input('D) Inserire un numero intero oppure premere invio per terminare la sequenza: ')
print()

# @param check servirà per poter uscire del ciclo
check = number

# @param redundant sarà la variabile che conterrà i numeri che compaiono più volte uno di seguito all'altro
redundant = ''

# @param servirà a tenere l'indice
c = 0

# @param new servirà per controllare se un valore compare più di una volta nella sequenza dei numeri ridondanti
new = True

while check != '':
    if len(number) > 1:
        if number[c] == number[c+1]:
            for item in redundant:
                if item == number[c]:
                    new = False
            if new:
                redundant += number[c]

        c += 1

    new = True

    print()
    check = input('D) Inserire un numero intero oppure premere invio per terminare la sequenza: ')
    number += check
    print()

for item in redundant:
    print(item, end=' ')

print('sono elementi ricorrenti')
