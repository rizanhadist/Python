# Class/blueprint
class Vehicle:
    # constructor/init
    def _init_(self, name):
        self.name = name
        
    # methods
    def maju(self, wheel):
        print("Brrrmmmmmm.........Majuuuu --->" + self.name + str(wheel))
    def mundur(self):
        print("Ngeeeeng............Muhnduur")


# mobil = Vehicle("BMW")

# mobil.maju(3)
# mobil.mundur()

class Car(Vehicle):
    def _init_(self, name, door):
        super()._init_(name)
        self.door =door
        
    
    def open_door(self):
        print("Open the door ---> ", self.door)

# class MotorCycle(Vehicle):
#     def _init_(self, wheel):
#         super()._init_(wheel)

bmw = Car("bmw", 4)
bmw.maju(2)
bmw.open_door()