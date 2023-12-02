# Part 1
# Zheng Lin Lei

'''
    Not working due minsunderstanding of the question :c Sorry

    I thought the question was asking for the number of games that can be played (SUM of the games that can be played)
    Not the unique MAX color can be loaded
'''


import re

RED = 12
GREEN = 13
BLUE = 14

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
def export(l):
    # format [id, [blue, red, green]]
    # id : int
    # blue : [int], red : [int], green : [int]
    return [[int(re.findall(r"Game (\d+)", i)[0]), sum(map(int, re.findall(r"(\d+) red", i))), sum(map(int, re.findall(r"(\d+) green", i))), sum(map(int, re.findall(r"(\d+) blue", i)))]for i in l]
        
a = list(map(lambda x: x[0], filter(lambda x: (x[1] <= RED and x[2] <= GREEN and x[3] <= BLUE), export(open('../in', "r").read().split('\n')))))

print("Part 1: " + str(a))