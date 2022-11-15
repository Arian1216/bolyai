n = [32,  5, 12, 8, 3, 75, 2, 15]
x = n[0]

for i in n:
    if x < i:
        x = i
print(x)

n = [32,  5, 12, 8, 3, 75, 2, 15]
x = n[0]

for i in range(len(n)): #0tol 7ig fut, mert 8 eleme van
    if x < n[i]:
        x = n[i]
        x_i = i
print(x,"A(z)",x_i,". elem.")

be = str(input("Adjon meg számokat"))
list = [be]
for i in range(len(list)):
    if x < be[i]:
        x = be[i]
        x_i = i
print(list,x_i) # ez meg nem jo