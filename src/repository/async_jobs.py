from .database_definitions import dbConnection
from  .task_repository import get_all_tasks
from models.task import task as taskmodel
from datetime import datetime
import asyncio
from sqlalchemy import select , text , bindparam , insert
import schedule

session = dbConnection().getSession()
print("session -> " + str(session))

async def verify_expired_tasks():
    
    async with session() as sess:
        # with session.begin():
            # tasks = await get_all_tasks()
        stm = select(taskmodel).where(taskmodel.expired == False)
        result = await sess.scalars(stm)
        print(result)
        now = datetime.now().date()
        for task_db in result:
            print(task_db)
            if(task_db.get_expire_date() < now):
                print("expirou!")
                task_db.set_expired()
            sess.merge(task_db)
            print(task_db.get_expired())
        await sess.commit()
            
            # session.update()
    
def test():
    print("chamou o job de teste")
    
    
schedule.every().day.at("00:00").do(verify_expired_tasks)
    
    
# interval = 60 * 60 * 3

async def main():
    interval = 5
    while True:
        await asyncio.sleep(interval)
        # await verify_expired_tasks()
    
    