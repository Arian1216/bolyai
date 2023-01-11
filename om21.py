# 1. feladat
def digit(be):
    x = 0
    for i in be:
        if i != ".":
            i = int(i)
            x = x + i
    return str(x)
a = input("ÉÉÉÉ.HH.NN.: ")

eredmeny = digit(a)

while len(str(eredmeny)) != 1:
    eredmeny = digit(eredmeny)

print("Keresett szam: ",eredmeny)

# 2. feladat

def mysplit(strng):
    lista = []
    lista = ""

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit("")
