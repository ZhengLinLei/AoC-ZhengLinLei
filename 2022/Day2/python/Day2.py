# Read File ../input.txt

# Part 1 and Part 2


# ZhengLinLei

plays = [play.split() for play in open('../input.txt').read().strip().splitlines()]

## P1
total = 0
for p1, p2 in plays:
    p1 = ord(p1) - ord('A')
    p2 = ord(p2) - ord('X')
    total += (p2 - p1 + 4) % 3 * 3 + p2 + 1
print(total)

# Short version
#print(sum((ord(p2) - ord(p1) - 19) % 3 * 3 + ord(p2) - 87 for p1, p2 in plays))

## P2 
total = 0
for p1, p2 in plays:
    p1 = ord(p1) - ord('A')
    p2 = ord(p2) - ord('X')
    total += p2 * 3 + (p1 + p2 - 1) % 3 + 1
print(total)

# Short version
#print(sum((ord(p2) - 88) * 3 + (ord(p1) + ord(p2) - 154) % 3 + 1 for p1, p2 in plays))