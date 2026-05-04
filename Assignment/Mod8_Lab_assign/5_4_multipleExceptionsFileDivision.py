try:
    filename = input("Enter file name to open: ")
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile content:")
        print(content)

    num = float(input("\nEnter a number: "))
    divisor = float(input("Enter divisor: "))
    result = num / divisor
    print(f"Result of division: {result}")

except FileNotFoundError:
    print("Error: File not found.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid numeric input.")
except Exception as e:
    print(f"Unexpected error: {e}")
