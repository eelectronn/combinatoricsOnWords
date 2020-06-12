from itertools import product
from math import ceil


def get_alphabet(k):
    return [str(_) for _ in range(k)]


def get_all_n_length_words(k, n):
    return [''.join(_) for _ in list(product(get_alphabet(k), repeat=n))]


def generate_repeateble_factors(n, k=2):
    n = n - 1
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


def generate_prefer_opposite(n):
    used_substr = set()
    repeatables = generate_repeateble_factors(n)
    de_bruijn = '0'*n
    ndr = '0'*(2*n - 1)
    used_substr.add(de_bruijn)
    used_substr.add('1'*n)
    while len(used_substr) < 2**n:
        first = '0'
        second = '1'
        if ndr[-1] == '0':
            first = '1'
            second = '0'
        if ndr[-n + 1:] + first not in used_substr:
            ndr += first
            de_bruijn += first
            used_substr.add(ndr[-n:])
        elif ndr[-n + 1:] + second not in used_substr:
            ndr += second
            de_bruijn += second
            used_substr.add(ndr[-n:])
        for i in range(max(0, len(ndr) - 2 * (n - 1)), len(ndr)):
            if ndr[i:] in repeatables:
                p = len(ndr) - i - n + 1
                scale = ceil(n / p) - 1
                ndr += ndr[-p:] * scale
                break
    ndr = ndr[:-n+1] + '1'*n + ndr[-n+1:]
    de_bruijn = de_bruijn[:-n+1] + '1' + de_bruijn[-n+1:]
    return ndr, de_bruijn


f = open('prefer_one_results.txt', 'w')
f.write('**Results starts**\n')
one_score = oppo_score = same = 0
for i in range(1, 18):
    f.write('n: ' + str(i) + '\n')
    ndr_1, db_1 = generate_prefer_one(i)
    f.write('Prefer One\n')
    f.write(db_1 + '\n')
    f.write(ndr_1 + '\n\n')
    ndr_op, db_op = generate_prefer_opposite(i)
    f.write('Prefer Opposite\n')
    f.write(db_op + '\n')
    f.write(ndr_op + '\n\n')
    if len(ndr_1) > len(ndr_op):
        f.write('Longer: prefer one\n')
        one_score += 1
    elif len(ndr_op) > len(ndr_1):
        f.write('Longer: prefer opposite\n')
        oppo_score += 1
    else:
        f.write('Same Length\n')
        same += 1
    f.write('\n\n')
f.write('*Score*\nPrefer One: ' + str(one_score) + '\nPrefer Opposite: ' + str(oppo_score) + '\nSame: ' + str(same))
