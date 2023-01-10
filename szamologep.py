def osszead(x,y):
    return x + y
def kivon(x,y):
    return x - y
def szorzas(x,y):
    return x * y
def osztas(x,y):
    if x or y == 0:
        print("Nem jo a 0.")
    return x / y
def negyzet(x,y):
    return x ** y

jelek = ["+","-","*",":","^"]

elso = input("Elso tag: ")
masodik = input("Masodik tag: ")

if jelek == "+":
    print(elso,"+",masodik,"=", osszead(elso,masodik))

elif jelek == "-":
    print(elso,"-",masodik,"=", kivon(elso,masodik))

elif jelek == "*":
    print(elso,"*",masodik,"=", szorzas(elso,masodik))

elif jelek == ":":
    print(elso,":",masodik,"=", osztas(elso,masodik))

elif jelek == "^":
    print(elso,"^",masodik,"=", negyzet(elso,masodik))

#otletem sincs innen hogyan tovabb
#ill. az egyszerre bekeres lehetetlennek tunik :(