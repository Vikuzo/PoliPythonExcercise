# # TRACCIA DELL'ESERCIZIO
# Leggere una sequenza di numeri interi conclusa da una riga vuota. Individuare i due
# massimi locali (numeri maggiori sia del valore precedente che di quello successivo)
# più vicini fra loro come posizione e stampare la loro posizione.

# @param lis la lista che conterrà i valori immessi dall'utente
lis = list()

# @param inp l'input dell'utente
inp = ' '

while inp != '':
    inp = input('Inserire un numero intero oppure invio se si vuole terminare la sequenza: ')

    if inp != '':
        lis.append(int(inp))

print('\n\n')

# @param maxis_index è la lista dove salveremo gli indici dei massimi locali
maxis_index = list()

for i in range(1, len(lis) - 1, 1):
    if lis[i - 1] < lis[i] > lis[i + 1]:
        maxis_index.append(i)


if len(maxis_index) < 1:
    print('NON CI SONO MASSIMI LOCALI!')
elif len(maxis_index) == 1:
    print("C'è solo un massimo locale.")
else:
    print(maxis_index)
    record = abs(maxis_index[0] - maxis_index[1])
    for i in range(len(maxis_index)):
        for j in range(len(maxis_index)):
            if record > abs(maxis_index[i] - maxis_index[j]) and i != j:
                record = abs(maxis_index[i] - maxis_index[j])

    print('La distanza minima tra due massimi locali è:', record)
