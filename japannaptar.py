ev = int(input("Év:"))

if 1984 <= ev <= 2043:
    naptar = ev % 10
    if naptar == 4 or naptar == 5:
        print("zöld év")
    elif naptar == 6 or naptar == 7:
        print("piros év")
    elif naptar == 8 or naptar == 8:
        print("sárga év")
    elif naptar == 0 or naptar == 1:
        print("fehér év")
    elif naptar == 2 or naptar == 3:
        print("fekete év")
else:
    print("Az évszám nem 1984 és 2043 között van.")