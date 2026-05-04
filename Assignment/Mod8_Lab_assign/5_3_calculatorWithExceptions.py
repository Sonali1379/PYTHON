try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")

    if op == "+":
        print(f"Result: {num1 + num2}")
    elif op == "-":
        print(f"Result: {num1 - num2}")
    elif op == "*":
        print(f"Result: {num1 * num2}")
    elif op == "/":
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Invalid operator.")

except ValueError:
    print("Error: Please enter valid numeric values.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
