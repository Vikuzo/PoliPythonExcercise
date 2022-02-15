# # TRACCIA DELL'ESERCIZIO
# Un array sparso è una sequenza di numeri, la maggior parte dei quali è zero. Un
# modo efficiente per memorizzare un array sparso è un dizionario, nel quale le chiavi
# sono le posizioni in cui sono presenti valori diversi da zero, e i valori sono i
# corrispondenti valori nella sequenza. Per esempio, la sequenza 0 0 0 0 0 4 0 0 0 2 9
# sarebbe rappresentata dal dizionario {5:4, 9:2, 10:9}. Scrivete una funzione,
# sparseArraySum, i cui argomenti sono due di tali dizionari, a e b, e che restituisca
# un array sparso che ne sia il vettore somma: il suo valore nella posizione i è la
# somma dei valori di a e b nella posizione i. I dizionari del programma chiamante non
# devono essere modificati.

def sparse_array_sum(a, b):
    keys1 = list(a.keys())
    keys2 = list(b.keys())
    keys = []
    array = []

    for item in keys1:
        keys.append(int(keys1[keys1.index(item)]))

    for item in keys2:
        keys.append(int(keys2[keys2.index(item)]))

    keys.sort()

    for i in range(keys[-1] + 1):
        array.append(0)

    for item in keys1:
        if item in keys2:
            array[int(item)] = a[item] + b[item]
        else:
            array[int(item)] = a[item]

    for item in keys2:
        if array[int(item)] == 0:
            array[int(item)] = b[item]

    print('Il vettore somma sparso è: ')
    [print(item, end=' ') for item in array]


def __main__():
    a = {5: 4, 9: 2, 10: 9}
    b = {6: 3, 8: 4, 9: 6, 10: 1}

    sparse_array_sum(a, b)


if __name__ == "__main__":
    __main__()
