import random
#test_seed = int(input("create a seed number: "))
#random.seed(test_seed)

names = input("Give me the list of names with each name seperated by a comma\n")

#split the names using a comma as a seperator
names = names.split(',')
number_of_names = len(names)
random_index = random.randint(0, number_of_names-1)
random_name = names[random_index]
print(f"{random_name} is going to buy the meal today!")