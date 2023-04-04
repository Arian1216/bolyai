with open('auto.txt','r',encoding='utf-8') as f:
    header = f.readline()
    with open('opel.txt','w',encoding='utf-8') as c:
        print(header,file=c)
        for line in f:
            data = line.strip().split('\t')
            if data[3] == 'Opel':
                 print('\t'.join(data),file=c)
        for counted in data[3]:
            data.count(data[3])
            # szamold meg a markakbol mennyi auto van