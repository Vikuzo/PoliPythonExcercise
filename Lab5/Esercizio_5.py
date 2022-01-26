# # TRACCIA DELL'ESERCIZIO
# In francese i nomi delle nazioni sono femminili quando terminano con la lettera e,
# altrimenti sono maschili, con l’eccezione dei nomi seguenti, che sono maschili anche
# se terminano con la e:
# • le Belize
# • le Cambodge
# • le Mexique
# • le Mozambique
# • le Zaïre
# • le Zimbabwe
# Scrivete un programma che acquisisca il nome di una nazione in francese e vi
# aggiunga l’articolo: “le” per i nomi maschili e “la” per quelli femminili, come “le
# Canada” o “la Belgique”. Se, però, il nome della nazione inizia con una vocale,
# l’articolo diventa “l’” (ad esempio, l’Afghanistan). Infine, per i paesi qui elencati,
# che hanno un nome plurale, si usa l’articolo “les”:
# • les Etats-Unis
# • les Pays-Bas

# @param country la variabile che conterrà il paese inserito dall'utente
country = input('Inserire il nome di una nazione in francese: ')

if country[0].lower() in 'aeiou':
    if country.lower() == 'etats-unis' or country.lower() == 'pays-bas':
        country = 'les ' + country
    else:
        country = "l'" + country
elif country.lower() == 'belize' or country.lower() == 'cambodge' or country.lower() == 'mexique' \
        or country.lower() == 'mozambique' or country.lower() == 'zaire' or country.lower() == 'zimbawe':
    country = "le " + country
elif country[-1] == 'a':
    country = "le " + country
else:
    country = "la " + country

print(country)
