# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
name = list(name1+name2)
true = list('true')
love = list('love')
count_true = 0
count_love = 0
for i in name:
    if i in true:
        count_true += 1
for i in name:
    if i in love:
        count_love += 1
count_true = str(count_true)
count_love = str(count_love)
love_score = int(count_true + count_love)
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

