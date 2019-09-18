def mandje(boodschappen):
    print("                       ")
    print('''1. Bekijk alle producten.
2. Voeg een product toe.
3. Verwijder een product.
4. Wijzig een product.
5. Boodschappen doen.
6. Sla producten op.
7. Exit de programma.''')
    print("                       ")
    inpurt = input("Kies een optie: ")

    def n1():
        print(boodschappen)
        input1 = input("wil je nog een keer het keuze menu zien?")
        if input1 == "ja":
            mandje(boodschappen)
        elif input1 == "nee":
            n7()
        else:
            print("geef antwoord met ja of nee aub")
        
        
    def n2():
        print("   .")




    if (inpurt == "1"):
        n1()
        return
    if (inpurt == "2"):
        n2()
        return
    if (inpurt == "3"):
        n3()
        return
    if (inpurt == "4"):
        n4()
        return
    if (inpurt == "5"):
        n5()
        return
    if (inpurt == "6"):
        n6()
        return
    if (inpurt == "7"):
        n7()
        return
   
    
mandje({4,7,2})



