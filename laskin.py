print("-----Tervetuloa käyttämään laskinta!-----")

while True:
    print("\nValitse mitä toimintoa haluat käyttää:\n A: Yhteenlasku \n B: Vähennyslasku"
          "\n C: Kertolasku \n D: Jakolasku")

    valinta = input("Valintasi (A - D), Q lopettaa: ").upper()

    #While loopin katkaisu
    if valinta == "Q":
        print("Ohjelma lopetetaan, kiitos hei!")
        break

    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))

    if valinta == "A":
        print("Yhteenlasku:", a + b)
    elif valinta == "B":
        print("Vähennyslasku:", a - b)
    elif valinta == "C":
        print("Kertolasku:", a * b)
    elif valinta == "D":
        print("Desimaalijakolasku:", a / b)
    else:
        print("Valintasi oli virheellinen.")

"""
Päivittäkää laskin tekemään laskutoimitukset funktioissa, eli 4 funktiota: 
yhteenlaskulle, vähennyslaskulle, kertolaskulle ja desimaalijaolle. If-elif-else
-rakenteessa kutsukaa funktioita.
"""
