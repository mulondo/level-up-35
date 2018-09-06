
class GuestList:
    def __init__(self):        
        self.users=[]

    def get_all_users(self):
        return self.users

    def add_user(self,username,email,password):
        user_id=len(self.users)+1
        user={
            'username':username,
            'email':email,
            'password':password,
            'user_id':user_id
        }
        self.users.append(user)
        return self.users
    
    def remove_user(self,userid):        
        for user in self.users:
            if user['user_id'] == userid:
                self.users.remove(user)
        return "doesnt exist"

class Person:
    def person_name(self,name):
        return "This is {}".format(name)

class User(Person):
    def person_name(self):
        return "Name is not known"

    def get_users(self):
        ur=GuestList()
        return ur.get_all_users()
    
    def add_user(self,username,email,password):
         u=GuestList()
         return u.add_user(username,email,password)

    def remove_user(self,userid):
        urs=GuestList()
        urs.remove_user(userid)