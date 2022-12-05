# Zheng Lin Lei
# Part 1 and 2


# Method with matrix
#  1   2   3
# Install numpy
# pip install numpy
import re
import numpy as np

# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
def getStacksNp(stackData):
    stackChars = [list(s) for s in stackData.split('\n')[:-1]]
    # print(stackChars)
    trarray = np.array(stackChars, dtype=np.unicode_).transpose()
    # print(trarray)
    stacks = [trarray[index] for index in range(1, len(trarray), 4)]
    stacks = [[s for s in row if s != ' '] for row in stacks]
    return stacks

# move 1 from 2 to 1
def getMoves(mdata):
    moves = []
    for move in mdata.split('\n'):
        quantity, source, dest = [int(x) for x in re.findall(r'\d+', move)]
        moves.append([quantity, source - 1, dest - 1])
    return moves

content = open('../input.txt').read()
stackData, moveData = content.split('\n\n')
moves = getMoves(moveData)
stacks = getStacksNp(stackData)
for quantity, source, dest in moves:   
    for i in range(quantity):
        top = stacks[source].pop(0)
        stacks[dest].insert(0, top)

answer1 = ''.join([s[0] for s in stacks])
answer1 = print(f'part 1: {answer1}')

# part 2
stacks = getStacksNp(stackData)
for quantity, source, dest in moves:
    stacks[dest] = stacks[source][:quantity] + stacks[dest]
    stacks[source] = stacks[source][quantity:]

answer2 = ''.join([s[0] for s in stacks])
print(f'part 2: {answer2}')
