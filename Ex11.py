# Write a program to check if a given string is a palindrome

def palindrom_checker(inpt):
    strg = inpt
    reversed_string = strg[::-1]
    print(reversed_string)
    if strg == reversed_string:
        print("This is a palindrom")
    else:
        print("This isn't a palindrom")


palindrom_checker("abcrhtcba")
