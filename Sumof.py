def solve(num,k):
    for i in range(len(num)-1) :
        for j in range (i -1, len(num)) :
            if num[i] + num[j] == k:
                return True
    return False

print(solve([10,15,3,7], 17))
        
    