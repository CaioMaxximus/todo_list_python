from sqlalchemy import Column, String, Boolean, Date, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from exceptions.personalized_exceptions import TaskValidationError
import string
from sqlalchemy.orm import validates
import random

Base = declarative_base()


def generate_id():
    characters = string.ascii_letters + string.digits
    id = "".join([random.choice(characters) for i in range(0, 10)])
    return id


class Task(Base):
    """
    Represents a unity task

    Attributes
    ---------

    __tablename__ : str
        name of the table in the database, property used by SqlAlchemy

    title : str
        the title of the task with a maximum size define in init method
    content : str
        the content of the task with a maximum size define in init method
    completed : bool
        represent the completeness of the title, even if task is
        expired or not

    expire_date: date
        represent the title expiration date
    expired: bool
        define if the task is expired (already passed the expiration date)

    """

    __tablename__ = 'tasks'

    id = Column(String(10), primary_key=True, default=lambda: generate_id())
    # id = Column(String(10), primary_key=True)
    _title = Column(String(70))
    _content = Column(String(1000))
    _completed = Column(Boolean)
    _expire_date = Column(Date)
    _expired = Column(Boolean)
    _color = Column(String(7))

    # def column_string(self, value , size):
    def __init__(self, title, content, expire_date,color, completed=False):
        """
        Parameters
        ---------
        title : str
        the title of the task with a maximum size define in init method
        content : str
        the content of the task with a maximum size define in init method
        expire_date: date
        represent the title expiration date
        completed : bool
        represent the completeness of the title, even if tsk is
        expired or not
        """
        self.title = title
        self.content = content
        self._completed = completed
        self.expire_date = expire_date
        self._expired = False
        self.color = color

    @validates("title")
    def validate_size_title(self, key, title):

        min_size = 1
        max_size = 70
        if min_size > len(list("".join(title.split(" ")))):
            raise TaskValidationError(f"Title must have at least {min_size} character")
        if max_size < len(title):
            TaskValidationError(f"Title must have less than {max_size} character")

    @validates("content")
    def validate_size_content(self, key, content):

        min_size = 10
        max_size = 1000
        if min_size > len(list("".join(content.split(" ")))):
            raise TaskValidationError(f"Content must have at least {min_size} character")
        if max_size < len(content):
            TaskValidationError(f"Content must have less than {max_size} character")

    # def validate_max_size_field(column, field_name, size):
    #     if len(column) > size:
    #         raise TaskValidationError(f"{field_name} must have less than {size} character")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self.validate_size_title(None, title)
        self._title = title

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self,content):
        self.validate_size_content(None, content)
        self._content = content

    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self, value=None):
        self._completed = not self._completed

    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self,date):
        self._expire_date = date

    @property
    def expired(self):
        return self._expired
    

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @expired.setter
    def expired(self,value=None):
        self._expired = not self._expired

    def __str__(self):
        exit = f"""-> Id: {self.id}\n
                    Title: {self.title}\n
                    Content: {self.content}
                    <-\n"""
        return exit


