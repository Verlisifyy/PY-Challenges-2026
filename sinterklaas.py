verlanglijst = []
while True:
    wens = input("Wat wil je van Sinterklaas hebben? ")

    if wens == "KLAAR!":
        break

    verlanglijst.append(wens)
verlanglijst.sort()
print("\nVerlanglijst in alfabetische volgorde:")
for item in verlanglijst:
    print(item)