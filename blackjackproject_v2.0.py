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
    while len(user_hand) < 2:
        choose_card = random.choice(cards)
        card_value = card_dict[choose_card]
        user_hand.append(card_value)
    user_hand_sum = sum(user_hand)
    print(f"Your cards : {user_hand}, current score: {user_hand_sum}")
    global users_sum
    users_sum = user_hand_sum
    
#user_card()
#print(user_hand)
#print(users_sum)
def computers_card():
    global computers_hand
    computers_hand = []
    while len(computers_hand) < 2:
        choose_card = random.choice(cards)
        card_value = card_dict[choose_card]
        computers_hand.append(card_value)
    computers_hand_sum = sum(computers_hand)
    print(f"Computer's first card: {computers_hand[0]}")
    global computers_sum
    computers_sum = computers_hand_sum
    
#computers_card()
#print(computers_hand)
#print(computers_sum)

reply = input("Would you like to play the Blackjack game? Type 'y' for YES or 'n' for NO: ")
if reply == 'y':
    print(logo)
    user_card()
    computers_card()
    response = input("Would you need more cards? Type 'y' for YES or 'n' for NO: ")
        
    if response == 'n':
        if users_sum > 21: 
            print("It's a Bust. You lost the Game.")
        else: 
            while computers_sum < 17: 
                choose_card = random.choice(cards)
                if choose_card == 'Ace' and users_sum > 10:
                    card_value = 1
                else:
                    card_value = card_dict[choose_card]
                    computers_hand.append(card_value)
                    computers_sum = sum(computers_hand)
            if users_sum <= 21 and computers_sum <= 21:
                if users_sum > computers_sum:
                    print(f"Your final hand is {user_hand}. Your total score is {users_sum}")
                    print(f"Computer's final hand is {computers_hand}. Computer's total score is {computers_sum}")
                    print("Congratulations. You won!")
                elif users_sum == computers_sum:
                    print(f"Your final hand is {user_hand}. Your total score is {users_sum}")
                    print(f"Computer's final hand is {computers_hand}. Computer's total score is {computers_sum}") 
                    print("It's a Draw!")
                else:
                    print(f"Your final hand is {user_hand}. Your total score is {users_sum}")
                    print(f"Computer's final hand is {computers_hand}. Computer's total score is {computers_sum}")
                    print("You lose!")
            else: 
                print(f"Your final hand is {user_hand}. Your total score is {users_sum}")
                print(f"Computer's final hand is {computers_hand}. Computer's total score is {computers_sum}")
                print("Congratulations. You won!")
    elif response == 'y':
        answer = True
        while response and answer:
            choose_card = random.choice(cards)
            if choose_card == 'Ace' and users_sum > 10:
                card_value = 1
            else:
                card_value = card_dict[choose_card]
            user_hand.append(card_value)
            user_total_score = sum(user_hand)
            print(f"Your cards : {user_hand}, current score: {user_total_score}")
            choose_card = random.choice(cards)
            if choose_card == 'Ace' and computers_sum > 10:
                card_value = 1
            else:
                card_value = card_dict[choose_card]
            computers_hand.append(card_value)
            computer_total_score = sum(computers_hand)
            print(f"Computer's first card: {computers_hand[0]}")
            response = input("Would you need more cards? Type 'y' for YES or 'n' for NO: ")
            if response == 'y':
                answer = True
            else:
                answer = False
        if user_total_score > 21: 
            print("It's a Bust. You lost the Game.")
        else:
            while computer_total_score < 17:
                choose_card = random.choice(cards)
                if choose_card == 'Ace' and users_sum > 10:
                    card_value = 1
                else:
                    card_value = card_dict[choose_card]
                computers_hand.append(card_value)
                computer_total_score = sum(computers_hand)
            if user_total_score <= 21 and computer_total_score <= 21:
                if user_total_score > computer_total_score:
                    print(f"Your final hand is {user_hand}. Your total score is {user_total_score}")
                    print(f"Computer's final hand is {computers_hand}. Computer's total score is {computer_total_score}")
                    print("Congratulations. You won!")
                elif user_total_score == computer_total_score: 
                    print(f"Your final hand is {user_hand}. Your total score is {user_total_score}")
                    print(f"Computer's final hand is {computers_hand}. Computer's total score is {computer_total_score}")
                    print("It's a Draw!")
                else:
                    print(f"Your final hand is {user_hand}. Your total score is {user_total_score}")
                    print(f"Computer's final hand is {computers_hand}. Computer's total score is {computer_total_score}")
                    print("You lose!")
            else: 
                print(f"Your final hand is {user_hand}. Your total score is {user_total_score}")
                print(f"Computer's final hand is {computers_hand}. Computer's total score is {computer_total_score}")
                print("Congratulations. You won!")
    else:
        print("Incorrect response. Please play again and make sure to enter the correct response : 'y' or 'n' ")

    
else: 
    print("Okay, No Problem. Goodbye!")

