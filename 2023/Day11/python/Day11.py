# Part 1 and Part # Zheng Lin Lei

from itertools import combinations

rd = open('../in').read().strip().split('\n')

e_row = set(); e_col = set(); stars = set()
for i, j in enumerate(rd):
    if len(set(j)) == 1:
        e_row.add(i)
    for k, l in enumerate(rd[i]):
        if l == '#':
            stars.add((i, k))
for k in range(len(rd[0])):
    if len(set([j[k] for j in rd])) == 1:
        e_col.add(k)

main = set(combinations(stars, 2))

def dj(comb, el):
    i, j = comb[0]; k, l = comb[1]
    x, y = abs(i - k), abs(j - l)
    for r in e_row:
        if r in range(*sorted((i, k))): x += el
    for c in e_col:
        if c in range(*sorted((j, l))): y += el
    return x + y


print('Part 1:', sum(dj(s, 1) for s in main))
print('Part 2:', sum(dj(s, 1000000 - 1) for s in main))