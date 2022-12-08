# Part 1 and 2ç

# Zheng Lin Lei

L = readlines("../input.txt")
X = length(L)
T = [L[y][x]-'0' for x∈1:X, y∈1:X]

f(x) = accumulate(max,[fill(-1,X) x[:,1:end-1]],dims=2)
p1 = sum(min.([rotr90(f(rotl90(T,k)),k) for k∈0:3]...).<T)

g(x,y,v) = all(v.<T[x,y]) ? (length(v)) : (findfirst(v.>=T[x,y]))
p2 = maximum([g(x,y,T[x+1:end,y])*g(x,y,T[x,y+1:end])*g(x,y,T[x-1:-1:1,y])*g(x,y,T[x,y-1:-1:1]) for x∈1:X, y∈1:X])

println((p1,p2))