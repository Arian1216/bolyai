v=int(input("Sebesség településen belül:"))
v2=int(input("Sebesség településen kivül:"))
v3=int(input("Sebesség az autópályán:"))
erkezes=int(input("Mikor érkezzen:"))

s=2.7
s2=7.9
s3=29.7

t=s/v #telepulesen belul
t2=s2/v2 #telepulesen kivul
t3=s3/v3 #autopalya

ido=t+t2+t3

ido2=erkezes*60-ido*60
h=ido2//60
hh=ido2%60
m= round(hh)

print("a.) feladat""\n","-"*20)
print("A szükséges idő az egyetemig:",round(ido,2),"óra")
print("b.) feladat""\n","-"*20)
print("A szükséges idő az egyetemig:", round(ido*60),"perc")
print("c.) feladat""\n","-"*20)
print("Az indulási idő:", round(h),":",m)