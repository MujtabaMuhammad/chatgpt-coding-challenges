# Write a program to print the first n numbers in the Fibonacci sequence.
def fibinocci_seq(n):

    first_num = 0
    second_num = 1
    seq = []

    while second_num <= n:
        seq.append(first_num)
        first_num, second_num = second_num, first_num + second_num

    print(seq)
    return

fibinocci_seq(1000)