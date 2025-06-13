class GrandFather:
    def __init__(self, name):
        self.name = name

    def hello(self):
        return f"Parent Name Is {self.name}"

class Parent(GrandFather):
    def __init__(self, name, grand_father):
        super().__init__(grand_father)
        self.name = name

class Child(Parent):
    def __init__(self, child_name, parent_name, grand_father):
        super().__init__(parent_name, grand_father)
        self.child_name = child_name
