oktet1 = int(input("Irja be az 1. oktet értékét az ip címből (0-255): "))
oktet2 = int(input("Irja be az 2. oktet értékét az ip címből (0-255): "))
oktet3 = int(input("Irja be az 3. oktet értékét az ip címből (0-255): "))
oktet4 = int(input("Irja be az 4. oktet értékét az ip címből (0-255): "))
kettes1 = ""
kettes2 = ""
kettes3 = ""
kettes4 = ""

ipv4_1 = oktet1
ipv4_2 = oktet2
ipv4_3 = oktet3
ipv4_4 = oktet4

for i in range(7, -1, -1):
    if oktet1 - 2 ** i >= 0:
        x = 1
        oktet1 = oktet1-2 ** i
    else:
        x = 0
    kettes1 = kettes1 + str(x)

#1. oktet

for i in range(7, -1, -1):
    if oktet2 - 2 ** i >= 0:
        x = 1
        oktet2 = oktet2-2 ** i
    else:
        x = 0
    kettes2 = kettes2 + str(x)

#2. oktet

for i in range(7, -1, -1):
    if oktet3 - 2 ** i >= 0:
        x = 1
        oktet3 = oktet3-2 ** i
    else:
        x = 0
    kettes3 = kettes3 + str(x)

#3. oktet

for i in range(7, -1, -1):
    if oktet4 - 2 ** i >= 0:
        x = 1
        oktet4 = oktet4-2 ** i
    else:
        x = 0
    kettes4 = kettes4 + str(x)

#4. oktet

print("A(z)",end=" ")
print(ipv4_1,ipv4_2,ipv4_3,ipv4_4,sep=".",end=" ")
print("ipv4 cím kettes számrendszerben kifejezve = ",end="")
print(kettes1,kettes2, kettes3, kettes4, sep=".")

ipadr = str(input("Írja be az ipv4 címet: "))
bin = ""

for i in range(7, -1, -1):
    if ipadr == "":

        if ipadr - 2 ** i >= 0:
            x = 1
            ipadr = ipadr-2 ** i
        else:
            x = 0
        bin = bin + int(x)

#ipv4adress
#sajnalom, de nem jott ossze, legalabb megprobaltam :)
print("Az",ipadr,"ipv4 cím kettes számrendszerben kifejezve = ", bin)