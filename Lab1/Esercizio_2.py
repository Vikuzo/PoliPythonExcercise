# # TRACCIA DELL'ESERCIZIO
# Supponete di andare in un ristorante di lusso insieme ad alcuni amici e che, al
# momento di pagare il conto, vogliate dividerlo in parti uguali, compresa la mancia
# del 15%. Descrivete, mediante un diagramma di flusso, un algoritmo che calcoli la
# somma dovuta da ciascuno. Il programma, noto l’importo del conto ed il numero
# degli amici, deve visualizzare l’importo del conto, la mancia, il costo totale e la
# somma dovuta da ciascuno; inoltre, deve mostrare quanta parte della somma dovuta
# da ciascuno serve per pagare il conto e quanta per la mancia.

# @param amount_to_pay rappresenta l'importa in euro che i nostri amici devono pagare
amount_to_pay = 150

# @param people rappresenta il numero di amici a cena
people = 4

# @param tip rappresenta la mancia da dare al cameriere (amount_to_pay : 100 = 15 : x)
tip = (100 * 15) / amount_to_pay

print("L'importo del conto è pari a:", amount_to_pay)
print("La mancia da consegnare al cameriere e pari a:", tip)
print("La somma totale spesa è pari a:", (amount_to_pay + tip))
print("La somma dovuta da ognuno degli amici è:", ((amount_to_pay + tip) / people))

print("\n\n")  # Il comando \n serve per andare a capo e tornare ad inizio riga

print("La somma dovuta da ognuno degli amici per pagare l'importo è:", (amount_to_pay / people))
print("La somma dovuta da ognuno degli amici per pagare la mancia è:", (tip / people))
