# traversal of a string sequence
planets = 'Planets'
for letter in planets:
    print('Letter : '+ letter)

# initialize length variable
length = 0      
for i in planets:
    # add 1 to the length on each iteration
    length += 1

print(len(planets) == length)
