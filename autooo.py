with open('auto.txt','r',encoding='utf-8') as source:
    lines = source.readlines()
    header = lines[0].strip().split('\t')
    tulajdonosok = []
    legoregebb_auto = {"ev": float("inf")}
    szinek = []
    nincs_katalizator = 0
    for line in lines[1:]:
        oszlop = dict(zip(header, line.strip().split('\t')))
        tulajdonosok.append(oszlop['Tulajdonos'])
        if int(oszlop['Év']) < legoregebb_auto["ev"]:
            legoregebb_auto["ev"] = int(oszlop['Év'])
            legoregebb_auto["rendszam"] = oszlop['Rendszám']
            legoregebb_auto["tulajdonos"] = oszlop['Tulajdonos']
        szinek.append(oszlop['Szín'])
        if oszlop['Katalizátor'].lower() == 'nem':
            nincs_katalizator += 1

if len(tulajdonosok) > 1:
    print("Van olyan tulajdonos, akinek több autója van.")
else:
    print("Nincs olyan tulajdonos, akinek több autója van.")
#print(f"A legöregebb autó rendszáma: {legoregebb_auto['rendszam']}, tulajdonosa: {legoregebb_auto['tulajdonos']}")
szin_szamlalo = {}
for szin in szinek:
    if szin not in szin_szamlalo:
        szin_szamlalo[szin] = 0
    szin_szamlalo[szin] += 1
leggyakoribb_szin = max(szin_szamlalo, key=szin_szamlalo.get())
print(f"A(z) {leggyakoribb_szin} színű autó fordul elő leggyakrabban az adatbázisban.")
print(f"{nincs_katalizator} autónak nincs katalizátora.")

#hogy oszinte legyek ezt a hazit most nem ertettem, meg internet segitsegevel se megyek semmire, KeyError