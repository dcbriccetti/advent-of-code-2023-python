from typing import Optional

from src.shared import get_lines

# List of words representing digits (excluding zero)
words = 'one two three four five six seven eight nine'.split()
# Reversed version of the words list
words_reversed = [word[::-1] for word in words]

def extract_nums(line: str):
    # Extract the first digit from the line using the words list
    first_digit = extract_digit(line, words)
    # Reverse the line for finding the last digit
    line_reversed = line[::-1]
    # Extract the last digit from the reversed line using the reversed words list
    last_digit = extract_digit(line_reversed, words_reversed)
    # Combine the first and last digits and convert to integer
    return int(str(first_digit) + str(last_digit))

def extract_digit(line: str, words: list[str]):
    # Variable to store the found digit, initially None
    found_digit: Optional[int] = None
    # Continue until a digit is found or the line is empty
    while not found_digit and line:
        if line[0].isdigit():
            # If the first character is a digit, use it
            found_digit = int(line[0])
            # Remove the first character from the line
            line = line[1:]
        else:
            # Loop through the list of words
            for i, word in enumerate(words, 1):
                if line.startswith(word):
                    # If the line starts with a word from the list, use its index as the digit
                    found_digit = i
                    # Remove the found word from the line
                    line = line[len(word):]
                    break
            # If no digit is found, remove the first character and continue
            if not found_digit:
                line = line[1:]
    return found_digit

# Read lines from the file, extract numbers from each line, and sum them up
print(sum(extract_nums(line) for line in get_lines('../data/1.txt')))
