print("Welcome to the tip calculator")
total_bill = float(input("What is the total bill? "))
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
percent_tip = (total_bill/100 ) * percent_tip
final_bill = total_bill + percent_tip
num_of_people = int(input("How many people would you like to split the bill? "))
bill_split = round(final_bill/num_of_people, 2)

print(f"Each person should pay: ${bill_split}")