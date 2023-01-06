from higher_lower_art import logo 
from higher_lower_art import versus
from random import randint
from higherlower_game_data import data
import os
correct_answer = '' #set the variable to empty first
score = 0 #track the score
numA = randint(0, 49) #pick a random integer
numB = randint(0, 49)#pick a random integer
while numA == numB:
    numB = randint(0, 49)
#print(num)
#print(data[num])
print(logo) #display the logo
play = True #create a flag for while loop
while play:
    print(f"Compare A : {data[numA]['name']}, {data[numA]['description']}, from {data[numA]['country']}.")#display account A
    #print(data[numA]['follower_count'])
    print(versus)
    print(f"Against B : {data[numB]['name']}, {data[numB]['description']}, from {data[numB]['country']}.")#display account B
    #print(data[numB]['follower_count'])
    number_of_A_followers = data[numA]['follower_count']#get the number of followers from account A
    number_of_B_followers = data[numB]['follower_count']#get the number of followers from account B
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    #Compare the number of followers
    if number_of_A_followers > number_of_B_followers:
        correct_answer = 'A'
    elif number_of_B_followers > number_of_A_followers:
        correct_answer = 'B'
    os.system('cls')
    print(logo)
    if answer == correct_answer:
        score += 1
        print(f"You're correct. Your current score is {score}.")
        numA = numB
        numB = randint(0,49)
        while numA == numB:
            numB = randint(0,49)
    else:
        print(f"Sorry, that's wrong. Your final score is {score}.")
        play = False