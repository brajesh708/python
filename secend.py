from functools import reduce

numbers = [1, 3, 5, 2, 4]
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(max_value)  # Output: 5

print(reduce(lambda x, y: x + y, numbers))  # Output: 15

print(reduce(lambda x, y: x * y, numbers))  # Output: 60

print(reduce(lambda x, y: x - y, numbers))  # Output: -12



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))




def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2

    return num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")


