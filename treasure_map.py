
a = ['🔛', '🔝', '🔜']
b = ['🟠', '🟡', '🟢']
c = ['❎', '🌐', '💠']

map = [a, b, c]
print(f'{a}\n{b}\n{c}')
position = input("Where would you like to put the treasure? Enter any 2 digit numbers formed by combining numbers between 1 and 3\n")
vertical = int(position[0])
horizontal = int(position[1])
map[horizontal-1][vertical-1] = 'X'

print(f'{a}\n{b}\n{c}')