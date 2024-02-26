''' Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.'''

def solve(num,k):
    for i in range(len(num)-1) :
        for j in range (i -1, len(num)) :
            if num[i] + num[j] == k:
                return True
    return False

print(solve([10,15,3,7], 17))