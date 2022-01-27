# # TRACCIA DELL'ESERCIZIO
# Lo schema dei posti a teatro è una tabella con i prezzi dei biglietti per ciascun posto,
# come questa:
# 10 10 10 10 10 10 10 10 10 10
# 10 10 10 10 10 10 10 10 10 10
# 10 10 10 10 10 10 10 10 10 10
# 10 10 20 20 20 20 20 20 10 10
# 10 10 20 20 20 20 20 20 10 10
# 10 10 20 20 20 20 20 20 10 10
# 20 20 30 30 40 40 30 30 20 20
# 20 30 30 40 50 50 40 30 30 20
# 30 40 50 50 50 50 50 50 40 30
# Scrivete un programma che gestisca un menù che chieda all’utente di scegliere un
# posto, un prezzo o l’uscita dal programma. Contrassegnate con un prezzo uguale a 0 i
# posti già venduti. Quando l’utente specifica un posto, accertatevi che sia libero e che
# le coordinate siano all’interno della tabella. Quando, invece, specifica un prezzo,
# assegnategli un posto qualsiasi tra quelli disponibili a quel prezzo

# @function display_seats mostra la piantina dei posti
# @param matrix contiene la matrice con la disposizione dei posti
def display_seats(matrix):
    print('La disposizione ed i prezzi dei posti a sedere: ')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()
    print()


# @function seat_based_on_price assegna il primo posto libero che trova a coloro che chiedono un posto in base al prezzo
# @param price il prezzo a cui desiderano acquistare il biglietto
# @param matrix la matrice che indica la disposizione dei posti
def seat_based_on_price(price, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == price:
                matrix[i][j] = 0
                return i, j

    return -1, -1


# @function __main__ la funzione che si occupa del lancio del programma
def __main__():
    prices = [10, 20, 30, 40, 50]
    seats = [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
             [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
             [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
             [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
             [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
             [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
             [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
             [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
             [30, 40, 50, 50, 50, 50, 50, 50, 40, 30]]

    choice = 'P'
    while choice != 'Q':
        choice = input('Inserire S se si voule scegliere il posto a sedere, P se si vuole scegliere solo il prezzo '
                       'o Q per terminare: ').upper()

        # Sviluppo se l'utente sceglie in base al prezzo
        if choice == 'P':
            display_seats(seats)
            price = 0
            while price not in prices:
                price = int(input('Inserire il prezzo al quale si vuole acquistare il biglietto: '))

            seat = seat_based_on_price(price, seats)

            if seat[0] == -1:
                print('Mi dispiace non sono più disponibili biglietti a quel prezzo.')
            else:
                print('Il posto a sedere da lei prenotato è alle coordinate:', seat[0] + 1, seat[1] + 1)

        # Sviluppo se l'utente sceglie in base al posto a sedere
        if choice == 'S':
            display_seats(seats)
            row = -1
            column = -1
            while (row < 0 or row > len(seats[0])) and (column < 0 or column > len(seats)):
                row = int(input('Inserire la riga alla quale si vuole sedere: ')) - 1
                column = int(input('inserire la colonna alla quale si vuole sedere: ')) - 1

            if seats[row][column] != 0:
                print('Il posto è disponibile. Le verrà assegnato')
                seats[row][column] = 0
            else:
                print("Errore nell'inserimento, il posto è già occupato, riprovare")


if __name__ == "__main__":
    __main__()
