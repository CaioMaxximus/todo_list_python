from tkinter import ttk
import tkinter as tk
import asyncio
from .creator import Creator
from tkinter import scrolledtext
from .Themes import Themes
from elements.task_window import TaskWindow

# from icons import arrow-turn-down-left.svg
Theme = Themes("")


class Home(tk.Frame):
    def __init__(self, parent, controler, tasks, width , height):
        tk.Frame.__init__(self, parent, borderwidth=2, relief="solid", bg=Theme.get_color("big_background_darker"),
                          width= int(0.7 * width) , height= (height) )

        self.tasks = tasks
        self.task_wigdets = {}
        self.wigdets_list = []
        self.parent = parent
        self.controler = controler
        self.number_of_columns = 3

        
        self.grid(row=0, column=0, sticky="nsew") 
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure(0, weight=1)

        # Top  bar
        self.frameTopBar = tk.Frame(self, borderwidth=0, relief="solid",
                                    background=Theme.get_color("big_background_darker"))
        self.frameTopBar.grid(row=0, column=0, sticky="ew")

        self.frameTopBar.grid_columnconfigure(0, weight=1)
        self.frameTopBar.grid_columnconfigure(1, weight=2)
        self.frameTopBar.grid_columnconfigure(2, weight=2)

        self.variable = tk.StringVar(self.frameTopBar)
        self.variable.set("NOT COMPLETED")
        opM = tk.OptionMenu(self.frameTopBar,
                            self.variable, "ALL", "COMPLETED", "NOT COMPLETED",
                            )
        opM.config(width=20)
        # opM.pack()
        opM.grid(row=0, column=0)
        ##delayin button creation on the top bar
        ##Creation Button

        filterImg = tk.PhotoImage(file=Theme.get_icon("filter"))
  
        buttonFilter = tk.Button(self.frameTopBar, text="Filter", bg=Theme.get_color("element_1"),
                                 command=lambda: asyncio.create_task(self.controler.get_all_tasks()), image=filterImg)
        buttonFilter.filterImg = filterImg
        buttonFilter.grid(row=0, column=1)
        # button.pack()
        self.creator_pg = Creator(self.parent,self.controler)
        # self.creator_pg.
        ##create new task
        addImg = tk.PhotoImage(file=Theme.get_icon("add-circle"))
        buttonCreateT = tk.Button(self.frameTopBar, text="+",
                                  command=lambda: controler.stack_page(self.creator_pg)
                                  , width=35, height=35, bg=Theme.get_color("element_1"), image=addImg)
        buttonCreateT.image = addImg
        buttonCreateT.grid(row=0, column=2)

        self.downFrame = tk.Frame(self, bg=Theme.get_color("big_background_darker"),
                                  borderwidth=0)
        self.downFrame.grid(row=1, column=0, sticky="nsew")
        self.downFrame.grid_rowconfigure(0, weight=1)
        self.downFrame.grid_columnconfigure(0, weight=14)
        self.downFrame.grid_columnconfigure(1, weight=2)

        self.canvas = tk.Canvas(self.downFrame, bg="#125304",highlightbackground= "#C19A6B", 
                   highlightthickness=5 )
        
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas.rowconfigure(0, weight=1)
        self.canvas.columnconfigure(0, weight=1)

        self.scroll_bar = tk.Scrollbar(self.downFrame,
                                       orient="vertical",
                                       command=self.canvas.yview)
        self.scroll_bar.grid(row=0, column=1, sticky='ns')

        # Frames list
        self.frameTasks = tk.Frame(self.canvas, borderwidth=2,
                                    bg="#125304")
        # self.frameTasks.grid(row = 0 ,column=0,sticky= 'ew')
        self.frameTasks.grid_columnconfigure(0, weight=10)
        self.frameTasks.grid_columnconfigure(1, weight=10)
        self.frameTasks.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        

        #self.frameTasks.bind("<B1-Motion>", lambda event, frame=self.frameTasks: self.resize_frame(event, frame))
        self.canvas.create_window((0, 0), window=self.frameTasks, anchor='nw')
        self.canvas.configure(yscrollcommand=self.scroll_bar.set)
        self.canvas.bind("<Enter>", self.bind_mouse_scroll)
        self.canvas.bind("<Leave>", self.unbind_mouse_scroll)
        # Adicionar rolagem pelo mouse (scroll wheel)

        self.filter_tasks_by_complete()

    # def set_mouse(self,widget ):
        

    def bind_mouse_scroll(self, event=None):
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_scroll)  # Windows
        self.canvas.bind_all("<Button-4>", self.on_mouse_scroll)  # Linux scroll up
        self.canvas.bind_all("<Button-5>", self.on_mouse_scroll)  # Linux scroll down

    def unbind_mouse_scroll(self, event=None):
        self.canvas.unbind_all("<MouseWheel>")
        self.canvas.unbind_all("<Button-4>")
        self.canvas.unbind_all("<Button-5>")

    def on_mouse_scroll(self, event):
        if event.num == 4:  # Linux scroll up
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:  # Linux scroll down
            self.canvas.yview_scroll(1, "units")
        else:  # Windows scroll
            self.canvas.yview_scroll(-1 * (event.delta // 120), "units")
    def resize_frame(self, event, frame):
        width = event.x
        height = event.y
        frame.config(width=width, height=height)
        #  print(width, height)
        self.filter_tasks_by_complete()
        # #  print("Resize canvas")
        self.on_canvas_resize(None)  # Atualiza o tamanho do Canvas


    def complete_task(self, task):
        return lambda t =task: asyncio.create_task( self.complete_task_pool(task.id))

    async def complete_task_pool(self, id):
        
        try:
            await self.controler.set_task_complete(id)
            self.task_wigdets[id]["obj"].change_complete_state()
            method = self.variable.get()
            if (method != "ALL"):
                # self.filter_tasks_by_complete()
                await asyncio.sleep(0.20)
                pos = self.task_wigdets[id]["pos"]
                self.move_chained_wigdets(id,pos[0],pos[1])

        except Exception as e:
            print(e)

    def remove_task(self , task):
        

        ## Gerando erro de corrotina esperada aqui
        return lambda t =task: asyncio.create_task(self.controler.remove_task(t.id, self.notify))
    
    def move_chained_wigdets(self,id, row, col):
        #  print(self.task_wigdets)
        widgets_num = len(self.task_wigdets)
        actual_pos = (row) * self.number_of_columns + col 
        new_list = self.wigdets_list.copy()  
        new_list.pop(actual_pos)  
        self.task_wigdets[id]["obj"].destroy()

   
        for i in range(actual_pos,widgets_num - 1):
            
            next_col = (col + 1) % self.number_of_columns
            next_row = row + (col+ 1) // self.number_of_columns
            #  print({"actual_pos":actual_pos,
            #        "next_col" :next_col,
            #        "next_row":next_row,
            #        })
            next_w = self.wigdets_list[actual_pos +1]
            next_w.set_grid(row,col)
            self.task_wigdets[next_w.task.id]["pos"] = (row,col)
            row = next_row
            col = next_col
            actual_pos += 1
        del self.task_wigdets[id]
        self.wigdets_list = new_list
  
        #  print(self.task_wigdets)

    def list_tasks(self, tasks):

        ## GET TASKS AS LISTS , ALWAYS  
        # #  print("listando task")
        # #  print(tasks)
        self.task_wigdets= {}
        self.wigdets_list = []


        for widget in self.frameTasks.winfo_children():
            # #  print(type(widget))
            #  print(widget)
            widget.destroy()
        
        row_counter = 0
        # #  print("_________")
        # #  print(tasks)
        for i, task in enumerate(tasks):
            # #  print(f"task : {i}")
            ##  print(task)
            # #  print(task)
            # self.frameTasks.update()
            columnN = (i % self.number_of_columns)
            rowN = (row_counter // self.number_of_columns)
            paddX = (10, 8) if columnN == 0 else (8, 1)

            # completeColor = Theme.get_color("correct") if task.completed else Theme.get_color("error")
            task_w = TaskWindow(self.frameTasks, borderwidth=2, relief="solid"
                                )
            task_w.setup(task, Theme, rowN , columnN, paddX,
                        self.parent,self.complete_task , self.remove_task)
            #  print(f"n_wigdet_{i}")
            self.task_wigdets[task.id] = {}
            self.task_wigdets[task.id]["obj"] = task_w
            self.task_wigdets[task.id]["pos"] = (rowN,columnN)
            self.wigdets_list.append(task_w)
            row_counter += 1

        self.frameTasks.update_idletasks()
        # self.canvas.update_scroll_region()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def filter_tasks_by_complete(self):

        method = self.variable.get()
        # #  print("filter_tasks")
        # #  print(self.tasks)
        if (method == "ALL"):
            # #  print("ALL")
            #  print(self.tasks.values())
            self.list_tasks(self.tasks.values())

        else:
            exit = []
            # #  print(method)
            completed = int(method == "COMPLETED")
            # #  print(completed)
            for task in (self.tasks.values()):
                if task.completed == completed:
                    # #  print(task.completed)
                    exit.append(task)
            # #  print(exit)        
            self.list_tasks(exit)

    def notify(self):
        self.tasks = self.controler.get_tasks()
        # #  print("######")
        #  print("chamou o notify")
        #  print(self.tasks)
        # self.list_tasks(self.tasks.values())
        self.filter_tasks_by_complete()