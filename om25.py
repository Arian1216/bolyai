allatok = {}
nev = ""
sorszam = 0
while nev != " ":
    nev = input("Neve: ")
    if nev == "":
        break
    faj = input("Fajta: ")
    kor = int(input("Kor: "))
    szuletesiev = 2023 - kor
    allatok[nev] = {"fajta": faj, "szuletesiev": szuletesiev}

for nev, info in allatok.items():
    sorszam += 1
    print(f"{sorszam}. Állat")
    print(f" - Nev --> {nev}")
    print(f" - Fajta --> {info['fajta']}")
    print(f" - Szuletesi ev --> {info['szuletesiev']}")