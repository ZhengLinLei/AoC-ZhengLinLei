# Part 1 Part 2
# Zheng Lin Lei

from collections import defaultdict
import math

lines = [x.strip() for x in open("../in")]
allowed = {"red": 12, "green": 13, "blue": 14}

games_list = []
for line in lines:
    game, content = line.split(":")
    game_id = int(game[5:])
    rounds = content.split(";")
    game_dict = defaultdict(int)
    rounds_list = []
    for round in rounds:
        drawings = round.split(",")
        drawings_list = []
        for drawing in drawings:
            n, color = drawing.strip().split(" ")
            game_dict[color] = max(game_dict[color], int(n))
            drawings_list.append(int(n) <= allowed[color])
        rounds_list.append(all(drawings_list))
    games_list.append((game_id, all(rounds_list), math.prod(game_dict.values())))

print(sum(i for i, r, _ in games_list if r))
print(sum(g for _, _, g in games_list))