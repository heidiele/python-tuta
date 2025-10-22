def suurin_arvo(a, b, c):
    # Selvitetään, mikä luvuista on suurin
    suurin = a

    if b > suurin:
        suurin = b
    if c > suurin:
        suurin = c

    # Palautetaan suurin arvo
    return suurin


# Kysytään luvut käyttäjältä
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))

# Kutsutaan funktiota ja tulostetaan tulos
tulos = suurin_arvo(luku1, luku2, luku3)
print("Suurin arvo on:", tulos)