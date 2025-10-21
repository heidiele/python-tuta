leiviska = int(input("Anna leiviskät:"))
naula = int(input("Anna naulat:"))
luoti = float(input("Anna luodit:"))

koko = ((leiviska * 20 + naula) * 32 + luoti) * 13.3

kg = int(koko //1000)
g = koko % 1000

print(f"Massa on {kg} kg ja {g:.1f} g")