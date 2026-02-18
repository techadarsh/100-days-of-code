# TypeError
# These errors occur when you are using the wrong data type. e.g. len(12345)
#
# Because you can only give the len() function Strings, it will refuse to work and give you a TypeError if you give it a number (Integer).
#
# PAUSE 1. Fix the len() function so it has no more warnings or errors.
# Type Checking
# You can check the data type of any value or variable in python using the type() function.
#
# print(type("abc")) #will give you <class 'str'>
#
# PAUSE 2. Write out 4 type checks to print all 4 data types
# Using the type() and print() functions to print out 4 lines into the output area so we get the full collection of data types that we learnt about. <class 'str'> <class 'int'> <class 'float'> and <class 'bool'>
#
# Type Conversion
# You can convert data into different data types using special functions. e.g.
#
# float()
#
# int()
#
# str()
#
# PAUSE 3. Make this line of code run without errors
# print("Number of letters in your name: " + len(input("Enter your name")))


print(len("12345"))


# How to get the data type of anything in python
# Type Checking
print(type("Hello World")) # will give <class 'str'>
print(type(123)) # will give <class 'int'>
print(type(12_323_344.343)) # will give <class 'float'>
print(type(True)) # will give <class 'bool'>

# Type Conversion
str()
int()
float()
bool()

print("123" + "345")
print(int("123") + int("345"))

# Exercise Problem:
#print("Number of letters in your name: " + len(input("Enter your name")))
print("Number of letters in your name: " + str(len(input("Enter your name"))))