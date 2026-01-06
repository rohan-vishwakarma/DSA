class Automatic:
    def __init__(self, control):
        self.automatic_control = control

    def name(self):
        return "automatic"

    def auto_start(self):
        print("Automatic Engine Started")
        return self.automatic_control

class Manual:
    def __init__(self, control):
        self.manual_control = control

    def name(self):
        return "manual"

    def manual_start(self):
        print("Manual Engine Started")
        return self.manual_control

class Car(Manual, Automatic):
    def __init__(self, car_name):
        Automatic.__init__(self, "Automatic Control")
        Manual.__init__(self, "Manual Control")
        self.car_name = car_name

new_car = Car("Honda City")
automatic = new_car.auto_start()      # Returns "Automatic Control"
manual    = new_car.manual_start()   # Returns "Manual Control"
print(f"Automatic : {automatic}")
print(f"Manual : {manual}")

print(new_car.name())

print(Car.mro())
