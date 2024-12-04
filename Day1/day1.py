with open('Day1/puzzle.txt') as f:
    data = [line.split() for line in f]

left, right = zip(*((int(values[0]), int(values[1])) for values in data))

left = sorted(left)
right = sorted(right)

total_diff = sum(abs(l - r) for l, r in zip(left, right))

print(total_diff)