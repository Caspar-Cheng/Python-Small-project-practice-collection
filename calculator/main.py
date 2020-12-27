from replit import clear
from art import logo

def add(a, b):
  return a + b
def subtract(a, b):
  return a - b
def multiply(a, b):
  return a * b
def divide(a, b):
  return a / b

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  
  num1 = float(input("What's the first number: "))
  for symbol in operations:
    print(symbol)
  to_continue = True
  while to_continue:
    operation = input("pick an operation from the line above: ")
    num2 = float(input("What's the second number: "))
    calculation = operations[operation]
    answer = calculation(num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")
    next = input(f"Type 'y' to continue calculating with {answer},or type 'n' to start a new calculation: ")
    if next == "y":
      num1 = answer
    else:
      to_continue = False
      clear()
      calculator()

calculator()