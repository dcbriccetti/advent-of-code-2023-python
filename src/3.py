from dataclasses import dataclass

@dataclass(frozen=True)
class Vector2:
    x: int
    y: int

    def __add__(self, other: 'Vector2'):
        return Vector2(self.x + other.x, self.y + other.y)

@dataclass(frozen=True)
class Number:
    value: int
    length: int
    position: Vector2

class Day3:
    def __init__(self):
        self.number_buffer: str = ''
        self.numbers = list[Number]()
        self.symbol_positions = set[Vector2]()
        self.adjacent_offsets = [
            Vector2(dx, dy)
            for dx in [-1, 0, 1]
            for dy in [-1, 0, 1]
            if dx or dy  # exclude (0, 0)
        ]

    def solve(self):
        with open('../data/3.txt', 'r') as f:
            self.find_numbers_and_symbols(f)

        print(f'Found {len(self.numbers)} numbers. {len(set(self.numbers))} are unique.')
        part_numbers = [number.value for number in self.numbers if self.is_adjacent_symbol(number)]
        print(f'Found {len(part_numbers)} part numbers totaling {sum(part_numbers)}')

    def find_numbers_and_symbols(self, file):
        def end_number():
            if self.number_buffer:
                number_x = x - len(self.number_buffer)
                number = Number(int(self.number_buffer), len(self.number_buffer), Vector2(number_x, y))
                print(f'Found number {number}')
                self.numbers.append(number)
                self.number_buffer = ''

        for y, line in enumerate(file):
            self.number_buffer = ''
            x = 0  # avoid warning
            for x, char in enumerate(line):
                is_symbol = not char.isdigit() and char != '.'
                if is_symbol or char == '.':
                    end_number()
                if is_symbol:
                    self.symbol_positions.add(Vector2(x, y))
                elif char.isdigit():
                    self.number_buffer += char
            end_number()

    def is_adjacent_symbol(self, number: Number) -> bool:
        for x_offset in range(number.length):
            for adjacent_offset in self.adjacent_offsets:
                adjacent_pos = Vector2(number.position.x + x_offset, number.position.y) + adjacent_offset
                if adjacent_pos in self.symbol_positions:
                    print(f'Symbol adjacent to {number} found at {adjacent_pos}')
                    return True
        return False

Day3().solve()
