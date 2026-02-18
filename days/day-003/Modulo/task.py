# Modulo Operator

print(6%2)
print(10%3)
print(6%4)

number = int(input("Enter a number: "))
modular_operation = number % 2

if modular_operation == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# we can convert modular_operation in boolean
mod_op_bool = bool(modular_operation)

if mod_op_bool:
    print(f"{number} is odd via bool")
else:
    print(f"{number} is even via bool")
