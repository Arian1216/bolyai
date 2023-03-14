countries = []
cities = []
capital = []
cities_letters = {}
letter_count = []

def founder(_founders):
    return _founders['Accession']

with open('eu.csv','r',encoding='utf-8') as source:

    for line in source:
        country_list=line.strip().split(',')
        country = {'Country': country_list[0], 'Capital': country_list[1], 'Accession': country_list[2]}
        countries.append(country)

countries.sort(key=founder)

min = countries[0]['Accession']
print(countries)
for z in range(len(country)):
    if min > countries[z]['Accession']:
        min = countries[z]['Accession']

sum = 0
for i in countries:
    year = i['Country']
    if i['Accession'] == min:
        sum += 1

for x in countries:
    cities.append(x['Capital'])
for y in cities:
    if y[0]=="B":
        capital.append(y)

letters = []
for country in countries:
    letters.append(len(country['Country']))
letters.sort()
fourth_shortest = letters[3] # ezt nem nagyon ertem, nem en csinaltam

print(sum,'Alapítója van az EU-nak.')
print('B-s fővárosok: ',capital)
print(fourth_shortest)
