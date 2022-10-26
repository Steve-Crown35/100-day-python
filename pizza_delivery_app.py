#This application helps buys to order pizza online
print('Welcome to Python Pizza Delivery!')
size = input("What size of pizza do you want? Small, Medium or Large\n")

add_pepperoni = input("Would you like to add pepperoni? Yes or No\n")

add_extra_cheese = input("Would you like to add extra cheese? Yes or No\n")


if size == "Small":
    bill = 15
elif size == "Medium":
    bill = 20
else:
    bill = 25

if add_pepperoni == "Yes" and add_extra_cheese == "No":
    if size == "Small":
        bill += 2
    else:
        bill += 3
    print(f"Your final bill is: ${bill}")
if add_pepperoni == "No" and add_extra_cheese == "Yes":
    bill += 1
    print(f"Your final bill is: ${bill}")
if add_pepperoni == "Yes" and add_extra_cheese == "Yes":
    if size == "Small":
        bill += 3
    else:
        bill += 4
    print(f"Your final bill is: ${bill}")
if add_pepperoni == "No" and add_extra_cheese == "No":
    bill = bill
    print(f"Your final bill is: ${bill}")