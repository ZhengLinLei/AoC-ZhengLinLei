# Part 1 and 2

# Zheng Lin Lei

rocks, i = ((0,1,2,3),(1,0+1j,2+1j,1+2j),(0,1,2,2+1j,2+2j),(0,0+1j,0+2j,0+3j),(0,1,0+1j,1+1j)), 0
jets, j = open('../input.txt').read(), 0
tower, cache = {-1}, {}

empty = lambda p: p.real in range(7) and p.imag>0 and p not in tower

for n in range(int(1e12)):
    h = max(x.imag for x in tower)
    p = complex(2, h+4)
    if n==2022: print("Part 1: ", int(h))

    key = i, j
    if key in cache:
        N, H = cache[key]
        d, m = divmod(1e12-n, N-n)
        if not m: print("Part 2: ", int(h + (H-h)*d)); break
    else: cache[key] = n, h

    rock = rocks[i]
    i = (i+1) % len(rocks)

    while True:
        jet = +1 if jets[j] == '>' else -1
        j = (j+1) % len(jets)

        if all(empty(p+jet+r) for r in rock): p += jet
        if all(empty(p-1j +r) for r in rock): p -= 1j
        else: break

    tower |= {p+r for r in rock}