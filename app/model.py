class User:
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