from datetime import datetime

naam = input("Wat is je naam? ")
leeftijd = int(input("Wat is je leeftijd? "))
huidig_jaar = datetime.now().year
jaar_100 = huidig_jaar + (100 - leeftijd)
print(naam, "wordt 100 jaar in", jaar_100)