name = "John Perry"
age = 75

print(name == "John Perry" and age != 57)
print(name == "John Scalzi" and age == 75)

print(name == "John Perry" or age != 57)
print(name == "John Scalzi" or age == 75)

print(name == "John Perry" or not age > 57)
print(name == "John Scalzi" or not (name == "John Perry" and age == 75))