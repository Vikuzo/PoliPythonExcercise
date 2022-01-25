# # TRACCIA DELL'ESERCIZIO
# Lo pseudocodice seguente descrive come trasformare una stringa contenente un
# numero telefonico a dieci cifre (come “4155551212”) in una stringa più facilmente
# leggibile, formattata secondo lo stile statunitense, come “(415) 555–1212”.
# • Prendere la stringa costituita dai primi tre caratteri e circondarla con
# parentesi tonde (questo è il prefisso, detto “area code”).
# • Concatenare il prefisso con la stringa contenente i tre caratteri successivi, un
# trattino e la stringa costituita dagli ultimi quattro caratteri si ottiene il numero
# nel formato richiesto
# Tradurre questo pseudocodice in un programma Python che memorizzi un numero
# telefonico di 10 cifre in una stringa, per poi visualizzarlo nel formato appena
# descritto.

# @param CELL il numero telefonico che andremo a formattare
CELL = '4155551212'

print('(' + CELL[0:3] + ')' + ' ' + CELL[3:len(CELL) - 4] + '-' + CELL[len(CELL) - 4:])
