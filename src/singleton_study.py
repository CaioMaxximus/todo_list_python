import os
# from sqlalchemy import create_engine, Column, Integer, String, Sequence
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from models.task import Base as taskBase
import asyncio


absPath = os.path.abspath(__file__) 
dirA = os.path.dirname(absPath)
srcDir = os.path.abspath(os.path.join(dirA, ".." , ".."))
dbPath = os.path.join(srcDir , "db" ,"database.db")
# conn = sqlite3.connect(dbPath)
# cursor = conn.cursor()
# cursor    


class DBConnection(object):
    
    _instance = None
    value = None
            
    
    def __init__(self , value):
        print("init")
        self.value = value
        print("setou o valor")
    
    def __new__(obj , *args, **kwargs):
        print("new")

        if obj._instance == None:
            print(obj._instance)
            obj._instance =  object.__new__(obj)
            # obj._instance.__init__()

        return obj._instance
    
    def getSession(self):
        return self.Session
    
    def getValue():
        return DBConnection.value
    

        
    

# if __name__ == "__main__":
    
obj1 = DBConnection(3)
obj2 = DBConnection(4)
print("obj são .. " ,id(obj1) == id(obj2))
print(obj1.value)
print(obj2.value)
print(DBConnection.getValue())
