# # TRACCIA DELL'ESERCIZIO
# Scrivete la funzione:
# def countWords(string)
# che restituisca il numero di parole presenti nella stringa string. Le parole sono
# sequenze di caratteri separate da spazi (si ipotizzi che tra due parole consecutive vi
# sia esattamente uno spazio). Ad esempio, countWords("Mary had a little
# lamb") restituisce 5.

# @function count_words conta le parole presenti in una frase
# @param sentence è la frase di cui vengono contate le parole
# @return counter è il numero di parole presenti nella frase
def count_words(sentence):
    counter = 0
    prev_item = ' '

    for item in sentence:
        if prev_item == ' ' and item != ' ':
            counter += 1

        prev_item = item

    return counter


# @function __main__ la funzione che si occupa del lancio del programma
def __main__():
    sentence = input('Inserire una frase per conoscere il numero di parole presenti al suo interno: ')
    print('\nIl numero di parole è:', count_words(sentence))


if __name__ == "__main__":
    __main__()
