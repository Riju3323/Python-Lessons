from os import system
from SA_Art import logo
print(logo)

participants = {}
flag = False

def find_highestbidder(temp):
  maxamt = 0
  winner = ""
  for bidder in temp:
    amt = temp[bidder]
    if amt > maxamt: 
      maxamt = amt
      winner = bidder
  print(f"The winner is {winner} with a bid of ${maxamt}")

while not flag:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  participants[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    flag = True
    find_highestbidder(participants)
  elif should_continue == "yes":
    system('clear')