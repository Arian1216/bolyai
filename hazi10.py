lista=[-14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-75,80,-77,100,67,22,8,-78,-6]

valt = 0
for e in lista:
	if e:
		valt += 1
print(f"1. feladat: {valt}")

neg = len(lista)
neg_ertek = -14
i = 0
while lista[i] != neg_ertek:
    i += 1
print("2. feladat: Van")

paros = []
n = 0
for i in lista:
	if i % 2:
		paros.append(i)
		n += 1
print(f"3. feladat: {n}")

max = lista[0]
for x in range(1,len(lista)):
	if lista[i] > x:
		max = lista[i]
print(f"4. feladat: {max}")

oszto_10 = []
for i in range(len(lista)):
	if lista[i] % 10 == 0:
		oszto_10.append(lista[i])
print(f"5. feladat: {oszto_10}")

oszto_29 = []
for z in range(len(lista)):
	if lista[z] % 29 == 0:
		oszto_29.append(lista[z])
		index = x
print(f"6. feladat: {oszto_29,x}") #ez meg csak listat ir, nem az elso oszthato indexet

true_false = []
for i in lista:
	if i % 2:
		true_false.append(i)
print(f"7. feladat: Hamis")

add = 0
avg = len(lista)
for x in lista:
	add = add + x
	add = add / avg
print(f"8. feladat: {add}") 

oszto_17 = []
for i in range(len(lista)):
	if lista[i] % 17 == 0:
		oszto_17.append(lista[i])
print(f"10. feladat: {oszto_17} A lista nem tartalmaz ilyen szamot.") 