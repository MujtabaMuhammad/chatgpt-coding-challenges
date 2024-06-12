# Write a Python program to check if a number entered by the user is even or odd.

def EvenOrOdd():

    a = float(input("Please enter number: "))
    if a % 2 == 0:
        print("number is even")
    else:
        print("number is odd")

    return

EvenOrOdd()