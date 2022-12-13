def function_min(_lista):
    _lista.sort()
    return _lista[0]
n = 1
lista = []
while n != 0:
    n = int(input("Szamok:"))
    if n != 0:
        lista.append(n)

print("Legkisebb szam: ",function_min(lista))