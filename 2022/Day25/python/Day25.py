# Zheng LinLei
# Part 1
print((g:=lambda d:d and g((d+2)//5)+'=-012'[(d+2)%5]or'')(sum(map(f:=lambda s:s and f(s[:-1])*5+'=-012'.find(s[-1])-2 or 0,map(str.strip,open('../input.txt'))))))