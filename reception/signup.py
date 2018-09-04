class Signup:
    def __init__(self):
        self.users={}

    def add_user(self, username, password):
        self.users[username] = password
        return self.users

    def get_user(self, username):
        if self.users[username]:
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
        self.users[username]=newpassord
        return  self.users





