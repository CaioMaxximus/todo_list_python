from sqlalchemy import Column, String , Boolean , Date
from sqlalchemy.ext.declarative import declarative_base
import string
import random

Base = declarative_base()


def generate_id():

    characters = string.ascii_letters + string.digits
    id = "".join([random.choice(characters) for i in range(0,10)])
    return id

class task(Base):
        
    __tablename__ = 'tasks'

    id = Column(String(10), primary_key= True,default=lambda : generate_id())
    title = Column(String(70))
    content = Column(String(1100))
    completed = Column(Boolean)
    expire_date = Column(Date)
    expired = Column(Boolean)
    
    def __init__(self,title , content,expire_date,completed =  False):
        # self.id = id
        self.title = title
        self.content = content
        self.completed = completed
        self.expire_date = expire_date
        self.expired = False
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
        self.expired = not(self.expired)

    