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

def print_assortiment():
    print("                            ")
    print("Dit zit in ons assortiment ",assortiment)        
        
def voeg_product_toe():
    producttoevoeg = input("Geef de naam van een product: ")
    bedragtoevoeg = int(input("Geef het bedrag van het product: "))
    assortiment[producttoevoeg] = bedragtoevoeg
    print("Dit zit er nu in je boodschappenmandje: ")
    print_assortiment()
    
def verwijder_product():
    print(assortiment)
    productverwijder = input("Geef de naam van een product die je wil verwijderen: ")

    if productverwijder in assortiment:
        del assortiment[productverwijder]
        print(assortiment)
        return assortiment
    else:
        print("Dat is geen product ")

def wijzig_product():
    print(assortiment)
    productwijzigen = input("Geef de naam van een product die je wil wijzigen: ")
    
    if productwijzigen in assortiment:
        wijzig = input("Waarnaar ga je de product wijzigen?: ")
        prijs = int(input("Wat wordt de prijs?: "))
        
        assortiment[wijzig] = assortiment.pop(productwijzigen)
        assortiment[wijzig] = prijs
        print (assortiment)
    else:
        print("Dit is geen product. ")
    
def toevoegen_boodschappenmand():
    kaas = True
    mandje = {}
    prijs = 0
    while kaas ==  True:
        print("Dit is wat we te koop hebben: ")
        print(assortiment)
        print("                   ")
        input0 = input("Wil je (nog) iets kopen?(ja/nee): ")
        print("                   ")
        if input0 == "ja":
            input1 = input("Wat wil je kopen? ")
            if input1 in mandje:
                l = assortiment[input1]
                r = int(input("Hoeveel wil je ervan kopen? "))
                w = l*r
                mandje[input1] = int(w)
                print(mandje)
            elif (input1 != assortiment):
                print("Dit zit niet in ons assortiment. ")
                print("           ")
            else:
                x = assortiment.get(input1)
                prijs = prijs + x
                print("                   ")
                print("Zoveel kost dit product: ",prijs)
                print("                   ")
                mandje[input1] = int(x)
        elif input0 == "nee":
            kaas = False
        else:
            print("Typ aub alleen 'ja' of 'nee'")
    
    print("                   ")
    print(mandje, "Dit zit er nu in uw mandje. ")
    print("Je boodschappen kosten", prijs, "euro. ")
        
def sla_op():
    print(assortiment)
    opslaan = open("producten.txt","w")
    opslaan.write(str(assortiment))
    opslaan.close
    print("Alle producten zijn opgeslagen.")
    
def afsluiten():
    print("doei")
while slose == False:
    print_functie()
    inpurt = input("Kies een optie: ")
        
    if (inpurt == "1"):
        print_assortiment()
    elif (inpurt == "2"):
        voeg_product_toe()
    elif (inpurt == "3"):
        verwijder_product()
    elif (inpurt == "4"):
        wijzig_product()
    elif (inpurt == "5"):
        toevoegen_boodschappenmand()
    elif (inpurt == "6"):
        sla_op()
    elif (inpurt == "x"):
        afsluiten()
        slose = True
            


#contacten

#functies
#functie items toevoegen
#functie items verwijderen
#functie laat items zien

#main applicatie
#while input <> '7':
