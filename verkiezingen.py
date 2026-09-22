stemmen = {}
while True:
    naam = input("Voer een naam in: ")

    if naam.upper() == "UITSLAG!":
        break

    naam = naam.lower()  
    if naam in stemmen:
        stemmen[naam] += 1
    else:
        stemmen[naam] = 1
winnaar = max(stemmen, key=stemmen.get)
print("De winnaar is:", winnaar)