import unittest
import sys
# sys.path.append("C:\\Users\\caios\Documents\\ProjetosPessoaisLinguagens\\Python\\to_do_list\\")
# sys.path.append("..\\src")
# sys.path.append("repository")
# sys.path.append("services")
from repository import task_repository as tk_repo
from models.task import task
from datetime import datetime
from async_test import async_test

class TestRepository(unittest.TestCase):
    

    @async_test
    async def test_save_task(self):
        await tk_repo.clear_database()
        task1 = task(title = "task test" ,
                    content = "task test content",
                    expire_date = datetime.now())
        await tk_repo.save_new_task(task1)
        res = await tk_repo.get_all_tasks()
        self.assertEqual(len(list(res.keys())) , 1 , "DataBase should have one task")

    @async_test
    async def test_generate_id(self):
        
        task1 = task(title = "task test" ,
                    content = "task test content",
                    expire_date = datetime.now())

        await tk_repo.save_new_task(task1) 
        tasksSaved = await tk_repo.get_all_tasks()
        generated_id =list(tasksSaved.values())[0].get_id()
        # print("chamou o test")
        self.assertEqual(len(generated_id) , 10 ,"Size should be equal to 10")
        await tk_repo.clear_database()
        # pass

    @async_test
    async def test_remove_task(self):
        await tk_repo.clear_database()

        task1 = task(title = "task test" ,
                    content = "task test content",
                    expire_date = datetime.now())

        await tk_repo.save_new_task(task1)
        tasksSaved = await tk_repo.get_all_tasks()
        await tk_repo.remove_task(list(tasksSaved.keys())[0])
        remainingTasks = await tk_repo.get_all_tasks()
        # print(tasksSaved)
        # print("chamou o test")
        self.assertEqual(len(remainingTasks) , 0 ,"DataBase should be empty")
        await tk_repo.clear_database()
         
    



    
# def main():
#     unittest.main()

if __name__ == '__main__':
    unittest.main()
    