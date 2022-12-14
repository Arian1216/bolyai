lista=[ -14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-75,80,-77,100,67,22,8,-78,-6]

p = 23
l = len(lista)
i=0
while i < l and lista[i] != p:
    i += 1
print("1. feladat: ","Van")

c = 0
for x in lista:
    if x:
        c += 1
print("2. feladat: ",c)

min = lista[0]
for e in lista:
    if e < min:
        min = e
print("3. feladat: ",min)

harmincharom = []
for y in range(len(lista)-33,9):
    if lista[y] % 33 == 0:
        harmincharom.append(lista[y])
print("4. feladat: ",y)

a = 0
for z in lista:
	a = a + z
	avg = a / len(lista) / 2
print("5. feladat: ",avg) 

true_false = []
for i in lista:
	if i < 0:
		true_false.append(i)
print("6. feladat: ","Hamis")

p_ = []
n = 0
for i in lista:
	if i % 2 == 1:
		p_.append(i)
		n += 1
print("7. feladat: ",n)

tizenkilenc = []
for w in range(len(lista)-19):
    if lista[w] % 19 == 0:
        tizenkilenc.append(lista[w])
print("9. feladat: ",w)

ot = []
for f in range(len(lista)):
    if lista[f] % 5 == 0:
        ot.append(lista[f])
print("10. feladat: ",ot)