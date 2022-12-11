# Part 1 and Part 2

# Zheng Lin Lei

import math
import operator
from math import floor


def solve(round):

    with open('../input.txt') as openfileobject:
        lines = [r.strip() for r in openfileobject.readlines()]

    monkey_items = []
    monkey_operation = []
    monkey_test = []
    monkey_inspections = []
    monkey_divisors_product = 1

    for i in range(0, len(lines), 7):
        monkey_inspections.append(0)
        monkey_items.append([int(x) for x in lines[i + 1].split(':')[1].split(',')])

        op_val = lines[i + 2].split(' ')[-1]

        if '*' in lines[i + 2]:
            monkey_operation.append(
                (lambda x, op_val=op_val: operator.mul(x, int(op_val) if op_val.isnumeric() else x)))
        else:
            monkey_operation.append(
                (lambda y, op_val=op_val: operator.add(y, int(op_val) if op_val.isnumeric() else y)))

        divisor = int(lines[i + 3].split(' ')[-1])
        monkey_divisors_product *= divisor
        true_monkey = int(lines[i + 4].split(' ')[-1])
        false_monkey = int(lines[i + 5].split(' ')[-1])
        monkey_test.append((lambda x, divisor=divisor, true_monkey=true_monkey,
                                   false_monkey=false_monkey: true_monkey if x % divisor == 0 else false_monkey))

    total_monkeys = len(monkey_items)
    for round_number in range(round):
        for monkey_number in range(total_monkeys):
            while monkey_items[monkey_number]:
                monkey_inspections[monkey_number] += 1
                item = monkey_items[monkey_number].pop()
                worry = monkey_operation[monkey_number](item)

                if round == 20:
                    worry = floor(worry / 3)

                new_monkey = monkey_test[monkey_number](worry)

                modded_worry = worry if round == 20 else (worry % monkey_divisors_product)

                monkey_items[new_monkey].append(modded_worry)

    sorted_handles = sorted(monkey_inspections, reverse=True)[:2]
    monkey_business = math.prod(sorted_handles)
    return monkey_business

print(f'Part 1: {solve(20)}')
print(f'Part 2: {solve(10000)}')