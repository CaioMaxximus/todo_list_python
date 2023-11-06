"""""
    Execute the files saving and changing

"""""
import json
from models import task as taskmodel
import random
import string

dataPath = "../../db/data.json"


def generate_id():
    
    characters = string.ascii_letters + string.digits
    id = "".join([random.choice(characters) for i in range(0,10)])
    return id

def load_json_file():
    tasks = []
    with open(dataPath , 'r') as json_file:
        tasks = json.load(json_file)
        
    return tasks

def save_new_task(tasks , newTask):
    id = generate_id()
    newTask.set_id(id)
    tasks[id] = newTask

def write_in_file(tasks):
    json_objects_list = json.dump([obj.__dict__ for obj in tasks])
    with open(dataPath , 'w') as json_file:
        json_file.write(json_objects_list)
        json_file.close()
    

# def remove_task():
#     pass

def remove_all_tasks():
    write_in_file([])
  

# def get_task(id):
#     pass

def get_all_tasks():
    tasks = load_json_file()
    tasks_obj = {}
    for task in tasks:
        newT = taskmodel(**task)
        tasks_obj[newT.get_id()] = (newT)
    return newT
    
    
print(get_all_tasks())