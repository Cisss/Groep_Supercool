while True:
    import random
    lijst_kaarten = ['2','3','4','5','6','7','8','9','10','B','V','H','A']
    kaart_index = random.randint(0,len(lijst_kaarten)-1)
    kaart = lijst_kaarten[kaart_index]
    kaart2_index = random.randint(0,len(lijst_kaarten)-1)
    kaart2 = lijst_kaarten[kaart2_index]
    
    print()
    print(kaart)
    print ("Hoger of lager?")
    user = input("Ik kies:")
    print(kaart2)

    if user == "lager" and kaart_index <= kaart2_index:
        print("Helaas, verloren!")
    elif user == "lager" and kaart_index > kaart2_index:
        print("Gewonnen!")
    elif user == "hoger" and kaart_index >= kaart2_index:
        print("Helaas, verloren!")
    elif user == "hoger" and kaart_index < kaart2_index:
        print("Gewonnen!")
    elif user != "lager" and user != "hoger":
        print() 
    else:
        print("U heeft niet goed getypt...")