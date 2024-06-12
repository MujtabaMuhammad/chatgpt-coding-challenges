# - Write a program to check if a given substring is present in a string.

def substring_checker():
    substring = input("Please enter the substring: ")
    string = input("Enter the main string: ")
    substr_ready = substring.strip().lower()
    string_ready = string.strip().lower()
    if substr_ready in string_ready:
        print("The substring is preset in the string, check is not case sensitive")
    else:
        print("The substring is not present in the string, check is not case sensitive")




substring_checker()