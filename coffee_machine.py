resources = {'water': 300, 'milk': 200, 'coffee': 100, 'money': 0}
drinks = [{'name': 'espresso', 'resources': {'water': 50, 'coffee': 18}, 'cost': 1.50},
          {'name': 'latte', 'resources': {'water': 200, 'coffee': 24, 'milk': 150}, 'cost': 2.50},
          {'name': 'cappuccino', 'resources': {'water': 250, 'coffee': 24, 'milk': 100}, 'cost': 3.00}]

# TODO: 1. Ask the buyer what drink they need
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
money = resources['money']

buy = True
while buy:
    response = input("What would you like? (espresso/latte/cappuccino/report): ").lower()

    if response == 'report':
        print(f"water: {water}ml\nmilk: {milk}ml\ncoffee: {coffee}g\nmoney: ${money}")
        buy = False
    # TODO: 2. Ask the buyer to insert their coins
    else:
        print("Please insert coins.")
        quarter_coin = float(input("how many quarters?: "))
        dime_coin = float(input("how many dimes?: "))
        nickle_coin = float(input("how many nickles?: "))
        penny_coin = float(input("how many pennies?: "))
        coins = (0.25 * quarter_coin) + (0.10 * dime_coin) + (0.05 * nickle_coin) + (0.01 * penny_coin)

        # TODO: 3. check that resources for the drink are sufficient and that the money inserted is sufficient for
        #  the drink
        if response == 'espresso':
            cost = drinks[0]['cost']
            change = round((coins - cost), 2)
            if water >= 50 and coffee >= 18 and coins >= cost:
                print(f'Here is ${change} in change')
                print('Here is your Espresso ☕. Enjoy!')
                water -= 50
                coffee -= 18
                money += 1.50
                # print(f"water: {water}ml\nmilk: {milk}ml\ncoffee: {coffee}g\nmoney: ${money}")
            elif coins < cost:
                print(f"Insufficient fund. Take back your coins and Insert up to ${cost} to get the drink.")
            else:
                if water < 50:
                    print("There's insufficient water for this drink. Please take back your coins and check back later.")
                elif coffee < 18:
                    print("There's insufficient coffee for this drink. Please take back your coins and check back later.")
                buy = False
        elif response == 'latte':
            cost = drinks[1]['cost']
            change = round((coins - cost), 2)
            if water >= 200 and coffee >= 24 and milk >= 150 and coins >= cost:
                print(f'Here is ${change} in change')
                print('Here is your Latte ☕. Enjoy!')
                water -= 200
                coffee -= 24
                milk -= 150
                money += 2.50
                # print(f"water: {water}ml\nmilk: {milk}ml\ncoffee: {coffee}g\nmoney: ${money}")
            elif coins < cost:
                print(f"Insufficient fund. Insert up to ${cost} to get the drink.")
            else:
                if water < 200:
                    print("There's insufficient water for this drink. Please take back your coins and check back later.")
                elif milk < 150:
                    print("There's insufficient milk for this drink. Please take back your coins and check back later.")
                elif coffee < 24:
                    print("There's insufficient coffee for this drink. Please take back your coins and check back later.")
                buy = False
        elif response == 'cappuccino':
            cost = drinks[2]['cost']
            change = round((coins - cost), 2)
            if water >= 250 and coffee >= 24 and milk >= 100 and coins >= cost:
                print(f'Here is ${change} in change.')
                print('Here is your cappuccino ☕. Enjoy!')
                water -= 250
                coffee -= 24
                milk -= 100
                money += 3.00
                # print(f"water: {water}ml\nmilk: {milk}ml\ncoffee: {coffee}g\nmoney: ${money}")
            elif coins < cost:
                print(f"Insufficient fund. Please take back your coins and insert up to ${cost} to get the drink.")
            else:
                if water < 250:
                    print("There's insufficient water for this drink. Please take back your coins and check back later.")
                elif milk < 100:
                    print("There's insufficient milk for this drink. Please take back your coins and check back later.")
                elif coffee < 24:
                    print("There's insufficient coffee for this drink. Please take back your coins and check back later.")
                buy = False

# TODO: 5. compute the users change and serve the drink

# TODO: 6. Ask the buyer what drink they need again


# TODO: 2. check that resources for the drink are sufficient

# TODO: 3. Ask the buyer to insert their coins

# TODO: 4. check that the money is sufficient for the drink

# TODO: 5. compute the users change and serve the drink
