def multi(num,k):
    n = len(num)
    for i in range(n-1):
        for j in range(i-1,n):
            if num[i] * num[j] == k:
                return True
    return False
print(multi([1,2,3,4,5],20))