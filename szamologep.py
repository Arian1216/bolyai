def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

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

# Get input from the user
expression = input('Enter a mathematical expression: ')

# Call the calculator function and print the result
result = calculator(expression)
print(result)
