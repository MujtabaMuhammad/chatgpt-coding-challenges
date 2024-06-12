# Write a program to count the frequency of each character in a string

def frequency_counter():
    character = input("Please enter the character to be counted: ")
    string = input("Enter the main string: ")
    substr_ready = character.strip().lower()
    string_ready = string.strip().lower()
    counter = 0
    for i in string_ready:
        if character == i:
            counter += 1
    print(counter)

frequency_counter()