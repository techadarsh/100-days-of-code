#If Else

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!\n")
else:
    print(f"Sorry you have to grow taller {120-height} cm before you can ride\n")


print("let's check your water usage")
water_level = int(input("What is your water level? "))
water_level_limit = 50
if water_level <= water_level_limit:
    print("You are alright today.")
else:
    print("You are over spending water today.")


# Comparator Operators
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to