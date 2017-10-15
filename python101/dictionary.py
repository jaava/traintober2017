# create new dictionary.
moons_of_saturn = {'Mimas': 396, 'Enceladus': 504, 'Tethys': 1062,
                   'Dione': 1123, 'Rhea': 1527, 'Titan': 5150}
print(moons_of_saturn)

# Add new item to the dictionary
moons_of_saturn['Iapetus']= 1470
print(moons_of_saturn)

# Remove key-value pair from moons_of_saturn
del moons_of_saturn['Titan']

print(moons_of_saturn['Rhea'])
