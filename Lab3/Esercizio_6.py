# # TRACCIA DELL'ESERCIZIO
# Considerando i valori numerici dei voti spiegati nell’Esercizio 2, scrivete un
# programma che traduca un numero compreso tra 0 e 4 nel voto letterale più vicino.
# Ad esempio, il numero 2.8 (che potrebbe essere la media di più voti) deve essere
# tradotto come B–. Risolvete i casi di parità in favore del voto migliore: ad esempio,
# 2.85 deve essere tradotto come B.

import sys

# Dichiariamo le costanti per la conversione
A = 4.0
A_MINUS = 3.7
B_PLUS = 3.3
B = 3.0
B_MINUS = 2.7
C_PLUS = 2.3
C = 2.0
C_MINUS = 1.7
D_PLUS = 1.3
D = 1.0
D_MINUS = 0.7

# @param grade rappresenterà il voto da convertire
grade = float(input('Inserire un voto numerico che vada da (0.0 a 4.0): '))

# Controllo rudimentale sulla correttezza dei dati
if grade < 0 or grade > 4:
    sys.exit("Errore nell'inserimento dei dati.")

# Effettuo le operazioni per trovare il voto letterario corrispettivo
if A >= grade >= A_MINUS + 0.15:
    print('Il voto è: A')
elif A_MINUS >= grade >= B_PLUS:
    print('Il voto è: A-')
elif B_PLUS >= grade >= B:
    print('Il voto è: B+')
elif B >= grade >= B_MINUS + 0.15:
    print('Il voto è: B')
elif B_MINUS >= grade >= C_PLUS:
    print('Il voto è: B-')
elif C_PLUS >= grade >= C:
    print('Il voto è: C+')
elif C >= grade >= C_MINUS + 0.15:
    print('Il voto è: C')
elif C_MINUS >= grade >= D_PLUS:
    print('Il voto è: C-')
elif D_PLUS >= grade >= D:
    print('Il voto è: D+')
elif D >= grade >= D_MINUS + 0.15:
    print('Il voto è: D')
elif grade >= D_MINUS:
    print('Il voto è: D-')
else:
    print('Il voto è: F')
