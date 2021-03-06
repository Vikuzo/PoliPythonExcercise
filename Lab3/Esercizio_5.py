# # TRACCIA DELL'ESERCIZIO
# Un anno di 366 giorni viene detto bisestile (leap) e serve a mantenere il calendario
# sincronizzato con il Sole, dal momento che la Terra vi ruota attorno una volta ogni
# 365.25 giorni. In realtà, questo numero non è esatto e per tutte le date successive al
# 1582 si applica la correzione gregoriana: solitamente gli anni divisibili per 4, come il
# 1996, sono bisestili, ma gli anni divisibili per 100, come il 1900, non lo sono; come
# eccezione all’eccezione, gli anni divisibili per 400, come il 2000, sono bisestili.
# Scrivete un programma che chieda all’utente un anno e determini se si tratta di un
# anno bisestile. Valutare anche se è possibile implementare il programma usando un
# unico enunciato if (con gli opportuni operatori booleani).

# @param year conterrà l'anno su cui effettuare le operazioni richieste
year = int(input('Inserire un anno per vedere se esso è bisestile: '))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("L'anno %d è bisestile." % year)
else:
    print("L'anno %d NON è bisestile." % year)
