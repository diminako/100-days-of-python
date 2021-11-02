import random

# random_integer = random.randint(0,1)
# if random_integer == 0:
#     print("Tails")
# else:
#     print("Heads")
# print(random_integer)

cars = ["Toyota", "Dodge", "VW", "Ford"]
random_integer = random.randint(0,len(cars) - 1)
print(cars[random_integer])


state_usa = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

state_usa.append("Puerto Rico")
print(state_usa[len(state_usa) - 1])

# testing extend
# state_usa.extend(["Dimitriville", "That's pretty neatville"])
# print(state_usa)

print(state_usa[random.randint(0, len(state_usa) - 1)])