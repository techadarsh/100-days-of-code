# The combination of the range() function with the Python For Loop allows us to run a loop for as many times as we wish. Instead of looping through each item in a List, we can loop through a range of numbers.
#
# Range Function
# range(1, 10)
#
# This code doesn't do anything by itself. For example, if you tried to print it, it would not give you individual numbers.
#
# But it can be used in conjunction with For Loops. e.g.
#
# for number in range(1, 10):
#     print(number)
# This will print out each of the numbers 1 - 9. So the range can also be expressed like this:
#
# a <= range(a, b) < b
#
# Where the range of numbers is inclusive of the lower bound but not inclusive of the upper bound.
#
# PAUSE 1 - The Gauss Challenge
# Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.

# range function
print(range(1,10))
# the range() function doesn't do anything by itself
# This function has been used in consumption of another function
# In our case it's going to be For Loop
for i in range(1,10): # this range function do include 1 bit not including 10
    print(i)

for i in range(1,10,2): # this will take starting point , end range, and then third parameter is interval
    print(i) # 1, 3, 5, 7, 9

# The Gauss Challenge
total_sum = 0
for i in range(1,101):
    total_sum += i

print(total_sum)

# FIZZ BUZZ game

for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)