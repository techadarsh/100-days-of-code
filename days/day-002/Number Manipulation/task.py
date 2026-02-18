# Flooring a Number
# You can floor a number or remove all decimal places using the int() function which converts a floating point number (with decimal places) into an integer (whole number).
#
# int(3.738492) # Becomes 3
#
# Rounding a Number
# However, if you want to round a decimal number to the nearest whole number using the traditional mathematical way, where anything over .5 rounds up and anything below rounds down. Then you can use the python round() function.
#
# round(3.738492) # Becomes 4
#
# round(3.14159) # Becomes 3
#
# round(3.14159, 2) # Becomes 3.14
#
# Assignment Operators
# Assignment operators such as the addition assignment operator += will add the number on the right to the original value of the variable on the left and assign the new value to the variable.
#
# +=
#
# -=
#
# *=
#
# /=
#
# f-Strings
# In Python, we can use f-strings to insert a variable or an expression into a string.
#
# age = 12
#
# print(f"I am {age} years old")
#
# # Will output I am 12 years old.


# Number Manipulation
# exercise
bmi = 84 / 1.65 ** 2
print(bmi) #30.85399449035813

print(int(bmi)) # 30

#Rounding a Number
print(round(bmi)) # 31

print(round(bmi, 3)) # 30.854
print(round(bmi, 2)) # 30.85
print(round(bmi, 1)) # 30.9

# assignment Operators
# +=
# -=
# *=
# /=

age = 10
age += 5
print(age) # gives us 15
age -= 5
print(age) # gives us 10
age *= 5
print(age) # gives us 50
age /= 5
print(age) # gives us 10.0


#f-Strings
# In Python, we can use f-strings to insert a variable or an expression into a string.
print(f"I am {int(age)} years old")

score = 0
height = 1.6
is_winning = True

print(f"Your Score is = {score}, your height is {height} and your height is {height}")

