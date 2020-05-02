"""
Created on May 01, 2020

@author: Harsh N. Patel

"""


def generate_modified_de_bruijn(k, n):
    substr = dict()
    answers = []
    longest = ''
    i = 0
    s = []
    while i > -1:
        curr = 0
        if len(s) == i + 1:
            curr = s[i] + 1
            if len(s) >= n:
                sub = ''.join(list(map(str, s[i - n + 1:])))
                if sub in substr:
                    if substr[sub] == i - n + 1:
                        del substr[sub]
            del s[i]
        if curr == k:
            i -= 1
            continue
        s.append(curr)
        if len(s) >= n:
            sub = ''.join(list(map(str, s[i - n + 1:])))
            if sub in substr:
                if i - substr[sub] + 1 >= 2 * n:
                    continue
            else:
                substr[sub] = i - n + 1
                if len(substr) == k ** n:
                    st = ''.join(list(map(str, s)))
                    answers.append(st)
                    if len(st) >= len(longest):
                        longest = st
                        print(f'{len(longest):03d}', longest)
        i += 1
    return answers


a = generate_modified_de_bruijn(k=3, n=4)
longest = a[0]
for i in range(len(a)):
    if len(a[i]) > len(longest):
        longest = a[i]
print(longest)
print(len(longest))
