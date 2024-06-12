#Create a program to calculate simple interest given principal, rate, and time.

def interest_calculator():
    principal = 500
    rate = 5
    time = 2
    interest = time * (principal*(rate/100))
    print(interest)



interest_calculator()