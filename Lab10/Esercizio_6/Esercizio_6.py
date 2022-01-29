# # TRACCIA DELL'ESERCIZIO
# Scrivere un programma che visualizzi l’elenco degli esami superati da uno studente,
# con i relativi voti. È disponibile un file, classes.txt, che contiene i nomi di tutti gli
# insegnamenti erogati nell’istituto scolastico (un college statunitense), il cui contenuto
# sarà simile a questo:
# CSC1
# CSC2
# CSC46
# CSC151
# MTH121
# …
# Poi, per ogni insegnamento, è disponibile un file (il cui nome è pari al codice
# dell’insegnamento seguito da .txt) che elenca gli studenti che hanno superato il
# relativo esame e contiene i numeri identificativi degli studenti (ID) e i voti, come
# questo, che potrebbe essere il file CSC2.txt:
# 11234 A–
# 12547 B
# 16753 B+
# 21886 C
# …
# Scrivere un programma che chieda all’utente l’identificativo (ID) di uno studente e
# visualizzi l’elenco degli esami che tale studente ha superato, con i relativi voti
# ottenuti, come in questo esempio:
# Student ID 16753
# CSC2 B+
# MTH121 C+
# CHN1 A
# PHY50 A–

import sys


student = input('Inserire la matricola di cui si vogliono conoscere i voti degli esami superati: ')

classes = "classes.txt"

try:
    with open(classes, 'r') as file:
        subjects = file.readlines()
except IOError:
    sys.exit('Il file sulle materie è stato cancellato')

try:
    for subject in subjects:
        with open(subject.strip() + '.txt', 'r') as file:
            for line in file:
                if line.split(' ')[0] == student:
                    print("L'alunno %s nella materia %s ha preso %s" % (student, subject.strip(), line.split(' ')[1]))
except IOError:
    sys.exit('Il file %s non esiste' % subject + '.txt')
