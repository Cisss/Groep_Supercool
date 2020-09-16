import random

def steenpapierschaar():
    # Options the user can choose from
    options = ['steen', 'papier', 'schaar']
    # Ask user
    user = input("steen, papier, schaar?")

    # Make random choice out of 'steen', papier' and 'schaar'
    comp = random.choice(['steen', 'papier', 'schaar'])

    # Show given answers
    print ("comp = " + comp)
    print ("user  = " + user)

    # When user and computer give the same answer
    if user == comp:
        print ("Gelijkspel!")
    # if user gives weird answer
    elif user not in options:
        print("Hey ho wat doe je nou..")
    # if computer is steen
    elif comp == "steen":
        if user == "papier":
            print ("Je hebt gewonnen")
        else:
            print ("Je hebt verloren...")
    # if computer is papier
    elif comp == "papier":
            if user == "steen":
                print ("Je hebt verloren...")
            else:
                print ("Je hebt gewonnen")
    # if computer is schaar
    elif comp == "schaar":
        if (user == "steen"):
            print ("je wint!")
        elif (user == "papier"):
            print ("Je hebt verloren")
