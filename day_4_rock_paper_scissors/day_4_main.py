import random
List_1 = ["rock","paper","scissors"]
rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
user_choice = int(input("Choose one: 0 for rock, 1 for paper, 2 for scissors\n: "))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("No valid choice")

computer_choice = random.randint(0,2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if user_choice<0 or user_choice>2:
    print("LOSE BY FORFEIT")
elif user_choice == computer_choice:
    print("DRAW")
elif List_1[computer_choice-1] == List_1[user_choice]:
    print("YOU LOSE")
elif List_1[user_choice] == List_1[computer_choice-2]:
    print("YOU WIN")

