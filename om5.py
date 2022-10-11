paratlan = 0
paros = 0
szam = 3

while szam != 0:
    number = int(input("Adj meg egy számot: "))
    szam -= 1  # ha ezt toroljuk akkor vegtelen lesz a ciklus
    if number % 2 == 1:
        paratlan += 1
    else:
        paros += 1
print("Páros:", paros, "\nPáratlan:", paratlan)

print(30*"-")

paros2 = 0
paratlan2 = 0
for i in range(3):
    number = int(input("Adj meg egy számot: "))
    if number % 2 == 1:
        paratlan2 += 1
    else:
        paros2 += 1
print("Páros:", paros2, "\nPáratlan:", paratlan2)

print(30*"-")
print("1. feladat")

text = "txt"

while text != "alma":
    text = input("Adjon meg egy szót: ")
print("Vége")
