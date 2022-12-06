lista = [32,  5, 12, 8, 3, 75, 2, 15]
even = []
odd = []

for i in lista:
    if i % 2:
        even.append(i)
    else:
        odd.append(i)
print(f"Paros szamok: {even}\nParatlan szamok: {odd}")