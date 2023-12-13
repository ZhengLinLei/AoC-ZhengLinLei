# Part 1 and Part 2
# Zheng Lin Lei
block = [p.splitlines() for p in open('../in').read().split("\n\n")]

def df(x, i): return sum(sum(a != b for a, b in zip(l[i:], l[i - 1 :: -1])) for l in x)
def m(x, y): return sum(j for j in range(1, len(x[0])) if df(x, j) == y)
def s(x, y): return m(x, y) + 100 * m([*zip(*x)], y)

print("Part 1: ", sum(s(p, 0) for p in block))
print("Part 2: ", sum(s(p, 1) for p in block))