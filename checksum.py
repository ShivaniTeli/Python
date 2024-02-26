def check(num):
    max_item = None
    max_count = -1
    count = {}
    for i in num:
        if i not in count:
            count[i] = 1
        else: 
            count[i] += 1
        if  count[i] > max_count:
            max_count = count[i]
            max_item = i
    return max_item
    
print(check([1,2,1,3,1]))
