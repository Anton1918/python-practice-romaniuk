print("Romaniuk Anton, IT-32")

first_number = float(input("Enter first number: "))
operator = input("Enter operator: ")
second_number = float(input("Enter second number: "))

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number == 0:
        print("Error: division by zero")
        result = None
    else:
        result = first_number / second_number
elif operator == "//":
    if second_number == 0:
        print("Error: division by zero")
        result = None
    else:
        result = first_number // second_number
elif operator == "%":
    if second_number == 0:
        print("Error: division by zero")
        result = None
    else:
        result = first_number % second_number
elif operator == "**":
    result = first_number ** second_number
else:
    print("Unknown operator")
    result = None

if result is not None:
    print(f"{first_number} {operator} {second_number} = {result:.4f}")