'''glo_var = 167
def arithmetic_operation(num):
  """This function takes any number and does arithmetic operation on the number based on the value of the glo_var """
  print(glo_var + num)
  print(glo_var - num)
  print(glo_var * num)
  print(glo_var / num)

arithmetic_operation(106)

def operation_with_local_var(num):
    """This function takes any number and does arithmetic operation on the number based on the value of the glo_var """
    global local_var
    local_var = 57
    print(local_var + num)
    print(local_var - num)
    print(local_var * num)
    print(local_var / num)

operation_with_local_var(457)

def sum_num():
    #global local_var
    print(15 + local_var)
sum_num()
'''
from guess_number_logo import logo
from random import randint
def guess_number():
    #numbers = []
    attempts_dict = {'e': 10, 'h': 5} 
    #for i in range(1,101):
    #    numbers.append(i)
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty_level = input("Choose a difficulty level. Type 'e' for EASY or 'h' for HARD: ")
    if difficulty_level == 'e':
        attempts = attempts_dict['e']
        print(f"You have {attempts} attempts to guess the number")
    elif difficulty_level == 'h':
        attempts = attempts_dict['h']
        print(f"You have {attempts} attempts to guess the number")
    else:
        print("please type either 'e' for EASY or 'h' for HARD to choose a difficulty level")
    while difficulty_level != 'e' and difficulty_level != 'h':
        difficulty_level = input("Choose a difficulty level. Type 'e' for EASY or 'h' for HARD: ")
        if difficulty_level == 'e':
            attempts = attempts_dict['e']
            print(f'You have {attempts} attempts to guess the number')
        elif difficulty_level == 'h':
            attempts = attempts_dict['h']
            print(f"You have {attempts} attempts to guess the number")
    computers_guess = randint(1,100)
    #print(computers_guess)
    #print(attempts)
    users_guess = int(input("Make a guess: "))
    repeat = True
    while attempts != 0 and repeat:
        if users_guess < computers_guess:
            attempts -= 1
            attempts_left = attempts
            print("Too low.")
            print(f"You have {attempts_left} attempts remaining to guess the number.")
            if attempts == 0:
                repeat = False
            else:
                users_guess = int(input("Guess again: "))
        elif users_guess > computers_guess:
            attempts -= 1
            attempts_left = attempts
            print("Too high.")
            print(f"You have {attempts_left} attempts remaining to guess the number.")
            if attempts == 0:
                repeat = False
            else:
                users_guess = int(input("Guess again: "))
        elif users_guess == computers_guess:
            print(f"You got it! The answer is {users_guess}.")
            repeat = False
    if attempts == 0:
        print(f"You lose!The number is {computers_guess}.")
    response = input("Would you like to play again? Type 'y' for YES or 'n' for NO: ")
    if response == 'y':
        guess_number()
guess_number()
