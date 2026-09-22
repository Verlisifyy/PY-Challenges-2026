# ik moest ff opzoeken wat de wiskundige term was voor faculteit, maar het is gewoon een product van alle positieve gehele getallen tot en met dat getal. Dus bijvoorbeeld de faculteit van 5 (geschreven als 5!) is 5 * 4 * 3 * 2 * 1 = 120. 
getal = int(input("Voer een getal in: "))
faculteit = 1
for i in range(1, getal + 1):   
	faculteit *= i
print("De faculteit is:", faculteit)