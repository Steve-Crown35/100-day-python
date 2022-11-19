def prime_number_checker(number):
    num = []
    for i in range(1, number + 1):
        if number % i == 0:
            num.append(i)
    if len(num) == 2:
        print("it's a prime number")
    else:
        print("it's not a prime number")


n = int(input("Enter the number to check if it's a prime number\n"))
prime_number_checker(number = n)