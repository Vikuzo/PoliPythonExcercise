# # TRACCIA DELL'ESERCIZIO
# Leggere una sequenza di numeri interi conclusa da una riga vuota. Stampare la
# posizione dei massimi locali (numeri maggiori sia del valore precedente che di quello
# successivo) se ce ne sono, altrimenti stampare il messaggio “Non ci sono massimi locali”

# @param lis la lista che conterrà i valori immessi dall'utente
lis = list()

# @param inp l'input dell'utente
inp = ' '

while inp != '':
    inp = input('Inserire un numero intero oppure invio se si vuole terminare la sequenza: ')

    if inp != '':
        lis.append(int(inp))

print('\n\n')

# @param maxis la lista che conterrà tutti i massimi locali
maxis = list()

for i in range(1, len(lis) - 1, 1):
    if lis[i - 1] < lis[i] > lis[i + 1]:
        maxis.append(lis[i])

if len(maxis) < 1:
    print('NON CI SONO MASSIMI LOCALI!')
else:
    print('I massimi locali sono:', end=' ')
    for item in maxis:
        print(item, end=' ')
