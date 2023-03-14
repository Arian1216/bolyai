#Optimalizalt kod + feature)

import re

sum = 0
legrovidebb_szo = ''
leghosszabb_szo = ''
with open('parduc_2.feladat.txt', 'r', encoding='utf-8') as source:
vers = ''.join(line for line in source)

words = re.findall(r'\b\w+\b', vers)
for word in words:
if not legrovidebb_szo or len(word) < len(legrovidebb_szo):
legrovidebb_szo = word
if len(word) > len(leghosszabb_szo):
leghosszabb_szo = word

sum = sum(1 for c in vers if c in 'aeiouáéíóöőúüűAEIOUÁÉÍÓÖŐÚÜŰ')

print(vers,'\n')
print('A vers',len(vers),'betűt és',len(words),'szót és',sum,'magánhangzót tartalmaz.')
print('A legrövidebb szó:', legrovidebb_szo)
print('A leghosszabb szó:', leghosszabb_szo)
