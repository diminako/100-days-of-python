# conditionals

# If / Else statement
print('Welcome to the Roller Coaster!')
height = int(input("What is your height?\n"))
if height >= 100:
    print('You may ride the roller coaster!')
else:
    print('Grow up kid!')
print('Neat!')

# Code Challenge Odd or even check
num = int(input('Please input a number... \n'))
if num % 2 == 0: # Modulo
    print(f'{num} is an even number!')
else:
    print(f'{num} is an odd number!')

# Nested if / else
print('Welcome to the Roller Coaster!')
height = int(input("What is your height?\n"))
if height >= 100:
    print('You may ride the roller coaster!')
    age = int(input('What is your age?'))
    if age <= 18:
        print('That will be $12.')
    else:
        print('That will be $20')
else:
    print('Grow up kid!')

# if / elif / else
print('Welcome to the Roller Coaster!')
height = int(input("What is your height?\n"))
if height >= 100:
    print('You may ride the roller coaster!')
    age = int(input('What is your age?'))
    if age < 12:
        print('That will be $5.')
    elif age <= 18:
        print('That will be $8')
    else:
        print('That will be $15')
else:
    print('Grow up kid!')
