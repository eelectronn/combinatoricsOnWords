"""
Created on May 09, 2020

@author: Harsh N. Patel

"""
import itertools


def count_occurrences(string, substring):
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return substring, count


a = list(itertools.product('01', repeat=5))
s = '00000000010001000110011001110100101010101101101111111110000'
a = [count_occurrences(s, ''.join(tup)) for tup in a]
a.sort(key=lambda x: x[1])
print(len(a))
for sub in a:
    print(sub)
