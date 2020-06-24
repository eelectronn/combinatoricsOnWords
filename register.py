from itertools import product
from math import ceil


def get_alphabet(k):
    return [str(_) for _ in range(k)]


def is_necklace(seq):
    n = len(seq)
    p = 1
    for i in range(1, n):
        if seq[i - p] > seq[i]:
            return False
        if seq[i - p] < seq[i]:
            p = i + 1
    if n % p != 0:
        return False
    return True


def is_co_necklace(seq):
    n = len(seq)
    for i in range(n):
        seq += str(1 - int(seq[i], 10))
    return is_necklace(seq)


def flip_bits(seq):
    s = ''
    for i in range(len(seq)):
        s += str(1 - int(seq[i], 10))
    return s


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


def pcr1_next(seq):
    j = n = len(seq)
    for i in range(1, n):
        if seq[i] == '0':
            j = i
            break
    gemma = seq[j:] + '0' + (j-1)*'1'
    if is_necklace(gemma):
        return str(1 - int(seq[0], 10))
    return seq[0]


def pcr2_next(seq):
    n = len(seq)
    j = -1
    for i in range(n):
        if seq[i] == '1':
            j = i
    gemma = seq[j+1:] + '1' + seq[1:j+1]
    if is_necklace(gemma):
        return str(1 - int(seq[0], 10))
    return seq[0]


def pcr3_next(seq):
    gemma = seq[1:] + '1'
    if is_necklace(gemma):
        return str(1 - int(seq[0], 10))
    return seq[0]


def pcr4_next(seq):
    if is_necklace('0' + seq[1:]):
        return str(1 - int(seq[0], 10))
    return seq[0]


def ccr1_next(seq):
    j = n = len(seq)
    for i in range(1, n):
        if seq[i] == '0':
            j = i
            break
    gemma = seq[j:] + '1' + (j-1)*'0'
    if is_co_necklace(gemma):
        return seq[0]
    return str(1 - int(seq[0], 10))


def ccr2_next(seq):
    n = len(seq)
    j = n - 1
    for i in range(n - 1, -1, -1):
        if seq[i] == '1':
            j = i
            break
    gemma = seq[j+1:] + '1' + flip_bits(seq[1:j+1])
    if is_co_necklace(gemma):
        return seq[0]
    return str(1 - int(seq[0], 10))


def ccr3_next(seq):
    n = len(seq)
    s = seq[1:] + '0'
    if s == '0'*n:
        return str(1 - int(seq[0], 10))
    if is_co_necklace(s):
        return seq[0]
    return str(1 - int(seq[0], 10))


def generate(n, next_bit):
    db = '0'*n
    ndr = '0' * (2 * n - 1)
    repeatable = generate_repeateble_factors(n)
    for _ in range(2 ** n - 1):
        bit = next_bit(db[-n:])
        db += bit
        ndr += bit
        for i in range(max(0, len(ndr) - 2 * (n - 1)), len(ndr)):
            if ndr[i:] in repeatable:
                p = len(ndr) - i - n + 1
                scale = ceil(n / p) - 1
                ndr += ndr[-p:] * scale
                break
    return ndr, db

largest = []
for i in range(2, 18):
    print('n:', i)
    l = -1
    large = 'prefer opposite'

    ndr, db = generate_prefer_opposite(i)
    print('prefer opposite')
    print(db)
    print(ndr)
    print(len(ndr))
    print()
    if len(ndr) > l:
        large = 'prefer opposite'
        l = len(ndr)

    ndr, db = generate(i, pcr1_next)
    print('pcr1')
    print(db)
    print(ndr)
    print(len(ndr))
    print()
    if len(ndr) > l:
        large = 'pcr1'
        l = len(ndr)

    ndr, db = generate(i, pcr2_next)
    print('pcr2')
    print(db)
    print(ndr)
    print(len(ndr))
    print()
    if len(ndr) > l:
        large = 'pcr2'
        l = len(ndr)

    ndr, db = generate(i, pcr3_next)
    print('pcr3')
    print(db)
    print(ndr)
    print(len(ndr))
    print()
    if len(ndr) > l:
        large = 'pcr3'
        l = len(ndr)

    ndr, db = generate(i, pcr4_next)
    print('pcr4')
    print(db)
    print(ndr)
    print(len(ndr))
    print()
    if len(ndr) > l:
        large = 'pcr4'
        l = len(ndr)

    ndr, db = generate(i, ccr1_next)
    print('ccr1')
    print(db)
    print(ndr)
    print(len(ndr))
    print()
    if len(ndr) > l:
        large = 'ccr1'
        l = len(ndr)

    ndr, db = generate(i, ccr2_next)
    print('ccr2')
    print(db)
    print(ndr)
    print(len(ndr))
    print()
    if len(ndr) > l:
        large = 'ccr2'
        l = len(ndr)

    ndr, db = generate(i, ccr3_next)
    print('ccr3')
    print(db)
    print(ndr)
    print(len(ndr))
    print()
    if len(ndr) > l:
        large = 'ccr3'
        l = len(ndr)
    largest.append(large)
print(largest)
