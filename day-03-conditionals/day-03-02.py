# Roller coaster pictures if statements
height = float(input("What is your height?..."))

if height > 99:
    age = int(input("Hop on!  Wait a second... how old are you?..."))
    if age < 12:
        print("That will be $5.")
        price = 5
    elif age < 18:
        print("That will be $7.")
        price = 7
    else:
        print("That will be $12.")
        price = 12
        
    want_photos = input("Do you want photos?... Y or N...")
    if want_photos == "Y":
        price += 3
    print(f'The total bill is ${price}')
else:
    print("Sorry you can't ride.")
    
# Pizza order program
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
price = 0

if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25

if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if extra_cheese == "Y":
    price += 1

print(f"The total for your pizze is {price}")
