a = [17,38,10,25,75]
for i in range(len(a)):
    a.sort()
    a.reverse()
print(a)

b = [17,38,10,25,75]
print(sorted(b))

#stringek
str_1 = "string"
print(str_1[0]) # a string korbejarhato mint a listak

str_2 = "string"
for i in range(len(str_2)): # a len meg tudja allapitani a string elemeit is
    print(str_2[i],end="")
print("\n")

be = str(input("szó: "))
for i in range(len(be)):
    print(be[i],end=" ")
print()
#for i in range(1,len(be),2):
 #   print(be[i])
#for i in range(len(be)):
  #  print(ord(be[i]))
