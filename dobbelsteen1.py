import random

aantal = int(input("Hoeveel dobbelstenen wil je gooien? "))
som = 0
for i in range(1, aantal + 1):
    worp = random.randint(1, 6)
    print("Dobbelsteen", i, ":", worp)
    som += worp

print("Som van alle ogen:", som)