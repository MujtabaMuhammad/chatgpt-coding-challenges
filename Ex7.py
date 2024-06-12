# Write a function to calculate the factorial of a number.

num = 10
factorial = 1
lst = [x for x in range(1,num+1,1)]
for i in lst:
    factorial *= i


print(lst, factorial)
