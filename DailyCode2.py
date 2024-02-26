'''Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].'''

def product_of_others(nums):
    n = len(nums)
    result = [1] * n

    # Calculate the product of all numbers to the left of the current number
    left_prod = 1
    for i in range(n):
        result[i] *= left_prod
        left_prod *= nums[i]

    # Calculate the product of all numbers to the right of the current number
    right_prod = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_prod
        right_prod *= nums[i]

    return result

print(product_of_others([1,2,3,4,5]))
print(product_of_others([3,2,1]))