# Part 1 and Part 2
# Sorry, I did not do it in vanilla
# Zheng Lin Lei


import re, time
from math import gcd

def part1(c, d):
    answer = 0
    g = r(c, d, 'AAA') # AAA to ZZZ
    while next(g)!='ZZZ': answer += 1
    return answer

def part2(c, d):
    As = [key for key in d.keys() if key[-1]=='A']
    gens = [r(c, d, A) for A in As]
    answer = 1
    for g in gens:
        rounds = 0
        while next(g)[-1] != 'Z': rounds += 1
        answer = (answer*rounds)//gcd(answer, rounds) # LCM GCD es lo mismo
    return answer

def r(c, d, start):
    i, stack = 0, [start]
    while 1:
        head = stack.pop(); stack.append(d[head][0] if c[i]=='L' else d[head][1])
        i = (i+1) % len(c)
        yield head # gritaaaaa

s = open('../in').read().strip()
c, b = s.split('\n\n')
d = {}
for b in b.split('\n'):
    x,y,z = re.findall('\w+', b)
    d[x] = [y, z]

a = time.time()

print("Part 1:", part1(c, d))
print("Part 2:", part2(c, d))

b = time.time()

print( (b - a) / 1000, 'ms')