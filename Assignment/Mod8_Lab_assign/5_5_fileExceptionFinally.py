file = None

try:
    filename = input("Enter file name to open: ")
    file = open(filename, "r")
    data = file.read()
    print("\nFile content:")
    print(data)

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied while opening the file.")
except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    if file is not None:
        file.close()
        print("\nFile closed successfully.")
