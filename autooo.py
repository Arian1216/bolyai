auto = []
with open('auto.txt','r',encoding='utf-8') as source:
    for line in source:
        adatok = line.strip().split('\t')
        #print(adatok)
        auto_szotar = {
            'rendszam': adatok[0],
            'tulajdonos': adatok[1],
            'cim': adatok[2],
            'marka': adatok[3],
            'tipus': adatok[4],
            'szin': adatok[5],
            'cm3': adatok[6],
            'forgalom': adatok[7],
            'megjegyzes': adatok[8],
            'katalizator': adatok[9],
        }
        auto.append(auto_szotar)
#1. feladat :)))
tulajdonos = [auto_szotar['tulajdonos'] for auto_szotar in auto]
if len(set(tulajdonos)) == len(tulajdonos):
    print('Nincs')
else:
    print('Van')
#2.feladat
if auto_szotar:
    legoregebb = sorted(auto, key=lambda x: x['forgalom'])[0]
print(legoregebb['rendszam'],legoregebb['tulajdonos'])

#3. feladat
szinek = [auto['szin'] for auto_szotar in auto]
gyakorisag = {szin: szinek.count(szin) for szin in set(szinek)}
_gyakorisag = sorted(auto, key=lambda x: x['szin'])[0]
print(_gyakorisag)