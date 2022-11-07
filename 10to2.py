
tizes = int(input("Kérem adjon meg egy számot (0-255): "))
kettes = ""

while tizes > 0 or tizes < 256:
    kettes = (str(tizes % 2) + kettes)
    tizes = tizes // 2

print(kettes)