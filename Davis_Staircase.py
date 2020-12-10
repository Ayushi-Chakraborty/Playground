#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n):
    if n==1:
        return 1
    if n==2: 
        return 2
    if n==3:
        return 4
    array=[0]*max(4,(n+1))
    array[0] = 1
    array[1] = 2
    array[2] = 4
    for i in range(3,n):
        array[i] = array[i-1]+array[i-2]+array[i-3]
    return array[n-1]
    
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
