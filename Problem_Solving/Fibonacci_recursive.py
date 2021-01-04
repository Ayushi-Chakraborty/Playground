"""Implement a function recursively to get the desired
Fibonacci sequence value.
"""

def get_fib(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    else:
        return get_fib(position-1) + get_fib(position-2)
    return -1

# Test cases
#Should print 34 
print get_fib(9)

#should print  89
print get_fib(11)

#should print 0
print get_fib(0)
