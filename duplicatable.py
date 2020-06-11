"""
Created on June 01, 2020

@author: Harsh N. Patel

"""


def no_duplicates(s, n):
    m = len(s)
    for i in range(m-2*n):
        for j in range(i+n, m-n):
            if s[i:i+n] == s[j:j+n]:
                return False
    return True


def duplicatable(s, n):
    print(s)
    m = len(s)
    for i in range(m):
        for j in range(i+1, min(i+n, m+1)):
            new_s = s[:i] + s[i:j] + s[i:]
            if no_duplicates(new_s, n):
                print(s[i:j], i, j)


w = '0000100110101111'
duplicatable(w, 4)
