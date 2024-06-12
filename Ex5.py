# Write a program to find the largest of three numbers entered by the user.


def ThreeNumberComparetor():
    
    a = float(input("Please enter first number: "))
    b = float(input("Please enter second number: "))
    c = float(input("Please enter third number: "))

    if a > b and a > c:
        print(str(a) + " is the largest number")
    elif b > a and b > c:
        print(str(b) + " is the largest number")
    else:
        print(str(c) + " is the largest number")

    return

ThreeNumberComparetor()

