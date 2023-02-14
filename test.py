def raadhetgetal():
    import random
    getal = random.randint(1, 100)
    while True:
        gok = input("Raad het getal: ")
        if gok == "stop":
            break
        if int(gok) == getal:
            print("Goed geraden!")
            break
        else:
            print("Helaas, probeer het nog eens!")
    def checkinput():
        if gok == "stop":
            return False
        else:
            return True