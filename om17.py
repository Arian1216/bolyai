def paros(num):
    txt = "paratlan"
    if num % 2 == 0:
        txt = "paros"
    return txt
def addf(_a,_b):


i = 1

add = 0
while i != 0:
    i = int(input("Input: "))
    add = addf(add,i)
    #add += i
    print(paros(i))

print("Osszeg: ", add)

#------------------------------------