def count_vowels(word):
    vowels = ['a,', 'e', 'i', 'o', 'u']
    counter = 0

    word = word.lower()

    for item in word:
        if item in vowels:
            counter += 1

    return counter


def __main__():
    word = input('Inserisci una parola per conoscere il numero di vocali presenti al suo interno: ')
    print('\nIl numero di vocali è:', count_vowels(word))


if __name__ == "__main__":
    __main__()
