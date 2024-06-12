# Write a program to count the occurrences of each element in a list.
var = ['h', 'b', 'z', 'g', 'x', 'j', 'u', 'f', 'r', 'v',
       'w', 'n', 'd', 'l', 'o', 'k', 'c', 'a', 'y', 'e',
       'a', 'j', 'q', 'i', 's', 'm', 'p', 'o', 'c', 'x',
       'f', 'e', 'u', 'k', 'm', 'n', 'd', 'v', 'q', 'l',
       't', 'z', 'y', 'b', 'r', 'j', 'p', 'h', 's', 'w',
       'i', 'u', 'g', 'a', 'o', 'e', 'y', 't', 'c', 'q',
       'n', 'm', 'l', 'k', 'd', 'w', 'v', 'f', 'r', 's',
       'i', 'j', 'x', 'p', 'a', 'z', 'b', 'h', 'g', 'o',
       'k', 'c', 'm', 'n', 'u', 'l', 't', 'x', 'w', 'y',
       'v', 'q', 'r', 's', 'd', 'b', 'e', 'f', 'j', 'h']

letter_search = 'e'
count = 0

for i in var:
    if i == letter_search:
        count += 1

print(count)
# alternatively
print(var.count('e'))
