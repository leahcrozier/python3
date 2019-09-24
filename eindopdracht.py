slose = False
assortiment = {"aardappel":7,"wortels":1,"ei":69}
#mandje = {}

def print_functie():
    print("                       ")
    print('''1. Bekijk alle producten.
2. Voeg een product toe.
3. Verwijder een product.
4. Wijzig een product.
5. Boodschappen doen.
6. Sla producten op.
7. Klik op x om te stoppen.''')
    print("                       ")

def n1():
    print(assortiment)        
        
def n2():
    producttoevoeg = input("geef de naam van een product ")
    bedragtoevoeg = int(input("geef het bedrag van het product "))
    assortiment[producttoevoeg] = bedragtoevoeg
    print("dit zit er nu in je boodschappenmandje")
    n1()
    
def n3():
    print(assortiment)
    productverwijder = input("Geef de naam van een product die je wil verwijderen ")

    if productverwijder in assortiment:
        del assortiment[productverwijder]
        print(assortiment)
        return assortiment
    else:
        print("Dat is geen product ")

def n4():
    print(assortiment)
    productwijzigen = input("Geef de naam van een product die je wil wijzigen ")
    
    if productwijzigen in assortiment:
        wijzig = input("Waarnaar ga je de product wijzigen? ")
        prijs = int(input("Wat wordt de prijs? "))
        
        assortiment[wijzig] = assortiment.pop(productwijzigen)
        assortiment[wijzig] = prijs
        print (assortiment)
    else:
        print("ok")
def n5():
    kaas = True
    mandje = {}
    while kaas ==  True:
        print("dit is wat we te koop hebben: ")
        print(assortiment)
        input0 = input("wil je (nog) iets kopen? ")
        if input0 == "ja":
            input1 = input("wat wil je kopen? ")
            if input1 in mandje:
                l = assortiment[input1]
                r = int(input("hoeveel wil je ervan kopen? "))
                w = l*r
                #x = assortiment.get(input1)
                #print(x)
                mandje[input1] = int(w)
                print(mandje)
            else:
                x = assortiment.get(input1)
                print(x)
                mandje[input1] = int(x)
                print(mandje)
        elif input0 == "nee":
            kaas = False
        else:
            print("typ aub alleen 'ja' of 'nee'")
    prijs = mandje.values()
    print(prijs)
        
    print(mandje, "dit zit er nu in uw mandje")
        
def n6():
    print(assortiment)
    opslaan = open("producten.txt","w")
    opslaan.write(str(assortiment))
    opslaan.close
    print("Alle producten zijn opgeslagen.")
    
def n7():
    print("doei")
while slose == False:
    print_functie()
    inpurt = input("Kies een optie: ")
        
    if (inpurt == "1"):
        n1()
    elif (inpurt == "2"):
        n2()
    elif (inpurt == "3"):
        n3()
    elif (inpurt == "4"):
        n4()
    elif (inpurt == "5"):
        n5()
    elif (inpurt == "6"):
        n6()
    elif (inpurt == "x"):
        n7()
        slose = True

            


#contacten

#functies
#functie items toevoegen
#functie items verwijderen
#functie laat items zien

#main applicatie
#while input <> '7':
