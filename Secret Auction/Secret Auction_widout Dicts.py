from os import system
from SA_Art import logo

print(logo)


flag = True

maxamt = 0
winnah = "_"

while(flag == True):
  nme = input("What is your name? : ")
  prc = int(input("What is your price($) : "))
  if prc>maxamt:
    maxamt = prc
    winnah = nme
  cher = input("Continue: y or n : ")
  if(cher == 'n'):
    flag = False
    print(f"The winner is: {winnah} with a bid of ($): {maxamt}")
  else:
    system('clear')
  



