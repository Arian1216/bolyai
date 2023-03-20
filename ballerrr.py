import re

shortest_word = ''
longest_word = ''
with open('parduc_2.feladat.txt', 'r', encoding='utf-8') as source:
    vers = ''.join(line for line in source)

    # kivétel lista a szavak számára, amelyek nem lehetnek a legrövidebb szavak
    exceptions = ['a', 'az', 'azt', 'ez', 'ezt', 'ott', 'itt', 'olyan',]

    words = re.findall(r'\b\w+\b', vers)
    for word in words:
        if word not in exceptions:
            if not shortest_word or len(word) < len(shortest_word):
                shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word

    sum = sum(1 for c in vers if c in 'aeiouáéíóöőúüűAEIOUÁÉÍÓÖŐÚÜŰ')

    print(vers,'\n')
    print('A vers',len(vers),'betűt és',len(words),'szót és',sum,'magánhangzót tartalmaz.')
    print('A legrövidebb szó:', shortest_word)
    print('A leghosszabb szó:', longest_word)