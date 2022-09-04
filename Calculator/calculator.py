#Calculator
from os import system
import sys
#Add
def add(n1, n2):
    return n1 + n2
#Sub
def substract(n1, n2):
    return n1 - n2
#Mult
def multiply(n1, n2):
    return n1 * n2
#Div
def divide(n1, n2):
    if (n2 == 0 or n1 == 0):
        return 
    else:
        return n1 / n2
#Mod
def modulus(n1, n2):
    return n1%n2
#Power
def power(n1, n2):
    return n1 ** n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide,
  "%": modulus,
  "^": power
}

def calculator():
  flagrun = True
  while (flagrun):
    num1 = int(input("Enter your first number: "))
    print("Available Operations: ")
    j = 1
    for i in operations:
      print(f" {i} ")
      j += 1

    oper = input("Choose operand: ")
    num2 = int(input("Enter your second number: "))

    function = operations[oper]
    print(f"The result is: {num1} {oper} {num2} = {function(num1,num2)}")
    cheker = input("Want to continue: 'y' or 'n': ")
    if(cheker == 'y'):
      system('clear')
      calculator()
    else:
      flagrun = False
      system('clear')
  
calculator()

    
  


