import unittest
import sys
sys.path.append("C:\\Users\\caios\Documents\\ProjetosPessoaisLinguagens\\Python\\to_do_list\\")
sys.path.append("..\\src")
sys.path.append("repository")
sys.path.append("services")
from repository import task_repository as tk_repo
from models import task
from datetime import datetime
from async_test import async_test

class TestRepository(unittest.TestCase):
    
    @async_test
    async def test_generate_id(self):
        
        task1 = task(title = "task test" ,
                    content = "task test content",
                    expire_date = datetime.now())

        await tk_repo.save_new_task(task1) 
        tasksSaved = await tk_repo.get_all_tasks()
        generated_id =list(tasksSaved.values())[0]
        print("chamou o test")
        self.assertEqual(len(generated_id) , 9 ,"Size should be equal to 10")
        # pass 
    
# def main():
#     unittest.main()

if __name__ == '__main__':
    unittest.main()
    