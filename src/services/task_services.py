from models import task as task_moddel
from datetime import datetime
from repository import task_repository

def get_all_tasks():
    return task_repository.get_all_tasks()

def add_new_task(tasks , title , content, expire_date):
   
    newT = task_moddel.task(completed=0,
                    title= title,
                    content=content,
                    expire_date= expire_date.strftime("%m/%d/%Y, %H:%M:%S"),
                id="")
    tasks = task_repository.save_new_task(tasks , newT)
    return tasks

def remove_task_by_id(tasks , id):
    task_repository.remove_task(tasks , id)
    
    