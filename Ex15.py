# Write a program to create a dictionary from two lists, one of keys and one of values.

lst1 = ['a', 'b', 'c', 'd', 'e']
lst2 = ['apple', 'ban', 'candy', 'dic', 'elephant']


def dict_cretr(lst1, lst2):
    result_dict = {}
    for i in range(len(lst1)):
        result_dict[lst1[i]] = lst2[i]

    print(result_dict)


dict_cretr(lst1, lst2)
