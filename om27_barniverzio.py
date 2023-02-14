osztaly={}
vege=True
while vege:
    _nev=input("Kérem adja meg a tanuló nevét:")
    if _nev=="":
        break
    _jegyek={"magyar":0,"matek":0,"töri":0,"angol":0,"info":0}
    for targy in _jegyek.keys():
        _jegyek[targy]=int(input(targy+":"))
    osztaly[_nev]=_jegyek

osztaly_osszeg=0
osztaly_szamlalo=0
for tanulo_neve,tanulo_jegyei in osztaly.items():
    tanulo_osszeg=0
    tanulo_szamlalo=0
    for jegy in tanulo_jegyei.values():
        tanulo_osszeg+=jegy
        tanulo_szamlalo+=1
    print(f"{tanulo_neve} átlaga: {tanulo_osszeg/tanulo_szamlalo}")
    osztaly_osszeg+=tanulo_osszeg
    osztaly_szamlalo+=tanulo_szamlalo

print(f"Az osztály átlaga: {osztaly_osszeg/osztaly_szamlalo}")
targy_osszeg={}
targy_szamlalo={}
for tanulo_neve,tanulo_jegyei in osztaly.items():
    for targy,jegy in tanulo_jegyei.items():
        if targy not in targy_osszeg:
            targy_osszeg[targy]=0
            targy_szamlalo[targy]=0
        targy_osszeg[targy]+=jegy
        targy_szamlalo[targy]+=1

for targy,osszeg in targy_osszeg.items():
    print(f"{targy} átlaga: {osszeg/targy_szamlalo[targy]}")