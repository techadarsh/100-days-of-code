"""
We've seen functions with only an execution body, functions with inputs that allow for variation in execution
of the function body and now we'll see the final form of functions. Functions that can have outputs.

PAUSE 1
Create a function called format_name() that takes two inputs: f_name and `l_name'.

PAUSE 2
Use the title() function to modify the f_name and l_name parameters into Title Case.

Syntax
You can create a function with a body, input and output like this:

def function_name(input_parameter):
    <body of function that uses input_argument>
    return output
Print vs. Output
Return vs. Display: The return statement is used to give back a value from a function, which can be used later,
while print is used to display a value to the console only for the programmer to see.
"""

def my_function():
    result = 3 * 2
    return result

print(my_function()) # gives => 6

def format_name(f_name, l_name):
    titled_name = f"{f_name} {l_name}".title()
    return titled_name

print(format_name("ADARSH", "sharma")) # gives => Adarsh Sharma

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

print(function_1("hello"))
print(function_2("hello"))
