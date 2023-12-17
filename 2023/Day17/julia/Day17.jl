# Part 1 and Part 2
# Zheng Lin Lei

function a(M,R)
    n = size(M,1); H,V = fill(sum(M),n,n),fill(sum(M),n,n); H[1] = V[1] = 0
    while true
        Σ = sum(H)+sum(V)
        for δ∈R, t∈1:n
            t>=δ+1 && (V[[t],:].=min.(V[[t],:],H[[t-δ],:]+sum(M[t-δ+1:t,:],dims=1))); t+δ<=n && (V[[t],:].=min.(V[[t],:],H[[t+δ],:]+sum(M[t:t+δ-1,:],dims=1))); t>=δ+1 && (H[:,[t]].=min.(H[:,[t]],V[:,[t-δ]]+sum(M[:,t-δ+1:t],dims=2))); t+δ<=n && (H[:,[t]].=min.(H[:,[t]],V[:,[t+δ]]+sum(M[:,t:t+δ-1],dims=2))) 
        end
        Σ==sum(H)+sum(V) && break
    end
    min(last(H),last(V))    
end

b = hcat(collect.(readlines("../in"))...).-'0'
println("Part 1: ", a(b,1:3))
println("Part 2: ", a(b,4:10))