from models.task import task
from datetime import datetime
from repository.task_repository import *

def getAllTasks():
    pass

def add_new_task(tasks , newTask):
    tasks = {}
    newT = task(completed=False,
                title= "Test",
                content="Test task",
                expire_date=datetime.now(),
                id=0)
    tasks = save_new_task(tasks , newT)
    print(tasks)
    