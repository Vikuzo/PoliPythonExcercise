# # TRACCIA DELL'ESERCIZIO
# Scrivete una funzione che calcoli il saldo di un conto bancario accreditando gli
# interessi annualmente. La funzione riceve come parametri il numero di anni, il saldo
# iniziale e il tasso d’interesse annuo.

# @function banking_account calcola addistanza di un ammontare di anni il valore del proprio saldo
# @param years contiene gli anni dopo i quali si vuole sapere il proprio saldo bancario
# @param starting_amount indica il saldo iniziale presente sul proprio conto
# @param yearly_interests indica gli interessi annui
# @return total_amount il valore finale del saldo bancario
def banking_account(years, starting_amount, yearly_interests):
    counter = 0
    total_amount = starting_amount

    while counter < years:
        total_amount += ((total_amount * yearly_interests)/100)
        counter += 1

    return total_amount


# @function __main__ la funzione che si occupa del lancio del programma
def __main__():
    years = int(input('Inserire il numero di anni tra cui si vuole conoscere il proprio saldo: '))
    starting_amount = float(input('Inserire la liquidità iniziale: '))
    yearly_interests = float(input('Inserire la percentuale di interessi annui: '))

    print('Il valore del proprio saldo bancario sarà: %.2f' % banking_account(years, starting_amount, yearly_interests)
          + '$')


if __name__ == '__main__':
    __main__()
