# # TRACCIA DELL'ESERCIZIO
# Scrivete un programma che legga il file di testo input.txt. Ogni riga letta va scritta nel
# file output.txt preceduta dal numero di riga, inserita come commento tra caratteri /* e
# */. Se, ad esempio, il file input.txt fosse il seguente:
# Enola Gay
# è il bombardiere che il 6 agosto 1945,
# sganciò su Hiroshima la prima bomba atomica
# soprannominata Little Boy.
# Il file output.txt generato sarebbe:
# /*1*/Enola Gay
# /*2*/è il bombardiere che il 6 agosto 1945,
# /*3*/sganciò su Hiroshima la prima bomba atomica
# /*4*/soprannominata Little Boy.

with open('input.txt', 'r') as file:
    lines = file.readlines()

for i in range(len(lines)):
    lines[i] = '\*' + str(i + 1) + '*\\ ' + lines[i]

with open('output.txt', 'w') as file:
    file.writelines(lines)

