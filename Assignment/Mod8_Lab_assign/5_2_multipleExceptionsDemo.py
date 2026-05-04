try:
    number = int(input("Enter an integer: "))
    divisor = int(input("Enter a divisor: "))

    result = number / divisor
    print(f"Division result: {result}")

    values = [10, 20, 30]
    index = int(input("Enter list index (0-2): "))
    print(f"Value at index {index}: {values[index]}")

except ValueError:
    print("Error: Please enter valid integer input.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except IndexError:
    print("Error: List index out of range.")
except Exception as e:
    print(f"Unexpected error: {e}")
