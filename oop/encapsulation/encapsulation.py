class Building:

    def __init__(self, btype, unit):
        self._type = btype
        self._unit = unit

    @property
    def get_type(self):
        return self._type

    @staticmethod
    def get_unit():
        return "this is my unit"

building = Building("commercial", "2bhk")
btype = building.get_type
print(btype)







