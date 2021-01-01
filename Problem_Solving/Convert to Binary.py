
#!/bin/python

"""
Task
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation. When working with different bases, it is common to show the base as a subscript.

Example

The binary representation of  is . In base , there are  and  consecutive ones in two groups. Print the maximum, .

Input Format

A single integer, .

Constraints

Output Format

Print a single base- integer that denotes the maximum number of consecutive 's in the binary representation of .

Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2
Explanation

Sample Case 1:
The binary representation of  is , so the maximum number of consecutive 's is .

Sample Case 2:
The binary representation of  is , so the maximum number of consecutive 's is .
"""

import math
import os
import random
import re
import sys

binlist = list()

def calculatequotient(n):
        if n==0:
                #print 0
                binlist.append(0)
        if n==1:
                #print 1
                binlist.append(1)
        else:
                quotient = n//2
                rem = n%2 
                #print rem 
                binlist.append(rem)
                calculatequotient(quotient)

def checkconsecutive1s(a):
    final = 0
    count = 0
    for i in a:
        if i == 0:
            count = 0
        if i==1:
            count = count + 1
        if final<count:
            final = count
    return final
        

if __name__ == '__main__':
    n = int(raw_input())
    calculatequotient(n)
    final = checkconsecutive1s(binlist)
    print final
