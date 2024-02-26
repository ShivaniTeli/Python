def solve(num, k):
    for i in range(len(num)):
        complement = k - num[i]
        if complement in num:
            return True
    return False

print(solve([10,15,3,7], 17))