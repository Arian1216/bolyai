name = []

with open('nevek.txt','r',encoding='utf-8') as source:
    lines = source.read()
    names = lines.strip().split('\n')
    name.append(names)
    print(name)

#1. feladat xd
print(name[0][1])
print(name[0][8])
print(name[0][16])
print(name[0][19])

#2. feladat :((((((
letters = []
for i in name:
    letters.append(len(i[0]))
print(f'{letters[0]}. nev a leghosszabb.')