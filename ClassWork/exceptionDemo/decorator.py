def number(func):
    def exec(value):
        if not str(value).isdigit():
            print("Invalid number")
        else:
            print("value")
    return exec


def char(func):
    def exec(value):
        if not str(value).isalpha():
            print("Invalid character")
        else:
            print("value")    
    return exec
@number
def get(value):
    print(value)
get("scd")
