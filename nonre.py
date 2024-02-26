def nonre(str):
    count = {}
    for i in str:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i in str:
        if count[i] == 1:
            return i
    return None

print(nonre("aaabcc"))
