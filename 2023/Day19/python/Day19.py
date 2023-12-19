# Part 1
# Zheng Lin Lei
# I have got another idea, so I decided to do both methods

import re
x, m, a, s = 0, 0, 0, 0;t = 0; ii, ss = map(lambda x: list(map(lambda y: list(map(lambda z: re.sub(r':([a-zA-Z]+)', r' and j("\1")', z), filter(None, y.replace('{', ',').replace('}', '').split(',')))), x.splitlines())), open('../in').read().split('\n\n')); js = { i[0]: i for i in ii }
def j(st): 
    if st in ['A', 'R']: return st
    for i in range(1, len(js[st])-1): 
        s = exec(js[st][i])
        if s: return s
    return j(js[st][-1])

for x in ss:
    exec(";".join(x));
    if (j('in') == 'A'): t = sum(x, m, a, s)


print("Part 1: ", t)