from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

def calculate_by_if_condition(f,s,o):
    if o == "+":
        return add(f,s)
    elif o == "-":
        return subtraction(f,s)
    elif o == "*":
        return multiplication(f,s)
    elif o == "/":
        return division(f,s)
    else:
        print("Invalid Operation")

continue_calculation = True
final_result = 0
operation_dictionary = {
    "+": add,
    "-": subtraction,
    "*": multiplication,
    "/": division
}
while continue_calculation:
    first_number = float(input(" What's the first number?: ")) if not final_result else final_result
    operation_type = input("\n + \n - \n * \n / \n Pick an Operation:  ")
    second_number = float(input("What's the next number?: "))
    # approach 1
    # final_result = calculate_by_if_condition(first_number,second_number,operation_type)

    # approach 2
    final_result = operation_dictionary[operation_type](first_number, second_number)

    print(f"{first_number} {operation_type} {second_number} = {final_result}")
    con_cal = input(f"\n Type 'y' to continue calculating with {final_result}, \n or type 'n' to start a new calculation,"
                    f"\n or type 'c' for close the calculator: ").lower()
    if con_cal == "n":
        final_result = 0
    elif con_cal == "c":
        continue_calculation = False
    elif con_cal == "y":
        continue_calculation = True

# Approach 2 => using dictionary


