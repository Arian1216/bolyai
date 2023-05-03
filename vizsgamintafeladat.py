#1. feladat
x = int(input('adjon meg egy szamot:'))
y = int(input('adjon meg egy masik szamot:'))
if x > y:
    print(x)
elif y < x:
    print(y)
elif x == y:
    print('egyenlo') # nem irja ki a megoldast lol

#2. feladat
def vizsga(_point): #ez lenne kulon fajlban :)))
    if _point >= 48:
        return  'Sikeres'
    else:
        return 'Sikertelen'
name = ' '
while name != '':
    name = str(input('Adja meg a nevet: '))
    if name:
        point = int(input('Adja meg a pontszamot: '))
        vizsga(point)