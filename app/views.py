from flask import Flask,jsonify,json,request
from work import User
import psycopg2
from db import cur
import re


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
    email_match=re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', useremail)
    if email_match == None:
	    return jsonify({'message':'Incorrect email format'})
    if userpassord.strip()=="":
        return jsonify({'error': 'password is missing'}), 400 
    
    username=request.json['username']
    useremail=request.json['email']
    userpassord=request.json['password']
    #users.add_user(username,useremail,userpassord)
    try:
        sql="INSERT INTO students(first_name,last_name) VALUES(%s,%s)"
        cur.execute(sql,(username,userpassord))

    except psycopg2.Error as err:
        return jsonify({'error':str(err)})
        
    return jsonify({'message':'succussfully registered'}),201


    #return jsonify({'message':'succussfully'}),201

@myapp.route('/api/users/<int:user_id>',methods=['DELETE'])
def remove_user(user_id):
    users.remove_user(user_id)
    return jsonify({'message':' user removed succussfully'}),200


if __name__==('__main__'):
    myapp.run(debug=True,port=5000)
