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
