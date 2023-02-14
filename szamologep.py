def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b
if jelek == "+":
    print(elso,"+",masodik,"=", osszead(elso,masodik))

def calculator(expression):
  # Split the input into two operands and an operator
  operand1, operator, operand2 = expression.split()
  
  # Convert the operands to floats
  operand1 = float(operand1)
  operand2 = float(operand2)
  
  # Call the appropriate function based on the operator
  if operator == '+':
    result = add(operand1, operand2)
  elif operator == '-':
    result = subtract(operand1, operand2)
  elif operator == '*':
    result = multiply(operand1, operand2)
  elif operator == '/':
    result = divide(operand1, operand2)
  
  # Return the result
  return result
elif jelek == "-":
    print(elso,"-",masodik,"=", kivon(elso,masodik))

elif jelek == "*":
    print(elso,"*",masodik,"=", szorzas(elso,masodik))

elif jelek == ":":
    print(elso,":",masodik,"=", osztas(elso,masodik))

# Get input from the user
expression = input('Enter a mathematical expression: ')
elif jelek == "^":
    print(elso,"^",masodik,"=", negyzet(elso,masodik))

# Call the calculator function and print the result
result = calculator(expression)
print(result)
