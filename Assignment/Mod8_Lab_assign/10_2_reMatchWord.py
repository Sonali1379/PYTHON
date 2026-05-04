import re


def main():
    # re.match() checks only from the beginning of the string.
    line1 = "Python is easy to learn."
    line2 = "I enjoy Python every day."

    word = "Python"
    pattern = r"\b" + re.escape(word) + r"\b"

    m1 = re.match(pattern, line1)
    m2 = re.match(pattern, line2)

    if m1:
        print(f"line1: match at start — {m1.group()!r}")
    else:
        print("line1: no match at start")

    if m2:
        print(f"line2: match at start — {m2.group()!r}")
    else:
        print("line2: no match at start (word is not at the beginning)")


if __name__ == "__main__":
    main()
