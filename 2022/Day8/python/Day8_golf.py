# Part 1 and Part 2

# Zheng Lin Lei

grid = [list(map(int, l)) for l in open('input').read().split('\n')]
height, width = len(grid), len(grid[0])
visible = [[False for _ in range(width)] for _ in range(height)]
best_scenic = 0

for x0 in range(width):
    for y0 in range(height):
        ss, h = 1, grid[y0][x0]
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x1, y1, s1 = x0+dx, y0+dy, 1
            while 0 <= x1 < width and 0 <= y1 < height and grid[y1][x1] < h:
                x1, y1, s1 = x1 + dx, y1 + dy, s1 + 1
            if not (0 <= x1 < width and 0 <= y1 < height):
                visible[y0][x0] = True
                s1 -= 1
            ss *= s1
        best_scenic = max(best_scenic, ss)

print(sum(map(sum, visible)))
print(best_scenic)