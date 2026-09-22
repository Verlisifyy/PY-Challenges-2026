tekst = input("typ je woord in: ")
# tekst is == to wat je intype aka string
legetekst = ""
for m in tekst:
    legetekst = m + legetekst
print("Reverse Order :  ", legetekst)
if(tekst == legetekst):
   print("het is een  Palindroom String")
else: print("het is geen palidroom string ") 