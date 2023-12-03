from tkinter import ttk
import tkinter as tk
from tkcalendar import Calendar
from services import task_services 
from functools import partial


class to_do_app(tk.Tk):
    
    
    def __init__(self, tasks , *args, **kwargs ):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.container = tk.Canvas(self,  width=500, height=500)
        self.container.pack(side = "top", fill = "both" , expand= True)
        # self.container.grid(stick = "nswe")
        self.container.grid_rowconfigure(0,weight=1)
        self.container.grid_columnconfigure(0,weight=1)
        self.stack = []
        # self.pages = []
        self.tasks = tasks
        
        frame = HomeP(self.container , self ,tasks)
        frame.grid(row = 0, column = 0, sticky ="nsew")
        self.stack.append(frame)
        print(self.stack[-1])
        frame.tkraise()
        self.observers = []
        self.observers.append(frame)
            
    def unstack(self):
        if(len(self.stack)>1):
            self.stack.pop()
        self.stack[-1].tkraise()

    
    def stack_page(self,page):
        self.stack.append(page(self.container,self))
        print(self.stack[-1])
        self.stack[-1].tkraise()
        
    def createTask(self,title,content,expireD):
        print(self.tasks)
        self.tasks = task_services.add_new_task(self.tasks.copy() ,title,content,expireD)
        self.notify()
    
    def notify(self):
        for e in self.observers:
            e.notify()
            
    def get_tasks(self):
        return self.tasks
    
    
        
    
    def remove_task(self,task , callback):
        
        new_window = tk.Toplevel(self)
        new_window.title("REMOVE TASK")
        
        def close_window(event):
            self.deiconify()
            
        def remove_task_confirmed(task_id):
            # print(task_id)
            # print(self.tasks[task_id])
            new_window.destroy()
            self.tasks =  task_services.remove_task_by_id(self.tasks , task_id)
            callback()
            self.deiconify()
       
        
        frame = tk.Frame(new_window,bg  = "white")
        frame.pack(side = "top", fill = "both" , expand= True)
        frame.rowconfigure(0,weight=1)
        frame.rowconfigure(1,weight=3)
        frame.columnconfigure(0,weight=1)
        
        top_frame = tk.Frame(frame)
        top_frame.grid(row= 0, column=0,padx=5 ,pady=10)
        message = tk.Label(top_frame, text = f"remove '{task}' permanently?")
        message.grid(row=0,column=0,padx=10,pady=5)
        
        bottow_frame = tk.Frame(frame)
        bottow_frame.grid(row= 1,column=0)
        bottow_frame.grid_columnconfigure(0,weight=1)
        bottow_frame.grid_columnconfigure(1,weight=1)        
            
        cancel_btn = tk.Button(bottow_frame, text="CANCEL" , command = new_window.destroy)
        cancel_btn.grid(row=0, column=0,padx=(1,10))
        remove_btn = tk.Button(bottow_frame, text="REMOVE", bg="red", command = partial(remove_task_confirmed,task))
        remove_btn.grid(row=0,column=1 , padx=(10,1))
        new_window.bind("<Destroy>", lambda event: close_window(event))
        new_window.geometry('250x150')
        self.withdraw()
        self.wait_window(new_window)
        
        
            
