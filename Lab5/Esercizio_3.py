# # TRACCIA DELL'ESERCIZIO
# In una simulazione predatore-preda, si calcolano le popolazioni di predatori
# (predators, abbreviato pred) e prede (preys) usando le equazioni seguenti:
# preyn+1 = preyn × (1 + A – B × predn)
# predn+1 = predn × (1 – C + D × preyn)
# In queste equazioni, le costanti hanno i seguenti significati:
# • A è il ritmo con cui le prede, in assenza di predatori, incrementano il proprio
# numero (tenendo conto delle nuove nascite e delle morti naturali)
# • B è il tasso di predazione, ossia il numero di prede uccise da ciascun
# predatore
# • C è il ritmo con cui i predatori, in assenza di cibo, riducono il proprio numero
# (tenendo conto delle morti di per assenza di ciboe delle nascite)
# • D è il tasso con cui i predatori aumentano in presenza di cibo, ossia il numero
# di predatori sopravvissuti per avere mangiato una preda.
# Scrivete un programma che chieda questi valori all’utente, oltre alle dimensioni
# iniziali delle popolazioni di prede e predatori, e al numero di intervalli di tempo che
# coinvolgono la simulazione. La simulazione procede applicando ripetutamente le due
# formule, con l’accortezza che nessuna popolazione può diventare negativa.
# Successivamente, il programma deve visualizzare la dimensione delle due
# popolazioni per il numero di intervalli di tempo assegnato. Eseguite, come esempio,
# una simulazione con A = 0.1, B = C = 0.01 e D = 0.00002, con popolazione iniziale
# di 1000 prede e 20 predatori.

import sys

# @param pred rappresenta il numero inziale di predatori
pred = int(input('Inserire il numero inziale di predatori: '))

# @param preys reppresenta il numero iniziale di prede
preys = int(input('Inserire il numero iniziale di prede: '))

# Dichiarazione delle costanti delle equazioni descritte
A = float(input('Inserire il valore da associare al parametro A della equazione: '))
B = float(input('Inserire il valore da associare al parametro B della equazione: '))
C = float(input('Inserire il valore da associare al parametro C della equazione: '))
D = float(input('Inserire il valore da associare al parametro D della equazione: '))

# @param period il periodo di tempo sul quale si vogliono effettuare i calcoli
period = int(input("Inserire il periodo per il quale si vuole calcolare l'equazione: "))

for i in range(1, period+1):
    new_preys = preys * (1 + A - B * pred)
    new_pred = pred * (1 - C + D * preys)

    if round(new_pred) != 0 and round(new_preys) != 0:
        pred = new_pred
        preys = new_preys

        print('Nel periodo %d ci sono %d predatori e %d prede' % (i, round(pred), round(preys)))
    else:
        sys.exit('Una delle due popolazioni ha raggiunto lo 0')
