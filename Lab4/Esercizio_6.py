# # TRACCIA DELL'ESERCIZIO
# Scrivete un programma che legga una parola e visualizzi tutte le sue sottostringhe,
# ordinate per lunghezza crescente. Se, ad esempio, l’utente fornisce la stringa “rum”,
# il programma deve visualizzare

# @param word conterrà la parola inserita dall'utente
word = input('Inserire una parola di cui si vogliono conoscere tutte le sottostringhe: ')

for length in range(1, len(word) + 1):
    for pos in range(0, len(word) - length + 1):
        print(word[pos:pos + length])
