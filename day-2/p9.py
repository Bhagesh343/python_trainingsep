# dictionary

from collections import Counter

# Taking input from the user
user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

# Creating a frequency dictionary
frequency_dict = Counter(numbers)

print("Number of occurrences:", dict(frequency_dict))

