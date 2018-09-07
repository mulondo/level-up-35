from flask import Flask,jsonify,json,request
from work import User


myapp=Flask(__name__)
users=User()
@myapp.route('/api/users',methods=['GET'])
def get_all():
    return jsonify({'Users':users.get_users()}),200

@myapp.route('/api/users',methods=['POST'])
def add_user():
    username=request.json['username']
    useremail=request.json['email']
    userpassord=request.json['password']

    # Validate entry
    if username.strip() == "":
        return jsonify({'error': 'username is missing'}), 400
    if type(username) is not str:
        return jsonify({'error': 'Wrong format'}), 400
    if useremail.strip() == "":
        return jsonify({'error': 'email is missing'}), 400
    if userpassord.strip()=="":
        return jsonify({'error': 'password is missing'}), 400 
    
    username=request.json['username']
    useremail=request.json['email']
    userpassord=request.json['password']
    users.add_user(username,useremail,userpassord)
    return jsonify({'message':'succussfully'}),201

@myapp.route('/api/users/<int:user_id>',methods=['DELETE'])
def remove_user(user_id):
    users.remove_user(user_id)
    return jsonify({'message':' user removed succussfully'}),200


if __name__==('__main__'):
    myapp.run(debug=True,port=5000)
