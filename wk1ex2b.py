    import time


    def adventure():
        """Runs one session of interactive fiction

        Well, it's "fiction," depending on the pill color chosen...

        arguments: no arguments (prompted text doesn't count as an argument)
        results: no results     (printing doesn't count as a result)
        """
        # zet deze waarde op 0.0 om te testen of snel te spelen,
        # ..of hoger voor meer dramatisch effect!
        delay = 2.0

        username = input("Hoe noemt men u, edele avonturier? ")

        print()
        print("Welkom,", username, "in het Libracomplex, een labyrint")
        print("van gewichtige wonderen en grote hoeveelheden ... taart!")
        print()
        print("Uw queeste: om een taart te vinden, en te eten!")
        print()

        flavor = input("Welke smaak zoekt u? ")
        if flavor == "aardbeien":
            print("Uw wijsheid in taartkeuze is overweldigend!")
        elif flavor == "kersen":
            print("Een Limburgse klassieker: een goede keuze, avonturier!")
        else:
            print("Ieder zijn smaak...")

        print()
        print("Voorwaarts naar de queeste!\n\n")
        print("Een gang strekt zich voor u uit; in het gedimde licht ziet u")
        print("aan de ene kant een tafel met onduidelijke vormen en")
        print("materialen, en aan de andere kant een deur op een kier,")
        print("waarachter gelach --is dat gelach?-- van studenten klinkt.")
        print("Verder zie je een oude vrouw die om hulp roept.")

        time.sleep(delay)

        print()
        choice1 = input("Kiest u de tafel, de deur of de oude vrouw? [tafel/deur/vrouw] ")
        print()

        if choice1 == "tafel":
            print("Als u de tafel benadert lijkt de onduidelijke massa")
            print("een steeds grotere vorm aan te nemen, tot ...")

            time.sleep(delay)

            print("... ze herkenbaar wordt als een grote stapel verpakte")
            print("taarten, het karton strak geplooid. Uw uitdaging --en")
            print("honger-- is op smakelijke wijze opgelost.")
            choice2 = ""
        elif choice1 == "vrouw":
            print()
            print("De vrouw zegt dat ze een grote lading heeft met taarten, maar dat je daar nog wel wat voor moet doen.")
            print("'Wat dan?' vraagt u vol van uw quest.")
            print("Dan komt ze met een raadsel...")
            print("")
            print("Verder in het labirint vind u uw welbegeerde schat in overvloed...")
            print("de taart met", flavor) 
            print("echter moet u er ook iets voor inleveren")
            print("Achter de deur, vind u geen schat, maar het brengt u wel dichterbij.")
            print("U levert dan iets in wat u zeer kostbaar is.")
            print("Aan tafel vind u een deel van uw schat, maar het zal bitter smaken...")
            print("aangezien het niet alles is waar van u gehoopt had...")
            delen = "False"
            choice2 = input("Wat kiest u [labirint/tafel/deur/stoppen]")
        elif choice1 == "deur":
            print("U opent de deur en ziet een congregatie van wijze dames")
            print("en heren, die allen genieten van hun taken. Samenwerking")
            print("en vrolijkheid zijn hier in overvloed aanwezig, maar...")

            time.sleep(delay)

            print("...ze hebben ALLE taart opgegeten! Resten van dozen")
            print("liggen overal verspreid. U wordt duizelig en grijpt")
            print("naar een taart. Er is niets. U ademt uit en valt,")
            print("en ligt verslagen tussen de resten van dozen die u")
            print("langzaam bedekken tot verstikking volgt.")
            print("Een oude vrouw komt naar u toe en probeert u levensernergie te stelen.")
            print()
            print("Vlak voordat u uw laatste adem uitblaast komt er een jongen naar u toe..")
            print("Hij verjaagd de oude vrouw en geeft je een keuze")
            print("Hij kan je dragen en je helpen te zoeken naar de grote hoeveelheid taart")
            print("Op voorwaarde de taart te delen")
            delen = input("wil je verder en de taart delen? [True, False]")
            choice2 = input("Ga je mee naar het labirint? [labirint, stoppen]")

        if choice2 == "labirint":
            print("")
            print("Oke, daar gaan we dan, bestijg uw paard want het wordt een lange tocht.")
            print("U gaat rijden en blijft maar rijden en rijden...")
            print("Tot dat u in in elkaar zakt van vermoeidheid.")
            print("De oude vrouw heeft u er ingeluisd...")
            print(delen)
            if delen == "True":
                print("")
                print("De oude vrouw komt en probeert jullie levensenergie te stellen")
                print("Samen zijn jullie echter sterker en overwinnen de oude vrouw")
                print("De grote hoeveelheid taart nemen jullie in ontvangst")
                print("Je moet de taart delen, maar hebt er wel een vriend bij")
                print("Taart samen eten is eigenlijk veel leuker dan alleen")
                print("Eind goed al goed...")
            else:
                print("Langzaam steelt ze uw levensenergie, tot dat zij weer een jonge vrouw is.")
                print("Dan eet zij ALLE taart in haar eentje op.")
                print("Vaarwel", username, ", Je hebt gefaald om de quest te volbrengen...")
        elif choice2 == "tafel":
            print("Proef de bittere smaak van het verlies...")
            print("Op tafel liggen drie taarten, na dat je ze hebt opgegeten, wordt je misselijk en kost je alles weer uit...")
            print("Je quest is gefaald,")
            print("Vaarwel,", username + "...")
        elif choice2 == "deur":
            print("U opent de deur en ziet een congregatie van wijze dames")
            print("en heren, die allen genieten van hun taken. Samenwerking")
            print("en vrolijkheid zijn hier in overvloed aanwezig, maar...")

            time.sleep(delay)

            print("...ze hebben ALLE taart opgegeten! Resten van dozen")
            print("liggen overal verspreid. U wordt duizelig en grijpt")
            print("naar een taart. Er is niets. U ademt uit en valt,")
            print("en ligt verslagen tussen de resten van dozen die u")
            print("langzaam bedekken tot verstikking volgt.")
            print("Een oude vrouw komt naar u toe en probeert u levensernergie te stelen.")
            print()
            print("Vlak voordat u uw laatste adem uitblaast komt er een jongen naar u toe..")
            print("Hij verjaagd de oude vrouw en geeft je een keuze")
            print("Hij kan je dragen en je helpen te zoeken naar de grote hoeveelheid taart")
            print("Op voorwaarde de taart te delen")
            delen = input("wil je verder en de taart delen? [True, False]")
            print("")
            print("Oke, daar gaan we dan, bestijg uw paard want het wordt een lange tocht.")
            print("U gaat rijden en blijft maar rijden en rijden...")
            print("Tot dat u in in elkaar zakt van vermoeidheid.")
            print("De oude vrouw heeft u er ingeluisd...")
            if delen == "True":
                print("De oude vrouw komt en probeert jullie levensenergie te stellen")
                print("Samen zijn jullie echter sterker en overwinnen de oude vrouw")
                print("De grote hoeveelheid taart nemen jullie in ontvangst")
                print("Je moet de taart delen, maar hebt er wel een vriend bij")
                print("Taart samen eten is eigenlijk veel leuker dan alleen")
                print("Eind goed al goed...")
        else:
            print("Helaas dan stopt het avontuur hier...")