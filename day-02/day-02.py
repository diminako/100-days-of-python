# Data Type's

# String
print("Hello"[3])
print("123"[1])
print("123"+"345")

# Integer
print(123+1_345)

# floats
print(3.14159)

# Boolean
print(True)

# casting
num_char = len(input("Gimme a num "))
print(type(num_char))
str_num_char = str(num_char)
print("Cool you converted '" + str_num_char + "' into a string.")
print(70 + float("100.5"))

# Exercise.  add the two numbers given by the input.
nums = input("Input a two digit number ")
first_num = int(nums[0])
second_num = int(nums[1])

print(first_num + second_num)

# Operators
print(7-3)
print(7*3)
print(2+1)
print(int(6/3))
print(2**3)
# PEMDAS L->R
print(int(3*3+3/3-3))

# BMI Exercise challenge
weight = input("How much do you weigh in kg? ")
height = input("How tall are you in m? ")
bmi = int(weight) / (float(height) ** 2)
print(float(bmi))

# round numbers
print(round(8/3)) # 3
print(round(8/3, 3)) # 2.667

# floor division
print(8 // 3)


result = 4/2
result /= 2
print(result)

# f string
score = 0
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

# Exercise your life in weeks
age = int(input("What is your current age?"))
days = str(age*365)
weeks = str(age*52)
months = str(age*12)
message = f'You have {days} days, {weeks} weeks, and {months} months left until 90.'
print(message)

# Exercise

print('Welcome to the Tip Calculator :)')
# get the total bill
total = float(input('How much was the total bill? \n$'))
# how many people
people_paying = int(input('How many people are you splitting the bill up with? \n'))
# what percentage tip
tip_amount = input('How much percentage do you want to tip? \n')
tip_percentage = float(("1." + tip_amount))
# total owed by each person rounded up
message = f'Your total bill was ${str(total)} split between {str(people_paying)} people with a tip of {str(tip_amount)}% \nso you owe: ${str(round((total / people_paying)*(tip_percentage), 2))}'

print(message)
