from itertools import product
from math import ceil

def get_alphabet(k):
    return [str(_) for _ in range(k)]


def get_all_n_length_words(k, n):
    return [''.join(_) for _ in list(product(get_alphabet(k), repeat=n))]

def generate_repeateble_factors(n, k=2):
    n = n - 1
    alphabet = get_alphabet(k)
    words = get_all_n_length_words(k, n)
    repeatable_factors = set()
    for word in words:
        for i in range(n):
            w = word + word[i:]
            factor = word
            for j in range(1, n-i+1):
                factor += w[j+n-1]
                if w[j:j + n] == word:
                    repeatable_factors.add(factor)
                    break
    return repeatable_factors


def generate_prefer_one(n, k=2):
    used_substr = set()
    repeatables = generate_repeateble_factors(n)
    de_bruijn = '0'*n
    ndr = '0'*(2*n - 1)
    used_substr.add(de_bruijn)
    while len(used_substr) < k**n:
        if ndr[-n+1:] + '1' not in used_substr:
            ndr += '1'
            de_bruijn += '1'
            used_substr.add(ndr[-n:])
        elif ndr[-n+1:] + '0' not in used_substr:
            ndr += '0'
            de_bruijn += '0'
            used_substr.add(ndr[-n:])
        for i in range(max(0, len(ndr) - 2*(n-1)), len(ndr)):
            if ndr[i:] in repeatables:
                p = len(ndr) - i - n + 1
                scale = ceil(n/p) - 1
                ndr += ndr[-p:]*scale
                break
    return ndr, de_bruijn


f = open('prefer_one_results.txt', 'a')
f.write('**Results starts**\n')
for i in range(1, 10):
    ndr, db = generate_prefer_one(i)
    f.write('n: ' + str(i) + '\n')
    f.write(db + '\n\n')
    f.write(ndr + '\n\n\n')

