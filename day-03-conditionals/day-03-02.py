# Picking back up after working hiatus.  :)
# num = int(input("Input a number "))
# if num % 2 == 0:
#     print("Your num is even")
# else:
#     print("Your num is odd.")
    
# age = int(input("What is your age? - "))
# if age > 17:
#     print("Step up and we will check your height.")
#     height = int(input("What is your height? - "))
#     if height > 100:
#         print("hop on and buckle up!")
#     else:
#         print("maybe try the kiddy rides shorty.")
# else:
#     print("Come back when your old enough.")

# new_age = int(input("What is your age? - "))
# if new_age > 17:
#     print("That will be $10.")
# elif new_age > 12:
#     print("That will be $5.")
# elif new_age < 12:
#     print("This is free.")
    
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / (height**2))
print("You BMI is " + str(bmi))
if bmi > 35:
    print("You are clinically obese.")
elif bmi > 30:
    print("You are obese.")
elif bmi > 25:
    print("You are overweight.")
elif bmi > 18.5:
    print("You are a normal BMI.")
else:
    print("You are underweight.")
    
