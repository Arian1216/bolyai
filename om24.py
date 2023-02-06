osztaly = {
    input("Add meg a neved: "):{'Magyar':4,
                                'Matematika':3,
                                'Angol nyelv':4,
                                'Történelem':5,
                                'Informatika':5
                                }
}

_Magyar = input("Adja meg a Magyar jegyét: ")
_Matematika = input("Adja meg a Matematika jegyét: ")
_Angolnyelv = input("Adja meg a Angolnyelv jegyét: ")
_Történelem = input("Adja meg a Történelem jegyét: ")
_Informatika = input("Adja meg a Informatika jegyét: ")



for nev, tantargy in osztaly.items():
    for tantargy, jegy in tantargy.items():
        print(tan)