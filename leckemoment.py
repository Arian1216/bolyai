sum = 0
with open('parduc_2.feladat.txt', 'r', encoding='utf-8') as source:
    for lines in source:
        vers = source.read()

    letters = len(vers)
    words = len(vers.split())

    for mgh in vers:
        if mgh in 'aeiouáéíóöőúüűAEIOUÁÉÍÓÖŐÚÜŰ':
            sum += 1
print(vers,'\n')
print('A vers',letters,'betűt és',words,'szót és',sum,'magánhangzót tartalmaz.')