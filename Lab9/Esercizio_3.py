# # TRACCIA DELL'ESERCIZIO
# Nei lunghi viaggi in auto, per ingannare il tempo, si può fare il gioco delle “parole
# concatenate”. Il primo giocatore dice una parola iniziale, poi a turno ciascun
# giocatore dovrà dire una nuova parola (ossia mai detta prima) la cui sillaba iniziale
# sia uguale alla sillaba finale della parola precedente. (NOTA: Per semplicità,
# ipotizziamo che tutte le sillabe siano lunghe esattamente 2 caratteri, quindi per “figli”
# la ‘sillaba’ finale sarà “li” e non “gli”).
# Ad esempio: gatto - torino - notte - tela - lana …
# Scrivere un programma per permettere di gestire una o più partite del gioco.
# Ciascuna partita termina quando un giocatore inserisce una parola già detta nella
# stessa partita, quando inserisce una parola non correttamente concatenata, oppure
# quando non riesce a proseguire (per abbandonare, inserisce *).

# @function checking_words controlla se una parola che sta per essere inserita è già presente o è inserita con una
# modalità errata
# @param word indica la parola da controllare
# @param words indica la lista di parole che sono state inserite
# @return True/False ritorna vero se la parola non compare mai nella lista falso altrimenti
def checking_words(word, words):
    for item in words:
        if item == word:
            return False

    if len(words) >= 1:
        if word[0:2] != words[-1][-2:]:
            return False

    return True


# @function __main__ la funzione che si occupa del lancio del programma
def __main__():
    run = True
    match = True
    words = []

    while run:
        while match:
            word = input("\nGiocatore 1, inserisci una parola che si concateni alla precedente oppure inserisci '*' "
                         "per terminare: ")

            if word == '*':
                match = False
                break

            if not checking_words(word, words):
                print("Giocatore 2 HAI VINTO!")
                break
            else:
                words.append(word)

            word = input("Giocatore 2, inserisci una parola che si concateni alla precedente oppure inserisci '*' per "
                         "terminare: ")

            if not checking_words(word, words):
                print("Giocatore 1 HAI VINTO!")
                break
            else:
                words.append(word)

        if input('\n\nInserisci 1 per rigiocare o qualsiasi altro tasto per terminare: ') != '1':
            run = False


if __name__ == "__main__":
    __main__()
