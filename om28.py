autok = []
auto = {}
def szam_e(_szam,szamjegy=None):
    jo = True
    for egy_szam in _szam:
        if not (egy_szam.isnumeric() or egy_szam == '.'):
            jo = False
            break
        if szamjegy != None and szamjegy != len(_szam):
            jo = False
        if not jo:
            print('Nem megfelelo az ertek')
        return jo

def oreg(_autok):
    min = _autok[0]['ev']
    min_nev = _autok[0]['nev']
    for _auto in _autok:
        if min > _auto['ev']:
            min = _auto['ev']
            min_nev = _auto['nev']
    return min_nev

def atlag_fogy(_autok):
    osszeg=0
    for i in range(len(_autok)):
        osszeg+=float(_autok[i]['fogy'])
        return round(osszeg/len(_autok), 2)

def rendezes(_autok, sort_on = 'nev'):
    decorated=[]
    vissza=[]
    for dict_ in _autok:
        decorated.append((dict_[sort_on], dict_))
    decorated.sort()
    for (key, _dict) in decorated:
        vissza.append(_dict)
    return vissza


snev = "a"
while snev != "":
    snev=input('Adjon meg egy markat: ')
    if snev != "":
        auto['nev'] = snev
        auto['ev'] = input('Adjon meg egy evjaratot:')
        while not szam_e(auto['ev'],4):
            auto['ev'] = input('Adjon meg egy evjaratot:')
        auto['fogy'] = input('Adja meg a fogyasztast:')
        while not szam_e(auto['fogy']):
            auto['fogy'] = input('Adja meg a fogyasztast:')
        auto['nev'] = snev
        autok.append(auto)
    auto = {}

print(autok)
print('Legregebbi auto:', oreg(autok))
print('Az autok atlagfogyasztasa:', atlag_fogy(autok))
print(rendezes(autok))