#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    p = str(n)
    if len(p) == 1:
            return n
    else:
        digit = [k*int(x) for x in p]
        while len(digit)>1:
            new_digit =[int(x) for x in str(sum(digit))]
            digit = new_digit
        return   digit[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
