#1. feladat
x = int(input('Adjon meg egy szamot: '))
y = int(input('Adjon meg egy masik szamot: '))
if x > y:
    print(x)
else:
    print(y) 

#2. feladat
def kodolas():
    newText = ''
    text = input('Adja meg a szoveget: ')
    letterToChange = input('Adja meg a kicserelendo betut: ')
    for char in text:
        if char == letterToChange:
            newText += str(ord(char))
        else:
            newText += char
    return newText   

print(kodolas())

#2. feladat

with open('autok.csv','r',encoding='utf-8') as s:
    cars = [lines.strip().split(';') for lines in s]
    print(cars)
