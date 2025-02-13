#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])  
        return

    fibonacci = [0, 1]  
    while len(fibonacci) < length:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])  

    print(fibonacci[:length])  

print_fibonacci(9)  

pass