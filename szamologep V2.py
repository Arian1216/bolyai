from math import factorial


def Numbers(var):
    return var == '0' or var == '1' or var == '2' or var == '3' or var == '4' or var == '5' or var == '6' or var == '7' or var == '8' or var == '9'

def Test4Num(varstr):
    n = 0
    var = ''
    try: 
        while Numbers(varstr[n]):
            var += varstr[n]
            n += 1
    except: pass
    return (int(var), n)

def operation(string, num1, num2):
    if string == '+':
        return num1 + num2
    if string == '-':
        return num1-num2
    if string == '*':
        return num1*num2
    if string == ':':
        return num1/num2
    if string == '^':
        return num1 ** num2
    if string == "!":
        for f in range(1,num1+1):
           fact = fact * f
        return num1 

def operator(operato):
    return operato == '+' or operato == '-' or operato == '*' or operato == ':' or operato == '^' or operato == "!"


negate = False
char = input('Adjon meg egy muveletet: ')

print(char + '=')
while True:
    try: 
        if char[0] == '-': #for negative numbers
            negate = True #because here the numbers are string format
            char = char[1:]
        number1 = Test4Num(char)[0]
        if negate == True:
            number1 = -number1
            negate = False
        end_number1 = Test4Num(char)[1]
        char = char[end_number1:]
        if char == '':
            print(number1)
            break
        op = char[0]
        char = char[1:]
        number2 = Test4Num(char)[0]
        end_number2 = Test4Num(char)[1]
        result = operation(op, number1, number2)
        number1 = result
        char = str(number1) + char[end_number2:]
        
    except: break