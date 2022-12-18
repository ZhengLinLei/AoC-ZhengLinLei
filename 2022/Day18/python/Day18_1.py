# Part 1
# Zheng Lin Lei
def part1(de):
    visited = []
    total_sa = len(de)*6
    for cube in de:
        visited.append(cube)
        x, y, z = cube[0], cube[1], cube[2]
        for e in [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]:
            if e in visited:
                total_sa -= 2
    return(total_sa)

with open('../input.txt') as file:
    l = file.readlines()
cubes_list = [x.rstrip('\n') for x in l]
for e in range(len(l)):
    cubes_list[e] = tuple([int(x) for x in l[e].split(",")])
print("Part 1: ", part1(cubes_list))