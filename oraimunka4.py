mez = int(input("Mennyi mézzel indul?"))
nyuszi = int(input("Milyen messze lakik Nyuszi?"))
malacka = int(input("Milyen messze lakik Malacka?"))
nyuszi_mez = int(input("Mennyit ad neki Nyuszi?"))


if mez > nyuszi:
    print(mez-nyuszi+nyuszi_mez)
else:
    print(0)