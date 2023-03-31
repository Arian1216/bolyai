with open('programnyelv_1feladat.txt', 'r', encoding='utf-8') as f: #1. feladat
    f.readline()
    f.readline()
    with open('evszamok.txt', 'w', encoding='utf-8') as c:
          #for lines in f:
          #   years = lines.strip().split(';')
        years = [lines.strip().split(';')[0] for lines in f] #proba volt, es  mukodott, jo ez az egy soros for
        for year in sorted(years):
            print(year, file=c)

with open('programnyelv_1feladat.txt', 'r', encoding='utf-8') as f:
    f.readline()
    f.readline()
    with open('programozo.txt','w',encoding='utf-8') as d:
        names = [_lines.strip().split(';')[2] for _lines in f]
        for name in sorted(names): 
            print(name, file=d)

with open('evszamok.txt', 'r', encoding='utf-8') as f: #3. feladat
    f.readline()
    f.readline()
    # az evszamok.txt-bol mert egyszerubb 
    with open('ismetles.txt','w',encoding='utf-8') as e:
        yearOnce = set(years)
        yearMore = [year for year in yearOnce if years.count(year) > 1]
        print('\n'.join(yearMore),file=e)

#kesz :) Velemenyem szerint ez egy jo hazi volt!