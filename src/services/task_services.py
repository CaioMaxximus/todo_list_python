from models import task as task_moddel
from datetime import datetime
from repository import task_repository
from exceptions.personalized_exceptions import TaskValidationError
def get_all_tasks(): 
    print("get all tasks")
    return task_repository.get_all_tasks()
    
async def add_new_task( title , content, expire_date):
   
    # print(title)
    # print(content)
    MIN_SIZE_TITLE = 1
    MIN_SIZE_CONTENT = 10
    if(len("".join(title.split(" ")).split()) < MIN_SIZE_TITLE):
        raise TaskValidationError("Title must have at least one character")
    # print(len(content))
    if(len("".join(title.split(" ")).split()) < MIN_SIZE_CONTENT):
        # print("erro content")
        raise TaskValidationError(f"Task content must have at least more than {(MIN_SIZE_CONTENT - 1)}  characteres")
    if()
    newT = task_moddel.task(completed=False,
                    title= title,
                    content=content,
                    expire_date= datetime.strptime(expire_date, '%m-%d-%Y').date(),
                )
    await task_repository.save_new_task(newT)
    tasks = await task_repository.get_all_tasks()
    return tasks

async def remove_task_by_id(id):
    # print(tasks)
    await task_repository.remove_task(id)
    return await task_repository.get_all_tasks()
    
def set_task_complete(id):
    return task_repository.set_task_complete(id)