# Part 1 and Part 2
# Zheng Lin Lei
block = [p.splitlines() for p in open('../in').read().split("\n\n")]
def s(x, y): m = lambda x, y: sum(j for j in range(1, len(x[0])) if sum(sum(a != b for a, b in zip(l[j:], l[j - 1 :: -1])) for l in x) == y); return m(x, y) + 100 * m([*zip(*x)], y)
print("Part 1: ", sum(s(i, 0) for i in block))
print("Part 2: ", sum(s(i, 1) for i in block))