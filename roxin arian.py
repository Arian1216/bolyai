def atlagfogy(_fogyasztas):
    _szamlalo = 0
    _osszeg = 0
    for adatok in _adatok:
        _szamlalo += _osszeg + adatok[_fogyasztas]
    return _osszeg/len(_adatok)

adatok = {}
_adatok = ['marka','fogyasztas','evjarat']

for i in range(len(_adatok)):
    marka = input("Adja meg az auto markajat:")
    if marka == "finish":
        break
    fogyasztas = float(input("Adja meg a fogyasztasat: "))
    evjarat = int(input("Adja meg az evjaratat: "))
    if evjarat > 2023:
        print("2023 vagy elobbi evjaratu autot adjon meg!")
        evjarat = int(input("Adja meg az evjaratat: "))

    adatok[marka] = {'fogyasztas':fogyasztas,'evjarat':evjarat}

for _adatok in adatok.items():
    print("Adatok:",adatok)

osszeg = 0

for fogy in adatok.values():
    print("Az atlagfogyasztas:",atlagfogy(fogy['fogyasztas']))