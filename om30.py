countries = []
with open('eu.csv','r',encoding='utf-8') as source:
    #for line in source:
        #print(line.strip().split(',')) listaba helyezes
    for line in source:
        country_list=line.strip().split(',')
        country = {'Country': country_list[0], 'Capital': country_list[1], 'Accession': country_list[2]}
        countries.append(country)
#print(countries)
#for country in countries:
    #print(country['Country']) #'fovarosa',country['Capital'],country['Accession'],'-ben csatlakozott.')
for country in countries:
    year = int(country['Accession'])
    print(year)