def count_words(sentence):
    counter = 0
    prev_item = ' '

    for item in sentence:
        if prev_item == ' ' and item != ' ':
            counter += 1

        prev_item = item

    return counter


def __main__():
    sentence = input('Inserire una frase per conoscere il numero di parole presenti al suo interno: ')
    print('\nIl numero di parole è:', count_words(sentence))


if __name__ == "__main__":
    __main__()
