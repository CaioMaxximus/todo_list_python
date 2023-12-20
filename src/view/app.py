from tkinter import ttk
import tkinter as tk
from tkcalendar import Calendar
from services import task_services 
from tkinter import messagebox

import asyncio
from .home import Home

class to_do_app(tk.Tk):
    
    
    def __init__(self, tasks , *args, **kwargs ):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        # self.loop = asyncio.get_event_loop()
        self.destroyed = False
        self.protocol("WM_DELETE_WINDOW" ,self.on_close)
        self.container = tk.Canvas(self,  width=500, height=500)
        self.container.pack(side = "top", fill = "both" , expand= True)
        # self.container.grid(stick = "nswe")
        self.container.grid_rowconfigure(0,weight=1)
        self.container.grid_columnconfigure(0,weight=1)
        self.stack = []
        # self.pages = []
        self.tasks = tasks
        
        frame = Home(self.container , self ,tasks)
        frame.grid(row = 0, column = 0, sticky ="nsew")
        self.stack.append(frame)
        print(self.stack[-1])
        frame.tkraise()
        self.observers = []
        self.observers.append(frame)
        asyncio.create_task(self.updater(1/120))
        
    def on_close(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.setDestroyed()
                    
    def setDestroyed(self):
        print("chamou o destroy!!")
        self.destroyed = True
        
        
    def unstack(self):
        if(len(self.stack)>1):
            self.stack.pop()
        self.stack[-1].tkraise()

    
    def stack_page(self,page):
        self.stack.append(page(self.container,self))
        print(self.stack[-1])
        self.stack[-1].tkraise()
        
    async def createTask(self,title,content,expireD):
        print(self.tasks)
        self.tasks = await task_services.add_new_task(self.tasks.copy() ,title,content,expireD)
        self.notify()
    
    def notify(self):
        for e in self.observers:
            e.notify()
            
    def get_tasks(self):
        return self.tasks
    
    async def updater(self, interval):
        print("chamou updater")
        while not self.destroyed:
            self.update()
            await asyncio.sleep(interval)
            # print("updater chamou")
        global exit
        exit = 0
        print("updater shutdown")
    
    
    async def remove_task_confirmed(self , new_window , callback ,task_id):
        # print(task_id)
        # print(self.tasks[task_id])
        print("removi tudo!")
        self.tasks = await task_services.remove_task_by_id(self.tasks , task_id)
        # self.deiconify()
        callback()
        new_window.destroy()  
    
    def remove_task(self,task , callback):
        
        new_window = tk.Toplevel(self)
        new_window.title("REMOVE TASK")
        
        def close_window(event):
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
        remove_btn = tk.Button(bottow_frame, text="REMOVE", bg="red", command =lambda : asyncio.create_task(self.remove_task_confirmed(new_window , callback , task)))
        remove_btn.grid(row=0,column=1 , padx=(10,1))
        new_window.bind("<Destroy>", lambda event: close_window(event))
        new_window.geometry('250x150')
        self.withdraw()
        # self.wait_window(new_window)
        
    async def set_task_complete(self, id):
        print("id ->" + id)
        await task_services.set_task_complete(id)
        # btText = button.cget("text")
        # changeTx = "o" if(btText == "O") else "O"
        # button.configure(text = changeTx)
        await self.get_all_tasks()
        
    async def get_all_tasks(self):
        self.tasks = await task_services.get_all_tasks()
        self.notify()
        
        
exit = 1

async def init(tasks):
    root = to_do_app(tasks)
    root.geometry('520x560')
    root.minsize(520, 540) 
    root.maxsize(530, 570)
    while(exit):
        await asyncio.sleep(1)
    print("init ended")
    # root.mainloop()
    # asyncio.