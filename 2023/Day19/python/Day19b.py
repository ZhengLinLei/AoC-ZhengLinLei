ss = open('../in').read().split('\n\n');ii, dd = ss; x,m,a,s = 0,0,0,0; A_ = lambda: 1 + x+m+a+s; R_ = lambda: 1; S_ = 0; exec(ii.replace(':', ' and ').replace(',', '_() or ').replace('{', '_ = lambda: ').replace('}', '_()')); exec(dd.replace(',', ';').replace('{', '').replace('}', ';S_+=in_()-1'))
def cc(l, h):
    x = max(h['x'] - l['x'], 0); m = max(h['m'] - l['m'], 0); a = max(h['a'] - l['a'], 0); s = max(h['s'] - l['s'], 0)
    return x * m * a * s

def j(l, h, w):
    if w == 'A': global t; t += cc(l, h); return
    if w == 'R': return
    for i in r[w]:
        if len(i) == 1: j(l, h, i[0])
        if '<' in i[0]: 
            k, v = i[0].split('<')
            nh = h.copy(); nh[k] = min(nh[k], int(v))
            if cc(l, nh) > 0: j(l.copy(), nh, i[1]); l[k] = max(l[k], int(v))
        if '>' in i[0]:
            k, v = i[0].split('>')
            nl = l.copy()
            nl[k] = max(nl[k], int(v) + 1)
            if cc(nl, h) > 0: j(nl, h.copy(), i[1])
            h[k] = min(h[k], int(v) + 1)

r, T_ = {}, 0
for l in ss[0]:
    print(l.split('{'))
    n, l = l.split('{'); r[n] = [p.split(":") for p in l[:-1].split(',')]

j({'x': 1, 'm': 1, 'a': 1, 's': 1}, {'x': 4001, 'm': 4001, 'a': 4001, 's': 4001}, "in")
print("Part 1: ", S_)
print("Part 2: ", T_)