class HomeP(tk.Frame):
    def __init__(self,parent, controler,tasks):
        tk.Frame.__init__(self , parent,borderwidth=2, relief="solid", bg="gray")
        # self.pack(side = "top", fill = "both" , expand= True)
        self.tasks = tasks
        self.controler = controler
     
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure(0,weight=1)
        
        ##Top  bar
        self.frameTopBar = tk.Frame(self,borderwidth=2, relief="solid",background ="white")
        self.frameTopBar.grid(row= 0,column=0,sticky="ew")
        
        self.frameTopBar.grid_columnconfigure(0,weight=1)
        self.frameTopBar.grid_columnconfigure(1,weight=2)
        self.frameTopBar.grid_columnconfigure(2,weight=2)

        self.variable = tk.StringVar(self.frameTopBar)
        self.variable.set("NOT COMPLETED")
        opM = tk.OptionMenu(self.frameTopBar,self.variable,"ALL" ,"COMPLETED" , "NOT COMPLETED")
        # opM.pack()
        opM.grid(row=0 ,column=0)
        ##delayin button creation on the top bar
        
        ##Creation Button
        
        buttonFilter = ttk.Button(self.frameTopBar,text="Filter",command= self.filter_tasks_by_complete)
        buttonFilter.grid(row=0 ,column=1)
        # button.pack()
        
        ##create new task
        
        buttonCreateT = tk.Button(self.frameTopBar,text="+",
                                  command= lambda : controler.stack_page(CreateP)
                                  , width = 5,height=3)
        buttonCreateT.grid(row=0 ,column=2)
        
        self.downFrame = tk.Frame(self, bg = "white")
        self.downFrame.grid(row=1,column=0,sticky="nsew")
        self.downFrame.grid_rowconfigure(0,weight = 1)
        self.downFrame.grid_columnconfigure(0,weight=10)
        self.downFrame.grid_columnconfigure(1,weight=2)

        self.canvas = tk.Canvas(self.downFrame,bg="white")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas.rowconfigure(0, weight=1)
        self.canvas.columnconfigure(0, weight=1)

        self.scroll_bar = ttk.Scrollbar(self.downFrame, orient="vertical", command = self.canvas.yview)
        self.scroll_bar.grid(row=0, column=1, sticky='ns')
        self.canvas.config(yscrollcommand = self.scroll_bar.set)
        
        #Frames list
        self.frameTasks = tk.Frame(self.canvas,borderwidth=2, relief="solid",
                                   width=470, 
                                   height=420)
        # self.frameTasks.grid(row = 0 ,column=0,sticky= 'ew')
        self.frameTasks.grid_columnconfigure(0, weight=10)
        self.frameTasks.grid_columnconfigure(1, weight=10)
        self.frameTasks.propagate(False)
        # self.canvas.config(scrollregion=self.canvas.bbox("all"))
        # frame_task = tk.Frame(self.frameTasks,borderwidth=2, relief="solid",
                                #   bg="lightgray",height=1000,width=1000)
        # frame_task.grid()
        self.frameTasks.bind("<B1-Motion>", lambda event, frame=self.frameTasks: self.resize_frame(event, frame))
        self.canvas.create_window((0, 0), window=self.frameTasks, anchor='nw')
        self.filter_tasks_by_complete()
        
    def resize_frame(self, event, frame):
        width = event.x
        height = event.y

        frame.config(width=width, height=height)
        print(width , height)

        self.on_canvas_resize(None)  # Atualiza o tamanho do Canvas

    
    def list_tasks(self, tasks):
        
        ## GET TASKS AS LISTS , ALWAYS
        for widget in self.frameTasks.winfo_children():
            widget.destroy()
        row_counter = 0
        for i , task in enumerate(tasks):
            # print(task)
            columnN = (i % 2)
            paddX = (1, 10) if columnN == 0 else (10, 1)
            bgColor = "#00D9C0" if task.completed else "#FF2B52" 
            frame_task = tk.Frame(self.frameTasks,borderwidth=2, relief="solid",
                                  )
            frame_task.grid(row = (row_counter // 2) , column = columnN,padx=paddX,pady=5)
            frame_task.rowconfigure(0, weight=1)
            frame_task.rowconfigure(1, weight=1)
            frame_task.rowconfigure(2, weight=10)
            
            frame_top = tk.Frame(frame_task)
            frame_top.grid()
            frame_top.grid_columnconfigure(0,weight = 3)
            frame_top.grid_columnconfigure(1,weight = 1)
            frame_top.grid_rowconfigure(0, weight=1)
            date_label = tk.Label(frame_top, text=task.expire_date )
            date_label.grid(row=0, column=0, padx=(1,4))
            remove_btn = tk.Button( frame_top,text = "X", height= 1 ,  bg = "red" ,  
                                   command= partial( self.controler.remove_task , task.id , self.notify))
            remove_btn.grid(row = 0 , column=1)
            
            title_label = tk.Label(frame_task, text=task.title ,wraplength=110 )
            title_label.grid(row=1, column=0, padx=(1,10), pady=2)
            
            content_label = tk.Label(frame_task, text=task.content, width=29, height=20,wraplength=120 , bg= bgColor)
            content_label.grid(row=2, column=0)
            row_counter += 1
            
        self.frameTasks.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))


    
            
    def filter_tasks_by_complete(self):
        
        method = self.variable.get()
        print("filter_tasks")
        # print(self.tasks)
        if(method == "ALL"):
            print("ALL")
            self.list_tasks(self.tasks.values())
        
        else:
            exit =  []
            # print(method)
            completed = int(method == "COMPLETED")
            print(completed)
            for task in (self.tasks.values()):
                if task.completed == completed:
                    print(task.completed)
                    exit.append(task)
            # print(exit)        
            self.list_tasks(exit)
                
                
    def notify(self):
        self.tasks = self.controler.get_tasks()
        self.list_tasks(self.tasks.values())
        
    
