from .database_definitions import dbConnection
from  .task_repository import get_all_tasks
from models.task import task as taskmodel
from datetime import datetime
import asyncio
from sqlalchemy import select , text , bindparam , insert
import schedule

# print("session -> " + str(session))
print("async jobs")

async def verify_expired_tasks():
    
    session = dbConnection().getSession()

    async with session() as sess:
        # with session.begin():
            # tasks = await get_all_tasks()
        stm = select(taskmodel).where(taskmodel.expired == False)
        result = await sess.scalars(stm)
        print("async_jobs")
        now = datetime.now().date()
        for task_db in result:
            print(task_db)
            if(not(task_db.get_expired())  and task_db.get_expire_date() < now):
                print("expirou!")
                task_db.set_expired()
            await sess.merge(task_db)
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
        try:
            await asyncio.sleep(interval)
            await verify_expired_tasks()
        except asyncio.CancelledError:
            raise
    