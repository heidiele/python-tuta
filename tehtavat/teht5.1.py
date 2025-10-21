import random

n = int(input("Kuinka monta noppaa heitetään? "))

summa = 0

for i in range(n):
    luku = random.randint(1, 6)
    print(luku)
    summa = summa + luku

print("Silmälukujen summa on:", summa)

