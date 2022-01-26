# # TRACCIA DELL'ESERCIZIO
# Scrivete un programma che legga una parola e visualizzi:
# a. la parola al contrario. Se, ad esempio, l’utente fornisce la stringa “Ciao”, il
# programma deve visualizzare oaiC
# b. le lettere maiuscole partendo dal fondo. Se, ad esempio, l’utente fornisce la
# stringa “CiAo”, il programma deve visualizzare AC.

# @param word sarà la variabile che conterrà la parola da modificare
word = input('Inserire una parola: ')

# @param new_wordl la variabile che conterrà le modifiche che effettueremo alla parola inserita
new_word = ''

# # Sviluppo punto a)
for i in range(-1, -len(word)-1, -1):
    new_word += word[i]

print('La parola al contrario è: %s\n' % new_word)


# # Sviluppo punto b)
new_word = ''

for i in range(-1, -len(word)-1, -1):
    if word[i].isupper():
        new_word += word[i]

print('Le maiuscole al contrario della parola sono: %s' % new_word)
