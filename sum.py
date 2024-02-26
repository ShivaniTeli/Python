def find_sum_pair(numbers, target):
  """
  Finds a pair of numbers in a set that add up to a given target.

  Args:
      numbers: A list of integers.
      target: The target sum.

  Returns:
      A tuple containing the two numbers that add up to the target, or None if no such pair exists.
  """

  seen = set()
  for num in numbers:
    complement = target - num
    if complement in seen:
      return num, complement
    seen.add(num)
  return None

# Example usage
numbers = [1, 2, 3,11,9]
target = 12
pair = find_sum_pair(numbers, target)

if pair:
  print(f"Pair found: {pair[0]} + {pair[1]} = {target}")
else:
  print("No pair found that adds up to the target.")
