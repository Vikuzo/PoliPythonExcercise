# # TRACCIA DELL'ESERCIZIO
# Cifratura monoalfabetica casuale. Il cifrario di Cesare, che trasla ogni lettera di una
# quantità fissa, è troppo facile da violare. Ecco un’idea migliore: come chiave, invece
# di usare un numero, usiamo una parola, che immaginiamo essere FEATHER. Per
# prima cosa eliminiamo le lettere duplicate dalla parola chiave, ottenendo FEATHR,
# poi aggiungiamo in fondo ad essa le altre lettere dell’alfabeto, in ordine inverso:
# F E A T H R Z Y X W V U S Q P O N M L K J I G D C B
# Ora cifriamo le lettere, seguendo questo schema:
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
# F E A T H R Z Y X W V U S Q P O N M L K J I G D C B
# Tutti gli altri caratteri (spazi, cifre, punteggiatura, …) devono rimanere invariati.
# Scrivete un programma che cifri o decifri un file di testo (il cui nome è inserito
# dall’utente) usando una parola chiave, inserita dall’utente e memorizzata in una
# variabile, e scrivendo le informazioni decifrate in un file di testo scelto dall’utente.

ALPHABET = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
ALPHABET2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def write_file(filename, word):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except IOError:
        print('Errore. Il file non esiste')

    new_lines = []
    for line in lines:
        lin = ''
        for ch in line.upper():
            if ch in ALPHABET:
                lin += word[ALPHABET2.index(ch)]
            else:
                lin += ch

        new_lines.append(lin)

    new_file = input('Inserire il nome del file su cui si vogliono screivere i dati cifrati: ')

    with open(new_file, 'w') as file:
        file.writelines(new_lines)


def read_file(filename, word):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except IOError:
        print('Errore. Il file non esiste')

    new_lines = []
    for line in lines:
        lin = ''
        for ch in line.upper():
            if ch in ALPHABET:
                lin += ALPHABET2[word.index(ch)]
            else:
                lin += ch

        new_lines.append(lin)

    new_file = input('Inserire il nome del file su cui si vogliono screivere i dati cifrati: ')

    with open(new_file, 'w') as file:
        file.writelines(new_lines)


def __main__():
    choice = input('Digitare W se si vuole cifrare un file in un altro, R se si vuole deifrare un file in un altro '
                   'nulla altrimenti ')
    word = input('Inserire la parola da utilizzare per la cifrazione: ').upper()

    cipher = ''

    for ch in word:
        if ch not in cipher:
            cipher += ch

    for ch in ALPHABET:
        if ch not in cipher:
            cipher += ch

    if choice == 'W':
        filename = input('Inserire il nome del file che si vuole cifrare: ')
        write_file(filename, cipher)

    if choice == 'R':
        filename = input('Inserire il nome del file che si vuole decifrare: ')
        read_file(filename, cipher)


if __name__ == "__main__":
    __main__()
