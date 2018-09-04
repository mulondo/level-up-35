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
