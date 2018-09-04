from flask import Flask, Request,jsonify,json


myapp = Flask(__name__)

@myapp.route('/level-up/learners',methods = ['GET'])
def get_learners():
    learners_list=[
        {'Mulondo':[{'age':22,'gender':'male','class':'p2'}]},
        {'peter':[{'age':22,'gender':'male','class':'p4'}]},
        {'John':[{'age':22,'gender':'male','class':'p4'}]}
        ]
    if len(learners_list)==0:
        return jsonify({"message ":"learners not found"}),401
    return jsonify({"learners":learners_list,"number":len(learners_list)}),201


if __name__ =='__main__':
    myapp.run(debug=True,port=5000)