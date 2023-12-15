# Part 1 and Part 2
# Zheng Lin Lei

a = open('../in').read().split(',')
b = lambda dd, y: sum([(v:=0) or [v:=(v+ord(c))*17%256 for c in s] and v for s in dd]) if y == 1 else sum((b:=[[] for _ in range(256)]) and [((l:=''.join([c for c in s if c.isalpha()])) and (o:=''.join([c for c in s if not c.isalnum()])) and (f:=''.join([c for c in s if c.isdigit()])) and (d:=(l,f)) and (a:=0) or 1) and not (a:=0) and [a:=(a+ord(c))*17%256 for c in l] and ((b[a].append(d) if l not in [x[0] for x in b[a]] else ((e:=[x[0] for x in b[a]].index(l)) or 1) and b[a].pop(e) and b[a].insert(e,d)) if o=='=' else b[a].pop([x[0] for x in b[a]].index(l)) if l in [x[0] for x in b[a]] else 0) for s in dd] and [(i+1)*(j+1)*int(n[1]) for i,p in enumerate(b) for j,n in enumerate(p)])
print('Part 1:', b(a, 1))
print('Part 2:', b(a, 2))