class Instagram:

    userList = {}
    list_of_users = []
    def __init__(self):
        self.following = 0
        self.followers = 0

    def signup(self, user):
        if user not in self.userList:
            self.list_of_users.append(user)
            self.userList[f"{user}"] = {}
            self.userList[f"{user}"]["total_followers"] = self.followers 
            self.userList[f"{user}"]["total_following"] = self.following 
            self.userList[f"{user}"]["followers"] = {}
            self.userList[f"{user}"]["following"] = {}
        else:
            return f"username {user} already Exist"

    def __str__(self):
        return str(self.userList)
    
class User(Instagram):

    message = {}
    error_id = 0

    Instagram.userList

    def __init__(self, user):
        self.followers = {}
        self.following = {}
        self.user = user
        self.validateUser(user)

    def validateUser(self, user):
        if user not in self.list_of_users:
            self.error_id = self.error_id + 1

            mess = "Please register Yourself"
            self.message[f"{self.error_id}"] = {}
            self.message[f"{self.error_id}"]["validation_error"] = mess

                
    def follow(self, username):
        if self.username not in self.following.keys() and self.username in self.userList:
            self.following[f"{username}"]
            User.__init__(self.followers[f"{self.user}"])

    def __str__(self):
        if bool(self.message) == True:
            return str(self.message)
        else:
            temp = Instagram.list_of_users
            temp.remove(self.user)
            return f"Followers: {self.followers}, Following: {self.following}, Instagram Users {temp}"

obj2 = Instagram()
obj2.signup("rohan")

obj2 = Instagram()
obj2.signup("kavya")

obj2 = Instagram()
obj2.signup("Raj")

obj = User("rohan")
obj.follow("Raj")
print(obj)




    

    


    
# obj = Instagram()
# obj.signup("Rohan")

# obj2 = Instagram()
# obj2.signup("Tom")

# obj3 = Instagram()
# obj3.signup("Radha")

# obj4 = Instagram()

# print(obj4)

    