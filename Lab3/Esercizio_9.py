# # TRACCIA DELL'ESERCIZIO
# Un supermercato premia i propri clienti con buoni spesa il cui importo dipende dalla
# quantità di denaro spesa in prodotti alimentari (groceries). Ad esempio, spendendo
# 50 dollari, si ottiene un buono spesa di importo pari all’otto percento di quella
# somma. La tabella seguente mostra la percentuale usata per calcolare il buono spesa
# relativo a somme diverse. Scrivete un programma che calcoli e visualizzi il valore
# del buono spesa consegnato al cliente, sulla base della somma di denaro che ha speso
# nell’acquisto di prodotti alimentari.
# Denaro speso          Percentuale del buono
# Meno di $ 10              Nessun buono
# Da $ 10 a $ 60                8%
# Da più di $ 60 a $ 150        10%
# Da più di $ 150 a $ 210       12%
# Più di $ 210                  14%

import sys

# @param cost totale della spesa
cost = float(input("Inserire l'importo d'acquisto relativo ai generi alimentari: "))

voucher = 0

# Ricerca della percentuale del buono
if cost < 10:
    pass
elif 10 < cost <= 60:
    voucher = (cost * 8)/100
elif 60 < cost <= 150:
    voucher = (cost * 10)/100
elif 150 < cost <= 210:
    voucher = (cost * 12)/100
elif cost > 210:
    voucher = (cost * 14)/100
else:
    sys.exit("Errore nell'inserimento dei dati")

print('Hai diritto ad un buon sconto di valore: %.2f' % voucher + '$')
