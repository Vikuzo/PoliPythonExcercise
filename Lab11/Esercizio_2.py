# # TRACCIA DELL'ESERCIZIO
# Scrivete un programma che chieda all’utente di fornire due stringhe, per poi
# visualizzare (evitando ripetizioni di caratteri nella stampa):
# • i caratteri che compaiono in entrambe le stringhe;
# • i caratteri che compaiono in una stringa ma non nell’altra;
# • le lettere che non compaiono in nessuna delle due stringhe.
# Suggerimento: trasformare una stringa in un insieme di caratteri.

string1 = input('Inserire la prima stringa: ')
string2 = input('Inserire la seconda stringa: ')

alphabet = {}

for ch in 'qwertyuiopasdfghjklzxcvbnm':
    alphabet[ch] = 0

for item in string1.lower():
    if item in alphabet.keys():
        if alphabet[item] == 0:
            alphabet[item] += 1

for item in string2.lower():
    if item in alphabet.keys():
        if alphabet[item] == 0 or alphabet[item] == 1:
            alphabet[item] += 1

print('\n\nI caratteri che compaiono in entrambe le stringhe sono: ')
for item in alphabet.keys():
    if alphabet[item] == 2:
        print(item, end=' ')

print("\n\nI caratteri che compaiono in una stringa ma non nell'altra: ")
for item in alphabet.keys():
    if alphabet[item] == 1:
        print(item, end=' ')

print("\n\nI caratteri che non compaiono in nessuna delle due stringhe: ")
for item in alphabet.keys():
    if alphabet[item] == 0:
        print(item, end=' ')
