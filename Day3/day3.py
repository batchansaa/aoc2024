import re

with open("Day3/puzzle.txt") as f:
    data = f.readlines()

enabled = True
product_sum = 0

mul_pattern = r"mul\((\d+),(\d+)\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"


for line in data:
    # Part 1 Answer:
    # products = [int(a) * int(b) for a, b in re.findall(r'mul\((\d+),(\d+)\)', line)]
    # product_sum += sum(products)

    instructions = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", line)
    for instruction in instructions:
        if re.match(do_pattern, instruction):
            enabled = True
        elif re.match(dont_pattern, instruction):
            enabled = False
        elif match := re.match(mul_pattern, instruction):
            if enabled:
                a, b = map(int, match.groups())
                product_sum += a * b

print(product_sum)