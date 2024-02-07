from sqlalchemy import Column, String, Boolean, Date, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from exceptions.personalized_exceptions import TaskValidationError
import string
import random

Base = declarative_base()


def generate_id():
    characters = string.ascii_letters + string.digits
    id = "".join([random.choice(characters) for i in range(0, 10)])
    return id


def check_min_size_field(column, field_name, size):
    if len(list("".join(column.split(" ")))) < size:
        raise TaskValidationError(f"{field_name} must have at least {size} character")
    # print(len(content))
    """if (len(list("".join(content.split(" ")))) < size):
        # print("erro content")
        raise TaskValidationError(f"Task content must have at least more than {(MIN_SIZE_CONTENT - 1)}  characteres")
    if (len(column) > constraint):
        raise ValueError(f"Invalid size for input , max : {constraint}")"""


def check_max_size_field(column, field_name, size):
    if len(column) > size:
        raise TaskValidationError(f"{field_name} must have less than {size} character")


class task(Base):
    __tablename__ = 'tasks'

    id = Column(String(10), primary_key=True, default=lambda: generate_id())
    title = Column(String(70))
    content = Column(String(1000))
    completed = Column(Boolean)
    expire_date = Column(Date)
    expired = Column(Boolean)

    # def column_string(self, value , size):
    def __init__(self, title, content, expire_date, completed=False):
        # self.id = id
        self.title = title
        self.content = content
        self.completed = completed
        self.expire_date = expire_date
        self.expired = False

        max_title_size = 70
        max_size_content = 1000
        min_size_title = 1
        min_size_content = 10
        check_max_size_field(self.content, "content", max_size_content,)
        check_max_size_field(self.title, "title", max_title_size)
        check_min_size_field(self.content, "content", min_size_content)
        check_min_size_field(self.title, "title", min_size_title)
        self.id = generate_id()

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_completed(self):
        return self.completed

    def get_expire_date(self):
        return self.expire_date

    def is_expired(self):
        pass

    def set_complete(self):
        self.completed = not self.completed

    def __str__(self):
        exit = f"""-> Id: {self.id}\n
                Title: {self.title}\n
                Content: {self.content}
                <-\n"""
        return exit

    def get_expired(self):
        return self.expired

    def set_expired(self):
        self.expired = not self.expired
