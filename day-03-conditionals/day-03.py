# conditionals

# If / Else statement
print('Welcome to the Roller Coaster!')
height = int(input("What is your height?\n"))
if height >= 100:
    print('You may ride the roller coaster!')
else:
    print('Grow up kid!')
print('Neat!')

print('----------------------')

# Code Challenge Odd or even check
num = int(input('Please input a number... \n'))
if num % 2 == 0: # Modulo
    print(f'{num} is an even number!')
else:
    print(f'{num} is an odd number!')

print('----------------------')

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

print('----------------------')

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

print('----------------------')

# For Loop for string
name= "Dimitri"
def hello(name):
    for i in name:
        print(i)

hello(name)

print('----------------------')

# BMI 2.0 Exercise
height = float(input("What is your height in m? "))
weight = float(input("What is you weight in k? "))
bmi = round(float(weight / height ** 2), 3)

if bmi <= 18:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <= 22:
    print(f"Your BMI is {bmi}, you are normal weight.")
elif bmi <= 28:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <= 33:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


print('----------------------')

# Leap year exercise
year = int(input("What year is it? "))
leap = "leap year"
not_leap = "not a leap year"

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            year = leap
        else:
            year = not_leap
    else:
        year = leap
else:
    year = not_leap
print(year)
        