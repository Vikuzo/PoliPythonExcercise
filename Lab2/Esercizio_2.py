# # TRACCIA DELL'ESERCIZIO
# Scrivere un programma che memorizzi in una costante un numero intero positivo di
# cinque cifre (quindi compreso tra 10000 e 99999), e visualizzi le singole cifre di cui
# è composto.
# Ad esempio, avendo il numero 16384, il programma deve visualizzare, su righe
# separate: 1 6 3 8 4.

# @param number l'intero che andremo a visualizzare
number = 16384

# Lo convertiamo in stringa per comodità
number = str(number)

# possiamo riferici ad ogni singolo elemento della stringa con un indice che parte da 0 ed arriva all'ultima posizione
# meno uno

print(number[0])
print(number[1])
print(number[2])
print(number[3])
print(number[4])

# Utilizzando un ciclo

print('\n\n\nUtilizzando i cicli:')

for item in number:
    print(item)

# Una soluzione alternativa è effettuare divisioni che portano a ridurre il numero intero composto da 5 valori a 5
# numeri interi come nel metodo mostrato
n = int(number)
n1 = n % 10
n = n // 10
n2 = n % 10
n = n // 10
n3 = n % 10
n = n // 10
n4 = n % 10
n = n // 10
n5 = n % 10

print('\n\n\nMantendeno la variabile come intero:')

# In questo caso gli indici coincidono con il nostro modo di dare importanza ai valori che compongono un numero,
# e quindi vanno stampati al contrario

print(n5)
print(n4)
print(n3)
print(n2)
print(n1)
