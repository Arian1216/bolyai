n = int(input('Adj meg egy szamot:'))
if n % 2 == 0:
    print('Paros')
else:
    print('Paratlan')

def email():
    Name = input('Add meg a neved:')
    startYear = input('Add meg a kezdo eved:')
    ClassName = input('Add meg az osztalyod:')
    return f"{Name.replace(' ','.')}.tech{startYear}{ClassName}@bolyaimovar.com"
print(email())

#with open('hegyekMo.txt','r',encoding='utf-8') as s:
