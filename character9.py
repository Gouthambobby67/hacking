import itertools

# Define the set of capital letters and numbers
capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'

# Generate all possible combinations of 4 capital letters followed by 4 numbers
combinations = list(itertools.product(capital_letters, repeat=4))
combinations = [''.join(combination) for combination in combinations]

# Add numbers to each combination
final_outcomes = [combination + ''.join(number) for combination in combinations for number in itertools.product(numbers, repeat=4)]

# Save all outcomes to a text file
file_path = 'all_outcomes.txt'
with open(file_path, 'w') as file:
    file.write('\n'.join(final_outcomes))

print(f"All possible outcomes saved to {file_path}")

