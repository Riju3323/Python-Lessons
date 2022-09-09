import random
from os import system
from art import logo

def numgame():
  print(logo)
  check = True
  while check==True:
    print("Welcome to the Number Guessing Game:")
    diff = input("Choose a difficulty level: 'easy' or 'hard':\n")
    if diff=="easy":
      life=10
    else:
      life=5
    nmbr = random.randint(0,100)
    while life>=0:
      print(f"Guesses Remaining: {life} ")
      usin = int(input("Enter a number: "))
      if usin == nmbr:
        print("You won!!")
      elif usin>nmbr:
        print("Too high!!")
        life -= 1
        # print(f"Guesses Remaining:{life}")
      elif usin<nmbr:
        print("Too low!!")
        life -= 1
        # print(f"Guesses Remaining:{life}")
      elif life==0:
        print("You ran out of Guesses!! Try Again")
    flag = input("Go Again: 'Y' or 'N': ")
    if flag == 'Y':
      system('clear')
      numgame()
    else:
      check = False

numgame()