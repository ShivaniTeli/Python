class num:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def fun(self):
        result= self.num1 + self.num2
        print(result)

e = num(5,8)
e.fun()