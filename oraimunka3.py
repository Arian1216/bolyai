a = int(input("adj meg egy számot:"))

if a % 2 == 0:
    print("Páros")
else:
    print("Páratlan")

#elsofeladat

szo_ism="tűzliliom"
szo_nism=input("Irja be a szót:")
if szo_nism=="tűzliliom":
    print("Ezt ismerem, ez egy csodaszép virág")
else:
    print("Ez egy nagyon szép szó")

#masodik feladat

jovedelem = int(input("Fizetés:"))

if jovedelem <= 14400:
    print("Nem kell adót fizetni")
elif jovedelem >= 14400 or jovedelem <= 34000:
    print("19% adót kell fizetni, azaz",round((jovedelem*0.19),0))
elif jovedelem > 34000:
    print("29% adó, azaz",round((jovedelem*0.29),0))

#harmadik feladat