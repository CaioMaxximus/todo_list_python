import os
# from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.task import Base as taskBase
import asyncio


# conn = sqlite3.connect(dbPath)
# cursor = conn.cursor()
# cursor    

class dbConnection(object):
    
    _instance = None
    engine = None
    Session = None
    
    async def init_models(self,base):
        async with self.engine.begin() as conn:
            # await conn.run_sync(base.metadata.drop_all)
            await conn.run_sync(base.metadata.reflect)
            # await conn.run_sync(base.metadata.create_all)
    
    def __init__(self , dbPath = ""):
        print("init_task")
        self.engine = create_async_engine("sqlite+aiosqlite:///" + dbPath, echo=True)
        # taskBase.metadata.create_all(self.engine)
        asyncio.run(self.init_models(taskBase))
        self.Session = sessionmaker(bind=self.engine, class_=AsyncSession, expire_on_commit=True)
    
    
    def __new__(obj, *args , **kwargs):
        if obj._instance == None:
            print("criou uma sessao")
            obj._instance =  object.__new__(obj)
            # obj._instance.__init__()

        return obj._instance
    
    def getSession(self):
        return self.Session
        
    

# if __name__ == "__main__":
# obj1 = dbConnection(r"C:\Users\maxximus\Documents\projetos\to_do_list\db\database.db")
# obj2 = dbConnection()
# print("obj são .. " ,obj1 == obj2)