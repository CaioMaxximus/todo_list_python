from models import task as task_moddel
from datetime import datetime
from repository import task_repository

def get_all_tasks(): 
    print("get all tasks")
    return task_repository.get_all_tasks()

def add_new_task(tasks , title , content, expire_date):
   
   
    MIN_SIZE_TITLE = 1
    MIN_SIZE_CONTENT = 10
    if(len("".join(title.split(" "))) < MIN_SIZE_TITLE):
        raise ValueError("Title must have at least one character")
    if(len("".join(content.split(" "))) < MIN_SIZE_CONTENT):
        raise ValueError(f"Task content must have at least more tha {(MIN_SIZE_CONTENT - 1)}  characteres")

    newT = task_moddel.task(completed=False,
                    title= title,
                    content=content,
                    expire_date= datetime.strptime(expire_date, '%m-%d-%Y').date(),
                )
    task_repository.save_new_task(newT)
    tasks = task_repository.get_all_tasks()
    return tasks

def remove_task_by_id(id):
    # print(tasks)
    task_repository.remove_task(id)
    return task_repository.get_all_tasks()
    
def set_task_complete(id):
    return task_repository.set_task_complete(id)