from msilib.schema import Class
import pymysql
# python3 -m pip install PyMySQL
import numpy as np
import pandas as pd
import json



conn = pymysql.connect(host='localhost',user='root',password='qiya981226',database='myapp',charset='utf8')
mycursor =conn.cursor()

class create_dict(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value

def show_data():
    mydict = []
    str = 'select * from student;'
    mycursor.execute(str)
    data = mycursor.fetchall()
    
    for row in data:
        mydict.append({"SID":row[0],"SName":row[1],"Class":row[2],"Year":row[3]})
        # mydict.add(row[0],({"SID":row[1],"SName":row[2],"Class":row[3],"Year":row[4]}))

    stud_json = json.dumps(mydict, indent=2, sort_keys=True)
    print(stud_json) 
    return stud_json


def show_one_data(SID):  
    mydict = []
    str = "select * from student WHERE SID = '%s'"%(SID)
    mycursor.execute(str)
    data = mycursor.fetchall()
    
    for row in data:
        mydict.append({"SID":row[0],"SName":row[1],"Class":row[2],"Year":row[3]})
        # mydict.add(row[0],({"SID":row[1],"SName":row[2],"Class":row[3],"Year":row[4]}))

    stud_json = json.dumps(mydict, indent=2, sort_keys=True)
    print(stud_json) 
    return stud_json 
    
def insert_data(SID,SName,Class,Year):
    sql = "INSERT INTO student VALUES ('%s','%s','%s',%d)"%(SID,SName,Class,Year)
    print (sql)
    mycursor.execute(sql)
    conn.commit()
    print(mycursor.rowcount, "记录插入成功。")
    return {'status': 'OK'}


def update_data(upID,upName,upClass,upYear):
    sql = "UPDATE student SET SID = '%s', SNAME = '%s', Class='%s', YOB = '%d' WHERE SID = '%s'"%(upID,upName,upClass,upYear,upID)
    mycursor.execute(sql)
    conn.commit()
    print(mycursor.rowcount, "条记录更新。")
    return {'status': 'OK'}

   

def delete_data(SID):
    sql = "DELETE FROM student WHERE SID = '%s'"%(SID)
    mycursor.execute(sql)
    conn.commit()
    print(mycursor.rowcount, "条记录删除。")
    return {'status': 'succssful'}



