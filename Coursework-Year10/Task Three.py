from random import randint
import time
global finished
global att
global character1
global character2
finished = False
att = ["Name", "Skill", "Strength"]
character1 = ["", 10, 10]
character2 = ["", 10, 10]
def block(x):
  time.sleep(x)
  print("====================================")
  time.sleep(1)
def dicethrows():
  global value
  global dice_six_c1
  global dice_six_c2
  dice_twelve = randint(1,12)
  dice_four = randint(1,4)
  dice_six_c1 = randint(1,6)
  dice_six_c2 = randint(1,6)
  value = round(int(dice_twelve) / int(dice_four))
def character_atts():
  dicethrows()
  character1[1] += int(value)
  dicethrows()
  character2[1] += int(value)
  dicethrows()
  character1[2] += int(value)
  dicethrows()
  character2[2] += int(value)
def rules():
  block(1)
  print("Welcome to the Player Game! \n The Rules are!")
  print("1. The Players both get a random skill and strength, if the user does not decide to enter it.")
  print("2. The difference between the Skills and Strengths is found out and divided by 5, to create the modifiers")
  print("3. The Players both roll a 6 sided dice.")
  print("4. The Player who gets the highest roll, gets the modifiers added to their score.")
  print("5. The Player with the lowest roll, gets their score decreased by the modifiers")
  block(20)
def print_c1():
  block(1)
  print("Character One")
  for i in range(0,3):
    print(att[i] + " = "  + str(character1[i]))
def print_c2():
  block(1)
  print("Character Two")
  for i in range(0,3):
    print(att[i] + " = " + str(character2[i]))
def run():
  rules()
  c1_name = input("Please input a name for character one : ")
  c2_name = input("Please input a name for character two : ")
  character_atts()
  character1[0] = c1_name
  character2[0] = c2_name
  input_own = input("Would you like to input your own stats for the two players? ")
  if input_own.upper() == "YES" or input_own.upper() == "Y":
    character1[1] = int(input("What will " + character1[0] + "'s skill be? "))
    character1[2] = int(input("What will " + character1[0] + "'s strength be? "))
    character2[1] = int(input("What will " + character2[0] + "'s skill be? "))
    character2[2] = int(input("What will " + character2[0] + "'s strength be? "))
  else:
    print("The stats have been randomly generated for you!")
  print_c1()
  print_c2()
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ABOVE SECTION IS GENERATING CHARACTER SKILL, STRENGTH AND NAMES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BELOW SECTION IS THE ENCOUTER OF THE PLAYERS IN GAME~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

def mods():
  global strength_mod
  global skill_mod
  strength_mod = round(abs(character1[2] - character2[2])/5)
  skill_mod = round(abs(character1[1] - character2[1])/5)
  if skill_mod < 2:
    skill_mod = randint(2,5)
  if strength_mod < 2:
    strength_mod = randint(2,5)

def check():
  global finished
  if character1[2] <= 0:
    character1[2] = 0
    block(1)
    print(character1[0] + " is dead!!")
    block(1)
    print(character2[0].upper() + " HAS WON WELL DONE!!!!!")
    finished = True
  elif character1[1] <= 0:
    character1[1] = 1
  elif character2[2] <= 0:
    character2[2] = 0
    block(1)
    print(character2[0] + " is dead!!")
    block(1)
    print(character1[0].upper() + " HAS WON WELL DONE!!!!!")
    finished = True
  elif character2[1] <= 0:
    character2[1] = 1

def encounter():
  global finished
  while finished == False:
    dicethrows()
    block(1)
    print(character1[0] + " rolled a, " + str(dice_six_c1))
    block(1)
    print(character2[0] + " rolled a, " + str(dice_six_c2))
    block(1)
    print("The Skill Modifier is " + str(skill_mod))
    print("The Strength Modifier is " + str(strength_mod))
    block(1)
    if dice_six_c1 > dice_six_c2:
      print(character1[0] + " rolled HIGHER than " + character2[0])
      print("Their Skill/Strength will now be increased!")
      print(character2[0] + "'s Skill/Strength will now be decreased!")
      character1[1] += skill_mod
      character1[2] += strength_mod
      character2[1] -= skill_mod
      character2[2] -= strength_mod
      block(1)
      print("The new scores are!")
      check()
      print_c1()
      print_c2()
    elif dice_six_c1 < dice_six_c2:
      print(character2[0] + " rolled HIGHER than " + character1[0])
      print("Their Skill/Strength will now be increased!")
      print(character1[0] + "'s Skill/Strength will now be decreased!")
      character2[1] += skill_mod
      character2[2] += strength_mod
      character1[1] -= skill_mod
      character1[2] -= strength_mod
      block(1)
      print("The new scores are!")
      check()
      print_c1()
      print_c2()
    else:
      print("Both rolled the same!! Keep Playing!")
  block(1)
  play_again = input("Would you like to play again? Yes or No - ")
  if play_again.upper() == "YES":
    finished = False
    start()
  else:
    print("Come again soon!")
    block(1)

def start():
  run()
  mods()
  encounter()

start()
