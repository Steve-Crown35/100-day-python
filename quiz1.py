from cgitb import reset


output = len('95637+12')
print(f'the ouput of the code is : {output}')



score = 67 
if score < 80 and score > 70:
    print("A")
elif score < 90 or score > 80:
    print("B")
elif score > 60 : 
    print("C")
else: 
    print("D")


def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return outer_function(a, b)

result = outer_function(5,10)
print(result)