# # TRACCIA DELL'ESERCIZIO
# Scrivete programmi che leggano una riga di dati in ingresso sotto forma di stringa e
# visualizzino quanto segue:
# a. le sole lettere maiuscole della stringa;
# b. a partire dalla seconda lettera della stringa, una lettera viene visualizzata e
# l’altra no, alternativamente;
# c. la stringa con tutte le vocali sostituita da un carattere di sottolineatura
# (underscore);
# d. il numero di cifre presenti nella stringa;
# e. le posizioni di tutte le vocali presenti nella stringa.

# # Sviluppo punto a)
# @param sentence sarà la nostra stringa
sentence = input('A) Inserire una stringa: ')

# @param new_sentence conterrà le nostre nuove frasi
new_sentence = ''

for item in sentence:
    if item.isalpha() and item.isupper():
        new_sentence += item

print('La frase scritta con le sole lettere maiuscole di cui è composta:', new_sentence)


# # Sviluppo punto b)
sentence = input('\n\nB) Inserire una stringa: ')

print('La frase stampata, da dopo la seconda lettera che la compone, a lette alterne:',
      sentence[0] + sentence[1:len(sentence):2])


# # Sviluppo punto c)
sentence = input('\n\nC) Inserire una stringa: ')
new_sentence = ''

for item in sentence:
    if item.upper() in 'AEIOU':
        new_sentence += '_'
    else:
        new_sentence += item

print('La frase sostituendo le vocali con simboli di sottolineatura è:', new_sentence)


# # Sviluppo punto d)
sentence = input('\n\nD) Inserire una stringa: ')

# @param c sarà il nostro contatore
c = 0

for item in sentence:
    if item.isdigit():
        c += 1

print("Le cifre presenti all'interno della frase sono:", c)


# # Sviluppo punto e)
sentence = input('\n\nE) Inserire una stringa: ')
new_sentence = ''

for i in range(len(sentence)):
    if sentence[i].upper() in 'AEIOU':
        new_sentence += str(i)

print('Le vocali si trovano alle posizioni: ', end='')
for item in new_sentence:
    print(item, end=' ')
