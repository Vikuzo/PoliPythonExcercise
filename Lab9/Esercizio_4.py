# # TRACCIA DELL'ESERCIZIO
# Un supermercato vuole ricompensare il proprio miglior cliente del giorno,
# mostrandone il nome su uno schermo all’interno del negozio. A questo scopo,
# vengono memorizzati in una lista (customers) i nomi di tutti i clienti del giorno e, in
# un’altra lista (sales), il corrispondente importo della spesa effettuata.
# Scrivete la funzione nameOfBestCustomer(sales, customers) che restituisca il
# nome del cliente che ha speso la cifra più alta.
# Poi, scrivete un programma che chieda al cassiere di digitare tutti gli importi spesi e i
# nomi dei relativi clienti, aggiungendoli via via a due liste distinte, per poi invocare la
# funzione che avete progettato e visualizzare il risultato. Usate il prezzo 0 come
# sentinella.

# @function name_of_best_customer la funzione che ordinerà le nostre liste in modo da sapere chi è il miglior acquirente
# @param sales è la lista con gli importi pagati da ogni singolo cliente
# @param customers è la lista con nominativi dei clienti
def name_of_best_customer(sales, customers):
    for i in range(len(sales)):
        for j in range(i + 1, len(sales)):
            if sales[i] < sales[j]:
                sales[i], sales[j] = sales[j], sales[i]
                customers[i], customers[j] = customers[j], customers[i]


# @function __main__ la funzione che si occupa del lancio del programma
def __main__():
    sale = 1
    sales = []
    customers = []

    while sale != 0:
        sale = float(input("Inserire il valore dell'importo pagato dal cliente oppure '0' se si è terminata la lista: "))

        if sale != 0:
            customer = input("Inserire il nominativo del cliente che ha effettueto quell'acquisto: ")
            sales.append(sale)
            customers.append(customer)

    name_of_best_customer(sales, customers)
    print("\n\nL'acquirente del giorno è %s con una spesa di %.2f$" % (customers[0], sales[0]))


if __name__ == "__main__":
    __main__()
