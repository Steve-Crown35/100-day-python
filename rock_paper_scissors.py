rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random
art = [rock, paper, scissors]
pick_number = int(input("Choose a number. Type 0 for rock, 1 for paper or 2 for scissors\n"))
if pick_number == 0:
    print(rock)
    random_index = random.randint(0,2)
    print("Computer chose : ")
    computer_choice = art[random_index]
    print(computer_choice)

    if pick_number == 0 and random_index == 2:
        print("Rock wins against scissors. You won! 👏")
    elif pick_number == 0 and random_index == 1:
        print("Rock loses against paper. You Lost! 😭")
    else: 
        print("It's a tie. Please play again.")
elif pick_number == 1: 
    print(paper)
    random_index = random.randint(0,2)
    print("Computer chose : ")
    computer_choice = art[random_index]
    print(computer_choice)
    if pick_number == 1 and random_index == 0:
        print("Paper wins against rock. You won! 👏")
    elif pick_number == 1 and random_index == 2:
        print("Paper loses against scissors. You Lost! 😭")
    else: 
        print("It's a tie. Please play again.")
elif pick_number == 2:
    print(scissors)
    random_index = random.randint(0,2)
    print("Computer chose : ")
    computer_choice = art[random_index]
    print(computer_choice)
    if pick_number == 2 and random_index == 0:
        print("Scissors loses against rock. You Lost! 😭")
    elif pick_number == 2 and random_index == 1:
        print("Scissors wins against paper. You won! 👏")
    else: 
        print("It's a tie. Please play again.")
else: 
    print("You entered the wrong input. Please enter a number between 0 and 2")


