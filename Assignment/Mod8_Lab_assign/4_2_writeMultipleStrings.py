lines = [
    "First line of text.\n",
    "Second line of text.\n",
    "Third line of text.\n"
]

with open("multipleStrings.txt", "w") as file:
    file.writelines(lines)

print("Multiple strings written to multipleStrings.txt successfully.")
