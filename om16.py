be = str(input("Adj meg egy szot: "))
for i in range(len(be)):
    print(chr(ord(be[i])-32), end="")
print()

for i in range(len(be)-1,-1,-1):
    print(chr(ord(be[i])-32), end="")
print()

mondat = str(input("Adjon meg egy mondatot: "))
for i in range(len(mondat)):
    print(mondat[i].capitalize(), end="")
print()

def paros(num):
    paros = False
    if num % 2 == 0:
        paros = True
    return paros