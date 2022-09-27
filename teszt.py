v=50
s=2.7
t=2.7/50 #telepulesen belul

v2=90
s2=7.9
t2=7.9/90 #telepulesen kivul

v3=130
s3=29.7
t3=29.7/130 #autopalya

ido=t+t2+t3

ido2=28800-22*60
h=ido2//3600
hh=ido2%3600
m= hh//60


print("a.) feladat""\n","-"*20)
print("A szükséges idő az egyetemig:",round(ido,2),"óra")
print("b.) feladat""\n","-"*20)
print("A szükséges idő az egyetemig:", round(ido*60),"perc")
print("c.) feladat""\n","-"*20)
print("Az indulási idő:", h,":",m)