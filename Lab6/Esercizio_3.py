# # TRACCIA DELL'ESERCIZIO
# Un’organizzazione non governativa ha bisogno di un programma per calcolare la
# quota di sussidio economico da assegnare a ciascuna famiglia bisognosa di
# assistenza. La formula è la seguente:
# • Se il reddito annuo della famiglia è compreso tra $ 30 000 e $ 40 000 e la
# famiglia ha almeno tre figli, il sussidio è pari a $ 1000 per ogni figlio.
# • Se il reddito annuo della famiglia è compreso tra $ 20 000 e $ 30 000 e la
# famiglia ha almeno due figli, il sussidio è pari a $ 1500 per ogni figlio.
# • Se il reddito annuo della famiglia è minore di $ 20 000, il sussidio è pari a $
# 2000 per ogni figlio.
# Scrivete una funzione che faccia questi calcoli, poi scrivete un programma che in un
# ciclo chieda all’utente di fornire il reddito annuo e il numero di figli di ciascuna
# famiglia richiedente il sussidio, visualizzando il valore corrispondentemente
# restituito dalla funzione. Usate –1 come valore sentinella per terminare l’immissione
# dei dati.

# @function subsidy_calculator calcola la quota di sussidio economico da assegnare alla famiglia
# @param revenue rappresenta il reddito annuo della famiglia
# @param children rappresenta il numero di figli presenti all'interno della famiglia
def subsidy_calculator(revenue, children):
    subsidy = 0

    if (revenue > 30000) and (revenue < 40000) and children >= 3:
        subsidy = 1000 * children

    if (revenue > 20000) and (revenue < 30000) and children >= 2:
        subsidy = 1500 * children

    if revenue < 20000:
        subsidy = 2000 * children

    if subsidy == 0:
        print('La famiglia non ha diritto a nessuna sorta di sussidio.\n')
    else:
        print('La famiglia ha diritto ad un sussidio pari a:', subsidy)

    return


# @function __main__ la funzione che si occupa del lancio del programma
def __main__():
    run = True

    while run:
        revenue = int(input("Inserire il reddito annuo della famiglia: "))
        children = int(input("Inserire il numero di filgi presenti all'interno della famiglia: "))

        subsidy_calculator(revenue, children)

        if input("Se vuoi chiudere il programma digita '-1': ") == '-1':
            run = False


if __name__ == "__main__":
    __main__()
