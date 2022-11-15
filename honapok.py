nap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
honap = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június',  'Július', 'Augusztus', 'Szeptember', 'Október', 'November', 'December']
datum = []
for i in range(12):
    datum.append(honap[i])
    datum.append(nap[i])

print(datum)
