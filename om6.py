# 1. feladat
n = int(input("Adjon meg egy számot: "))
m = int(input("Adjon meg még egy számot: "))
for i in range(n, m):
    if i % 2 == 0:
        print(i, end="-")

print("\n",30*"*")

# 2. feladat
number = 0
sor = 1
while number < 10:
    number = int(input("Adjon meg egy számot: "))
    sor += 1