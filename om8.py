E = int(input("Irj be egy pzitiv egesz szamot: "))
prim=True
osszeg = 0
for i in range(2, E//2+1):
    if E % i == 0:
        prim = False
        osszeg = osszeg + i
        print("Az %iosztoja %i-nek"%(i,E))
if prim:
    print("A %i primszam" % (E))
else:
    print("Osztóinak összege:", osszeg)

#1. feladat

print(30*".")

