import math


def log(base, number):

  if base <= 0 or number <= 0:
    return "Invalid input: both base and number must be greater than 0"
  if base == 1:
    return "Invalid input: base cannot be 1"

  result = math.log(number, base)
  return result


print(log(10, 1000))
print(log(2, 8))
print(log(3, 81))
print(log(1, 5))
print(log(-2, 10))
