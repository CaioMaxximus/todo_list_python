class task():
    
    def __init__(self, id ,title , content,expire_date,completed):
        self.id = id
        self.title = title
        self.content = content
        self.completed = completed
        self.expire_date = expire_date
        
        
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
        
    
    
        