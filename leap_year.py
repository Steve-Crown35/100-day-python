year = int(input("Enter a year\n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")