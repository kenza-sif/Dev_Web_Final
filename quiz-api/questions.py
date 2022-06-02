import json
import sqlite3
class Question:
    def __init__(self, title: str,position:int,text:str,img:str,ans:list):
        self.title = title
        self.position=position
        self.text= text
        self.img=img
        self.ans=ans

    def tojson(q):
        x={
            "text": q.text,
            "title" : q.title,
            "image" : q.img,
            "position" : q.position,
            "possibleAnswers" : q.ans
        }
        return json.dumps(x)    
        
    def addtodb(q):
        db_connection = sqlite3.connect("DBQuiz.db")
        db_connection.isolation_level = None
        cur = db_connection.cursor()
        cur.execute("begin")
        cur.execute("Select * from Question ORDER BY Position")
        records= cur.fetchall()
        if(q.position<=len(records)+1):
            listq=[q.title,q.text,q.position,q.img]
            for j in range(len(records),q.position-1,-1):
                cur.execute("Update Question set Position=" +str(j+1)+ " where Position="+str(j))
            insertion=cur.execute("insert into Question(Title,Description,Position,Image) values(?,?,?,?)",listq)
            cur.execute("Select * from Question where Position="+str(q.position))
            row=cur.fetchone()
            for i in range(0,len(q.ans)):
                
                lista=[row[0],q.ans[i]["text"],str(q.ans[i]["isCorrect"]),i+1]
                insertion=cur.execute("insert into PossibleAnswers(QuestionID,text,isCorrect,Position) values(?,?,?,?)",lista)
            cur.execute("commit")
    

def updatedb(pos,q):
    db_connection = sqlite3.connect("DBQuiz.db")
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    cur.execute("Select * from Question where Position="+str(pos))
    row=cur.fetchone()
    if(row==None):
        return 404
    if(pos<q.position):
        for i in range(pos+1,q.position+1):
            cur.execute("Update Question set Position=" +str(i-1)+ " where Position="+str(i))
    if(pos>q.position):
        for i in range(pos-1,q.position-1,-1):
            cur.execute("Update Question set Position=" +str(i+1)+ " where Position="+str(i))

    cur.execute("update Question set Title=\""+q.title+"\",Description=\""+q.text+"\", Position=\""+str(q.position)+"\",Image=\""+q.img+"\" where ID="+str(row[0]) )
    cur.execute("Delete from PossibleAnswers where QuestionID = " +str(row[0]))
    for i in range(0,len(q.ans)):
        lista=[row[0],q.ans[i]["text"],str(q.ans[i]["isCorrect"]),i+1]
        insertion=cur.execute("insert into PossibleAnswers(QuestionID,text,isCorrect,Position) values(?,?,?,?)",lista)
    cur.execute("commit")
            
def deletefromdb(pos):
    db_connection = sqlite3.connect("DBQuiz.db")
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    cur.execute("Select * from Question where Position="+str(pos))
    row=cur.fetchone()
    if(row==None):
        return 404
    cur.execute("Select * from Question ORDER BY Position")
    records= cur.fetchall()
    for j in range(pos+1, len(records)+1):
        cur.execute("Update Question set Position=" +str(j-1)+ " where Position="+str(j))
    cur.execute("Delete from PossibleAnswers where QuestionID = " +str(row[0]))
    cur.execute("Delete from Question where ID =" + str(row[0]))
    cur.execute("commit")
    return 204


def cleardb():
    db_connection = sqlite3.connect("DBQuiz.db")
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    cur.execute("Delete from PossibleAnswers")
    cur.execute("Delete from Question")
    cur.execute("commit")
    return 204

def getquest(pos):
    db_connection = sqlite3.connect("DBQuiz.db")
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    cur.execute("Select * from Question where Position="+str(pos))
    row=cur.fetchone()
    if(row==None):
        return 404
    cur.execute("Select * from PossibleAnswers where QuestionID="+str(row[0]))
    record=cur.fetchall()
    listAns=[]
    for i in range(0,len(record)):
        correct=record[i][2]
        if(correct.lower()=='false'):
            correct = False
        else:
            correct = True
        listAns.append({"text": record[i][1],"isCorrect": correct})
    quest=Question(row[2],row[1],row[3],row[4],listAns)
    return quest.tojson()

def fromjson(dictjson):
    #dictjson = json.loads(s)
    quest = Question(dictjson["title"],dictjson["position"],dictjson["text"],dictjson["image"],dictjson["possibleAnswers"])
    return quest

def sizeDB():
    db_connection = sqlite3.connect("DBQuiz.db")
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    cur.execute("Select Count(*) from Question")
    row=cur.fetchone()
    return row[0]




#js={"text":"Quelle est la couleur du cheval blanc d\'Henry IV ?","title":"Dummy Question","image":"falseb64imagecontent","position": 1,"possibleAnswers": [{"text": "Noir","isCorrect": 'false'},{"text": "Gris","isCorrect": 'false'},{"text": "Blanc","isCorrect": 'true'},{"text": "La réponse D","isCorrect": 'false'}]}

 
#qest = fromjson(js)
#print(sizeDB())
#qest.addtodb()
#updatedb(10,qest)
#cleardb()
#print(getquest(1))
#print(getquest(2))