from blackjack_art import logo
import random
cards = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'King', 'Queen']
card_dict = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'King':10, 'Queen': 10}
#choose_card = random.choice(cards)
#print(choose_card)
#card_value = card_dict[choose_card]
#print(card_value)
def sum(list1):
    sum = 0
    for i in list1:
        sum += i
    return sum

def user_card():
    global user_hand 
    user_hand = []
    sum = 0
    while len(user_hand) < 2:
        choose_card = random.choice(cards)
        card_value = card_dict[choose_card]
        user_hand.append(card_value)
    for i in user_hand: 
        sum += i
    print(f"Your cards : {user_hand}, current score: {sum}")
    global users_sum
    users_sum = sum
    
#user_card()
#print(user_hand)
#print(users_sum)
def computers_card():
    global computers_hand
    computers_hand = []
    sum = 0
    while len(computers_hand) < 2:
        choose_card = random.choice(cards)
        card_value = card_dict[choose_card]
        computers_hand.append(card_value)
    for i in computers_hand: 
        sum += i
    print(f"Computer's first card: {computers_hand[0]}")
    global computers_sum
    computers_sum = sum
    
#computers_card()
#print(computers_hand)
#print(computers_sum)

reponse = input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ")
if reponse == 'y':
    print(logo)
    user_card()
    computers_card()
    reply = input("Type 'y' to get another card, type 'n' to check your bet: ")
    reply = True
    while reply:       
        choose_card = random.choice(cards)
        if choose_card == 'Ace' and users_sum > 10:
            card_value = 1
        else:
            card_value = card_dict[choose_card]
        user_hand.append(card_value)
        user_score = sum(user_hand)
        print(f"Your cards : {user_hand}, current score: {user_score}")
        choose_card = random.choice(cards)
        if choose_card == 'Ace' and computers_sum > 10:
            card_value = 1
        else:
            card_value = card_dict[choose_card]
        computers_hand.append(card_value)
        computers_score = sum(computers_hand)
        print(f"Computer's first card: {computers_hand[0]}")
        if user_score > 21:
            #print("This is a Bust. You loss! 😭")
            reply = False
        else:
            reply = print("Type 'y' to get another card, type 'n' to check your bet: ")
            if reply == 'n':
                reply = False
    while computers_score < 17: 
        choose_card = random.choice(cards)
        card_value = card_dict[choose_card]
        computers_hand.append(card_value)
        computers_score = sum(computers_hand)


    print(f"your total score is : {user_score}")
    print(f"computer's total score is : {computers_score}")
    if user_score > 21:
        print("This is a Bust. You loss! 😭")
    elif users_sum < computers_sum:
        print("You lose. 😭")
    elif users_sum == computers_sum:
        print("It's a Draw")
    else: 
        print("You won!😀")
else:
    print("Okay, no problem. Goodbye!")

    
