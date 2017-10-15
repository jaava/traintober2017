names = ['Alice', 'John', 'Dave', 'Lisa', 'Matthew'] # create new list
print(names)

names[1:3] = ['Amy']    # replace 2 items 'John' and 'Dave' with 'Amy'
print(names)

names[1:3] = []     # remove 2 items 'Amy' and 'Lisa'
print(names)

names[0:] = [] #Clear List Items
print(names)
