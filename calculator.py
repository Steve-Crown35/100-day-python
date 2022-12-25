#This program is a simple calculator 
from calculator_logo import logo

#start out by creating functions that will carry out the basic arithmetic operations 
def sum(n1,n2):
    return n1 + n2
def difference(n1,n2):
    return n1 - n2
def product(n1,n2):
    return n1 * n2
def quotient(n1,n2):
    return n1 / n2

#Create a dictionary to store the operators as key and the function as value
operations = {
    "+" : sum,
    "-" : difference,
    "*": product,
    "/": quotient
}
#Create a variable to get the numbers
'''
num1 = int(input("Enter the first number: "))
for operator in operations:
    print(operator)
choose_operator = input("pick an operator from the line above: ")
num2 = int(input("Enter the second number: "))
operation_result = operations[choose_operator](num1, num2)

print(f"{num1} {choose_operator} {num2} = {operation_result}")
more_operation = input(f"Type 'y' to continue calculating with {operation_result}, or type 'n' to exit: ")

while more_operation == 'y':
    for operator in operations:
        print(operator)
    choose_operator = input("pick an operator from the line above: ")
    num2 = int(input("Enter the next number: "))
    num1 = operation_result #Use num1 to hold the last value of operation_result before a new 
    #operation_result value is created in the next line
    operation_result = operations[choose_operator](operation_result, num2)
    more_operation = input(f"Type 'y' to continue calculating with {operation_result}, or type 'n' to exit: ")
#final_result = operation_result
print(f"{num1} {choose_operator} {num2} = {operation_result}")
'''
def calculator():
    print(logo)
    num1 = float(input("Enter the first number: "))
    for operator in operations:
        print(operator)
    more_operations = True
    while more_operations:
        choose_operator = input("pick an operator from the line above: ")
        num2 = float(input("Enter the next number: "))
        operation_result = operations[choose_operator](num1, num2)
        print(f"{num1} {choose_operator} {num2} = {operation_result}")
        keep_calculating = input(f"Type 'y' to continue calculating with {operation_result} or type 'n' to exit: ")
        if keep_calculating == "y":
            num1 = operation_result
            for operator in operations:
                print(operator)
        else:
            more_operations = False
            calculator()
    print(f"{num1} {choose_operator} {num2} = {operation_result}")

calculator()