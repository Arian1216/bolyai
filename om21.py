# 1. feladat

be = input("Adjon meg egy datomot (ev:honap:nap): ")
x = 0
for i in be:
    if i != ".":
        i = int(i)
        x = x + i
print("Keresett szam: ",x)

# 2. feladat

