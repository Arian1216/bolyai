countries = []
def founder(_founders):
    return _founders['Accession']

with open('eu.csv','r',encoding='utf-8') as source:

    for line in source:
        country_list=line.strip().split(',')
        country = {'Country': country_list[0], 'Capital': country_list[1], 'Accession': country_list[2]}
        countries.append(country)

countries.sort(key=founder)

print(countries)


