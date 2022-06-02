import json
import sqlite3

class Participation:
    def __init__(self, name:str, answers:list):
        self.name=name
        self.answers=answers
    
    def getResult(self):
        x={
            "playerName": self.name,
            "score":self.score
        }
        return json.dumps(x)
    

    def calculateScore(self):
        db_connection = sqlite3.connect("DBQuiz.db")
        db_connection.isolation_level = None
        cur = db_connection.cursor()
        cur.execute("begin")
        cur.execute("Select Count(*) from Question")
        row=cur.fetchone()
        if (row[0]!=len(self.answers)):
            return 400
        self.score=0
        for i in range(0,row[0]):
            cur.execute("Select * from Question where Position="+str(i+1))
            question=cur.fetchone()
            cur.execute("Select Position from PossibleAnswers where QuestionID="+str(question[0])+" and isCorrect=\"True\"")
            correct=cur.fetchone()
            if(correct[0]==self.answers[i]):
                self.score+=1
        listP=[self.name,self.score]
        insertion=cur.execute("insert into Participations(Name,Score) values(?,?)",listP)
        cur.execute("commit")   
        return self.getResult()

def clearparticipations():
    db_connection = sqlite3.connect("DBQuiz.db")
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    cur.execute("Delete from Participations")
    cur.execute("commit")
    return 204


def createParticipation(dictjson):
    return Participation(dictjson["playerName"],dictjson["answers"])
    
def allScores():
    db_connection = sqlite3.connect("DBQuiz.db")
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    L=[]
    cur.execute("begin")
    cur.execute("Select * from Participations ORDER BY Score DESC")
    records=cur.fetchall()
    for i in range(0,len(records)):
        r={
            "playerName": records[i][1],
            "score":records[i][2]
        }
        rjson = json.dumps(r)
        L.append(r)
    return L
print(allScores())