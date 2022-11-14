oktet = ""
for k in range(1,5):
    a = int(input("Irja be az 1. oktet értékét az ip címből (0-255): "))
    kettes = ""
    for i in range(7, -1, -1):
        if a - 2 ** i >= 0:
            x = 1
            a = a-2 ** i
        else:
            x = 0
        kettes = kettes + str(x)
    oktet = oktet + kettes+"."
    if k == 4:
        oktet = oktet + kettes
print("Az ipv4 cím kettes számrendszerben = ",oktet)

ip = str("IPV4: ")
bin = ""
for x in ip:
    if x == ".":
    for i in range(7, -1, -1):
        if x - 2 ** i >= 0:
            x = 1
            x = x - 2 ** i
        else:
            x = 0
        bin = bin + str(x)
    oktet = oktet + bin + "."
    if x == 4:
        oktet = oktet + bin
    print("Az ipv4 cím kettes számrendszerben = ", oktet)