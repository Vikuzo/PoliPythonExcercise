# # TRACCIA DELL'ESERCIZIO
# Quando utilizzate uno sportello bancario automatico (ATM, automatic teller
# machine) con la vostra carta, dovete usare un numero identificativo personale (PIN,
# personal identification number) per poter accedere al vostro conto. Se un utente
# sbaglia tre volte l’inserimento del PIN, la macchina trattiene la carta e la blocca.
# Nell’ipotesi che il PIN dell’utente sia “1234”, scrivete un programma che chieda
# all’utente di digitare il PIN, consentendo al massimo tre tentativi e agendo in questo
# modo:
# • se l’utente inserisce il numero corretto, visualizzate il messaggio “Your PIN
# is correct” e terminate il programma;
# • se l’utente inserisce un numero sbagliato, visualizzate il messaggio “Your PIN
# is incorrect” e, se avete chiesto il PIN meno di tre volte, chiedetelo di
# nuovo;
# • se l’utente inserisce un numero sbagliato per tre volte, visualizzate il messaggio
# “Your bank card is blocked” e terminate il programma.

import sys

# @param PIN sarà la password dell'utente
PIN = '1234'

# @param c farà da contatore delle volte che l'utente ha provato ad inserire il PIN
c = 0

# @param unchecked rappresenterà se il PIN è corretto o meno
unchecked = True

while c < 3 and unchecked:
    if PIN == input('Inserire il proprio PIN (Es. 1234): '):
        unchecked = False
        print('Your PIN is correct')
    else:
        c += 1
        print('Your PIN is incorrect.')

if c == 3:
    print('Your bank card is blocked')

sys.exit()
