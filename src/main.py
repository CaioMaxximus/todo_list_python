
import sys
import os
from models.task import Base as taskBase
import asyncio
from repository import database_definitions

sys.path.append("modules")
sys.path.append("repository")
sys.path.append("services")
sys.path.append("view")
print("main")
absPath = os.path.abspath(__file__) 
dirA = os.path.dirname(absPath)
rootDir = os.path.abspath(os.path.join(dirA , ".."))
dbPath = os.path.join(rootDir , "db" ,"database.db")
assetsPath = os.path.join(rootDir,"assets")
sys.path.append(assetsPath)
print(sys.path)
from repository import async_jobs
from services import task_services
from view.app import init
from view.Themes import Themes
# from view.pages import init
import asyncio
from repository import async_jobs
import sys


themes_dic = {
    0:"office_vibes",
    1:"cyberpunk_vibes"
}

Themes(themes_dic[1])



async def main(args):
    
    await (database_definitions.dbConnection().setConection([taskBase],dbPath))
    # await task_services.drop_tables()
    tasks = await task_services.get_all_tasks()
    print("passei tasks")
    task_view = asyncio.create_task(init(tasks, args))
    # task_background = asyncio.create_task(async_jobs.main())

    await task_view
    # task_background.cancel()

    #await asyncio.gather(*[] )


async def test():
    while True:
        await asyncio.sleep(2)
        print("oi")


if __name__ == '__main__':
    print(dbPath)  # asyncio.run()
    asyncio.run(main(sys.argv))


