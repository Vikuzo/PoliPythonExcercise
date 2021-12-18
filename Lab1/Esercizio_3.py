# # TRACCIA DELL'ESERCIZIO
# In un programma di calendarizzazione (scheduling) di eventi si deve verificare se
# due appuntamenti della stessa giornata si sovrappongono. Per semplicità, ipotizziamo
# che gli appuntamenti inizino sempre a un’ora esatta (senza minuti) e usiamo l’orario
# militare (cioè con le ore che vanno da 0 a 23). Lo pseudocodice seguente descrive un
# algoritmo che determina se l’appuntamento che inizia all’ora start1 e termina all’ora
# end1 si sovrappone all’appuntamento che inizia all’ora start2 e termina all’ora end2.
# Se start1 > start2
# s = start1
# Altrimenti
# s = start2
# Se end1 < end2
# e = end1
# Altrimenti
# e = end2
# Se s < e
# Gli appuntamenti si sovrappongono
# Altrimenti
# Gli appuntamenti non si sovrappongono
# i. Seguite passo dopo passo l’esecuzione dello pseudo-codice con gli appuntamenti
# 10–12 e 11–13, poi con gli appuntamenti 10–11 e 12–13
# ii. Disegnate il diagramma di flusso per l’algoritmo
# iii. Spiegate il funzionamento dell’algoritmo e verificate se esso sia corretto

# @param start1 rappresenta l'ora di inizio del primo appuntamento
start1 = 10
# @param start2 rappresenta l'ora di inizio del secondo appuntamento
start2 = 12

# @param end1 rappresenta l'ora di fine del primo appuntamento
end1 = 11
# @param end2 rappresenta l'ora di fine del secondo appuntamento
end2 = 13

# Questa condizione verifica quale dei due appuntamenti incomincia per ultimo
if start1 > start2:
    s = start1
else:
    s = start2

# Questa condizione verifica quale dei due appuntamenti si conclude per primo
if end1 < end2:
    e = end1
else:
    e = end2

# Questa condizione verifica se il secondo appuntamento comincia prima che il primo si concluda
if s < e:
    print("Gli appuntamenti si sovrappongono.")
else:
    print("Gli appuntamenti non si sovrappongono.")
