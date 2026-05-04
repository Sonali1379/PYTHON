import re


def main():
    text = "Learning Python is fun. Python is powerful."
    word = "Python"

    pattern = r"\b" + re.escape(word) + r"\b"
    match = re.search(pattern, text)

    if match:
        print(f"Found '{word}' at index {match.start()}–{match.end()}: {match.group()!r}")
    else:
        print(f"Word '{word}' not found.")


if __name__ == "__main__":
    main()
