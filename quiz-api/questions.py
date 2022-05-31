import json
import sqlite3
class Question:
    def __init__(self, title: str,position:int,text:str,img:str,ans:list):
        self.title = title
        self.position=position
        self.text= text
        self.img=img
        self.ans=list

    def tojson(q):
        x={
            "text": q.text,
            "title" : q.title,
            "image" : q.img,
            "position" : q.position
        }
        return json.dumps(x)    
        
    def addtodb(q):
        db_connection = sqlite3.connect("DBQuiz.db")
        db_connection.isolation_level = None
        cur = db_connection.cursor()
        cur.execute("begin")

def fromjson(s):
    dictjson = json.loads(s)
    quest = Question(dictjson["title"],dictjson["position"],dictjson["text"],dictjson["image"])
    return quest

