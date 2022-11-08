print(100*".")

listam=['hétfő ', 'kedd', 'szerda', 1800, 20.357, 'csütörtök', 'péntek']

print(listam)
for i in range(7):
    print(listam[i])
print(100*".")
for i in listam:
    print(i)

print(100*".")

list=['hétfő ', 'kedd', 'szerda', 'Július', 'csütörtök', 'péntek']
list.append("szombat")
list.insert(1,"narancs")
print(list)

print(100*".")

lista=['hétfő ', 'kedd', 'szerda', 'Július',20.357, 'csütörtök', 'péntek']
lista.remove('kedd')
print(lista)

print(100*".")

x1 = [23,32,2,3,432,26,21,7,5,10]
x1.sort()
print(x1)

x2 = [23,32,2,3,432,26,21,7,5,10]
x2.sort()
x2.reverse()
print(x2)

x3 = [23,32,2,3,432,26,21,7,5,10]
print(x3.index(23))