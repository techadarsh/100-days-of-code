"""
Multiple Inputs
You can have multiple inputs in functions. All you need to do is separate them with a comma ,.

PAUSE 1
Create a function with multiple inputs

 Hint 1
PAUSE 2
Modify the function so that it prints the expected values.

def greet_with(name, location)
    Hello name
    What is it like in location
Positional Arguments
By default, when you create a function in Python, it will keep the order of arguments in the function definition.

e.g. In the function below, the first argument that goes in will always be printed before the second one. a = 2, b = 1

def my_function(a, b)
  print(a)
  print(b)

 my_function(2, 1)
 #It will print:
 # 2
 # 1
Keyword Arguments
You can use keywords when you provide the arguments when you call a function so that there is less confusion which value is assigned to which input parameter.

PAUSE 3
Call the greet_with() function using keyword arguments.
"""
# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

def greet_with(name, location):
    print(f"Hello {name}, what is it like in {location}")

greet_with("Adarsh Sharma", "India") # Provisional Arguments
greet_with("India","Adarsh")

greet_with(location="India", name="Adarsh Sharma") # Keyword Arguments
