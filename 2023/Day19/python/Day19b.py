ii, dd = open('../in').read().split('\n\n'); x,m,a,s = 0,0,0,0; A_ = lambda: 1 + x+m+a+s; R_ = lambda: 1; S_ = 0; exec(ii.replace(':', ' and ').replace(',', '_() or ').replace('{', '_ = lambda: ').replace('}', '_()')); exec(dd.replace(',', ';').replace('{', '').replace('}', ';S_+=in_()-1'))

print("Part 1:", S_)