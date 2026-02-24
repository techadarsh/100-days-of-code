"""
The first step of solving a problem is being able to describe the problem.

PAUSE 1
Look at the code in task.py and answer the following questions:

What is the for loop doing?
When is the function meant to print "You got it"?
What are your assumptions about the value of i?
PAUSE 2
Fix the code so that the print statement executes.
"""
# Debugging
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# => for loop will iterate 19 times from 1 to 19 and if condition is set to check if i == 20 which is never gonna happen
# 2. When is the function meant to print "You got it"?
# => Function mean to print You got it when i becomes 20 but in this scenario this is not possible
# 3. What are your assumptions about the value of i?
# => I will start from 1 and ends on 19
