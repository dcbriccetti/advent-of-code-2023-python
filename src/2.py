import math
from typing import Sequence

from src.shared import get_lines

RGB = Sequence[int]
GameDrawCounts = Sequence[RGB]

def rgb(draw: list[str]) -> Sequence[int]:
    """Converts a list of color strings to an RGB tuple."""
    color_map = {'red': 0, 'green': 1, 'blue': 2}
    color_counts = [0, 0, 0]
    for color_str in draw:
        count, color = color_str.split(' ')
        color_counts[color_map[color]] = int(count)
    return color_counts

def extract_draw_counts(line: str) -> Sequence[Sequence[int]]:
    """Extracts game draw counts from a line of text."""
    draws = line.split(': ')[1].split('; ')
    return [rgb(draw.split(', ')) for draw in draws]

def max_rgbs(draw_counts_list: Sequence[RGB]) -> Sequence[int]:
    """Finds the maximum RGB values from a list of RGB values."""
    return tuple(max(draw_counts[i] for draw_counts in draw_counts_list) for i in range(3))

lines = get_lines('../data/2.txt')
games = [extract_draw_counts(line) for line in lines]
limits: RGB = 12, 13, 14
possible_games_id_sums = 0
powers_sum = 0

for game_id, draw_counts_list in enumerate(games, 1):
    maxes = max_rgbs(draw_counts_list)
    powers_sum += math.prod(maxes)
    if all(max_count <= limit for max_count, limit in zip(maxes, limits)):
        possible_games_id_sums += game_id

print(f'Sum of possible games IDs: {possible_games_id_sums}')
print(f'Sum of powers: {powers_sum}')
