"""
Functions terminate at the return keyword. If you write code below the return statement that code will not be executed.

However, you can have multiple return statements in one function. So how does that work?

Conditional Returns
When we have control flow, as in the code will behave differently (go down different execution paths)
depending on certain conditional checks, we can end up with multiple endings (returns).

e.g.

def canBuyAlcohol(age):
    if age >= 18:
        return True
    else:
        return False
Empty Returns
You can also write return without anything afterwards, and this just tells the function to exit.

e.g.

def canBuyAlcohol(age):
    # If the data type of the age input is not a int, then exit.
    if type(age) != int:
        return

    if age >= 18:
        return True
    else:
        return False
"""
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Enter Your Full Name"
    titled_name = f"{f_name} {l_name}".title()
    return titled_name


print(format_name(input("Enter your first name\n"), input("Enter your Last Name\n"))) # gives => Adarsh Sharma


