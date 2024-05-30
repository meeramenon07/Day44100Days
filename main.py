
import random, os, time
#import getpass
#from getpass import getpass as input

bingoCard = []

def randomNumber():
  number = random.randint(1,90)
  return number

def prettyPrint():
  for row in bingoCard:
    for item in row:
      print(item, end="\t|\t")
    print()

def createCard():
  global bingoCard
  numbers = []
  for i in range(8):
    numInput = randomNumber()
    while numInput in numbers:
      numInput = randomNumber()
    numbers.append(randomNumber())

  numbers.sort()

  bingoCard = [ [ numbers[0],numbers[1], numbers[2]],[ numbers[3], "BG", numbers[4] ], [ numbers[5], numbers[6], numbers[7]] ]

createCard()
while True:
  prettyPrint()
  numInput = int(input("Next Number: "))
  for row in range(3):
    for item in range(3):
      if bingoCard[row][item] == numInput:
        bingoCard[row][item] = "X"

  number_of_X = 0
  for row in bingoCard:
    for item in row:
      if item=="X":
        number_of_X +=1

  if number_of_X == 8:
    print("You have won")
    break

  time.sleep(1)
  os.system("clear")





























































