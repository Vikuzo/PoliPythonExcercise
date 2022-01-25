# # TRACCIA DELL'ESERCIZIO
# Scrivete un programma che traduca un voto in lettere nel corrispondente voto
# numerico. I voti in lettere sono A, B, C, D e F, eventualmente seguiti da un segno + o –.
# I loro valori numerici sono, nell’ordine, 4, 3, 2, 1 e 0. I voti F+ e F– non esistono.
# Un segno + aumenta il voto numerico di 0.3, mentre un segno – lo diminuisce della
# stessa quantità. Il voto A+ è comunque uguale a 4.0.
# Enter a letter grade: B–
# The numeric value is 2.7.

import sys

# @param ADD sarà il valore aggiuntivo al punteggio relativo ai + ed ai -
ADD = 0.3

# @param grade sarà il voto che inserirà l'utente
# il metodo upper() ci permette di assicurarci che le lettere inserite siano a stampatello
grade = input('Inserire un voto a lettere(esempio: A+, A o A-): ').upper()

# @param mark sarà il voto finale che stamperemo
mark = 0.0

# Controlliamo che l'utente non abbia inserito F+ o F- (che nella traccia abbiamo detto non esistere)
if len(grade) > 1:
    if grade[0] == 'F':
        sys.exit('I valori inseriti non sono accettabili')
    if grade[1] == '+':
        mark += 0.3
    else:
        mark -= 0.3

# Diamo ad ogni lettera il suo corrispettivo valore
if grade[0] == 'A':
    mark += 4.0
elif grade[0] == 'B':
    mark += 3.0
elif grade[0] == 'C':
    mark += 2.0
elif grade[0] == 'D':
    mark += 1.0
else:
    mark += 0.0

# controlliamo che il voto finale non abbia superato il massimo consentito
if mark > 4.0:
    mark = 4.0
elif mark < 0:
    mark = 0.0

print(grade, 'ha come corrispettivo numerico:', mark)
