#1. feladat
x = int(input('Adjon meg egy szamot: '))
y = int(input('Adjon meg egy masik szamot: '))

if x > y:
     print(x)
else:
    print(y) 

#2. feladat
def kodolas(_text,_letterToChange):

    newText = ''
    for char in _text:
        if char == _letterToChange:
            newText += str(ord(char))
        else:
            newText += char
    return newText

text = input('Adja meg a szoveget: ')
letterToChange = input('Adja meg a kicserelendo betut: ')

print(kodolas(text,letterToChange))

#3. feladat

acc = 0
_acc = 0
with open('autok.csv','r',encoding='utf-8') as s:
    #a, feladat
    s.readline()
    cars = [lines.strip().split(';') for lines in s]
    #b, feladat
    for car in cars:
        if car[0] == 'Munkács' and car[1] == 'Záhony':
            acc += int(car[4])
    print(acc)
    #c, feladat
    for car in cars:
        if car[4]:
            _acc += int(car[4])
            average = _acc/len(cars)
    print(round(average,1))
    #d,feladat
    with open('budapestrol.dat','w',encoding='utf-8') as d:
        for car in cars:
            if car[0] == 'Budapest':
                print(';'.join(car),file=d)
