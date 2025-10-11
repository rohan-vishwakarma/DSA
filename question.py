
import re

file_name = "coding.txt"  # Default filename

try:
    # Read file content
    with open(file_name, 'r') as file:
        content = file.read()

    # Extract all numbers using regex
    numbers = re.findall(r'\d+', content)
    numbers = list(map(int, numbers))
    total = sum(numbers)

    print(f"Found {len(numbers)} numbers.")
    print(f"Sum of numbers: {total}")

except FileNotFoundError:
    print("File not found. Please make sure the file exists.")


