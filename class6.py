class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")
  def pfun(self):
    print(self.brand , self.model)

class Car(Vehicle):
  print("CAR")
  pass

class Boat(Vehicle):
  print("BOAT")
  pass
    
class Plane(Vehicle):
  print("PLANE")
  pass

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  x.pfun()
  x.move()
