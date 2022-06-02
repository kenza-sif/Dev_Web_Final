from asyncio.windows_events import NULL
from flask import Flask, request 
from jwt_utils import *
from participation import *
from questions import *
from flask_cors import CORS 
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": sizeDB(), "scores": allScores()}, 200
   
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

@app.route('/participations',  methods=['POST'])
def AddParticipation():
        part=request.get_json()
        p=createParticipation(part)
        res = p.calculateScore()
        if(res == 400):
            return '',400           
        return res, 200

@app.route('/questions/<int:position>',  methods=['DELETE'])
def DeleteQuestion(position):
    authorization = request.headers.get('Authorization')
    if type(authorization) is not str:
        return '', 401
    else:
        return '', deletefromdb(position)

@app.route('/questions/clear',  methods=['DELETE'])
def ClearDatabase():
    authorization = request.headers.get('Authorization')
    if type(authorization) is not str:
        return '', 401
    else:
        return '',cleardb()

@app.route('/participations',  methods=['DELETE'])
def ClearParticipations():
    authorization = request.headers.get('Authorization')
    if type(authorization) is not str:
        return '', 401
    else:
        return '',clearparticipations()

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
    app.run()



