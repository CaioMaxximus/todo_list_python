from tkinter import ttk
import tkinter as tk




class to_do_app(tk.Tk):
    
    
    def __init__(self, tasks , *args, **kwargs ):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.container = tk.Frame(self)
        self.container.pack(side = "top", fill = "both" , expand= True)
        
        self.container.rowconfigure(0,weight=1)
        self.container.columnconfigure(0,weight=1)
        self.stack = []
        # self.pages = []
        self.tasks = tasks
        
            
        frame = HomeP(self.container , self ,tasks)
        frame.grid(row = 0, column = 0, sticky ="nsew")
        self.stack.append(frame)
        print(self.stack[-1])
        frame.tkraise()
        # self.stack_page(frame)
            
            # self.pages.appen(e)
            

    def unstack(self):
        if(len(self.stack)>1):
            self.stack.pop()
        self.stack[-1].tkraise()

    
    def stack_page(self,page):
        self.stack.append(page(self.container,self))
        print(self.stack[-1])
        self.stack[-1].tkraise()
    
class HomeP(tk.Frame):
    def __init__(self,parent, controler,tasks):
        tk.Frame.__init__(self , parent,borderwidth=2, relief="solid", bg="black")
        # self.pack(side = "top", fill = "both" , expand= True)
        
        self.tasks = tasks
     
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure(0,weight=1)
        
        ##Top  bar
        self.frameTopBar = tk.Frame(self,borderwidth=2, relief="solid",background ="blue")
        self.frameTopBar.grid(row= 0,column=0)
        
        self.frameTopBar.grid_columnconfigure(0,weight=1)
        self.frameTopBar.grid_columnconfigure(1,weight=2)
        self.frameTopBar.grid_columnconfigure(2,weight=2)

        self.variable = tk.StringVar(self.frameTopBar)
        self.variable.set("ALL")
        opM = tk.OptionMenu(self.frameTopBar,self.variable,"ALL" ,"COMPLETED" , "NOT COMPLETED")
        # opM.pack()
        opM.grid(row=0 ,column=0)
        ##delayin button creation on the top bar
        
        ##Creation Button
        
        buttonFilter = tk.Button(self.frameTopBar,text="Filter",command= self.filter_tasks_by_complete)
        buttonFilter.grid(row=0 ,column=1)
        # button.pack()
        
        ##create new task
        
        buttonCreateT = tk.Button(self.frameTopBar,text="+",
                                  command= lambda : controler.stack_page(CreateP)
                                  , width = 5,height=3)
        buttonCreateT.grid(row=0 ,column=2)
        
        #Frames list
        self.frameTasks = tk.Frame(self,borderwidth=2, relief="solid",background='red')
        self.frameTasks.grid(row=1,column=0)
        self.frameTasks.grid_columnconfigure(0, weight=1)
        self.frameTasks.grid_columnconfigure(1, weight=1)
        

        self.list_tasks(self.tasks.values())
        
    
    def list_tasks(self, tasks):
        
        
        ## GET TASKS AS LISTS , ALWAYS
        for widget in self.frameTasks.winfo_children():
            widget.destroy()
        row_counter = 0
        for i , task in enumerate(tasks):
            # print(task)
            frame_task = tk.Frame(self.frameTasks,borderwidth=2, relief="solid", bg="lightgray")
            frame_task.grid(row = (row_counter // 2) , column = (i % 2))
            title_label = ttk.Label(frame_task, text=task.title)
            title_label.grid(row=0, column=0, padx=5, pady=2)
            content_label = ttk.Label(frame_task, text=task.content)
            content_label.grid(row=1, column=0, padx=5, pady=2)
            row_counter += 1
            
    def filter_tasks_by_complete(self):
        
        method = self.variable.get()
        print("filter_tasks")
        # print(self.tasks)
        if(method == "ALL"):
            print("ALL")
            self.list_tasks(self.tasks.values())
        
        else:
            exit = []
            # print(method)
            completed = int(method == "COMPLETED")
            print(completed)
            for task in (self.tasks.values()):
                if task.completed == completed:
                    print(task.completed)
                    exit.append(task)
            # print(exit)        
            self.list_tasks(exit)
                
        
        
        
    
class CreateP(tk.Frame):
    def __init__(self,parent, controler):
        
        tk.Frame.__init__(self , parent,borderwidth=2, relief="solid", bg="blue")
        # self.pack(side = "top", fill = "both" , expand= True)
        self.grid(row=0,column=0, sticky ="nsew")
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=10)
        self.grid_columnconfigure(0,weight=1)
        self.controler = controler
        # self.grid_columnconfigure(1,weight=1)
        
        ##top bar
        
        self.frameTopBar = tk.Frame(self,borderwidth=2, relief="solid",background ="blue")
        self.frameTopBar.grid(row= 0,column=0)
        self.frameTopBar.grid_columnconfigure(0,weight=1)
        self.frameTopBar.grid_columnconfigure(1,weight=5)
        ##Title creation
        self.titleIn = tk.Text( self.frameTopBar,bg="gray",height=2,width=25)
        self.titleIn.grid(row = 0, column=0)
        
        ##Button to create
        
        self.createTakBtn = tk.Button( self.frameTopBar,text="Create Task",command= self.create_task)
        self.createTakBtn.grid(row=0,column=1)
        
        
        ##Content area
        
        self.contentIn = tk.Text(self)
        self.contentIn.grid(row=1,column=0)

    def create_task(self):
        self.controler.unstack()
    
    


def init(tasks):
    root = to_do_app(tasks)
    root.geometry('500x500')
    root.mainloop()