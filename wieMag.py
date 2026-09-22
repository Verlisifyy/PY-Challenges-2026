import random
aantal_spelers = int(input("Hoeveel spelers zijn er? "))
spelers = []
for i in range(aantal_spelers):
    naam = input(f"Naam van speler {i + 1}: ")
    spelers.append(naam)
begin_speler = random.choice(spelers)
print("\nDe speler die mag beginnen is:")
print(begin_speler)