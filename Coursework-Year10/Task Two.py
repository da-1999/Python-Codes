from random import randint
global att
global character1
global character2
att = ["Name", "Skill", "Strength"]
character1 = ["", 10, 10]
character2 = ["", 10, 10]
def dicethrows():
  dice_twelve = randint(1,12)
  dice_four = randint(1,4)
  global value
  value = round(int(dice_twelve) / int(dice_four))
def character_skill():
  global character1
  global character2
  global value
  dicethrows()
  character1[1] += int(value)
  dicethrows()
  character2[1] += int(value)
def character_strength():
  global character1
  global character2
  global value
  dicethrows()
  character1[2] += int(value)
  dicethrows()
  character2[2] += int(value)
def run():
  global character1
  global character2
  global att
  c1_name = input("Please input a name for character one : ")
  c2_name = input("Please input a name for character two : ")
  character_skill()
  character_strength()
  character1[0] = c1_name
  character2[0] = c2_name
  print("====================")
  print("Character One")
  for i in range(0,3):
    print(att[i] + " = "  + str(character1[i]))
  print("====================")
  print("Character Two")
  for i in range(0,3):
    print(att[i] + " = " + str(character2[i]))
def save_to_file():
  file = open("characters.txt", mode = 'w')
  file.write("====================\n")
  file.write("Character One\n")
  for i in range(0,3):
    file.write(att[i] + " = "  + str(character1[i]) + "\n")
  file.write("====================\n")
  file.write("Character Two\n")
  for i in range(0,3):
    file.write(att[i] + " = " + str(character2[i]) + "\n")
  file.write("====================\n")
  file.close()

run()
save_to_file()
