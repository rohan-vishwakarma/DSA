import sys

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class OptimisedStudent:
    __slots__ = ['name', 'age']
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("rohan", 23)
s2 = OptimisedStudent("rohan", 23)

print("Student object:", sys.getsizeof(s1))
print("Student __dict__:", sys.getsizeof(s1.__dict__))


print("OptimisedStudent object:", sys.getsizeof(s2))
# s2 has no __dict__, so this would raise AttributeError if you try:
# print(sys.getsizeof(s2.__dict__))
