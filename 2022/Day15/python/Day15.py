# Part 2

# Zheng Lin Lei

import itertools
import re

with open('../input.txt') as f:
    lines = f.read().split('\n')

beacons = {}; distances = {}

for l in lines:
    sx, sy, bx, by = list(map(int, re.findall('-?\d+', l)))

    beacons[sx+1j*sy] = bx+1j*by
    distances[sx+1j*sy] = abs(sx-bx) + abs(sy-by)

coverage = set()

min_x = int(min(s.real-d for s,d in distances.items()))
max_x = int(max(s.real+d for s,d in distances.items()))

reserved = set(beacons.values()) | set(beacons.keys())

count = 0; y = 2_000_000

for x in range(min_x, max_x + 1):
    if any(abs(s.real - x) + abs(s.imag- y) <= d and x+1j*y not in reserved for s,d in distances.items()):
        count += 1

print("Part 1: ", count)

# part 2
impossible = [[] for _ in range(4_000_001)]

for s,d in distances.items():
    first_half = list(range(0, d+1))
    for y,x in zip(range(int(s.imag) - d, int(s.imag) + d + 1), first_half + list(reversed(first_half[:-1]))):
        if not 0 <= y <= 4_000_000:
            continue
        impossible[y].append((s.real - x, s.real + x + 1))

# used a stackoverflow answer for these two functions :/
def range_diff(r1, r2):
    s1, e1 = r1
    s2, e2 = r2
    endpoints = sorted((s1, s2, e1, e2))
    result = []
    if endpoints[0] == s1 and endpoints[1] != s1:
        result.append((endpoints[0], endpoints[1]))
    if endpoints[3] == e1 and endpoints[2] != e1:
        result.append((endpoints[2], endpoints[3]))
    return result

def multirange_diff(r1_list, r2_list):
    for r2 in r2_list:
        r1_list = list(itertools.chain(*[range_diff(r1, r2) for r1 in r1_list]))
    return r1_list

for y,imp in enumerate(impossible):
    l = multirange_diff([[0, 4_000_001]], imp)

    if l:
        x = l[0][0]
        print("Part 2: ", x*4_000_000+y)
        break