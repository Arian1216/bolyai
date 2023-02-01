osztaly = {}

def avg(m,ma,a,t,i):
    x = m+ma+a+t+i
    return float(x/5)

_nev = ""

while _nev != " ":
    _nev = input("Adje meg a nevét: ")
    if _nev == "":
        break
    _magyar = int(input("Adja meg a Magyar jegyét: "))
    _matek = int(input("Adja meg a Matematika jegyét: "))
    _angol = int(input("Adja meg a Angolnyelv jegyét: "))
    _tori = int(input("Adja meg a Történelem jegyét: "))
    _info = int(input("Adja meg a Informatika jegyét: "))
    osztaly[_nev] = {}
    osztaly[_nev]["Magyar"] = _magyar
    osztaly[_nev]["Matek"] = _matek
    osztaly[_nev]["Angol"] = _angol
    osztaly[_nev]["Töri"] = _tori
    osztaly[_nev]["Info"] = _info
    osztaly[_nev]["Átlag"] = avg(_magyar,_matek,_angol,_tori,_info)
for nev,tantargy in osztaly.items():
    print(f"{nev}:{tantargy}")

