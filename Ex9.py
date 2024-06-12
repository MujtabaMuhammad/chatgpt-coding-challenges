# Write a program to find the sum of the first n natural numbers


last_number = 5
sm = 0

lst = [x for x in range(last_number)]
for i in lst:
    sm += i

print(sm)
