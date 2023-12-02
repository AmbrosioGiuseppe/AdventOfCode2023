# Aprire il file
with open('input.txt', 'r') as file:
    # Leggere il contenuto del file
    contenuto = file.read()

    # Spezzare il testo in parole
    parole = contenuto.split()

# 'parole' ora contiene la lista di tutte le parole nel file
somma = 0

for parola in parole:
    #print(list(parola))
    numeri = [carattere for carattere in parola if carattere.isdigit()]
    numeroTotale = str(numeri[0]) + str(numeri[-1])
    somma += int(numeroTotale)

print(somma)
