# 1. feladat
n = int(input("Adjon meg egy számot: "))
m = int(input("Adjon meg még egy számot: "))
for i in range(n, m):
    if i % 2 == 0:
        print(i, end="-")

print("\n",30*"*")

# 2. feladat
number = 0
osszeg = 0
sor = 1
while number < 10:
    number = int(input("Adja meg a 10-nél kisebb számot:"))
    osszeg = number + osszeg
    sor += 1
    if number > 10:
        print("Az utolsó szám nem kisebb tíznél.")
        print("A 10-nél kisebb számok összege:",osszeg-number)

#3. feladat
print(30*"*")

a = int(input("A= "))
b = int(input("B= "))
c = int(input("C= "))

if (a + b > c) and (b + c > a) and (a + c > b):
    T = (a + b + c) / 2
    K = a + b +c
    print("A háromszög megszerkeszthető.","\n","A háromszög területe:",T ,"A háromszög kerülete:",K)
else:
    print("Nem lehet megszerkeszteni a háromszöget")