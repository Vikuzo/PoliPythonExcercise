# # TRACCIA DELL'ESERCIZIO
# Lo pseudocodice seguente descrive come, in una libreria, viene calcolato l’importo di
# un ordine a partire dal costo totale dei libri ordinati e dal loro numero.
# • Leggere il costo totale dei libri e il numero di libri.
# • Calcolare le tasse (il 7.5 per cento del costo totale dei libri).
# • Calcolare i costi di spedizione ($2 per ogni libro).
# • Il prezzo totale dell’ordine è la somma del costo totale dei libri, delle tasse e
# dei costi di spedizione.
# • Visualizzare l’importo dell’ordine.
# Scrivere un programma in Python che implementi questo pseudocodice. Il costo
# totale dei libri e il numero di libri devono essere memorizzati in due variabili
# costanti.

# @param TAX_RATE tasse sul costo totale del libro in percentuale
TAX_RATE = 7.5

# @param SHIPPING_PER_BOX costo di spedizione del singolo libro
SHIPPING_PER_BOX = 2.00

# la funzione input() ci permette di ottenere delle informazioni dall'utente che possiamo associare a delle variabili.
# Fra parentesi possiamo inserire una variabile come parametro che verrà visualizzata a schermo prima di
# richiedere l'input

# @param COST costo di tutti i libri acquistati (inserito dall'utente)
COST = float(input('Inserire il costo totale dei libri acquistati: '))

# @param TOTAL_BOOKS totale dei libri acquistati (inserito dall'utente)
TOTAL_BOOKS = float(input('Inserire il totale dei libri acquistati: '))

# @param tax il costo dei libri con l'aggiunta delle tasse
tax = (COST * TAX_RATE)/100

# @param shipping il costo della spedizione
shipping = TOTAL_BOOKS * SHIPPING_PER_BOX

print("\n\nl'importo totale dovuto è: %.2f" % (COST + tax + shipping) + '$')
