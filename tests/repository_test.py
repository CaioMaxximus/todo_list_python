import unittest
import sys
# sys.path.append("C:\\Users\\caios\Documents\\ProjetosPessoaisLinguagens\\Python\\to_do_list\\")
# sys.path.append("..\\src")
# sys.path.append("repository")
# sys.path.append("services")
from repository import task_repository as tk_repo
from models.task import Task
from datetime import datetime
from async_test import async_test


class TestRepository(unittest.TestCase):

    @async_test
    async def setUp(self):
        self.task1 = Task(title="task test",
                          content="task test content",
                          expire_date=(datetime.now()))
        await tk_repo.clear_database()

    async def tearDownAsync(self):
        await tk_repo.clear_database()

    @async_test
    async def test_save_task(self):
        await tk_repo.save_new_task(self.task1)
        res = await tk_repo.get_all_tasks()
        self.assertEqual(len(list(res.keys())), 1, "DataBase should have one task")

    @async_test
    async def test_generate_id(self):
        await tk_repo.save_new_task(self.task1)
        tasks_saved = await tk_repo.get_all_tasks()
        generated_id = list(tasks_saved.values())[0].id
        # print("chamou o test")
        self.assertEqual(len(generated_id), 10, "Size should be equal to 10")
        await tk_repo.clear_database()
        # pass

    @async_test
    async def test_remove_task(self):
        await tk_repo.save_new_task(self.task1)
        tasks_saved = await tk_repo.get_all_tasks()
        await tk_repo.remove_task(list(tasks_saved.keys())[0])
        remaining_tasks = await tk_repo.get_all_tasks()
        # print(tasksSaved)
        # print("chamou o test")
        self.assertEqual(len(remaining_tasks), 0, "DataBase should be empty")
        await tk_repo.clear_database()


# def main():
#     unittest.main()

if __name__ == '__main__':
    unittest.main()
