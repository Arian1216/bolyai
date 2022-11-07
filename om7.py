A = int(input("Adja meg az 1. számot: "))
B = int(input("Adja meg az 2. számot: "))
jel = str(input("+, -, *, /, **, %: "))

if jel == "+":
    print(A,"+",B,"=",A + B)
elif jel == "-":
    print(A,"-",B,"=",A - B)
elif jel == "*":
    print(A,"*",B,"=",A * B)
elif jel == "/":
    print(A,"/",B,"=",A / B)
elif jel == "**":
    print(A,"**",B,"=",A ** B)
elif jel == "%":
    print(A,"%",B,"=",A % B)
#1. feladat

print(50*".")

C = int(input("Adja meg a számot: "))
kettes=""
for i in range(7, -1, -1):
    if C - 2 ** i >= 0:
        x = 1
        C = C-2 ** i
    else:
        x = 0
    kettes = kettes + str(x)
print(kettes)

#2. feladat

print(50*".")

D = int(input("Irj be egy pzitiv egesz szamot: "))
prim=True
for i in range(2, D//2+1):
    if D % i == 0:
        prim = False
        print("Az %iosztoja %i-nek"%(i,D))
if prim:
    print("A %i primszam" % (D))