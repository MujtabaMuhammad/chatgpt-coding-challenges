# Write a program to merge two dictionaries.

'''way 1'''


def dict_merger(dic1, dic2):
    return dic1.update(dic2)


dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

print(dict_merger(dict1, dict2))
print(dict2)
print(dict1)

'''way 2'''


def merge(dic1, dic2):
    dic3 = dic1 | dic2
    return dic3


print(merge(dict1, dict2))
