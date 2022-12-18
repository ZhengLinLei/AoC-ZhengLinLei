import numpy as np

def valid(x,y,z,dimension):
    return 0 <= x <= dimension and 0 <= y <= dimension and 0 <= z <= dimension

def neighbors(x,y,z):
    return {(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z+1), (x,y,z-1)}

def read_points(data):
    return list(tuple(map(int, x.split(','))) for x in data.split("\n"))

def flow(matrix, dimension):
    # list all coordinates on the outside of the cube
    check_set = set.union(*(({(0, i, j), (dimension, i, j),
        (i, 0, j), (i, dimension, j),
        (i, j, 0), (i, j, dimension)}) for i in range(dimension+1) for j in range(dimension+1)))

    while check_set:
        check_set2 = set()
        # mark all empty unmarked neighbors of the previously marked points:
        for x,y,z in check_set:
            if valid(x,y,z,dimension) and matrix[x, y, z] == 0:
                matrix[x,y,z] = 2
                check_set2 |= neighbors(x,y,z)
        check_set = check_set2

points = set(read_points(open('../input.txt').read()))
dimension = max(max(point) for point in points)
matrix = np.zeros((dimension+1, dimension+1, dimension+1), dtype=int)
for point in points:
    matrix[point] = 1
flow(matrix, dimension)
print('Part 2: ', sum(sum(not valid(*n, dimension) or matrix[n] == 2 for n in neighbors(*p)) for p in points))
