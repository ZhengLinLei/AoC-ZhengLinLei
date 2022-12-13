# Part 1 and Part 2

# Zheng Lin Lei

def in_order(l1, l2):
    if isinstance(l1, int) and isinstance(l2, int):
        if l1 == l2:
            return None
        return l1 < l2

    if isinstance(l1, list) and isinstance(l2, list):
        for e1, e2 in zip(l1, l2):
            if (comparison := in_order(e1, e2)) is not None:
                return comparison
        return in_order(len(l1), len(l2))

    if isinstance(l1, int):
        return in_order([l1], l2)
    return in_order(l1, [l2])


text = open("../input.txt", "r").read()
pairs = [[eval(l) for l in pair.splitlines()]for pair in text.strip().split("\n\n")]
print("Part 1: ", sum(i for i, (left, right) in enumerate(pairs, 1) if in_order(left, right)))

packets = [p for pair in pairs for p in pair]
position_1 = 1 + sum(1 for p in packets if in_order(p, [[2]]))
position_2 = 2 + sum(1 for p in packets if in_order(p, [[6]]))
print("Part 2: ", position_1 * position_2)