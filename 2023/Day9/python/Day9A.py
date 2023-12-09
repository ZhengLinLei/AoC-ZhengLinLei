# Part 1 and Part 2
# Zheng Lin Lei

def g1(seq: list[int]) -> tuple[int, int]:
    if not any(seq):
        return 0, 0
    pre, post = g1([v2 - v1 for v1, v2 in zip(seq, seq[1:])])
    return seq[0] - pre, seq[-1] + post


text = open('../in').read().strip().splitlines()
ss = [[int(x) for x in line.split()] for line in text]
ppl = [g1(seq) for seq in ss]
print('Part 1:', sum(post for _, post in ppl))
print('Part 2:', sum(pre for pre, _ in ppl))