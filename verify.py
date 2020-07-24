pdw = {
    '0': '01',
    '1': '00'
}
s = '0100'
for n in range(3, 20):
    s_new = ''
    for c in s:
        s_new += pdw[c]
    s = s_new
    string_attractor = [0, 2**(n-1)-1, 3*(2**(n-2))-1]
    subs = dict()
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] in subs:
                subs[s[i:j]].append(i)
            else:
                subs[s[i:j]] = [i]
    all_subs = True
    for sub in subs:
        this_sub = False
        for o in subs[sub]:
            for attractor in string_attractor:
                if o <= attractor < o + len(sub):
                    this_sub = True
                    break
            if this_sub:
                break
        all_subs &= this_sub
    print(n, all_subs)
