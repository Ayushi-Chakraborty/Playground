"""
convert all lowercase letters to uppercase letters and vice versa.

For Example:

HackerRank.com presents "Pythonist 2". -> hACKERrANK.COM PRESENTS "pYTHONIST 2"
Pythonist 2 → pYTHONIST 2

"""


def swap_case(s):
    l = len(s)
    a = [x for x in s]
    for i in range(l):
        if ord(a[i]) >=65 and ord(a[i]) <= 90:
            a[i] = chr(ord(a[i]) + 32)
        elif ord(a[i])>=97 and ord(a[i]) <= 122:
            a[i] = chr(ord(a[i]) - 32)
    
    return ''.join(a)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
    #testscase
    result = swap_case("HackerRank.com presents "Pythonist 2".")
    
    #Output should be: hACKERrANK.COM PRESENTS "pYTHONIST 2".
    print(result)
    
