import sys


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import word_count
from stats import letter_count
from stats import sort_list


counts = letter_count()
sorted_items = sort_list(counts)
for item in sorted_items:
    print(f"{item['char']}: {item['num']}")
