import unittest
from async_test import async_test
import datetime
from exceptions.personalized_exceptions import TaskValidationError
from services import task_services
from models.task import task

class TestService(unittest.TestCase):

    @async_test
    async def test_add_new_task_small_title(self):
        content = "contentfdsfsdffdsfsd"
        title = "A"
        expire_date = (datetime.date.today().strftime('%m-%d-%Y'))
        with self.assertRaises(TaskValidationError):
            await task_services.add_new_task(title, content, expire_date)
        
    @async_test
    async def test_add_new_task_small_content(self):
        content = "content"
        title = "A" * 10
        expire_date = (datetime.date.today().strftime('%m-%d-%Y'))
        with self.assertRaises(TaskValidationError):
            await task_services.add_new_task(title, content, expire_date)

    # @async_test
    # async def test_add_new_task_small_title(self):
    #     content = "content"
    #     title = "A"
    #     expire_date = str(datetime.date.today())
    #     with self.assertRaises(TaskValidationError):
    #         await task_services.add_new_task(title, content, expire_date)
    #     with self.assertRaises(TaskValidationError):
    #         await task_services.add_new_task(title * 10, content, expire_date)

if __name__ == '__main__':
    unittest.main()