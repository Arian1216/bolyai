with open('auto.txt', 'r', encoding="utf-8") as f:
    header = f.readline().strip().split(';')
    data = [line.strip().split(';') for line in f]
# 1. Van-e olyan tulajdonos, akinek több autója van?
tulajdonos_dict = {}
for line in data:
    tulajdonos = line[0]
    if tulajdonos in tulajdonos_dict:
        tulajdonos_dict[tulajdonos] += 1
    else:
        tulajdonos_dict[tulajdonos] = 1

tobb_auto_tulajdonos = False
for tulajdonos, auto_szam in tulajdonos_dict.items():
    if auto_szam > 1:
        print(f"{tulajdonos} {auto_szam} autót birtokol.")
        tobb_auto_tulajdonos = True

if not tobb_auto_tulajdonos:
    print("Nincs olyan tulajdonos, akinek több autója lenne.")

# 2. Mi a rendszáma és ki a tulajdonosa a legöregebb autónak?
rendszamok = [line for line in data if len(line) > 2]
if not rendszamok:
    print("Az adatfájlban nincsenek rendszámmal, tulajdonossal és gyártási évvel rendelkező autók.")
else:
    legidosebb_auto = min(rendszamok, key=lambda x: int(x[2]))
    print(f"A legöregebb autó tulajdonosa {legidosebb_auto[0]} és a rendszáma {legidosebb_auto[1]}.")

# 3. Milyen színű autó fordul elő leggyakrabban?
szin_dict = {}
for line in data:
    szin = line[3]
    if szin in szin_dict:
        szin_dict[szin] += 1
    else:
        szin_dict[szin] = 1

leggyakoribb_szin = max(szin_dict, key=szin_dict.get)
print(f"A leggyakoribb autószín {leggyakoribb_szin}.")

# 4. Hány autónak nincs katalizátora?
nincs_katalizator_szam = 0
for line in data:
    if line[4] == "nincs":
        nincs_katalizator_szam += 1

print(f"{nincs_katalizator_szam} autónak nincs katalizátora.")

# 5. irányítószám szerint sorba
rendezett_adatok = sorted(data, key=lambda x: x[5])
for line in rendezett_adatok:
    print(line)