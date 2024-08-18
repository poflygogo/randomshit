class Vehicle:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def move(self):
        print("The vehicle is moving")

class Car(Vehicle):
    def __init__(self):
        super().__init__()

    def move(self):
        print("The car is moving")

# Creating a Car object
my_car = Car(100, "red", "Toyota")
my_car.move()  # Output: "The car is moving"