# # TRACCIA DELL'ESERCIZIO
# Il gioco di Nim. Si tratta di un gioco molto noto, con un certo numero di varianti:
# quella qui descritta ha una strategia vincente davvero interessante. Due giocatori
# prelevano alternativamente biglie da un mucchietto. Ad ogni mossa, un giocatore
# sceglie quante biglie prendere: almeno una e al massimo metà delle biglie
# disponibili. Poi è il turno dell’altro giocatore. Il giocatore che prende l’ultima biglia
# perde la partita.
# Scrivete un programma che consenta all’utente di giocare contro il computer.
# Generate un numero intero compreso tra 10 e 100 e usatelo come dimensione iniziale
# del mucchietto di biglie. Generate un numero intero, 0 o 1, e utilizzatelo per decidere
# se sarà l’utente o il computer a giocare per primo. Generate un numero intero, 0 o 1,
# e usatelo per decidere se il computer giocherà in modo intelligente o stupido:
# giocando in modo stupido, ad ogni sua mossa il computer semplicemente preleva dal
# mucchietto un numero di biglie casuale (ma valido, cioè compreso tra 1 e n/2, se nel
# mucchietto sono rimaste n biglie); in modalità intelligente, invece, preleva un
# numero di biglie tale che il numero di quelle che rimangono nel mucchio sia una
# potenza di due diminuita di un’unità, cioè 3, 7, 15, 31 o 63. Quest’ultima è sempre
# una mossa valida, tranne quando la dimensione del mucchio è proprio uguale a una
# potenza di due diminuita di un’unità: in tal caso il computer fa una mossa scelta a
# caso (ovviamente tra quelle valide). Come potrete verificare sperimentalmente, il
# computer non può essere battuto quando gioca in modalità intelligente e fa la prima
# mossa, a meno che la dimensione iniziale del mucchio non sia 15, 31 o 63.
# Analogamente, un giocatore umano che faccia la prima mossa e conosca la strategia
# qui descritta è in grado di battere il calcolatore.

from random import randint
from math import log

# @param difficulty la difficoltà a cui giocheremo generata randomicamente( 0 -> facile, 1 -> difficile)
difficulty = randint(0, 1)

# @param balls il numero di biglie, anch'esse generate casualmente
balls = randint(10, 100)

if difficulty == 0:
    print('Stai giocando a FACILE.\n')
    print('Le biglie inziali sono:%d \n' % balls)

    # @param firs_to_move deciderà chi inizierà a giocare (0 -> per il computer, 1 -> per l'utente)
    first_to_move = randint(0, 1)

    # @param run terrà vivo il programma fino alla conclusione della partita
    run = True

    move = first_to_move

    if first_to_move == 0:
        print('Inizia il computer.')
    else:
        print("Inizia l'utente.")

    while run:
        # Giocata del computer
        if move == 0:
            if balls == 1:
                balls_taken = 1
            else:
                balls_taken = randint(1, balls//2)

            balls -= balls_taken

            if balls == 0 and balls_taken == 1:
                print('Il computer ha perso! HAI VINTO!')
                run = False
            else:
                print('Il computer ha preso %s biglie. Ne rimangono %s.\n' % (balls_taken, balls))

            move = 1
        # Giocate dell'utente
        else:
            balls_taken = (balls//2) + 1

            while balls_taken > (balls//2):
                balls_taken = int(input('Prendi un mucchio di biglie (Ricorda, puoi prendere da 1 alla metà): '))
                if balls == 1:
                    break

            balls -= balls_taken
            if balls == 0 and balls_taken == 1:
                print('HAI PERSO! Il computer ha vinto!')
                run = False
            else:
                print('Hai preso %s biglie. Ne rimangono %s.\n' % (balls_taken, balls))
            move = 0

else:
    print('Stai giocando a DIFFICILE\n')
    print('Le biglie inziali sono:', balls)

    first_to_move = randint(0, 1)
    run = True

    move = first_to_move

    if first_to_move == 0:
        print('Inizia il computer.')
    else:
        print("Inizia l'utente.")

    while run:
        # Giocata del computer
        if move == 0:
            if balls == 1:
                balls_taken = 1
            elif balls == 3 or balls == 7 or balls == 15 or balls == 31 or balls == 63:
                balls_taken = randint(1, balls // 2)
            else:
                balls_taken = 2 ** (int(log(balls, 2)) - 1)

            balls -= balls_taken

            if balls == 0 and balls_taken == 1:
                print('Il computer ha perso! HAI VINTO!')
                run = False
            else:
                print('Il computer ha preso %s biglie. Ne rimangono %s.\n' % (balls_taken, balls))

            move = 1
        # Giocate dell'utente
        else:
            balls_taken = (balls // 2) + 1

            while balls_taken > (balls // 2):
                balls_taken = int(input('Prendi un mucchio di biglie (Ricorda, puoi prendere da 1 alla metà): '))
                if balls == 1:
                    break

            balls -= balls_taken
            if balls == 0 and balls_taken == 1:
                print('HAI PERSO! Il computer ha vinto!')
                run = False
            else:
                print('Hai preso %s biglie. Ne rimangono %s.\n' % (balls_taken, balls))
            move = 0
