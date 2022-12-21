mutable struct Monkey
    waiting_for::Array{String}      # which monkeys this one is waiting for
    shout::Int64                    # what this monkey will shout
    operation::String               # what operation this monkey does to those it waits for
end

function wrangle_monkeys()
    """Wrangle monkeys out of a file and into a dictionary with the data"""
    monkeys = Dict{String, Monkey}()
    open("../input.txt", "r") do input
        for line in eachline(input)
            name, action = split(line, ": ")
            if length(action) == 11
                waiters = split(action, " ")
                monkeys[name] = Monkey([waiters[1], waiters[3]], 0, waiters[2])
            else
                monkeys[name] = Monkey([], parse(Int, action), "")
            end
        end
    end
    return monkeys
end

function say_what(monkey::String, monkeys::Dict{String, Monkey}, ignore_humn::Bool)
    """Monkey says what? (Work out what a monkey will shout)"""
    # if the monkey is the special one that we replace then return nothing (only on part 2)
    if monkey == "humn" && ignore_humn
        return nothing
    end

    # if the monkey isn't waiting on anyone then just shout away my friend
    if length(monkeys[monkey].waiting_for) == 0
        return monkeys[monkey].shout
    end

    # work out what the two monkeys that this one is waiting for will shout
    first_waiter = say_what(monkeys[monkey].waiting_for[1], monkeys, ignore_humn)
    second_waiter = say_what(monkeys[monkey].waiting_for[2], monkeys, ignore_humn)

    # if either returns nothing then you don't what to shout and just return nothing
    if ignore_humn && (first_waiter === nothing || second_waiter === nothing)
        return nothing
    end

    # otherwise calculate your shout value based on the operation
    shout = 0
    if monkeys[monkey].operation == "+"
        shout = first_waiter + second_waiter
    elseif monkeys[monkey].operation == "-"
        shout = first_waiter - second_waiter
    elseif monkeys[monkey].operation == "*"
        shout = first_waiter * second_waiter
    elseif monkeys[monkey].operation == "/"
        shout = first_waiter ÷ second_waiter
    end

    # update the shout value and erase the waiting room to speed up the next time
    monkeys[monkey].shout = shout
    monkeys[monkey].waiting_for = []

    return shout
end

function part_one()
    # just work out what the root will shout
    monkeys = wrangle_monkeys()
    return say_what("root", monkeys, false)
end

function part_two()
    monkeys = wrangle_monkeys()

    # check the two potential targets
    targets = [say_what(monkeys["root"].waiting_for[i], monkeys, true) for i in 1:2]

    # whichever is the fixed value, work out what you need to shout to make the other match it
    if targets[1] === nothing
        return what_do_i_shout(monkeys["root"].waiting_for[1], targets[2], monkeys)
    else
        return what_do_i_shout(monkeys["root"].waiting_for[2], targets[1], monkeys)
    end
end

function what_do_i_shout(monkey::String, target::Int64, monkeys::Dict{String, Monkey})
    """Work out what a monkey needs to should to produce a target value"""
    # base case, if we hit "humn" then that's our solution
    if monkey == "humn"
        return target
    end

    # work out what the monkey on either side shouts
    branches = [say_what(monkeys[monkey].waiting_for[i], monkeys, true) for i in 1:2]

    # check which has a fixed value and which we need to look at next
    value, next = 1, 2
    if branches[1] === nothing
        value = 2
        next = 1
    end

    # work out the next target value based on the old target, fixed value and operation
    new_target = 0
    if monkeys[monkey].operation == "+"
        new_target = target - branches[value]
    elseif monkeys[monkey].operation == "-"
        if value == 2
            new_target = target + branches[value]
        else
            new_target = branches[value] - target
        end
    elseif monkeys[monkey].operation == "*"
        new_target = target ÷ branches[value]
    elseif monkeys[monkey].operation == "/"
        if value == 2
            new_target = target * branches[value]
        else
            new_target = branches[value] ÷ target
        end
    end

    # drill down to the next monkey that we're uncertain of
    return what_do_i_shout(monkeys[monkey].waiting_for[next], new_target, monkeys)
end

println("Part 1: ", part_one())
println("Part 2: ", part_two())