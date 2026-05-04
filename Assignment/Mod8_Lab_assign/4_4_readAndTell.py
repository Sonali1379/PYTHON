with open("myfile.txt", "r") as file:
    start_pos = file.tell()
    print(f"Cursor position before reading: {start_pos}")

    data = file.read()
    print("\nFile data:")
    print(data)

    end_pos = file.tell()
    print(f"\nCursor position after reading: {end_pos}")
