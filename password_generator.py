from select import select
import string
import random
letters = list(string.ascii_letters)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '^', '*', '(', ')', '_', '+', '=', '<', '>', '?']


print("Welcome to the PyPassword Generator!")
number_of_letters = int(input("How many letters would you need in your password?\n"))
number_of_symbols = int(input("How many symbols would you need in your password?\n"))
num = int(input("How many numbers would you need in your password?\n"))
password_bank = []
for letter in range(number_of_letters):
    random_letter = random.choice(letters)
    password_bank.append(random_letter)
for symbol in range(number_of_symbols):
    random_symbol = random.choice(symbols)
    password_bank.append(random_symbol)
for number in range(num):
    random_number = random.choice(numbers)
    password_bank.append(random_number)
#print(password_bank)
generated_password = " "
while len(password_bank) != 0:
    random_select = random.choice(password_bank)
    generated_password += random_select
    password_bank.remove(random_select)
  


print(generated_password)