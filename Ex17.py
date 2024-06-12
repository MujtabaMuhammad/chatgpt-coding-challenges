# Write a program to remove duplicates from a list.
lst = [1, 2, 2, 3]

for i in lst:
    if lst.count(i) > 1:
        lst.remove(i)
print(lst)

