try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        raise ValueError("Invalid operator entered.")

    print(f"Result: {result}")

except ValueError:
    print("Error: Invalid input. Please enter numeric values and a valid operator.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
