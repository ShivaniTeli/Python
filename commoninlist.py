def common(a, b):
    index1 = 0
    index2 = 0
    result = []
    while  index1 < len(a) and index2 <len(b):
        if a[index1] == b[index2]:
            result.append(a[index1])
            index1 += 1
            index2 += 1
        elif a[index1] > b[index2]:
            index2 += 1
        else:
            index1 += 1
    return result

print(common([1, 2, 3, 4], [3,  4, 5, 6])) 