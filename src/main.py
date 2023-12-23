import sys
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.task import Base as taskBase
import asyncio
from repository import database_definitions

sys.path.append("modules")
sys.path.append("repository")
sys.path.append("services")
sys.path.append("view")
print("main")

from repository import async_jobs
from services import task_services
from view.app import init
from datetime import datetime
# from view.pages import init
import asyncio




# tasks = {}
# for i in range(0,10):
    
#     task_services.add_new_task(tasks,f"task {i}" ,f"task {i} content",
#                  datetime.now())
#     print("Task number " + str(i))

# print(get_all_tasks())

async def main():
    
    tasks = await task_services.get_all_tasks()
    print("passei tasks")
    # init()
    # for e in tasks.values():
    #     print(e)
    # await init(tasks)
    await asyncio.gather(*[init(tasks)]) 

async def test():
    while True:
        await asyncio.sleep(2)
        print("oi")

absPath = os.path.abspath(__file__) 
dirA = os.path.dirname(absPath)
srcDir = os.path.abspath(os.path.join(dirA , ".."))
dbPath = os.path.join(srcDir , "db" ,"database.db")
print(dbPath)
database_definitions.dbConnection().setConection(dbPath)
# asyncio.run()
# asyncio.run(test())
asyncio.run(main())
# loop = asyncio.get_event_loop()
# loop.run_forever()
# loop.close()

