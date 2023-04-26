#1. feladat
x = int(input('adjon meg egy szamot:'))
y = int(input('adjon meg egy masik szamot:'))
if x > y:
    print(x)
elif y < x:
    print(y)
elif x == y:
    print('egyenlo')

#2. feladat
def vizsga(_point,_name): #ez lenne kulon fajlban :)))
    if _point >= 48:
        print(' {_name} sikeres')
    else:
        print('f {_name} sikertelen')

while name != '':
    name = str(input())