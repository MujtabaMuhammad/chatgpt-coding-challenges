# Create a program that asks the user for two numbers and an arithmetic operation (+, -, *, /) and prints the result.
def arthematic_operator():
    a = float(input("Please enter first number: "))
    b = float(input("Please enter second number: "))
    operation = input("What operation would you like to perform multiplication, division, addition or subtraction?")
    if operation.lower() == "multiplication":
        result = a * b
        print(result)

    elif operation.lower() == "addition":
        result = a + b
        print(result)

    elif operation.lower() == "subtraction":
        result = a - b
        print(result)

    elif operation.lower() == "division":
        result = a / b
        print(result)

    else:
        print("Operation not recognized, try again")
        quit()

    return


arthematic_operator()