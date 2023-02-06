ember = {'név':'Géza', 'születési_év':1999,
         'lakhely':'Makkoshotyka',
         'foglalkozás':'szarvasmarha-tenyésztő',
         'szemei száma':2,
         'kedvenc lottószámok':[1,2,3,4,5]}

print(ember.keys())
print(ember.values())

del ember['szemei száma']

ember['születési_év'] = 1980
print("Az ember neve", ember['név'])
ember['kutya'] = 'Bodri'

for key in ember.keys():
    print(key, ":", ember[key])

#############################################

print()

book = {

}
szerzo = " "
while book != szerzo:
    szerzo = input("Szerző: ")
    if szerzo == "":
        break
    cim = input("Cím: ")
    book.update({szerzo:cim})
for szerzo, cim in book.items():
    print(szerzo,"-",cim)

#############################################

print()