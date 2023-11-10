import sys
from datetime import datetime
sys.path.append("modules")
sys.path.append("repository")
sys.path.append("services")
sys.path.append("view")
from services import task_services
from view.pages import init


# tasks = {}
# for i in range(0,10):
    
#     task_services.add_new_task(tasks,f"task {i}" ,f"task {i} content",
#                  datetime.now())
#     print("Task number " + str(i))

# print(get_all_tasks())

def main():
    tasks = task_services.get_all_tasks()
    # init()
    # for e in tasks.values():
    #     print(e)
    
    init(tasks)    
main()