print("Welcome to the Treasure Island. Your mission is to find the hidden treasure that will make you the richest person in the world")
first_direction = input("Choose your direction. East, West or South\n")
first_direction = first_direction.lower()
if first_direction == "east":
    second_direction = input("Choose right or left")
    second_direction = second_direction.lower()
    if second_direction == "right":
        print("Wrong direction. Game Over!")
    elif second_direction == "left":
        get_to_island = input("How would you like to get to the island of great treasure? swim or wait for a boat\n")
        get_to_island = get_to_island.lower()
        if get_to_island == "swim":
            print("You have been terminated by a shark. Game over!")
        elif get_to_island == "wait for a boat":
            pick_a_color = input("choose a color. Red, Blue or Green")
            pick_a_color = pick_a_color.lower()
            if pick_a_color == "green":
                print("Big Congratulations. The treasure is yours. You won.")
            else:
                print("You lost. Please play again.")
        else:
            print("You entered the wrong expression. Game over!")
    else:
            print("You entered the wrong expression. Game over!")
elif first_direction == "south":
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
            direction = input("Pick a direction. Nortth or South\n")
            direction = direction.lower()
            if direction == "north":
                print("No treasure in this direction. You lost")
            elif direction == "south":           
                pick_a_color = input("choose a color. Red, Blue or Green")
                pick_a_color = pick_a_color.lower()
                if pick_a_color == "green":
                    print("Big Congratulations. The treasure is yours. You won.")
                else:
                    print("You lost. Please play again.")
        else:
            print("You entered the wrong expression. Game over!")
    else:
            print("You entered the wrong expression. Game over!")
else:
    print("Wrong direction. Game over!")

        
