osztaly = {}

def avg(m,ma,a,t,i):
    x = m+ma+a+t+i
    return float(x/5)

_nev = ""
osszeg = 0
while _nev != " ":
    _nev = input("Adja meg a nevet: ")
    if _nev == "":
        break
    _magyar = int(input("Adja meg a Magyar jegyet: "))
    _matek = int(input("Adja meg a Matematika jegyet: "))
    _angol = int(input("Adja meg a Angolnyelv jegyet: "))
    _tori = int(input("Adja meg a Tortenelem jegyet: "))
    _info = int(input("Adja meg a Informatika jegyet: "))
    osztaly[_nev] = {}
    osztaly[_nev]["Magyar"] = _magyar
    osztaly[_nev]["Matek"] = _matek
    osztaly[_nev]["Angol"] = _angol
    osztaly[_nev]["Tori"] = _tori
    osztaly[_nev]["Info"] = _info
    osztaly[_nev]["Atlag"] = avg(_magyar,_matek,_angol,_tori,_info)
for nev,tantargy in osztaly.items():
    print(f"{nev}:{tantargy}")
for jegy in tantargy.values():
    osszeg += int(jegy)
print(osszeg)