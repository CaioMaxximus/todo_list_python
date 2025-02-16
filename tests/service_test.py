import unittest
from async_test import async_test
import datetime
from exceptions.personalized_exceptions import TaskValidationError
from services import task_services
from repository import task_repository
from models.task import Task


class TestService(unittest.TestCase):

    @async_test
    async def setUp(self):
        self.content = "content"
        self.title = "A"
        self.expire_date = (datetime.date.today().strftime('%m-%d-%Y'))
        color = "#FFEB99"
        await task_repository.clear_database()

    async def tearDownAsync(self):
        await task_repository.clear_database()

    @async_test
    async def test_add_new_task_small_title(self):
        with self.assertRaises(TaskValidationError):
            await task_services.add_new_task(self.title, self.content, self.expire_date,color = "#FFEB99",)

    @async_test
    async def test_add_new_task_small_content(self):
        expire_date = (datetime.date.today().strftime('%m-%d-%Y'))
        with self.assertRaises(TaskValidationError):
            await task_services.add_new_task(self.title * 10, self.content, expire_date,color = "#FFEB99")

    @async_test
    async def test_add_new_task_big_content(self):
        pass

    @async_test
    async def test_remove_task(self):
        await task_services.add_new_task(self.title * 10, self.content * 10, self.expire_date,color = "#FFEB99")
        tasks = await task_services.get_all_tasks()
        task_created = list(tasks.values())[0]
        tasks_remaining = await task_services.remove_task_by_id(task_created.id)
        self.assertEqual(len(tasks_remaining), 0)

    @async_test
    async def test_set_task_complete(self):
        await task_services.add_new_task(self.title * 10, self.content * 10, self.expire_date,color = "#FFEB99")
        tasks = await task_services.get_all_tasks()
        task_created = list(tasks.values())[0]
        await task_services.set_task_complete(task_created.id)
        task_updated = await task_services.get_all_tasks()
        task_updated = list(task_updated.values())[0]

        self.assertEqual(task_updated.completed, True)


if __name__ == '__main__':
    unittest.main()
