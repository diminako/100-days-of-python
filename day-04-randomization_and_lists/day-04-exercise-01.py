# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

rando = random.randint(0, len(names) - 1)

print(f"{names[rando]} is going to buy the meal today.")
