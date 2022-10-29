




print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')



print("Welcome to the Treasure Island. Your mission is to find the hidden treasure that will make you the richest person in the world.")
first_direction = input("Choose your direction. East, West or South\n")
first_direction = first_direction.lower()
if first_direction == "east":
    second_direction = input("Choose right or left\n")
    second_direction = second_direction.lower()
    if second_direction == "right":
        print("Wrong direction. Game Over!")
    elif second_direction == "left":
        get_to_island = input("How would you like to get to the island of great treasure? swim or wait for a boat\n")
        get_to_island = get_to_island.lower()
        if get_to_island == "swim":
            print("You have been terminated by a shark. Game over!")
        elif get_to_island == "wait for a boat":
            pick_a_color = input("choose a color. Red, Blue or Green\n")
            pick_a_color = pick_a_color.lower()
            if pick_a_color == "green":
                print("Big Congratulations. You found the treasure. You won.")
            else:
                print("It's a room full of beast. Game over! Please play again.")
        else:
            print("You entered the wrong expression. Game over!")
    else:
            print("You entered the wrong expression. Game over!")
elif first_direction == "south":
    print("This direction has a longer route to the treasure island but you can still get there if you do not give up along the way.")
    movement = input("How would you like to proceed? walk or run\n")
    movement = movement.lower()
    if movement == "walk":
        print("Wrong choice of movement. Game over!")
    elif movement == "run":
        food_choice = input("Choose your meal. Rice or Beans?\n")
        food_choice = food_choice.lower()
        if food_choice == "rice":
            print("Not the right meal to eat for a walk across the desert. Game over!")
        elif food_choice == "beans":
            direction = input("Pick a direction. North or South\n")
            direction = direction.lower()
            if direction == "north":
                print("No treasure in this direction. You lost")
            elif direction == "south":           
                pick_a_color = input("choose a color. Red, Blue or Green\n")
                pick_a_color = pick_a_color.lower()
                if pick_a_color == "green":
                    print("Big Congratulations. You found the treasure. You won.")
            else:
                print("It's a room full of beast. Game over! Please play again.")
        else:
            print("You entered the wrong expression. Game over!")
    else:
            print("You entered the wrong expression. Game over!")
else:
    print("Wrong direction. Game over!")

        
