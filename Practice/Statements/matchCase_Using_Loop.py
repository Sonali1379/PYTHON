wanting = 'y'
while wanting!='n':
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter another number : "))
    choice = input("Enter choice (+, -, *, /) : ")
    match choice :
        case "+" :
            print(num1 + num2)
        case "-" :
            print(num1 - num2)
        case "*" :
            print(num1 * num2)
        case "/" :
            print(num1 / num2)
        case _ :
            print("Invalid choice")
    wanting = input("Do u want to continue ? y or n : ")