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
with open('autok.csv','r',encoding='utf-8') as s: #a, feladat
    s.readline()

    cars = [lines.strip().split(';') for lines in s]

    #b, feladat
    for car in cars:
        if car[0] == 'Munkács' and car[1] == 'Záhony':
            acc += int(car[4])
    print(acc)
    #acc = [_lines.strip().split(',')[4] for _lines in cars]
    #average = sum(acc)/len(acc)

    #print(average)

