class Emp :
    def __init__(self,name,age) :
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"
        pass
e = Emp("Shivani",25)
print(e)
#print(e.age)
    