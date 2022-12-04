with open(r'../input.txt') as f:
    data = f.read().splitlines()
    data = [x.strip() for x in data]
        
data = [line.split(',') for line in data]
envelops, overlaps = 0,0

for pair in data:
    line = []
    for assn in pair:
        assn = assn.split('-')
        line.extend([int(string) for string in assn])
    
    if line[0] <= line[2] and line[1] >= line[3]:
        envelops += 1
    elif line[0] >= line[2] and line[1] <= line[3]:
        envelops += 1
        
    if line[1] >= line[2] and line[0] <= line[3]:
        overlaps += 1
    

print(f'Part 1: {envelops}')
print(f'Part 2: {overlaps}')