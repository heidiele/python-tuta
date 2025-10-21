luku = int(input("Anna kokonaisluku: "))

if luku < 2:
    print("Luku ei ole alkuluku.") #Alkuluku on suurempi kuin 1 ja jaollinen vain itsellään ja ykkösellä
else:
    jaollisia = 0 #Muuttuja jaollisia laskee, kuinka monella luvulla luku menee tasan.

    for i in range(2, luku):
        if luku % i == 0:
            print(f"Luku on jaollinen {i}lla.")
            jaollisia = jaollisia + 1

    if jaollisia == 0:
        print("Luku on alkuluku.")
    else:
        print("Luku ei ole alkuluku.")

