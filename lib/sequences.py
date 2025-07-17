#!/usr/bin/env python3

def print_fibonacci(length):

    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    elif length == 2:
        print([0,1])
        return 
    

    fib_list = [0,1]
    for i in range(length - 2):
        count = fib_list[-1] + fib_list[-2]
        fib_list.append(count)
    print(fib_list)

            