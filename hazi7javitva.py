tizes = int(input("Kérem adjon meg egy számot (0-255): "))
kettes = ""

for i in range(7, -1, -1):
    if tizes >= 0:
        kettes = (str(tizes % 2) + kettes)
        tizes = tizes // 2
print(kettes)