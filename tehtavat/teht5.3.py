luku = int(input("Anna kokonaisluku: "))

if luku < 2:
    print("Ei ole alkuluku")
else:
    jaollinen = 0

    for i in range(2, luku):
        if luku % i == 0:
            print(f"Luku on jaollinen {i}lla")
            jaollinen += 1

    if jaollinen == 0:
        print("Luku on alkuluku.")
    else:
        print("Luku ei ole alkuluku.")