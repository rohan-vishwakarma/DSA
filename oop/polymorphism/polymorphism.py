class Sedan:
    def speed(self):
        return "Sedan runs at 120 km/hr"

class HatchBack:
    def speed(self):
        return "Hatchback runs at 100 km/hr"

class Suv:
    def speed(self):
        return  "Suv runs at 150 km/hr"


for cars in [Sedan(), HatchBack(), Suv()]:
    print(cars.speed())