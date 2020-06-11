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


n = 4
a = list(itertools.product('01', repeat=n))
s = '010100110111100001'
print(len(s))
a = [count_occurrences(s, ''.join(tup)) for tup in a]
a.sort(key=lambda x: x[1])
print(len(a))
for sub in a:
    print(sub)
print('------------')
a.sort(key=lambda x: x[0])
border_count = 0
for sub in a:
    for i in range(n//2):
        if sub[0][:i+1] == sub[0][-i-1:]:
            print(sub)
            border_count += 1
            break
print(border_count)
