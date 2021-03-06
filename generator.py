"""
Created on May 01, 2020

@author: Harsh N. Patel

"""


def generate_modified_de_bruijn(k, n):
    cont = set([str(j)*n for j in range(k)])
    substr = dict()
    used_symbols = []
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
            if used_symbols[curr - 1] == i:
                del used_symbols[curr - 1]
                curr = k
        if curr == k:
            sub = ''.join(list(map(str, s[i - n:])))
            if sub in cont:
                s = s[0:i - n + 1]
                i -= n - 1
            i -= 1
            continue
        s.append(curr)
        if curr > len(used_symbols):
            continue
        if curr == len(used_symbols):
            used_symbols.append(i)
        if len(s) >= n:
            sub = ''.join(list(map(str, s[i - n + 1:])))
            if sub in substr:
                if i - substr[sub] + 1 >= 2 * n:
                    continue
            else:
                substr[sub] = i - n + 1
                if sub in cont:
                    s += [s[i] for _ in range(n - 1)]
                    i += n - 1
                if len(substr) == k ** n:
                    st = ''.join(list(map(str, s)))
                    answers.append(st)
                    if len(st) >= len(longest):
                        longest = st
                        print(str(len(longest)), longest)
        i += 1
    return answers


task = [(2, 5)]

f = open('results.txt', 'a', 1)
f.write('results begin\n')
for t in task:
    a = generate_modified_de_bruijn(k=t[0], n=t[1])
    print('k:', t[0], 'n:', t[1])
    print(len(a))
    print(a)
    print('---------------------')
    # f.write('k: ' + str(t[0]) + ' n: ' + str(t[1]) + '\n' + str(len(a)) + '\n' + a + '\n----------------------\n')
