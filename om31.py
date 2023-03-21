name = ""
with open('new.txt','a',encoding='utf-8') as source:
#    while name != " ":
#        name = input('Adj meg neveket: ')
#        print(name , file=source, end=',')
    source.write('teszt')
