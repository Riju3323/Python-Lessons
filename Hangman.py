import random
wordd_list = ["ardvark","baboon","camel"]
numrnndm = (random.randint(0,2))
wrddd = wordd_list[numrnndm]
compl = False
display = []
numchk = len(wrddd)
ercnt = 3

for i in wrddd:
  display += "_"

print(display)

while compl:
  letter = input("Guess a Letter: ").lower()
  for i in range(len(wrddd)):
    if letter == wrddd[i]:
      display[i]=letter
      numchk -= 1
    else:
      ercnt -= 1
      print("Chances Left: {ercnt}")
    if ercnt == 0:
      print("Game Over")
      compl = True
      break
    if numchk == 0:
      print("You Won")
      compl = True
      break      
  



      