import random

rock = ''' 

  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''

   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

sissor = '''

   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
images = [rock,paper,sissor]
user = int(input("entr 0 for rock, 1 for paper , 2 for sissor\n"))
print(images[user])

computer_choose= random.randint(0,2)
print("computer choose:")
print(images[computer_choose])

if user == 0 and computer_choose == 0:
  print("game draw")
elif user == 1 and computer_choose == 1:
  print("draw")
elif user == 2 and computer_choose == 2:
  print("draw")
elif user == 0 and computer_choose == 1:
  print("u win")
elif user == 0 and computer_choose == 2:
  print("u win")
elif user == 2 and computer_choose == 1:
  print("u win")
elif user == 1 and computer_choose == 2:
  print("u lose")
elif user == 1 and computer_choose == 0:
  print("u lose")
else:
    print("u lose")