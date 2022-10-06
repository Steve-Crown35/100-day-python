print("2000 is a great number")

calculation_to_units = 24
name_of_unit = "hours"
#print(f"50 days has {50 * calculation_to_units} {name_of_unit}")
#print(f"100 days has {100 * calculation_to_units} {name_of_unit}")
#print(f"150 days has {150 * calculation_to_units} {name_of_unit}")


def daysTounits(days):
    print(f"{days} days has {days * calculation_to_units} {name_of_unit}")

daysTounits(50)
daysTounits(100)
daysTounits(150)
daysTounits(228)