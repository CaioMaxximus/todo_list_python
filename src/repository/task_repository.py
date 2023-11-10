"""""
    Execute the files saving and changing

"""""
import json
from models.task import task as taskmodel
import random
import string
from datetime import datetime

dataPath = "C:\\Users\\caios\\Documents\\ProjetosPessoaisLinguagens\\Python\\to_do_list\db\\data.json"


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
    ##Adicionar thread
    write_in_file(list(tasks.values()))
    return tasks

def write_in_file(tasks):
    with open(dataPath , 'w') as json_file:
        json.dump([obj.__dict__ for obj in tasks] , json_file)

        # json_file.write(json_objects_list)
        # json_file.close()
    

def remove_task(id,tasks):
    
    try:
        del tasks[id]
        write_in_file(list(tasks.values()))
        return tasks
    except ValueError:
        print(f"Invalid id Value! {id}")

def remove_all_tasks():
    write_in_file([])
  

# def get_task(id):
#     pass

def get_all_tasks():
    tasks = load_json_file()
    tasks_obj = {}
    print("chamou")
    for task in tasks:
        # date = task["expire_date"]
        # task["expire_date"] = datetime.strptime(date ,"%m/%d/%Y, %H:%M:%S")
        newT = taskmodel(**task)
        tasks_obj[newT.get_id()] = (newT)
    return tasks_obj
    
    
# print(get_all_tasks())