lista=[-14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-75,80,-77,100,67,22,8,-78,-6]

x = 0
for i in lista:
	if i:
		x += 1
print(f"1. feladat: {x}")

kezd_ert = []
veg_ert = []

for f in lista:
	if f < -10:
		kezd_ert.append(f)
	else:
		veg_ert.append(f)
print(f"2. feladat: {kezd_ert, veg_ert}")