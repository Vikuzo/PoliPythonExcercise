# # TRACCIA DELL'ESERCIZIO
# Scrivete un’applicazione che gestisca la prevendita di un numero limitato di biglietti
# del cinema. Ogni acquirente può comprare al massimo 4 biglietti e non ne possono
# essere venduti più di 100. Il programma deve chiedere all’utente quanti biglietti
# intende acquistare, per poi visualizzare il numero di biglietti rimasti. L’operazione va
# ripetuta fino all’esaurimento dei biglietti, visualizzando al termine il numero di
# acquirenti.

# @param tickets ammontare dei biglietti disponibile
tickets = 10

# @param c ci aiuterà a tenere traccia degli acquirenti
c = 0

while tickets > 0:
    print('I biglietti ancora disponibili sono: %d' % tickets)
    # @param t i biglietti comprati da un utente in un certo momento
    t = 5
    while t < 0 or t > 4 or (tickets - t) < 0:
        t = int(input('Inserire il numero di biglietti che si vuole acquistare: '))

    tickets -= t
    c += 1
    print('\n')

print('i biglietti sono stati venduti tutti. Gli acquirenti totali sono stati:', c)
