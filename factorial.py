num = int(input("enter number:"))
fact = 1
if num > 1:
    #print("negative")
#elif num == 1 :
    #print("fact is 1")
#else:
 
    for i in range(1,num+1):
        fact = fact * i
    print(fact)