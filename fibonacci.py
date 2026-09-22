# deze code heb ik 4 jaar geleden toen ik SD op vista maastricht zat

#  programma voor fibbonaci code te laten zien na hoeveel sequences iemand wilt 
fibonacci = input("hoeveel van de fibbonacci wilt u zien:")
x = fibonacci.isnumeric()

#eerste twee sequences
if x == True:
    fibonacci = int(fibonacci)
    nummer1, nummer2 = 0, 1
    begin = 0
    #check of de nummer die ingevoerd valid is
    if fibonacci <=0:
        print("fout")
    #als er 1 fibbonaci is return to nummer1
    elif fibonacci == 1:
        print ("fibbonacci code tot ", fibonacci, ":")
        print(nummer1)
    #geneer fibonacci code
    else:
        print("Fibonacci sequence:")
        while  begin < fibonacci:
            print(nummer1)
            cijfercombo = nummer1 + nummer2
            #rekenwerk voor de correcte fibonacci code
            nummer1 = nummer2
            nummer2 = cijfercombo
            begin += 1
else:
    print("Vul een getal in")