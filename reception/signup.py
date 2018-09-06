class Signup:
    def __init__(self):
        self.users=[]

    def add_user(self, username, password, email):
        reg_user={
            "email":email,
            "username":username,
            "password":password
        }
        self.users.append(reg_user)
        return self.users

    def get_user(self, username,password):
        for usr in self.users:
            if usr['username']==username and usr['email']==password:
                return usr
        else:
            return "Wrong user name or password"
    
    def validate_input(self, username, password):        
        if type(username) is not str or type(password) is not str:
            raise TypeError("incorrect input")
        else:
            return "right format"
            
    def check_length(self):
        return len(self.users)

    def change_password(self,username, newpassord):
        for usrs in self.users:
            if  usrs['username']==username:
                usrs['password']=newpassord
                return  usrs

    def remove_user(self,username):
        for usr in self.users:
            if usr['username']==username:
                usr['username']="" 
                return usr
        return "user doesnot exist" 
    
    def forgot_username(self,email,password):
        for ur in self.users:
            if ur['email'] == email:
                return ur
        return "incorrect email or password"
# people=Signup()
# print(people.validate_input("1322","34567"))
    
    





