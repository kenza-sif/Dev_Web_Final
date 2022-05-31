from asyncio.windows_events import NULL
from flask import Flask, request 
from jwt_utils import *
from questions import *
app = Flask(__name__)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": sizeDB(), "scores": []}, 200
   
@app.route('/login',  methods=['POST'])
def Login(): 
    payload = request.get_json()
    token= build_token() 
    if payload["password"]== "Vive l'ESIEE !":
        return {'token' : token}, 200
    else :
        return '', 401

@app.route('/questions',  methods=['POST'])
def AddQuestion():
    authorization = request.headers.get('Authorization')
    if type(authorization) is not str:
        return '', 401
    else:
        quest=request.get_json()
        q=fromjson(quest)
        q.addtodb()
        return '', 200

@app.route('/questions/<int:position>',  methods=['DELETE'])
def DeleteQuestion(position):
    authorization = request.headers.get('Authorization')
    if type(authorization) is not str:
        return '', 401
    else:
        return '', deletefromdb(position)

@app.route('/questions/<int:position>',  methods=['GET'])
def GetQuestion(position):
    getQ=getquest(position)
    if getQ==404:
        return '',404
    return getQ,200

@app.route('/questions/<int:position>',  methods=['PUT'])
def UpdateQuestion(position):
    authorization = request.headers.get('Authorization')
    if type(authorization) is not str:
        return '', 401
    else:
        quest=request.get_json()
        q=fromjson(quest)
        return '', updatedb(position,q)


if __name__ == "__main__":
    app.run(ssl_context='adhoc')



