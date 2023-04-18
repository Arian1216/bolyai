# n = int(input('Adj meg egy szamot:'))
# if n % 2 == 0:
#     print('Paros')
# else:
#     print('Paratlan')

# def email(Name,Year):
#     #Year = 2023-str(Year-int(_Year[0]-8)+_Year[1]) a yeart darabolni kell listaba stb hogy jo legyen
#     return f"{Name.replace(' ','.').lower()}.tech{Year}@bolyaimovar.com"
# Name = input('Add meg a neved:')
# Year = input('Kerem adja meg az osztalyt')
# print(email(Name.replace('áéíöüóőúű','aeiou'),Year)) a replace nem mukodik


with open('hegyekMo.txt','r',encoding='utf-8') as s:
    s.readline()
    mt = [lines.strip('\ufeff').split(';')[2] for lines in s]
    for height in sorted(mt):
        print(height)
