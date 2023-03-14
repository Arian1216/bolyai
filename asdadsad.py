orszagok=[]
varosok=[]
alapit=[]
kezdok=[]
varosbetu={}
betuszam=[]
BBBOrszag=[]
elsovaros=[]
elso=0
with open("eu.csv",'r',encoding='utf-8') as forras:
    for sor in forras:
        orszagok_lista=sor.strip().split(",")
        # varosok.append(orszagok_lista[0])
        egy_orszag={"orszag":orszagok_lista[0],"fovaros":orszagok_lista[1],"csatlakozasa":orszagok_lista[2]}
        orszagok.append(egy_orszag)
print("Ezek az országok a tagjai:",orszagok)
print(50*"-") #-----------------------------------------------------------
# print(varosok)
# --------------------------------
# for i in orszagok:
#     print(i['orszag'])
# --------------------------------
for i in orszagok:
    alapit.append(i['csatlakozasa'])
alapit.sort()
# print(alapit)
elso=alapit[0]
for ii in alapit:
    if ii==elso:
        kezdok.append(ii)
alapitoszam=len(kezdok)
print("Ennyi ország volt része alapításakor:",alapitoszam)
print(50*"-") #-----------------------------------------------------------
for k in orszagok:
    varosok.append(k["fovaros"])
for kk in varosok:
    if kk[0]=="B":
        BBBOrszag.append(kk)
print("B-vel kezdődő országok neve:",BBBOrszag)
print(50*"-") #-----------------------------------------------------------
for l in varosok:
    varosbetu[l]=(len(l))
for ll in varosbetu.values():
    betuszam.append(ll)
betuszam.sort()
kevesbetu=betuszam[orszagok_lista[1]]
print(kevesbetu)
# for lll in varosbetu.values():
#     if lll==kevesbetu: