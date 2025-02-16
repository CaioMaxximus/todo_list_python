"""""
    Execute the files saving and changing

"""""
from models.task import Task as taskmodel
from datetime import datetime
from .database_definitions import dbConnection
from sqlalchemy import select , text , bindparam , insert

# print("repository")

async def save_new_task(newTask):
    # newTask.set_id(id)
    session = dbConnection().getSession()
    async with session() as sess:

        stm = insert(taskmodel).values(_title= newTask.title,
                                       _content= newTask.content,
                                       _completed= newTask.completed,
                                       _expire_date= newTask.expire_date,
                                       _expired= newTask.expired,
                                       _color = newTask.color)
        await sess.execute(stm)
        await sess.commit()
    return 



async def remove_task(id):

    session = dbConnection().getSession()

    async with session() as sess:       
        # print("chamou o remove!!")
        await sess.execute(text("delete from tasks where id= :id").bindparams(bindparam("id", id)))
        await sess.commit()

    return 


async def get_all_tasks():
    # tasks = load_json_file()
    session = dbConnection().getSession()

    tasks_obj = {}

    async with session() as sess:
        # print("chamou")
        stm = select(taskmodel)
        # stm = text("select * from tasks")
        result = await sess.scalars(stm)
        for task in result:
            # print(task.__dir__())
            tasks_obj[task.id] = task
        # print(tasks_obj)
    # print("*************")
    # print(tasks_obj)
    return tasks_obj

async def set_task_complete(id):

    session = dbConnection().getSession()

    # print(id)
    async with session() as sess:
        await sess.execute(text("update tasks set _completed = not _completed where id = :id").bindparams(bindparam("id", id)))
        await sess.commit()

async def clear_database():
    session = dbConnection().getSession()
    async with session() as sess:
        await sess.execute(text("delete from tasks"))
        await sess.commit()

async def drop_tables():
    session = dbConnection().getSession()
    async with session() as sess:
        await sess.execute(text("drop table tasks"))
        await sess.commit()

# async def get_all_tasks_expired():
    

# def generate_id():
    
#     characters = string.ascii_letters + string.digits
#     id = "".join([random.choice(characters) for i in range(0,10)])
#     return id

# def load_json_file():
#     tasks = []
#     with open(dataPath , 'r') as json_file:
#         tasks = json.load(json_file)
        
#     return tasks

# def save_new_task(tasks , newTask):
#     id = generate_id()
#     newTask.set_id(id)
#     tasks[id] = newTask
#     ##Adicionar thread
#     write_in_file(list(tasks.values()))
#     return tasks

# def write_in_file(tasks):
#     with open(dataPath , 'w') as json_file:
#         json.dump([obj.__dict__ for obj in tasks] , json_file)

#         # json_file.write(json_objects_list)
#         # json_file.close()
    

# def remove_task(tasks,id):
    
#     try:
#         del tasks[id]
#         write_in_file(list(tasks.values()))
#         return tasks
#     except ValueError:
#         print(f"Invalid id Value! {id}")

# def remove_all_tasks():
#     write_in_file([])
  

# # def get_task(id):
# #     pass

# def get_all_tasks():
#     tasks = load_json_file()
#     tasks_obj = {}
#     print("chamou")
#     for task in tasks:
#         # date = task["expire_date"]
#         # task["expire_date"] = datetime.strptime(date ,"%m/%d/%Y, %H:%M:%S")
#         newT = taskmodel(**task)
#         tasks_obj[newT.get_id()] = (newT)
#     return tasks_obj
#print(get_all_tasks())