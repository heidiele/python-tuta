def keskiarvo(a, b, c):
    #Lasketaan kolmen luvun keskiarvo
    ka = (a + b + c) / 3
    print("Keskiarvo on:", ka)
    return

#Kysytään luvut käyttäjältä
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))

#Kutsutaan funktiota annetuilla arvoilla
keskiarvo(luku1, luku2, luku3)

