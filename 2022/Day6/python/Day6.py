# Part 1 and 2
# Zheng Lin Lei


def f(s, n):
    p = ""
    for i, c in enumerate(s):
        j = p.rfind(c)
        if j < 0:
            if len(p) >= n-1:
                return i+1
            else:
                p += c
        else:
            p = p[j+1:]+c
    return 0


t = open("../input.txt", "rt").read().strip()
print(f(t, 14))
