# # TRACCIA DELL'ESERCIZIO
# Scrivete un programma che legga tutte le righe di un file di testo (input.txt), ne
# inverta l’ordine e le scriva in un altro file (output.txt). Ad esempio, se il file input.txt
# contiene queste righe:
# Mary had a little lamb
# Its fleece was white as snow
# And everywhere that Mary went
# The lamb was sure to go.
# allora il file output.txt conterrà:
# The lamb was sure to go.
# And everywhere that Mary went
# Its fleece was white as snow
# Mary had a little lamb

with open('input.txt', 'r') as file:
    lines = file.readlines()

with open('output.txt', 'w') as file:
    lines[-1] = lines[-1] + '\n'
    lines[0] = lines[0][0:len(lines[0]) - 1]

    for i in range(len(lines) - 1, -1, -1):
        file.write(lines[i])
