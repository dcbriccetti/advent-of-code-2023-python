from src.shared import get_lines

total = 0

for line in get_lines('../data/4.txt'):
    numbers = line.split(': ')[1]

    winning, mine = [
        set(int(ch) for ch in numbers_group.split())
        for numbers_group in numbers.split(' | ')
    ]

    num_wins = len(winning.intersection(mine))
    points = pow(2, num_wins - 1) if num_wins else 0
    total += points
print(total)
