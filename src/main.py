import sys
from datetime import datetime
sys.path.append("modules")
sys.path.append("repository")
sys.path.append("services")
sys.path.append("view")
from services import task_services
from view.app import init
# from view.pages import init
from repository import database_definitions , async_jobs
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


database_definitions.dbConnection()
# asyncio.run()
# asyncio.run(test())
asyncio.run(main())
# loop = asyncio.get_event_loop()
# loop.run_forever()
# loop.close()

