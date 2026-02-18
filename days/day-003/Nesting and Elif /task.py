# Nesting and ELif
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    if age >= 18:
        price = 12
    elif age >= 12:
        price = 7
    else:
        price = 5
    print(f"your ticket price is ${price}")
else:
    print("Sorry you have to grow taller before you can ride.")
