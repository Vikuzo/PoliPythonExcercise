# # TRACCIA DELL'ESERCIZIO
# Scrivere un programma che memorizzi una stringa in una variabile e, a partire da
# quella variabile, visualizzi i primi tre caratteri della stringa, seguiti da tre punti,
# ancora seguiti dagli ultimi tre caratteri.
# Ad esempio, se la stringa viene inizializzata al valore “Mississippi”, il programma
# deve visualizzare “Mis...ppi”.

# @param sentence conterrà la stringa su cui andremo a fare le nostre operazioni
sentence = 'Buongiorno'

# A sinistra dell'operatore : ho indicato l'indice di partenza mentre a destra l'indice di conclusione, effettuando uno
# "slicing" poi effettuando la concatenazione fra stringhe grazie all'operatore di somma (+), infatti nelle stringhe
# questo operatore ti permette di unire due stringhe:
# E.S. 'Buon' + 'Giorno' = 'BuonGiorno'
print('Soluzione più intuitiva: ')
print(sentence[0:3] + '...' + sentence[len(sentence) - 3:len(sentence)])

# è possibile anche utilizzare gli indici negativi in python dove -1 indica l'elemento più a destra della stringa.
print('\nSoluzione con indici negativi: ')
print(sentence[0:3] + '...' + sentence[-3:])

# Cosa succede della stringa è più corta di 6 caratteri? E se è più breve di 3 caratteri?

# Se la stringa è lunga meno di 6 caratteri ma almeno 3 il programma continuerà a funzionare correttamente, mentre
# quando è più corto di 3 nella prima soluzione ci troveremo ad avere uno slicing completamente casuale, per renderlo
# più chiaro immaginiamo di avere solo 2 caratteri "sentence[len(sentence) - 3:len(sentence)]" sarà uguale a -1 e
# quindi staremo dicendo al computer di andare dalla posizione finale alla posizione finale nel secondo caso invece
# verranno stampati i caratteri disponibili, di seguito un esempio

sentence = 'Bu'
print('\n\n\nCosa succede con una parola troppo corta:')
print(sentence[0:3] + '...' + sentence[len(sentence) - 3:len(sentence)])
print(sentence[0:3] + '...' + sentence[-3:-1] + sentence[-1])
