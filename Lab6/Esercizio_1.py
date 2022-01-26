# # TRACCIA DELL'ESERCIZIO
# Scrivete la funzione:
# def countVowels(string)
# che restituisca il numero di vocali presenti nella stringa string. Le vocali sono le
# lettere a, e, i, o e u, oltre alle rispettive versioni maiuscole.

# @function count_vowels si occupa di contare le vocali presenti in una parola
# @param word è la parola di cui conterà le vocali
# @return counter è il numero di vocali presenti nella parola
def count_vowels(word):
    vowels = ['a,', 'e', 'i', 'o', 'u']
    counter = 0

    word = word.lower()

    for item in word:
        if item in vowels:
            counter += 1

    return counter


# @function __main__ la funzione che si occupa del lancio del programma
def __main__():
    word = input('Inserisci una parola per conoscere il numero di vocali presenti al suo interno: ')
    print('\nIl numero di vocali è:', count_vowels(word))


if __name__ == "__main__":
    __main__()
