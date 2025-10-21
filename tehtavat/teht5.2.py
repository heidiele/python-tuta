luvut = []

syote = input("Anna luku lisättäväksi listaan (tyhjä lopettaa): ")

while syote != "":
    luku = int(syote)
    luvut.append(luku)
    syote = input("Anna luku (tyhjä lopettaa): ")

luvut.sort(reverse=True)  # suurimmasta pienimpään

print("Viisi suurinta lukua:")
for i in range(5):
    if i < len(luvut): #varmistaa, että käytetään vain olemassa olevia indeksejä, jos len on pienempi kuin ideksi ei tulosteta mitään
        print(luvut[i])