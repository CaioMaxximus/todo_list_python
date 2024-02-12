from models import task as task_moddel
from datetime import datetime
from repository import task_repository


async def get_all_tasks():
    # print("get all tasks")
    return await task_repository.get_all_tasks()


async def add_new_task(title, content, expire_date):
    # print(title)
    # print(content

    new_t = task_moddel.Task(completed=False,
                             title=title,
                             content=content,
                             expire_date=datetime.strptime(expire_date, '%m-%d-%Y').date(),
                             )
    await task_repository.save_new_task(new_t)
    tasks = await task_repository.get_all_tasks()
    return tasks


async def remove_task_by_id(id):
    # print(tasks)
    await task_repository.remove_task(id)
    return await task_repository.get_all_tasks()


async def set_task_complete(id):
    return await task_repository.set_task_complete(id)
