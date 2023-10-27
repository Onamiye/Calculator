#code originally written for 100 days of code challenge
#this program performs arithmetic operations on two numbers initially and optionally, performs more operations on the result generated from the previous calculation.

def add(n1,n2):
  return (n1+n2)

def subtract(n1, n2):
  return (n1-n2)

def multiply(n1, n2):
  return (n1*n2)

def divide(n1, n2):
  return (n1/n2)

Operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}



num1 = int(input("What's the first number: "))


for symbol in Operations:
  print(symbol)


operation_symbol =input("Pick a symbol from the line above: ")

num2 = int(input("What's the second number: "))

calculator_function = Operations[operation_symbol]
first_answer = calculator_function(num1,num2)
print(f"{num1} {operation_symbol} {num2} = {first_answer} ")

continue_ = input("Type y to continue and n to quit: ")

while continue_ != "n":
  operation_symbol =input("Pick a symbol from the line above: ")
  num3 = int(input("Enter another number: "))
  calculator_function = Operations[operation_symbol]
  second_answer = calculator_function(first_answer,num3)
  print(f"{first_answer} {operation_symbol} {num3} = {second_answer} ")
  
  first_answer = second_answer
  continue_ = input("Type y to continue and n to quit: ")
  
  
