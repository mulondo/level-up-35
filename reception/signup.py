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

    def get_user(self, username):
        for usr in self.users:
            if usr['username']==username:
                return self.users
        else:
            return "Wrong user name or password"
    
    def validate_input(self, username, password):
        if username or password is not str:
            return "wrong input format"
        elif username or password is None:
            return "Username or password is empty"

    def check_length(self):
        return len(self.users)

    def change_password(self,username, newpassord):
        for usrs in self.users:
            if usrs['username']==username:
                usrs['password']=newpassord
        return  self.users    
    
    def forgot_username(self,email,password):
        for user in self.users:
            if (user['email']==email and user['password']==password):
                return self.users
        return "incorrect email or password"




