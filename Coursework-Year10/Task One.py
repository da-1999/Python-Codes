from random import randint
global running
running = True
print("Welcome to Dice Simulator!")
def simulating_dice():
  global running
  print("===========================================")
  sides = input("Would you like to simulate a 4, 6 or 12 sided dice? ")
  printtext = "You chose to roll a, " + str(sides) + " sided dice, and you rolled a, "
  if sides == "4":
    print(printtext + str(randint(0,4)))
  elif sides == "6":
    print(printtext + str(randint(0,6)))
  elif sides == "12":
    print(printtext + str(randint(0,12)))
  else:
    print("Please enter either 4, 6 or 12")
    simulating_dice()
def run_again():
  global running
  print("===========================================")
  again = input("Would you like to run the dice again? ")
  again = again.upper()
  if again == "YES" or again == "Y":
    running = True
  elif again == "NO" or again == "N":
    running = False
while running == True:
  simulating_dice()
  run_again()

