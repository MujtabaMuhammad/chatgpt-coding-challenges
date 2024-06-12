# Write a program that creates a list of squares of numbers from 1 to n.
def sqrer(n):
    sqr = [n**2 for n in range (1,n+1)]
    print(sqr)
    return



sqrer(10)