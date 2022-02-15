# # TRACCIA DELL'ESERCIZIO
# Scrivete un programma “censore”, che legga un file (bad_words.txt) contenente
# una lista di “parolacce” (come “sesso”, “droga”, “C++” e così via), una per riga,
# inserendole in un insieme. Leggere poi un altro file di testo: il programma deve
# riscrivere il secondo file letto, generandone un terzo nel quale tutte le lettere di
# ciascuna parolaccia (comprese quelle nelle sotto-parole contenenti parolacce) siano
# state sostituite da un numero di asterischi pari alla sua lunghezza.

bad_words = set()

with open('bad_words.txt', 'r') as file:
    for line in file:
        bad_words.add(line.strip())

filename = input('Inserire il file che si vuole censurare: ')

new_file = []
with open(filename, 'r') as file:
    for line in file:
        new_file.append('')
        c = 0
        for word in line.split(' '):
            if word in bad_words:
                for i in range(len(word)):
                    new_file[c] += '*'
            else:
                new_file[c] += word

            new_file[c] += ' '


with open(filename, 'w') as file:
    file.writelines(new_file)
