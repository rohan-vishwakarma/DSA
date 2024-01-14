import json

class Graduation:

    data  = {}

    primary_key = 1

    def __init__(self, degreeName):
        self.degreeName = degreeName
        self.validate(self.degreeName)
    

    def validate(self, value):
        choices = ('MSC', 'MCA', 'BCA', 'BSCIT')
        if value not in choices:
            raise Exception("Please Enter A appropriate Degree ") 
        
        
    def __str__(self):
        return str(self.data)

class Student(Graduation):

    def __init__(self, name , age, degreeName):
        super().__init__(degreeName)
        self.name = name
        self.age = age

    def admission(self):
        if self.name not in Graduation.data:
            student_data = Graduation.data

            student_data[f"{Graduation.primary_key}"] = {}
            student_data[f"{Graduation.primary_key}"]["name"] = self.name
            student_data[f"{Graduation.primary_key}"]["age"] = self.age
            student_data[f"{Graduation.primary_key}"]["degree"] = self.degreeName
            
            Graduation.data = student_data
            Graduation.primary_key +=1


    
obj = Student("Rohan Vishwakarma", 21, "MCA")
obj.admission()

obj2 = Student("Kavya Sharma", 20, "MSC")
obj2.admission()

obj3 = Student("Aravya", 21, "BSCIT")
obj3.admission()

python_obj = str(obj)

print(json.dumps(python_obj))



