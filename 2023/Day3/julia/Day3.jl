# Part 1 Part 2
# Zheng Lin Lei

function read_puzzle(file)
    text = readlines(file)
    matrix = [text[r][c] for r in 1:length(text), c in 1:length(text[1])]
    return matrix
end

function gg_number(m, start_r, start_c)
    s = 0
    rightmost = start_c
    while 1 <= rightmost <= size(m, 2)
        if isdigit(m[start_r, rightmost])
            rightmost += 1
        else
            break
        end
    end
    start_c = rightmost - 1
    d = 1
    while start_c >= 1 && isdigit(m[start_r, start_c])
        s += d * (m[start_r, start_c] - '0')
        start_c -= 1
        d *= 10
    end
    return s, start_r, start_c + 1
end

function find_gear_ratios(schematic, stars)
    tot = 0
    for v in values(stars)
        if length(v) != 2
            continue
        end
        n_1, _, _ = gg_number(schematic, v[1][1], v[1][2])
        n_2, _, _ = gg_number(schematic, v[2][1], v[2][2])
        tot += n_1 * n_2
    end
    return tot
end

function part1(schematic)
    engine_parts = Set()
    total = 0
    for r in 1:size(schematic, 1)
        for c in 1:size(schematic, 2)
            if schematic[r, c] == '.' || isdigit(schematic[r, c])
                continue
            end
            # this is a symbol, look for adjacent numbers
            for dr in (-1, 0, 1)
                for dc in (-1, 0, 1)
                    if dr == 0 && dc == 0
                        continue
                    end
                    if ! (1 <= r + dr <= size(schematic, 1))
                        continue
                    end
                    if ! (1 <= c + dc <= size(schematic, 2))
                        continue
                    end
                    if isdigit(schematic[r + dr, c + dc])
                        n, start_r, start_c = gg_number(schematic, r + dr, c + dc)
                        if (start_r, start_c) in engine_parts
                            continue
                        else
                            total += n
                        end
                        push!(engine_parts, (start_r, start_c))
                    end
                end
            end
        end
    end
    return engine_parts, total
end

function part2(schematic)
    stars = Dict()
    for r in 1:size(schematic, 1)
        for c in 1:size(schematic, 2)
            if schematic[r, c] != '*'
                continue
            end
            stars[(r, c)] = []
            for dr in (-1, 0, 1)
                for dc in (-1, 0, 1)
                    if dr == 0 && dc == 0
                        continue
                    end
                    if ! (1 <= r + dr <= size(schematic, 1))
                        continue
                    end
                    if ! (1 <= c + dc <= size(schematic, 2))
                        continue
                    end
                    if isdigit(schematic[r + dr, c + dc])
                        n, start_r, start_c = gg_number(schematic, r + dr, c + dc)
                        if (start_r, start_c) in stars[(r, c)]
                            continue
                        else
                            push!(stars[(r, c)], (start_r, start_c))
                        end
                    end
                end
            end
        end
    end
    return stars
end



schematic = read_puzzle("../in")
parts, sum_of_parts = part1(schematic)
println(sum_of_parts)

stars = part2(schematic)
sum_of_ratios = find_gear_ratios(schematic, stars)
println(sum_of_ratios)
