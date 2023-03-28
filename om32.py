# with open('enfajlom.txt','r',encoding='utf-8') as f:
#     with open('txt.txt','w',encoding='utf-8') as _f:
#         for l in f:
#             print(l.strip(),file=_f)
# with open('4013.jpg','rb') as f:
#     with open('copy.jpg','wb') as _f:
#         size = 4096
#         image = f.read(size)
#         while len(image)>0:
#             _f.write(image)
#             image = f.read(size)



with open('programnyelv_1feladat.txt','r',encoding='utf-8') as f:
    f.readline()
    f.readline()
    with open('programnyelv_1feladat_masolat.txt','w',encoding='utf-8') as _f:
        for l in f:
            _l = l.strip().split(';')
            _f.writelines(_l[0]+';'+_l[1]+'\n')
            # print(_l[0]+';'+_l[1],file=_f) vagy ez printtel :))))))))))
