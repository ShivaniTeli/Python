def fun(a):
    if a >0 :
        result = a + fun(a-1)
        print(result)
    else:
        result = 0
    return result
        
fun(5)