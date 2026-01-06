class GrandFather:
    def __init__(self, name):
        self.__name = name

    def get_gf_name(self):
        return self.__name


class Father(GrandFather):
    def __init__(self, name, grand_father_name):
        self.__name = name
        super().__init__(grand_father_name)

    def get_f_name(self):
        return  self.__name

class Child(Father):
    def __init__(self, child_name, father_name, grand_father_name):
        self.__name = child_name
        super().__init__(father_name, grand_father_name)

    def __str__(self):
        return f"Child name is {self.__name} \nFather name is {self.get_f_name()} \nGrandfather name is {self.get_gf_name()}"


child = Child("rohan", "joseph", "john")

print(child)

