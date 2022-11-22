lista=[-14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-75,80,-77,100,67,22,8,-78,-6]

ertek = 0
for elem in lista:
    if elem:
        ertek += 1
print(f"1. feladat: {ertek}")

paros = []
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        paros.append(lista[i])
print(f"3.feladat: {paros}")

maxElem = lista[0]
for i in range(1,len(lista)):
    if lista[i] > maxElem:
        maxElem = lista[i]
        index = i
print(f"4. feladat: {maxElem, index}")

oszto = []
for i in range(len(lista)):
    if lista[i] % 10 == 0:
        oszto.append(lista[i])
print(f"5.feladat: {oszto}") # f string -> f"..{..}"

oszto29 = []
for i in range(len(lista)):
    if lista[i] % 29 == 0:
        oszto.append(lista[i])
print(f"5.feladat: {oszto29}")
