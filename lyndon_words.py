"""
Created on May 15, 2020

@author: Harsh N. Patel

"""

W = ''
n = 4
S = ['0', '1']
k = len(S)
S.sort()
w = [-1]
while w:
    w[-1] += 1
    m = len(w)
    if n % len(w) == 0:
        W += ''.join(S[i] for i in w) + ' '
        print(''.join(S[i] for i in w))
    while len(w) < n:
        w.append(w[-m])
    while w and w[-1] == k - 1:
        w.pop()

print(W)
