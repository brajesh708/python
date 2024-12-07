from functools import reduce

numbers = [1, 3, 5, 2, 4]
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(max_value)  # Output: 5