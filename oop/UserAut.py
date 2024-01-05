from flask import jsonify


class UserAuth:

    last_id  = 0
    userDict = {}
    def __init__(self, user, password):
        UserAuth.last_id +=1
        self.id = UserAuth.last_id
        self.user = user
        self.password = password

    def save(self):
        UserAuth.userDict[str(self.id)] = {
            "user": self.user,
            "password": self.password
        }
        
    def __str__(self):
        return jsonify(UserAuth.userDict)
        
obj = UserAuth("rohan", "Rohan@1234")
obj1 = UserAuth("kavyasharma", "kavya@1234")
obj2 = UserAuth("kavyasharma", "kavya@1234")
obj.save()  
obj1.save()  
obj2.save()  

print(UserAuth.userDict)  