class CreateP(tk.Frame):
    def __init__(self,parent, controler):
        
        tk.Frame.__init__(self , parent,borderwidth=2, relief="solid", bg="blue")
        # self.pack(side = "top", fill = "both" , expand= True)
        self.grid(row=0,column=0, sticky ="nsew")
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=8)
        self.grid_rowconfigure(2,weight=8)
        self.grid_rowconfigure(3,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.controler = controler
        # self.grid_columnconfigure(1,weight=1)
        ##top bar
        self.frameTopBar = tk.Frame(self,borderwidth=2, relief="solid",background ="blue")
        self.frameTopBar.grid(row= 0,column=0,sticky ="nsew")
        self.frameTopBar.grid_columnconfigure(0,weight=1)
        self.frameTopBar.grid_columnconfigure(1,weight=8)
        self.frameTopBar.grid_columnconfigure(3,weight=1)
        # self.frameTopBar.grid_columnconfigure(2,weight=5) 
        ##Title creation
        
        self.closeBtn = tk.Button( self.frameTopBar,text="X",command= self.controler.unstack ,bg="red",
                                  height=2 ,width=3)
        print("----")
        self.controler.update()
        self.update()
        self.frameTopBar.update()
        self.closeBtn.update()

        self.closeBtn.grid(row=0,column=0,pady=(self.frameTopBar.winfo_height() - self.closeBtn.winfo_height()) // 2)
        self.titleIn = tk.Text( self.frameTopBar,bg="gray",height=2,width=20)
        self.titleIn.update()
        self.titleIn.grid(row = 0, column=1,sticky="we")
        ##Calendar
        
        self.calendarIn= Calendar(self,year = 2020, month = 5,
               day = 22,date_pattern = 'mm-dd-yyyy')
        self.calendarIn.grid(row = 1)
         ##Content area
        
        self.contentIn = tk.Text(self,height=8,width=35)
        self.contentIn.grid(row=2,column=0)
        
        ##Button to create
        self.createTakBtn = tk.Button( self,text="Create Task",command= self.create_task)
        self.createTakBtn.grid(row=3,column=0)
        
    def create_task(self):
        title = self.titleIn.get("1.0", "end-1c")
        expireD = self.calendarIn.get_date()
        content = self.contentIn.get("1.0", "end-1c")
        print(title,expireD,content)
        self.controler.createTask(title,content,expireD)
        self.controler.unstack()


def init(tasks):
    root = to_do_app(tasks)
    root.geometry('500x500')
    root.mainloop()