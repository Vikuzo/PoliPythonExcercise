# # TRACCIA DELL'ESERCIZIO
# A) Scrivete un programma che conti le occorrenze di ciascuna parola presente in un
# file di testo, il cui nome è inserito da tastiera. Si assuma che il file contenga solo
# caratteri alfabetici o di spaziatura. B) Successivamente, migliorate il programma in
# modo che visualizzi le 100 parole più comuni (in caso di parità alla posizione 100, è
# indifferente quali parole si stampino).

import sys


filename = input('Inserisci il nome del file di cui vuoi calcolare il numero di ogni parola presente: ')
dictionary = dict()

try:
    with open(filename, 'r') as file:
        for line in file:
            for word in line.strip().split(' '):
                if word in dictionary.keys():
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
except IOError:
    sys.exit('Il file inserito non esiste')

sorted_dictionary = sorted(dictionary.values())
if len(sorted_dictionary) < 100:
    count_100 = 1
else:
    count_100 = sorted_dictionary[len(sorted_dictionary) - 100]

count = 0
for word in sorted(dictionary):
    if dictionary[word] > count_100:
        print('%s %d' % (word, dictionary[word]))
        count += 1

for word in sorted(dictionary):
    if dictionary[word] == count_100 and count < 100:
        print('%s %d' % (word, dictionary[word]))
        count += 1
