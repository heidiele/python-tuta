import random

n = int(input("Montako noppaa heitetään? "))

summa = 0

for i in range(n):
    luku = random.randint(1, 6)
    print(luku)
    summa += luku

print("Silmälukujen summa on", summa)