# Part 1 and Part 2

# Zheng Lin Lei

module Day13

INPUT_PATH = joinpath(@__DIR__, "../input.txt")

@enum Ordered RIGHT WRONG UNDECIDED

function parse_input(s)
    pairs = split(rstrip(s), "\n\n")
    data = []
    for pair ∈ pairs
        first, second = split(pair, "\n")
        push!(data, (eval(Meta.parse(first)), eval(Meta.parse(second))))
    end
    data
end

function ordered((left, right))::Ordered
    if typeof(left) == Int && typeof(right) == Int
        if left < right
            return RIGHT
        elseif left > right
            return WRONG
        else
            return UNDECIDED
        end
    elseif typeof(left) <: Vector && typeof(right) <: Vector
        for i ∈ 1:min(length(left), length(right))
            status = ordered((left[i], right[i]))
            if status != UNDECIDED
                return status
            end
        end
        if length(left) < length(right)
            return RIGHT
        elseif length(left) > length(right)
            return WRONG
        else
            return UNDECIDED
        end
    else
        if typeof(left) == Int
            return ordered(([left], right))
        elseif typeof(right) == Int
            return ordered((left, [right]))
        end
    end
end

function part1(input = read(INPUT_PATH, String))
    pairs = parse_input(input)
    sum(findall(p -> ordered(p) == RIGHT, pairs))
end

function part2(input = read(INPUT_PATH, String))
    pairs = parse_input(input)
    packets = [p[i] for p ∈ pairs for i ∈ 1:2]
    push!(packets, [[2]], [[6]])
    sort!(packets; lt=(a,b)->ordered((a,b))==RIGHT)
    div1, div2 = findfirst(p->p==[[2]], packets), findfirst(p->p==[[6]], packets)
    div1 * div2
end

end # module Day13