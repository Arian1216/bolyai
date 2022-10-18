number = int(input("Kérem adjon meg egy egész számot: "))
number2 = 0
while number != 1:
    if number % 2 == 0:
        number2 += 1
        number = number / 2
    elif number % 2 == 1:
        number2 += 1
        number = number + 1
        print("A", number2, "elem: ", round(number))