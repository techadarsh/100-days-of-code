# Multiple IFs
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12

    want_photo = input("Do you want to have a photo take? Type Y for yes and n for No.")
    if want_photo == "y":
        # Add $3 to bill
        bill += 3

    print(f"Your bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
