class Automatic:
    def __init__(self, control):
        self.automatic_control = control

    def auto_start(self):
        print("Automatic Engine Started")
        return self.automatic_control

class Manual:
    def __init__(self, control):
        self.manual_control = control

    def manual_start(self):
        print("Manual Engine Started")
        return self.manual_control

class Car(Automatic, Manual):
    def __init__(self, car_name):
        Automatic.__init__(self, "Automatic Control")
        Manual.__init__(self, "Manual Control")
        self.car_name = car_name

new_car = Car("Honda City")
p = new_car.auto_start()      # Returns "Automatic Control"
p1 = new_car.manual_start()   # Returns "Manual Control"
print(p)
print(p1)
