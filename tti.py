m = float(input("Kérem adja meg a magasságát m-ben:"))
kg = float(input("Kérem adja meg a testsúlyát kb-ban:"))

tti = kg/(m**2)
ideal_minimum = 18.5
ideal_maximum = 24.99
ideal = (m**2)*ideal_minimum
ideal2 = (m**2)*ideal_maximum

print(30*"*"+5*"-"+30*"*")
print("Az ön testtömegindexe:", round(tti, 2), "%")
print("Az ön magasságához az ideális testtömeg:", round(ideal, 2), "kg", "és", round(ideal2, 2), "kg között van")
