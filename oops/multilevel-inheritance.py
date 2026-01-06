class GrandFather:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

class Father(GrandFather):
    def __init__(self, name, grandfather_name):
        super().__init__(grandfather_name)
        self._name = name

    def get_name(self):
        return self._name

class Child(Father):
    def __init__(self, name, father_name, grandfather_name):
        GrandFather.__init__(grandfather_name)
        Father.__init__(father_name)
        self._name = name


child = Child("john", "rock", "joseph")