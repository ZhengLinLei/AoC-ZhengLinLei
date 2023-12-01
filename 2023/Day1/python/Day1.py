# Part 1 and Part 2
# Zheng Lin Lei
import re
part2 = True

def gg(l):
    return sum(map(lambda x: int(x[0] + x[-1]), map(lambda x: [a for a in [*x] if a.isdigit()], l)))

a = open('../in', "r").read().split('\n')
if not part2:
    b = gg(a)
    print("Part 1 {}".format(b))
#
else:
    aa = {"one": '1',"two": '2',"three": '3',"four": '4',"five": '5',"six": '6',"seven": '7',"eight": '8',"nine": '9'}
    ll = "(" + "|".join(list(aa.keys())) + ")"
    c = gg(list(map(lambda x: "".join(x), [[x if (x := "".join([v for k, v in aa.items() if line[i:].startswith(k)])) else line[i] for i in range(len(line))] for line in a])))
            

    print("Part 2 {}".format(c))

