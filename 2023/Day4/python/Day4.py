# Part 1 and Part 2
# Zheng Lin Lei
# import re

# lines = open('../in').read().strip().split('\n')

# total_score = 0; p = {key : 1 for key in range(1, len(lines) + 1)}
# for line in lines:
#     card = re.split(r'[:|]', line)
#     i, w, e = [int(card[0].split(' ')[-1]), card[1].strip().split(' '), card[2].strip().split(' ')]
#     wi = sum(1 for number in e if number in w and number != '')
#     if wi != 0:
#         total_score += 2**(wi- 1)
        
#     for i in range(wi): p[i + i + 1] += 1*p[i]

# print("Part 1: ", total_score)
# card_total = sum(value for value in p.values())
# print("Part 2: ", card_total)

f = open("../in").read().strip().split('\n')
d = dict(zip(range(1, len(f) + 1), [1] * len(f)))
s = 0
for line in f:
    id = int(line.split(":")[0].split()[1])
    n1, n2 = [set(map(int, x.split())) for x in line.split(":")[1].split("|")]
    s += 2**(len(n1 & n2)-1) if n1 & n2 else 0
    d.update({i: d[i]+1*d[id] for i in range(id + 1, id + 1 + len(n1 & n2))})

print("Part 1:" + str(s))
print("Part 2:" + str(sum(d.values())))