class person:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def fun(self):
        print(self.a, self.b)

class student(person):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c = c
        result = self.a + self.b + self.c
        print(result)
s = student(12,3,4)
print(s)