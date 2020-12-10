#!/bin/python

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
